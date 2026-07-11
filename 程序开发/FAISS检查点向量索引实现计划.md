# FAISS 检查点向量索引 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace ChromaDB 向量检索为 FAISS + 检查点机制，实现崩溃后快速恢复

**Architecture:** 
- 新建 `wiki_faiss_build.py` 负责构建 FAISS 索引（嵌入缓存 + 原子写入 + 检查点）
- 修改 `wiki_vector_query.py` 搜索后端从 ChromaDB 切换为 FAISS（自动 fallback 到 .bak）
- ChromaDB 保留为可选 fallback 路径，不卸载

**Tech Stack:** Python 3, faiss-cpu, sentence_transformers (bge-m3), numpy

## Global Constraints

- bge-m3 模型必须离线加载（`HF_HUB_OFFLINE=1`）
- 所有文件写入必须通过临时文件 → rename 实现原子性
- 索引文件位于 `wiki/vector_store/` 下
- 查询时自动 fallback：embedding.faiss → embedding.faiss.bak → ChromaDB（兜底）

---

### Task 1: 安装 faiss-cpu + 验证

**Files:**
- Modify: 无（系统级依赖安装）

- [ ] **Step 1: 安装 faiss-cpu**

```bash
pip3 install faiss-cpu
```

- [ ] **Step 2: 验证可用**

```bash
python3 -c "
import faiss
import numpy as np
d = 1024  # bge-m3 维度
index = faiss.IndexFlatL2(d)
index.add(np.random.rand(10, d).astype(np.float32))
D, I = index.search(np.random.rand(1, d).astype(np.float32), 3)
print(f'faiss version: {faiss.__version__}')
print(f'search ok: {I.shape}')
"
```

Expected output: version string + shape (1, 3)

---

### Task 2: 创建 wiki_faiss_build.py

**Files:**
- Create: `~/.claude/skills/LLM-Wiki管理工具/scripts/wiki_faiss_build.py`

**This task:** 构建 FAISS 索引、嵌入缓存管理、原子写入、检查点。

- [ ] **Step 1: 脚本框架 + 参数解析**

```bash
touch ~/.claude/skills/LLM-Wiki管理工具/scripts/wiki_faiss_build.py
chmod +x ~/.claude/skills/LLM-Wiki管理工具/scripts/wiki_faiss_build.py
```

写入以下完整实现：

```python
#!/usr/bin/env python3
"""
FAISS 向量索引构建器（原子写入 + 检查点）。
替代 ChromaDB 的向量写入路径。

用法:
  python3 wiki_faiss_build.py --incremental   # 增量（仅新文件）
  python3 wiki_faiss_build.py --full          # 全量重建
  python3 wiki_faiss_build.py --status        # 查看索引状态
"""
import os, sys, pickle, argparse, time
from pathlib import Path
import numpy as np
import faiss
import sentence_transformers as st

VAULT = "/Users/panbo/Obsidian/20260520"
VECTOR_DIR = os.path.join(VAULT, "wiki/vector_store")
CACHE_FILE = os.path.join(VECTOR_DIR, "embedding_cache.pkl")
FAISS_FILE = os.path.join(VECTOR_DIR, "embedding.faiss")
FAISS_BAK = os.path.join(VECTOR_DIR, "embedding.faiss.bak")
META_FILE = os.path.join(VECTOR_DIR, "metadata.pkl")
SRC_DIR = os.path.join(VAULT, "wiki/sources")

os.makedirs(VECTOR_DIR, exist_ok=True)


def _load_cache() -> dict:
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "rb") as f:
            return pickle.load(f)
    return {}


def _save_cache(cache: dict):
    tmp = CACHE_FILE + ".tmp"
    with open(tmp, "wb") as f:
        pickle.dump(cache, f)
    os.replace(tmp, CACHE_FILE)


def _atomic_write_faiss(index, path: str):
    tmp = path + ".tmp"
    faiss.write_index(index, tmp)
    os.replace(tmp, path)


def _atomic_write_meta(metadata: list, path: str):
    tmp = path + ".tmp"
    with open(tmp, "wb") as f:
        pickle.dump(metadata, f)
    os.replace(tmp, path)


def _scan_source_files() -> list:
    files = []
    for f in sorted(os.listdir(SRC_DIR)):
        if not f.endswith(".md"):
            continue
        fpath = os.path.join(SRC_DIR, f)
        if os.path.getsize(fpath) < 50:
            continue
        files.append((f, fpath))
    return files


def build_incremental(model=None):
    if model is None:
        model = st.SentenceTransformer("BAAI/bge-m3", local_files_only=True)
    
    cache = _load_cache()
    files = _scan_source_files()
    
    new_files = [(name, path) for name, path in files if name not in cache]
    existing = [(name, path) for name, path in files if name in cache]
    
    print(f"Total source files: {len(files)}")
    print(f"Cached: {len(cache)}, New: {len(new_files)}")
    
    if not new_files:
        print("No new files to embed. Rebuilding index from cache...")
    else:
        for name, path in new_files:
            with open(path) as fh:
                text = fh.read()
            text = text.split("---", 2)
            text = text[2] if len(text) > 2 else text[0]
            text = text.strip()
            if not text:
                continue
            emb = model.encode(text).astype(np.float32)
            cache[name] = emb
            print(f"  embed: {name}")
        _save_cache(cache)
    
    # Build FAISS index
    if not cache:
        print("No embeddings in cache, nothing to build")
        return
    
    dim = list(cache.values())[0].shape[0]
    names = []
    embeddings = []
    for name, path in files:
        if name in cache:
            names.append(name)
            embeddings.append(cache[name])
    
    embs = np.array(embeddings, dtype=np.float32)
    index = faiss.IndexFlatIP(dim)
    index.add(embs)
    
    # Metadata mapping: index position → filename
    metadata = names
    
    _atomic_write_faiss(index, FAISS_FILE)
    _atomic_write_meta(metadata, META_FILE)
    
    # Update checkpoint
    if os.path.exists(FAISS_FILE):
        _atomic_write_faiss(index, FAISS_BAK)
    
    print(f"\nFAISS index built: {len(names)} vectors")
    print(f"Index dim: {dim}")
    print(f"Files: {FAISS_FILE}, {META_FILE}, {FAISS_BAK}")


def build_full():
    model = st.SentenceTransformer("BAAI/bge-m3", local_files_only=True)
    cache = {}
    files = _scan_source_files()
    
    print(f"Full rebuild: {len(files)} files...")
    for name, path in files:
        with open(path) as fh:
            text = fh.read()
        text = text.split("---", 2)
        text = text[2] if len(text) > 2 else text[0]
        text = text.strip()
        if not text:
            continue
        emb = model.encode(text).astype(np.float32)
        cache[name] = emb
    
    _save_cache(cache)
    build_incremental(model)
    print("Full rebuild complete")


def show_status():
    cache = _load_cache()
    print(f"Embedding cache: {len(cache)} files")
    for f in [FAISS_FILE, FAISS_BAK, META_FILE]:
        if os.path.exists(f):
            sz = os.path.getsize(f)
            print(f"  {Path(f).name}: {sz / 1024:.1f} KB")
        else:
            print(f"  {Path(f).name}: NOT FOUND")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--incremental", action="store_true", help="增量模式（仅新文件）")
    parser.add_argument("--full", action="store_true", help="全量重建")
    parser.add_argument("--status", action="store_true", help="查看索引状态")
    args = parser.parse_args()
    
    if args.status:
        show_status()
    elif args.full:
        build_full()
    else:
        build_incremental()
```

- [ ] **Step 2: 验证脚本运行**

```bash
cd ~/.claude/skills/LLM-Wiki管理工具/scripts
HF_HUB_OFFLINE=1 python3 wiki_faiss_build.py --status
```

Expected: Shows cache count + file sizes (may be 0 for first run)

- [ ] **Step 3: 初次全量构建**

```bash
cd ~/.claude/skills/LLM-Wiki管理工具/scripts
HF_HUB_OFFLINE=1 python3 wiki_faiss_build.py --incremental
```

Expected: Processes all source files, creates embedding_cache.pkl + embedding.faiss + metadata.pkl + embedding.faiss.bak

---

### Task 3: 修改 wiki_vector_query.py

**Files:**
- Modify: `~/.claude/skills/LLM-Wiki管理工具/scripts/wiki_vector_query.py`

目标：搜索路径从 ChromaDB 改为 FAISS fallback chain。

- [ ] **Step 1: 添加 FAISS 加载和搜索函数**

在 `wiki_vector_query.py` 中添加以下代码（在文件开头 `import` 块之后）：

```python
# ---- FAISS 加载（自动 fallback） ----
VECTOR_DIR = os.path.join(os.path.dirname(__file__), "..", "wiki/vector_store")  # 不准确，稍后修正

# 实际路径硬编码（和 SKILL.md 的 vault 路径一致）
FAISS_VAULT = "/Users/panbo/Obsidian/20260520"
FAISS_VECTOR_DIR = os.path.join(FAISS_VAULT, "wiki/vector_store")
FAISS_FILE = os.path.join(FAISS_VECTOR_DIR, "embedding.faiss")
FAISS_BAK = os.path.join(FAISS_VECTOR_DIR, "embedding.faiss.bak")
META_FILE = os.path.join(FAISS_VECTOR_DIR, "metadata.pkl")

def _load_faiss_index():
    """加载 FAISS 索引，自动 fallback 到 .bak"""
    for path in [FAISS_FILE, FAISS_BAK]:
        if os.path.exists(path):
            try:
                return faiss.read_index(path)
            except Exception as e:
                print(f"  FAISS load warning ({path}): {e}", file=sys.stderr)
                continue
    return None


def _load_faiss_metadata():
    """加载 FAISS 元数据"""
    if os.path.exists(META_FILE):
        with open(META_FILE, "rb") as f:
            return pickle.load(f)
    return None
```

- [ ] **Step 2: 修改 `query()` 函数**

将现有的 `query()` 函数改为 FAISS 优先：

```python
def query(q: str, n: int = N_RESULTS) -> list[dict]:
    """向量搜索，FAISS 优先，ChromaDB 兜底。"""
    model = st.SentenceTransformer("BAAI/bge-m3", local_files_only=True)
    
    # 1. 尝试 FAISS
    index = _load_faiss_index()
    metadata = _load_faiss_metadata()
    
    if index is not None and metadata is not None:
        embedding = model.encode(q).astype(np.float32)
        D, I = index.search(np.array([embedding]), n)
        
        results = []
        for idx, score in zip(I[0], D[0]):
            if idx < 0 or idx >= len(metadata):
                continue
            fname = metadata[idx]
            fpath = os.path.join(FAISS_VAULT, "wiki/sources", fname)
            snippet = ""
            if os.path.exists(fpath):
                with open(fpath) as f:
                    snippet = f.read()[:500]
            results.append({
                "filename": fname,
                "path": fpath,
                "score": float(score),
                "snippet": snippet,
            })
        return results
    
    # 2. 降级到 ChromaDB
    print("  FAISS 不可用，降级到 ChromaDB...", file=sys.stderr)
    try:
        client = PersistentClient(CHROMA_DIR)
        col = client.get_collection("all_docs")
        embedding = model.encode(q).tolist()
        chroma_results = col.query(query_embeddings=[embedding], n_results=n)
        # ... 原有 ChromaDB 结果格式化
    except Exception as e:
        print(f"  ChromaDB 也失败: {e}", file=sys.stderr)
        return []
```

**需要修改第 2 步函数签名**——当前函数进行 ChromaDB 查询并返回格式化结果。实际修改时需完整替换。保留原有的 ChromaDB 查询代码作为降级路径。

- [ ] **Step 3: 验证查询**

```bash
cd ~/.claude/skills/LLM-Wiki管理工具/scripts
HF_HUB_OFFLINE=1 python3 -c "
from wiki_vector_query import query
results = query('中国工业', n=3)
for r in results:
    print(f\"  {r['filename']}: {r['score']:.3f}\")
"
```

Expected: 返回 3 条结果，得分在 0.3-0.9 范围

---

### Task 4: 更新 SKILL.md 和 log.md

**Files:**
- Modify: `~/.claude/skills/LLM-Wiki管理工具/SKILL.md`
- Modify: `/Users/panbo/Obsidian/20260520/wiki/log.md`

- [ ] **Step 1: 检查最新的 vault 路径**

```bash
ls /Users/panbo/Obsidian/20260520/wiki/vector_store/
```

If `embedding.faiss` exists, proceed.

- [ ] **Step 2: 更新 SKILL.md 中的查询流程**

SKILL.md 中 `### Query（查询）` 部分目前描述 ChromaDB 向量搜索：

找到 `### Query（查询）` 段落的 "向量搜索（优先）" 子段落，在第一行后追加 FAISS 说明：

```markdown
> **向量后端已切换为 FAISS + 检查点机制**。索引文件位于 `wiki/vector_store/`。
> 查询自动 fallback：`embedding.faiss` → `embedding.faiss.bak` → ChromaDB。
> 索引构建使用 `scripts/wiki_faiss_build.py --incremental`。
```

- [ ] **Step 3: 更新 SKILL.md 中的 build 流程**

在 SKILL.md 的 `### Ingest（新增源）` 部分或新建小节：

```markdown
### 向量索引构建（FAISS）

使用 `scripts/wiki_faiss_build.py` 构建 FAISS 向量索引（替代 ChromaDB 写入路径）：

- `--incremental`（默认）— 仅对新文件 embed，重建 FAISS 索引（推荐日常用）
- `--full` — 全量重建（模型升级或 cache 损坏时用）
- `--status` — 查看索引状态

**检查点保护**：索引文件通过原子 rename 写入，成功时自动备份 `.bak`。
查询时自动 fallback：`.faiss` → `.bak` → ChromaDB，永不空回。
```

- [ ] **Step 4: 追加 log.md**

```bash
cat >> /Users/panbo/Obsidian/20260520/wiki/log.md << 'LOGEOF'

## 2026-07-10 FAISS 检查点向量索引切换

- **替代**: ChromaDB → FAISS + 原子写入 + .bak 检查点
- **新建脚本**: scripts/wiki_faiss_build.py（增量/全量构建）
- **修改**: wiki_vector_query.py（FAISS 优先搜索）
- **索引文件**: wiki/vector_store/{embedding.faiss, embedding.faiss.bak, metadata.pkl, embedding_cache.pkl}
- **崩溃恢复**: 查询自动 fallback .bak，无需全量重建
LOGEOF
```
