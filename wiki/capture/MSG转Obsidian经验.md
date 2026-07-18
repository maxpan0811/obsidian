---
title: MSG转Obsidian经验
type: capture
tags: [auto-capture, reference]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


## MSG → Obsidian MD 转换要点

### 工具
- `extract-msg` Python 库（pip3 install extract-msg）
- 转换脚本：`/tmp/convert_msg_to_md.py`

### 输出格式
- YAML frontmatter: title, source, from, to, date, tags
- 元数据引用块：发件人、收件人、日期
- 分隔线后接正文 body 内容

### 路径
- 源：`/Users/panbo/Documents/RAW/MSG/*.msg`
- 目标：`/Users/panbo/Library/Mobile Documents/iCloud~md~obsidian/Documents/20260520/老婆邮件/`

### 避坑
- MSG 文件名中的双空格/多余空格需归一化（`re.sub(r'\s+', ' ', name)`），否则 duplicate detection 失效
- 正文优先用 `msg.body`，回退到 `msg.htmlBody` 去标签
- `msg.to` 可能是 list，需要 `", ".join()` 处理
- sender 用 `str(msg.sender)` 转为字符串
