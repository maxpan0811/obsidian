---
title: zhihu-pipeline-html-removed
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


**变更（2026-06-22）：** 知乎管线只输出 .md 格式，不再输出 .html。

**已执行：**
1. SKILL.md 删除全部 `--format html` 引用（5 处修改）
2. 删除 87 个有 .md 副本的 .html 文件 + 8 个已配对文件
3. 2 个纯 .html 文件（无 .md）转为 .md 后删除 html
4. `ingested_files.json` 中 106 条 `知乎管理工具/*.html` 路径更新为 `*.md`
5. 知乎目录最终状态：0 .html / 116 .md

**How to apply:** `fetch_batch.py` 默认已为 `--format md`，无需额外参数。
