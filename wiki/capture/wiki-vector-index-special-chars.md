---
title: wiki-vector-index-special-chars
type: capture
tags: [auto-capture, reference]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


# 含特殊字符文件名的 ChromaDB 向量索引

## 问题
`wiki_vector_ingest.py` 通过 shell 接受文件路径参数。文件名含 `#`、`@`、`[`、`]`、空格等特殊字符时，shell 将其解释为注释标记、单词分隔或通配符，导致文件路径被切碎成多个无效参数。

## 解法
用 Python subprocess 以 list 传参，完全绕过 shell 解析：

```python
import subprocess, sys, os

ingest_script = os.path.expanduser("~/.claude/skills/LLM-Wiki管理工具/scripts/wiki_vector_ingest.py")

# 文件列表（正常Python list，无需 shell escaping）
files = ["# 新中国电影往事 #.md", "1.6K 太赞了 !!! 让你的Windows桌面美到爆炸.md", ...]
file_paths = [os.path.join(src_dir, f) for f in files]

env = dict(os.environ)
env["HF_HUB_OFFLINE"] = "1"  # 离线模式，不重连 HF

result = subprocess.run(
    [sys.executable, ingest_script] + file_paths,  # 列表传参！
    capture_output=False,
    env=env,
    timeout=1800  # 30 分钟超时
)
```

## 关键点
- `subprocess.run` 的 `args` 参数传 list → Python 直接调用 execve，不走 shell → 文件名原样传递
- `capture_output=false` → 实时输出进度到终端
- `HF_HUB_OFFLINE=1` → 防止因网络限制导致 bge-m3 模型加载失败

## 性能
185 个含特殊字符的文件，subprocess 单次调用 + 脚本内 BATCH_SIZE=8 批处理，耗时约 6-8 分钟（含模型加载）。

## 替代方案对比
| 方案 | 优点 | 缺点 |
|------|------|------|
| subprocess list args ✅ | 最小改动，复用现有脚本 | 每次调用加载一次模型 |
| 内嵌 Python 直接调 ChromaDB | 模型只加载一次，可全程 inline | 需复制 chunk/embed 逻辑，代码量翻倍 |
| xargs -0 + find -print0 | 也算可靠 | 文件名含换行符时仍有风险 |
