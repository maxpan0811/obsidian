---
title: feedback_evernote_export_network_hang
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


`evernote2` 的 Thrift 客户端在网络断开时会永久卡死（`getNote` 调用不返回，不抛异常，不响应 `socket.setdefaulttimeout`）。表现：脚本进程活着但连续 >5 分钟无输出，TCP 连接 `ESTABLISHED` 但无数据传输。

处理方式：
1. 脚本开头加 `socket.setdefaulttimeout(60)`
2. 创建 `run_export.py` 包装器，设 120s 超时并内联 token（绕过 `source .env` 失效问题）
3. 卡死时直接 `pkill -9 -f "export_favorite_html"` 然后重启——`processed.json` 记录进度，已处理的跳过

**Why:** 一次导出 2000+ 条笔记的网络环境不稳定，需要 kill + rerun 能安全断点续传的架构。

**How to apply:** 发现卡死 → 先检查 `pgrep -f "export_favorite_html"` 进程存活 + `tail -3` 输出文件 → 确认无新输出 >5 分钟 → pkill 重启 → 用 `run_export.py` 或 `EVERNOTE_TOKEN=... python3 -u scripts/export_favorite_html.py`。
