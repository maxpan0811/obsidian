---
title: fix-mcp-python-command
type: capture
tags: [auto-capture, reference]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


macOS (darwin-arm64) 系统只提供 python3，没有 python 命令。如果 MCP 服务器的 command 设为 python，会报错：
```
fetch: failed — Executable not found in $PATH: "python"
```

修复方法：用 `python3 -m mcp_server_fetch` 代替 `python -m mcp_server_fetch`（或 `claude mcp add fetch -s user -- python3 -m mcp_server_fetch`）。

同理适用于其他需要 python 命令的 MCP 服务器配置。安装 homebrew python 后也不会自动创建 python 符号链接（macOS 系统完整性保护），所以改 command 而非依赖符号链接更可靠。

**参考：** 修复步骤见 `~/.claude/rules/fix-mcp-python-command.md`

**相关：** [[reference_mcp_api]]
