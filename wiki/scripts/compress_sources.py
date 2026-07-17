#!/usr/bin/env python3
"""
wiki/sources/ 全文→摘要压缩脚本（规则提取，不经过LLM）。
已完成全量压缩。如需重新跑，先删除 .compress_state.json

用法:
  python3 compress_sources.py               # 全量压缩（可中断重入）
  python3 compress_sources.py --dry-run      # 只统计，不改写
"""
import os, re, sys, json, time

SRC_DIR = "/Users/panbo/Obsidian/20260520/wiki/sources"
DRY_RUN = "--dry-run" in sys.argv

# 状态文件：记录已处理文件，支持断点续跑
STATE_FILE = os.path.join(SRC_DIR, ".compress_state.json")

# 结果统计
stats = {
    "total": 0, "skipped_empty": 0, "had_summary": 0,
    "extracted": 0, "short": 0, "errors": 0,
    "already_done": 0,
}


def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE) as f:
            return set(json.load(f).get("done", []))
    return set()


def save_state(done_set):
    tmp = STATE_FILE + ".tmp"
    with open(tmp, "w") as f:
        json.dump({"done": sorted(done_set)}, f)
    os.replace(tmp, STATE_FILE)


def extract_summary_from_text(text: str) -> str | None:
    """规则提取摘要。"""
    # 1. 找 速读摘要 / 智能摘要 区
    for marker in ["速读摘要", "智能摘要"]:
        idx = text.find(marker)
        if idx >= 0:
            # 从 marker 开始到 "原文约" 或下一个 "---" 或 "#"
            end_markers = ["\n原文约", "\n---\n", "\n#"]
            end = len(text)
            for em in end_markers:
                ei = text.find(em, idx + len(marker))
                if ei > 0 and ei < end:
                    end = ei
            summary = text[idx:end].strip()
            # 截取 600 字以内
            if len(summary) > 600:
                summary = summary[:600]
            return summary
    return None


def compress_file(filepath: str) -> tuple[bool, str]:
    """
    处理单文件。返回 (changed, summary_or_empty)
    changed=False 表示无改动（已压缩过或错误）
    """
    with open(filepath) as f:
        text = f.read()

    if not text.strip():
        stats["skipped_empty"] += 1
        return False, ""

    # 分割 YAML frontmatter
    parts = text.split("---", 2)
    if len(parts) < 3 or parts[0].strip() != "":
        # 没有标准 YAML → 跳过
        stats["errors"] += 1
        return False, ""

    yaml_part = parts[1]
    body = parts[2].strip()

    # 检查是否已经压缩过（body 很短且含有 [摘要] 标记 或 body < 500 字）
    if len(body) < 800 and "速读摘要" not in body and "智能摘要" not in body and (
        "[摘要]" in text or body.count("\n") < 10
    ):
        body_lower = body.lower()
        if any(tag in body_lower for tag in ["原文约", "建议阅读"]):
            pass  # 还是全文，需要处理
        else:
            stats["already_done"] += 1
            return False, ""

    # 提取摘要
    summary = extract_summary_from_text(body)
    yinxiang_summary = None

    if summary:
        stats["had_summary"] += 1
    else:
        # 无现成摘要 → 取首 500 字正文（跳过头部的原文链接/大图引用）
        body_clean = body.strip()
        # 去掉开头的 # 标题行（已在 YAML 中）
        lines = body_clean.split("\n")
        content_start = 0
        for i, line in enumerate(lines[:10]):
            stripped = line.strip()
            # 跳过空行、标题、原文链接分隔线
            if stripped == "" or stripped.startswith("#") or stripped == "---":
                content_start = i + 1
            elif stripped.startswith("原文链接"):
                content_start = i + 1
            elif stripped.startswith("Original"):
                content_start = i + 1
            elif re.match(r'^\[!\[', stripped):
                content_start = i + 1
            else:
                break
        body_trimmed = "\n".join(lines[content_start:]).strip()
        # 取 500 字
        summary = body_trimmed[:500]
        stats["extracted"] += 1

    # 检查是否太短（< 30 字 = 没啥内容）
    if len(summary.strip()) < 30:
        stats["short"] += 1
        return False, ""

    # 提取原文链接
    orig_link = ""
    link_match = re.search(r'原文链接:\s*(https?://\S+)', body)
    if link_match:
        orig_link = link_match.group(1)

    # 构建新内容
    new_body_parts = []
    if orig_link:
        new_body_parts.append(f"原文链接: {orig_link}")
    new_body_parts.append("")
    new_body_parts.append(summary)
    new_body_parts.append("")
    new_body_parts.append("<!-- [摘要] 规则提取，如需全文请查看 vault 原始笔记 -->")
    new_body = "\n".join(new_body_parts)

    new_text = f"---{yaml_part}---\n\n{new_body}"

    if not DRY_RUN:
        with open(filepath, "w") as f:
            f.write(new_text)

    return True, summary


def main():
    done_set = load_state()
    files = sorted([f for f in os.listdir(SRC_DIR) if f.endswith(".md")])
    total = len(files)

    # 排除状态文件中已记录的
    pending = [f for f in files if f not in done_set]

    if DRY_RUN:
        print(f"[DRY RUN] 共 {total} 文件, {len(done_set)} 已处理, {len(pending)} 待处理")

    t_start = time.time()

    for i, fname in enumerate(pending):
        fpath = os.path.join(SRC_DIR, fname)
        try:
            changed, _ = compress_file(fpath)
        except Exception as e:
            print(f"  ERROR: {fname}: {e}")
            stats["errors"] += 1
            continue
        finally:
            done_set.add(fname)

        stats["total"] += 1

        if not DRY_RUN and (i + 1) % 500 == 0:
            save_state(done_set)
            elapsed = time.time() - t_start
            rate = (i + 1) / elapsed if elapsed > 0 else 0
            eta = (len(pending) - i - 1) / rate if rate > 0 else 0
            print(f"  [{i+1}/{len(pending)}] {rate:.0f} files/s | "
                  f"ETA: {eta/60:.0f}m{eta%60:.0f}s | "
                  f"done={len(done_set)}")

    if not DRY_RUN:
        save_state(done_set)

    elapsed = time.time() - t_start
    print(f"\n{'='*50}")
    print(f"完成！")
    print(f"  总文件: {total}")
    print(f"  本次处理: {len(pending)}")
    print(f"  已有摘要: {stats['had_summary']}")
    print(f"  首段提取: {stats['extracted']}")
    print(f"  过短跳过: {stats['short']}")
    print(f"  错误: {stats['errors']}")
    print(f"  耗时: {elapsed/60:.1f} 分钟")


if __name__ == "__main__":
    main()