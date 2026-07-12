# FAISS Pipeline v2 实现计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**目标:** 重写 FAISS 构建管线（分块+批量编码+checkpoint+版本备份），简化查询管线（去 ChromaDB），一次性全量构建 23,668 个源文件。

**架构:** 单文件构建脚本（~250 行）+ 单文件查询脚本（~180 行），纯 FAISS + pickle，无外部数据库依赖。分块逻辑从现有 `wiki_vector_ingest.py` 提取复用。

**技术栈:** Python 3.14, faiss-cpu, sentence_transformers (bge-m3), numpy, pickle

## 全局约束

- 所有路径硬编码为 `/Users/panbo/Obsidian/20260520/wiki/vector_store/`
- 模型：BAAI/bge-m3，`local_files_only=True`，`device="cpu"`
- 环境变量：`HF_HUB_OFFLINE=1`, `OMP_NUM_THREADS=1`, `TOKENIZERS_PARALLELISM=false`
- 删除铁律：只移 `~/.Trash`，禁止 `os.remove`/`rm`
- 查询接口向后兼容：`query()` 和 `query_fulltext()` 输出格式不变
- 不修改 wiki/sources/ 内容、ingested_files.json、ingest 流程

---

### Task 1: 重写 `wiki_faiss_build.py`（核心构建脚本）

**文件:**
- 重写: `/Users/panbo/.claude/skills/LLM-Wiki管理工具/scripts/wiki_faiss_build.py`
- 备份旧版: `wiki_faiss_build.py.v1`（移到 `~/.Trash`）

**接口:**
- 产出: `build_incremental(model=None, limit=0)`, `build_full()`, `show_status()`
- 产出文件: `embedding_cache.pkl`, `embedding.faiss`, `metadata.pkl`, `checkpoint.json`, 版本备份

- [ ] **Step 1: 写完整脚本**

```python
#!/usr/bin/env python3
"""
FAISS 向量索引构建器 v2（分块 + 批量编码 + checkpoint + 版本备份）。
替代 ChromaDB 的向量写入路径。

用法:
  python3 wiki_faiss_build.py --incremental   # 增量（默认，仅新文件）
  python3 wiki_faiss_build.py --full          # 全量重建（清空 cache）
  python3 wiki_faiss_build.py --limit N       # 限制处理文件数（测试用）
  python3 wiki_faiss_build.py --status        # 查看索引状态
"""
import os, sys, pickle, argparse, json, time, re, glob as _glob
from pathlib import Path
import numpy as np
import faiss

# ---- 环境预设（必须在 import sentence_transformers 之前） ----
os.environ.setdefault("HF_HUB_OFFLINE", "1")
os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")
os.environ.setdefault("LOKY_MAX_CPU_COUNT", "1")

VAULT = "/Users/panbo/Obsidian/20260520"
VECTOR_DIR = os.path.join(VAULT, "wiki/vector_store")
CACHE_FILE = os.path.join(VECTOR_DIR, "embedding_cache.pkl")
FAISS_FILE = os.path.join(VECTOR_DIR, "embedding.faiss")
META_FILE = os.path.join(VECTOR_DIR, "metadata.pkl")
CHECKPOINT_FILE = os.path.join(VECTOR_DIR, "checkpoint.json")
SRC_DIR = os.path.join(VAULT, "wiki/sources")

BATCH_SIZE = 32           # 批量编码文件数
CHECKPOINT_EVERY = 100    # 每 N 个文件存一次 checkpoint
MAX_CHUNK_CHARS = 1000    # 每块最大字符数
OVERLAP_CHARS = 150       # 相邻块重叠字符数
NUM_BACKUPS = 3           # 保留版本数

os.makedirs(VECTOR_DIR, exist_ok=True)


# ═══════════════════════════════════════════════════════════════════
# 分块逻辑（从 wiki_vector_ingest.py 提取）
# ═══════════════════════════════════════════════════════════════════

def _chunk_text(text: str) -> list[str]:
    """按段落分块，合并至 MAX_CHUNK_CHARS，相邻块 OVERLAP_CHARS 重叠。"""
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    raw_chunks = []
    buf = ""
    for para in paragraphs:
        if len(buf) + len(para) + 2 > MAX_CHUNK_CHARS and buf:
            raw_chunks.append(buf.strip())
            buf = ""
        buf = (buf + "\n\n" + para) if buf else para
    if buf.strip():
        raw_chunks.append(buf.strip())

    if len(raw_chunks) <= 1:
        return raw_chunks

    result = [raw_chunks[0]]
    for i in range(1, len(raw_chunks)):
        prev = raw_chunks[i - 1]
        overlap = prev[-OVERLAP_CHARS:] if len(prev) > OVERLAP_CHARS else prev
        result.append(overlap + "\n\n" + raw_chunks[i])
    return result


# ═══════════════════════════════════════════════════════════════════
# 文件 I/O
# ═══════════════════════════════════════════════════════════════════

def _load_cache() -> dict:
    """加载 embedding cache。自动迁移 v1 格式（单向量 → 向量列表）。"""
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "rb") as f:
            cache = pickle.load(f)
        # 迁移 v1 格式：{filename: np.array} → {filename: [np.array]}
        migrated = 0
        for k, v in cache.items():
            if isinstance(v, np.ndarray):
                cache[k] = [v]
                migrated += 1
        if migrated:
            print(f"  Migrated {migrated} v1 cache entries to v2 (chunked format)")
            _save_cache(cache)
        return cache
    return {}


def _save_cache(cache: dict):
    """原子写入 embedding cache。"""
    tmp = CACHE_FILE + ".tmp"
    with open(tmp, "wb") as f:
        pickle.dump(cache, f)
    os.replace(tmp, CACHE_FILE)


def _atomic_write(obj, path: str, *, is_index: bool = False):
    """原子写入：先写 .tmp，再 os.replace()。"""
    tmp = path + ".tmp"
    if is_index:
        faiss.write_index(obj, tmp)
    else:
        with open(tmp, "wb") as f:
            pickle.dump(obj, f)
    os.replace(tmp, path)


def _load_checkpoint() -> dict | None:
    """加载 checkpoint，不存在或损坏返回 None。"""
    if os.path.exists(CHECKPOINT_FILE):
        try:
            with open(CHECKPOINT_FILE) as f:
                return json.load(f)
        except (json.JSONDecodeError, KeyError):
            return None
    return None


def _save_checkpoint(data: dict):
    """原子写入 checkpoint。"""
    tmp = CHECKPOINT_FILE + ".tmp"
    with open(tmp, "w") as f:
        json.dump(data, f)
    os.replace(tmp, CHECKPOINT_FILE)


def _rotate_backups():
    """轮转版本备份：.2→.3, .1→.2, 当前→.1。"""
    for ext in ["", ".1", ".2", ".3"]:
        for base in [FAISS_FILE, META_FILE]:
            path = base + ext
            if os.path.exists(path + ".tmp"):
                try:
                    os.replace(path + ".tmp", os.path.join(os.path.dirname(path), ".Trash-" + os.path.basename(path + ".tmp")))
                except:
                    pass

    # 从旧到新删除，为新版本腾位置
    for i in range(NUM_BACKUPS, 0, -1):
        src_ext = f".{i-1}" if i > 1 else ""
        dst_ext = f".{i}"
        for base in [FAISS_FILE, META_FILE]:
            src = base + src_ext
            dst = base + dst_ext
            if i == NUM_BACKUPS:
                # 删除最老的备份
                if os.path.exists(dst):
                    os.replace(dst, dst + ".tmp")
                    try:
                        os.replace(dst + ".tmp", os.path.join(os.path.dirname(dst), ".Trash-" + os.path.basename(dst + ".tmp")))
                    except:
                        pass
            else:
                # 轮转
                if os.path.exists(src):
                    os.replace(src, dst)

    # 当前版本 → .1
    if os.path.exists(FAISS_FILE):
        os.replace(FAISS_FILE, FAISS_FILE + ".1")
    if os.path.exists(META_FILE):
        os.replace(META_FILE, META_FILE + ".1")


# ═══════════════════════════════════════════════════════════════════
# 源文件扫描与文本提取
# ═══════════════════════════════════════════════════════════════════

def _scan_source_files() -> list[tuple[str, str]]:
    """扫描 wiki/sources/，返回 [(filename, fullpath), ...]。跳过 < 50 字节的文件。"""
    files = []
    for f in sorted(os.listdir(SRC_DIR)):
        if not f.endswith(".md"):
            continue
        fpath = os.path.join(SRC_DIR, f)
        if os.path.getsize(fpath) < 50:
            continue
        files.append((f, fpath))
    return files


def _extract_text(filepath: str) -> str:
    """从 .md 源页中提取正文（去除 YAML frontmatter）。"""
    with open(filepath) as fh:
        text = fh.read()
    parts = text.split("---", 2)
    return (parts[2] if len(parts) > 2 else parts[0]).strip()


# ═══════════════════════════════════════════════════════════════════
# 构建主逻辑
# ═══════════════════════════════════════════════════════════════════

def _load_model():
    """延迟加载 bge-m3 模型（确保 env 已设置）。"""
    # 清理残留 loky 信号量（Python 3.14 兼容）
    for f in _glob.glob("/tmp/loky-*"):
        try:
            os.unlink(f)
        except:
            pass
    import sentence_transformers as st
    model = st.SentenceTransformer("BAAI/bge-m3", local_files_only=True, device="cpu")
    return model


def build_incremental(model=None, limit=0):
    """增量构建：扫描新文件，分块 + 批量编码，更新 FAISS 索引。"""
    if model is None:
        model = _load_model()

    cache = _load_cache()
    all_files = _scan_source_files()
    checkpoint = _load_checkpoint()

    # 确定待处理文件
    new_files = [(name, path) for name, path in all_files if name not in cache]

    # 从 checkpoint 续传：跳过已完成的文件
    if checkpoint and checkpoint.get("files_done", 0) > 0:
        done_set = set(checkpoint.get("done_files", []))
        new_files = [(n, p) for n, p in new_files if n not in done_set]
        if len(done_set) > 0:
            print(f"Resuming from checkpoint: {len(done_set)} files done, {len(new_files)} remaining")

    if limit > 0 and len(new_files) > limit:
        new_files = new_files[:limit]

    total = len(new_files)
    print(f"Total source files: {len(all_files)}")
    print(f"Cached: {len(cache)}, New to embed: {total}")

    if total == 0:
        print("No new files to embed. Rebuilding index from cache...")
        _rebuild_index(cache, all_files)
        return

    # 批量编码
    processed = 0
    t_start = time.time()
    batch_files = []      # 当前批次的文件名
    batch_texts = []      # 当前批次的所有 chunk 文本
    batch_chunk_counts = []  # 每个文件有多少个 chunk

    for i, (name, path) in enumerate(new_files):
        text = _extract_text(path)
        if not text:
            cache[name] = []  # 标记为已处理（空文件）
            processed += 1
            continue

        chunks = _chunk_text(text)
        if not chunks:
            cache[name] = []
            processed += 1
            continue

        batch_files.append(name)
        batch_chunk_counts.append(len(chunks))
        batch_texts.extend(chunks)

        # 攒够 BATCH_SIZE 个文件（不是 chunk 数）就编码
        if len(batch_files) >= BATCH_SIZE or i == len(new_files) - 1:
            # 批量编码所有 chunk
            prefixed = [f"为这个句子生成表示以用于检索：{t}" for t in batch_texts]
            embs = model.encode(prefixed, normalize_embeddings=True, show_progress_bar=False)

            # 分配回各文件
            idx = 0
            for j, (fname, n_chunks) in enumerate(zip(batch_files, batch_chunk_counts)):
                cache[fname] = [embs[idx + k].astype(np.float32) for k in range(n_chunks)]
                idx += n_chunks
                processed += 1

            batch_files = []
            batch_texts = []
            batch_chunk_counts = []

            # 进度报告
            elapsed = time.time() - t_start
            rate = processed / elapsed if elapsed > 0 else 0
            eta = (total - processed) / rate if rate > 0 else 0
            print(f"  [{processed}/{total}] {processed/total*100:.1f}% | "
                  f"{rate:.1f} files/s | ETA: {eta/60:.0f}m{eta%60:.0f}s")

        # checkpoint
        if processed > 0 and processed % CHECKPOINT_EVERY == 0:
            _save_cache(cache)
            _save_checkpoint({
                "files_done": processed,
                "total_files": total,
                "done_files": list(cache.keys()),
                "last_file": name,
                "timestamp": time.time(),
            })

    # 最终保存
    _save_cache(cache)
    _save_checkpoint({
        "files_done": total,
        "total_files": total,
        "done_files": list(cache.keys()),
        "last_file": new_files[-1][0] if new_files else "",
        "timestamp": time.time(),
        "completed": True,
    })
    print(f"Cache updated: {len(cache)} files, {sum(len(v) for v in cache.values())} chunks")

    # 重建 FAISS 索引
    _rebuild_index(cache, all_files)


def _rebuild_index(cache: dict, all_files: list):
    """从 cache 重建 FAISS 索引 + metadata + 版本备份。"""
    if not cache:
        print("No embeddings in cache, nothing to build")
        return

    # 收集所有 chunk 的 embedding 和 metadata
    all_embs = []
    all_meta = []
    for name, _ in all_files:
        if name not in cache:
            continue
        embeddings = cache[name]
        for chunk_idx, emb in enumerate(embeddings):
            all_embs.append(emb)
            # 生成 chunk 预览（前 200 字符）
            fpath = os.path.join(SRC_DIR, name)
            preview = ""
            if os.path.exists(fpath):
                text = _extract_text(fpath)
                chunks = _chunk_text(text)
                if chunk_idx < len(chunks):
                    preview = chunks[chunk_idx][:200]
            all_meta.append((name, chunk_idx, preview))

    if not all_embs:
        print("No embeddings to index")
        return

    embs = np.array(all_embs, dtype=np.float32)
    dim = embs.shape[1]
    index = faiss.IndexFlatIP(dim)
    index.add(embs)

    # 轮转旧备份
    _rotate_backups()

    # 原子写入新索引
    _atomic_write(index, FAISS_FILE, is_index=True)
    _atomic_write(all_meta, META_FILE)

    print(f"\nFAISS index built: {len(all_embs)} chunks from {len(set(m[0] for m in all_meta))} files (dim={dim})")
    print(f"  {FAISS_FILE} ({os.path.getsize(FAISS_FILE)/1024/1024:.1f}MB)")
    print(f"  {META_FILE} ({os.path.getsize(META_FILE)/1024/1024:.1f}MB)")
    print(f"  Backups: .1, .2, .3")


def build_full():
    """全量重建：清空 cache，重新 embed 所有文件。"""
    print("Full rebuild: embedding all files from scratch...")
    # 清空旧 cache
    if os.path.exists(CACHE_FILE):
        os.replace(CACHE_FILE, CACHE_FILE + ".old")
    if os.path.exists(CHECKPOINT_FILE):
        os.replace(CHECKPOINT_FILE, CHECKPOINT_FILE + ".old")
    build_incremental()
    print("Full rebuild complete.")


def show_status():
    """查看索引状态。"""
    cache = _load_cache()
    total_chunks = sum(len(v) for v in cache.values())
    print(f"Embedding cache: {len(cache)} files, {total_chunks} chunks")

    for label, fpath in [
        ("embedding.faiss", FAISS_FILE),
        ("metadata.pkl", META_FILE),
        ("embedding_cache.pkl", CACHE_FILE),
        ("checkpoint.json", CHECKPOINT_FILE),
    ]:
        if os.path.exists(fpath):
            size = os.path.getsize(fpath)
            print(f"  {label}: {size/1024/1024:.1f}MB" if size > 1024*1024 else f"  {label}: {size/1024:.1f}KB")
        else:
            print(f"  {label}: NOT FOUND")

    # 版本备份
    for i in range(1, NUM_BACKUPS + 1):
        bak = FAISS_FILE + f".{i}"
        if os.path.exists(bak):
            print(f"  embedding.faiss.{i}: {os.path.getsize(bak)/1024/1024:.1f}MB (backup)")

    # 检查索引一致性
    if os.path.exists(FAISS_FILE):
        idx = faiss.read_index(FAISS_FILE)
        if os.path.exists(META_FILE):
            with open(META_FILE, "rb") as f:
                meta = pickle.load(f)
            print(f"\nConsistency: index={idx.ntotal} chunks, metadata={len(meta)} entries {'✓' if idx.ntotal == len(meta) else '✗ MISMATCH!'}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="FAISS 向量索引构建器 v2")
    parser.add_argument("--incremental", action="store_true", help="增量模式（默认，仅新文件）")
    parser.add_argument("--full", action="store_true", help="全量重建（清空 cache）")
    parser.add_argument("--limit", type=int, default=0, help="限制处理文件数（0=不限制）")
    parser.add_argument("--status", action="store_true", help="查看索引状态")
    args = parser.parse_args()

    if args.status:
        show_status()
    elif args.full:
        build_full()
    else:
        build_incremental(limit=args.limit)
```

- [ ] **Step 2: 备份旧版脚本**

```bash
cp ~/.claude/skills/LLM-Wiki管理工具/scripts/wiki_faiss_build.py \
   ~/.claude/skills/LLM-Wiki管理工具/scripts/wiki_faiss_build.py.v1
```

- [ ] **Step 3: 验证 --limit 100 小批量测试**

```bash
cd ~/.claude/skills/LLM-Wiki管理工具
OMP_NUM_THREADS=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \
python3 scripts/wiki_faiss_build.py --limit 100
```

Expected: 处理 100 个新文件，显示进度，生成 cache/faiss/metadata，checkpoint 记录完成。

- [ ] **Step 4: 验证 --status**

```bash
python3 scripts/wiki_faiss_build.py --status
```

Expected: 显示 cache 文件数、chunk 数、索引一致性 ✓。

- [ ] **Step 5: 验证查询可用**

```bash
python3 scripts/wiki_vector_query.py "测试查询"
```

Expected: 返回 JSON 结果，source 为 "FAISS"，有 score 和 preview。

---

### Task 2: 简化 `wiki_vector_query.py`（去 ChromaDB）

**文件:**
- 修改: `/Users/panbo/.claude/skills/LLM-Wiki管理工具/scripts/wiki_vector_query.py`

**接口:**
- 保持: `query(q, n=5) -> list[dict]`, `query_fulltext(q, n=5) -> list[dict]`, `multi_hop_query(question) -> dict`
- 去掉: ChromaDB 导入和 fallback 逻辑

- [ ] **Step 1: 重写脚本**

```python
#!/usr/bin/env python3
"""LLM-Wiki 向量查询助手（FAISS + 多跳推理）。

用法:
  python3 wiki_vector_query.py <查询词>              # 标准向量搜索
  python3 wiki_vector_query.py --multi-hop <查询词>  # 多跳推理搜索

多跳模式流程：
  1. 标准向量搜索（top-10）
  2. LLM（DeepSeek）从结果中提取关键实体
  3. 基于实体进行第二轮向量搜索
  4. 合并去重，输出检索链路追踪

环境变量要求：DEEPSEEK_API_KEY（多跳模式需要）
"""
import sys, json, os, pickle
os.environ.setdefault("HF_HUB_OFFLINE", "1")
from pathlib import Path
from openai import OpenAI

N_RESULTS = 5

VAULT = "/Users/panbo/Obsidian/20260520"
VECTOR_DIR = os.path.join(VAULT, "wiki/vector_store")
SRC_DIR = os.path.join(VAULT, "wiki/sources")
FAISS_FILE = os.path.join(VECTOR_DIR, "embedding.faiss")
META_FILE = os.path.join(VECTOR_DIR, "metadata.pkl")
# 版本化备份列表（查询时自动 fallback）
FAISS_CANDIDATES = [
    os.path.join(VECTOR_DIR, "embedding.faiss"),
    os.path.join(VECTOR_DIR, "embedding.faiss.1"),
    os.path.join(VECTOR_DIR, "embedding.faiss.2"),
    os.path.join(VECTOR_DIR, "embedding.faiss.3"),
]


def _load_model():
    """延迟加载 bge-m3（确保 env 就绪）。"""
    import sentence_transformers as st
    model = st.SentenceTransformer("BAAI/bge-m3", local_files_only=True, device="cpu")
    return model


def _load_index():
    """加载 FAISS 索引，自动 fallback 版本备份。"""
    import faiss
    for path in FAISS_CANDIDATES:
        if os.path.exists(path):
            try:
                return faiss.read_index(path)
            except Exception as e:
                print(f"  FAISS load warning ({path}): {e}", file=sys.stderr)
                continue
    raise RuntimeError("所有 FAISS 索引文件都不可用，请运行 wiki_faiss_build.py")


def _load_metadata():
    """加载 metadata，自动 fallback 版本备份。"""
    for path in [META_FILE] + [META_FILE + f".{i}" for i in range(1, 4)]:
        if os.path.exists(path):
            try:
                with open(path, "rb") as f:
                    return pickle.load(f)
            except Exception as e:
                print(f"  Metadata load warning ({path}): {e}", file=sys.stderr)
                continue
    raise RuntimeError("所有 metadata 文件都不可用，请运行 wiki_faiss_build.py")


def _search(q: str, model, n: int) -> list[dict]:
    """FAISS 向量搜索，返回 [(filename, chunk_idx, score, preview), ...]。"""
    import faiss, numpy as np

    index = _load_index()
    metadata = _load_metadata()

    prefixed = f"为这个句子生成表示以用于检索：{q}"
    emb = model.encode([prefixed], normalize_embeddings=True)
    D, I = index.search(emb.astype(np.float32), n * 2)

    results = []
    for idx, score in zip(I[0], D[0]):
        if idx < 0 or idx >= len(metadata):
            continue
        fname, chunk_idx, preview = metadata[idx]
        results.append({
            "source": "FAISS",
            "subdir": "wiki/sources",
            "file": fname,
            "rel_path": os.path.join("wiki/sources", fname),
            "chunk_idx": chunk_idx,
            "score": round(float(score), 4),
            "preview": preview or "",
        })
    return results


def _dedup_by_file(results: list[dict]) -> list[dict]:
    """同文件多 chunk 命中 → 保留最高分。"""
    best = {}
    for r in results:
        fname = r["file"]
        if fname not in best or r["score"] > best[fname]["score"]:
            best[fname] = r
    return sorted(best.values(), key=lambda x: -x["score"])


def query(q: str, n: int = N_RESULTS) -> list[dict]:
    """标准向量搜索（FAISS，分块去重）。"""
    model = _load_model()
    results = _search(q, model, n)
    return _dedup_by_file(results)[:n]


def query_fulltext(q: str, n: int = N_RESULTS) -> list[dict]:
    """向量搜索（含完整文本），FAISS 分块去重。"""
    model = _load_model()
    results = _search(q, model, n)
    deduped = _dedup_by_file(results)[:n]

    out = []
    for r in deduped:
        fpath = os.path.join(SRC_DIR, r["file"])
        text = ""
        if os.path.exists(fpath):
            with open(fpath) as f:
                text = f.read()
        r["text"] = text
        out.append(r)
    return out


def extract_entities(question: str, results: list[dict], api_key: str) -> tuple:
    """用 LLM 从检索结果中提取关键实体，返回 (entities_list, reasoning)。"""
    client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

    context_parts = []
    for i, r in enumerate(results[:5]):
        fname = r.get("file", "unknown")
        text = r.get("text", "")[:500]
        context_parts.append(f"[文档{i+1}] {fname}:\n{text}")

    context = "\n\n".join(context_parts)

    prompt = f"""你是一个知识库检索代理。你的任务是从检索结果中提取关键实体，用于进行第二轮向量搜索以回答用户问题。

用户问题：{question}

以下是相关知识库文档片段。请提取关键的"桥梁实体"——这些实体在不同文档之间共享，是连接不同文档的线索。

实体类型：
- 人名（张三、李四）
- 公司/组织名（A公司、盘古大模型项目组）
- 项目名
- 金额/数字
- 日期/时间段
- 具体事件

规则：
1. 只提取在文档片段中**明确出现**的实体
2. 优先提取跨文档共同提及的实体（它们是连接不同文档的桥梁）
3. 每个实体用中文名称列出
4. 输出 JSON 格式

提取的文档片段：
{context}

输出格式（仅 JSON，不要多余内容）：
{{"entities": ["实体1", "实体2", ...], "reasoning": "为什么提取这些实体"}}"""

    try:
        resp = client.chat.completions.create(
            model="deepseek-chat",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1,
            response_format={"type": "json_object"},
        )
        content = resp.choices[0].message.content
        data = json.loads(content)
        entities = data.get("entities", [])
        reasoning = data.get("reasoning", "")
        return entities, reasoning
    except Exception as e:
        print(f"[WARN] LLM 实体提取失败: {e}", file=sys.stderr)
        return [], ""


def deduplicate(results: list[dict]) -> list[dict]:
    """按 (file, subdir) 去重，保留得分最高的记录。"""
    seen = set()
    deduped = []
    for r in sorted(results, key=lambda x: -x["score"]):
        key = (r.get("file", ""), r.get("subdir", ""))
        if key not in seen:
            seen.add(key)
            deduped.append(r)
    return deduped


def multi_hop_query(question: str) -> dict:
    """多跳推理查询主流程。"""
    api_key = os.environ.get("DEEPSEEK_API_KEY", "")
    trace = []

    # Step 1: 初始向量搜索
    print("[多跳 Step 1/3] 初始向量搜索...", file=sys.stderr)
    round1 = query_fulltext(question, n=10)
    trace.append({
        "step": 1,
        "action": "初始向量搜索",
        "query": question,
        "results_count": len(round1),
        "top_files": [r["file"] for r in round1[:5]],
        "top_scores": [r["score"] for r in round1[:5]],
    })

    if not round1:
        print("[多跳] 初始搜索无结果，跳过实体提取", file=sys.stderr)
        return {"question": question, "results": [], "all_unique_results": [], "trace": trace}

    # Step 2: LLM 提取实体
    print("[多跳 Step 2/3] LLM 提取关联实体...", file=sys.stderr)
    entities, reasoning = [], ""
    if api_key:
        entities, reasoning = extract_entities(question, round1, api_key)
    else:
        print("[WARN] 无 DEEPSEEK_API_KEY，跳过实体提取步骤", file=sys.stderr)

    trace.append({
        "step": 2,
        "action": "LLM 实体提取",
        "entities_found": entities,
        "reasoning": reasoning,
    })

    if not entities:
        print("[多跳] 未提取到新实体，跳过第二轮搜索", file=sys.stderr)
        return {
            "question": question,
            "results": round1[:N_RESULTS],
            "all_unique_results": round1,
            "trace": trace,
        }

    # Step 3: 基于实体进行第二轮搜索
    print(f"[多跳 Step 3/3] 基于 {len(entities)} 个实体进行第二轮搜索...", file=sys.stderr)
    entity_results = []
    for entity in entities[:5]:
        er = query_fulltext(entity, n=3)
        entity_results.extend(er)

    merged = deduplicate(round1 + entity_results)
    new_unique = deduplicate(entity_results)

    trace.append({
        "step": 3,
        "action": "实体驱动第二轮搜索",
        "entity_queries": entities[:5],
        "new_results_before_dedup": len(entity_results),
        "new_unique_results": len(new_unique),
        "total_after_merge": len(merged),
    })

    return {
        "question": question,
        "results": merged[:N_RESULTS],
        "all_unique_results": merged,
        "trace": trace,
    }


if __name__ == "__main__":
    args = sys.argv[1:]
    multi_hop = "--multi-hop" in args
    args = [a for a in args if a != "--multi-hop"]

    if not args:
        print(__doc__)
        sys.exit(1)

    question = " ".join(args)

    if multi_hop:
        result = multi_hop_query(question)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        results = query(question)
        print(json.dumps(results, ensure_ascii=False, indent=2))
```

- [ ] **Step 2: 验证查询（测试分块去重）**

```bash
cd ~/.claude/skills/LLM-Wiki管理工具
python3 scripts/wiki_vector_query.py "ChromaDB 崩溃原因"
```

Expected: 返回 JSON 结果，source="FAISS"，同一文件不重复出现。

- [ ] **Step 3: 验证多跳模式**

```bash
DEEPSEEK_API_KEY=$(grep DEEPSEEK ~/.zshrc | head -1 | cut -d= -f2-) \
python3 scripts/wiki_vector_query.py --multi-hop "FAISS 和 ChromaDB 的区别"
```

Expected: 有 trace 输出，包含 step 1/2/3。

---

### Task 3: 跑全量构建

**文件:**
- 修改: `wiki/vector_store/` 下所有文件（通过脚本自动生成）

**注意:** 这是长时间运行任务（~1.8 小时），需在 tmux 或后台运行。

- [ ] **Step 1: 先验证当前状态**

```bash
python3 ~/.claude/skills/LLM-Wiki管理工具/scripts/wiki_faiss_build.py --status
```

Expected: 显示当前 cache 有 2,305 文件（v1 格式会被自动迁移）。

- [ ] **Step 2: 启动全量增量构建**

```bash
cd ~/.claude/skills/LLM-Wiki管理工具
OMP_NUM_THREADS=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \
nohup python3 -u scripts/wiki_faiss_build.py --incremental \
  > /tmp/faiss_build.log 2>&1 &
echo "PID: $!"
```

- [ ] **Step 3: 监控进度（每分钟检查一次）**

```bash
tail -5 /tmp/faiss_build.log
```

Expected: 进度行显示 `[N/23668] X% | Y.Y files/s | ETA: ZmSs`.

- [ ] **Step 4: 构建完成后验证**

```bash
python3 ~/.claude/skills/LLM-Wiki管理工具/scripts/wiki_faiss_build.py --status
```

Expected: 约 23,668 文件，约 71K chunks，索引一致性 ✓。

- [ ] **Step 5: 验证查询质量**

```bash
python3 ~/.claude/skills/LLM-Wiki管理工具/scripts/wiki_vector_query.py "ChromaDB HNSW 索引损坏"
```

Expected: 返回相关结果，score > 0.6 的结果与 ChromaDB 话题相关。

---

### Task 4: 清理 ChromaDB

- [ ] **Step 1: 确认 FAISS 查询正常（最后检查）**

```bash
python3 ~/.claude/skills/LLM-Wiki管理工具/scripts/wiki_vector_query.py "LLM Wiki 知识库管理"
```

- [ ] **Step 2: 移动 ChromaDB 数据到废纸篓**

```python
import shutil, os
src = os.path.expanduser("~/.local/share/chromadb_knowledge")
dst = os.path.join(os.path.expanduser("~/.Trash"), "chromadb_knowledge")
if os.path.exists(src):
    shutil.move(src, dst)
    print(f"Moved chromadb_knowledge to ~/.Trash ({os.path.getsize(dst)/1024/1024/1024:.1f}GB freed)")
```

- [ ] **Step 3: 清理 vector_store 中的 ChromaDB 残留**

```bash
ls ~/Obsidian/20260520/wiki/vector_store/
```

删除这些 ChromaDB 残留目录（移到废纸篓）：
- `06c97c96-cb60-4331-9639-84c48601087c/`
- `7bdba940-51dd-4ded-812c-f41ce14e23d4/`
- `7f0cfb88-63f0-487c-aace-facce8d55438/`
- `chroma.sqlite3`
- `vector_index.json`

```python
import shutil, os
vs = "/Users/panbo/Obsidian/20260520/wiki/vector_store"
to_remove = [
    "06c97c96-cb60-4331-9639-84c48601087c",
    "7bdba940-51dd-4ded-812c-f41ce14e23d4",
    "7f0cfb88-63f0-487c-aace-facce8d55438",
    "chroma.sqlite3",
    "vector_index.json",
]
for f in to_remove:
    path = os.path.join(vs, f)
    if os.path.exists(path):
        shutil.move(path, os.path.join(os.path.expanduser("~/.Trash"), f))
        print(f"Moved: {f}")
```

---

### Task 5: 更新 SKILL.md

**文件:**
- 修改: `/Users/panbo/.claude/skills/LLM-Wiki管理工具/SKILL.md`

- [ ] **Step 1: 更新热区状态**

把 SKILL.md 第 17 行（热区 → Wiki 当前状态）替换为：

```markdown
**Wiki 当前状态**（2026-07-11）
- 已入库：23,668 source 页，ingested_files.json 20,232 条目
- **向量数据库**：FAISS v2（分块 + 批量编码 + checkpoint + 版本备份）。bge-m3，1024 维，~71K chunks。
- ChromaDB 已废弃删除（崩过 3 次，v2 统一到 FAISS）。
- **查询流程**：FAISS 向量搜索 → grep 补漏 → Tavily
- **Ingest 流程**：创建/更新 wiki 源页 → `wiki_faiss_build.py --incremental`
- 上次 lint：2026-07-09
```

- [ ] **Step 2: 更新 Gotchas 表**

删除 ChromaDB 相关陷阱行，更新 FAISS 行：

```markdown
| FAISS 索引构建 | 全量构建 ~1.8 小时，中断后自动从 checkpoint 续传。每 100 文件存一次 checkpoint + cache。 | 用 `--status` 查看进度，`--limit N` 测试 |
| sentence_transformers + Python 3.14 | joblib/loky 线程池在批量 embed 后泄漏 POSIX 信号量 | 脚本启动时清理 `/tmp/loky-*` + `OMP_NUM_THREADS=1 TOKENIZERS_PARALLELISM=false` |
| FAISS 版本备份 | 保留最近 3 次成功构建，查询自动 fallback .faiss → .faiss.1 → .2 → .3 | 无需手动干预 |
```

- [ ] **Step 3: 更新 Ingest 步骤 6（向量索引）**

将第 233-250 行的向量索引步骤替换为：

```markdown
6. **⚠️ 必做：向量索引本批次创建/更新的所有 wiki 文件**
   向量索引是 ingest 的必修课，不跑等于没入库。
   ```bash
   # 增量构建（仅索引新文件，自动 checkpoint）
   OMP_NUM_THREADS=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \
   python3 ~/.claude/skills/LLM-Wiki管理工具/scripts/wiki_faiss_build.py --incremental
   ```
   > 全量重建用 `--full`；测试用 `--limit N`；查看状态用 `--status`。
   > 中断后重跑同命令，自动从 checkpoint 续传。
```

- [ ] **Step 4: 更新 Query 步骤 1（向量搜索）**

将第 279-280 行的查询命令替换为：

```markdown
1. **向量搜索（优先）** — 用 FAISS 索引查询（自动 fallback 版本备份）。根据问题类型选择模式：

   标准模式（单文档问题）：
   ```bash
   python3 ~/.claude/skills/LLM-Wiki管理工具/scripts/wiki_vector_query.py "<问题>"
   ```

   多跳模式（跨文档推理）：
   ```bash
   python3 ~/.claude/skills/LLM-Wiki管理工具/scripts/wiki_vector_query.py --multi-hop "<问题>"
   ```
   > FAISS 索引自动 fallback：embedding.faiss → .faiss.1 → .faiss.2 → .faiss.3，永不空回。
```

---

## 完成检查

- [ ] `wiki_faiss_build.py --status` 显示 ~23,668 文件，~71K chunks，一致性 ✓
- [ ] `wiki_vector_query.py` 查询返回 FAISS 结果，无 ChromaDB 引用
- [ ] ChromaDB 数据已移到废纸篓
- [ ] vector_store 中无 ChromaDB 残留
- [ ] SKILL.md 已更新

---

## 执行日志

### 2026-07-12 上午 · 会话 `f52edae5`

**上溯会话**：`2dc6f55f`（2026-07-11 晚，设计+实现+启动构建）

**中断原因**：macOS 系统更新，凌晨自动重启，构建进程被杀。

**重启时状态**：
- cache: 3,210 文件 / 8,947 chunks
- FAISS 索引: 2,953 chunks（上次 rebuild 时 cache 只有 2,410 文件）
- checkpoint: `files_done=800`, `total_files=21258`, `last_file=-索罗斯们的民主梦-_2108.md`
- 索引 vs cache 不一致：cache 里有 8,947 chunks，但 FAISS 索引还停留在 2,953 chunks。**数据没丢，只是最后一次 rebuild 没来得及跑。**

**当前进度**（2026-07-12 12:18）：
- 在 Warp 终端续跑 `--incremental`
- 进程 PID 18564，内存 16GB，已跑 ~26 分钟
- 剩余 ~20,458 文件待 embed

**已完成任务**：
- [x] Task 1: 构建脚本 `wiki_faiss_build.py` v2（364 行）
- [x] Task 2: 查询脚本 `wiki_vector_query.py`（286 行，去 ChromaDB）
- [-] Task 3: 全量构建 — 🔄 进行中
- [ ] Task 4: 清理 ChromaDB — 等待构建完成
- [ ] Task 5: 更新 SKILL.md — 已部分更新（热区/Ingest/Query/Gotchas），ChromaDB 残留引用已清理

**本次会话操作**：
1. `--status` 确认中断点和数据完整性
2. 分析 cache vs FAISS 索引不一致的原因（rebuild 时机）
3. 在 Warp 终端续跑 `--incremental`
4. 更新 memory `20260711-faiss-pipeline-v2.md`
5. 更新 SKILL.md（`ChromaDB 向量索引` → `FAISS 向量索引`，构建时间 ~17h → ~1.8h）
6. 追加本执行日志