---
title: 一张图看懂 MCP
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/一张图看懂 MCP.md
tags: [evernote, impression, yinxiang]
---


![](.evernote-content/4633ED5A-57EE-4D28-BEC3-328CCF3CD0B9/ED98F1E3-71FA-4119-8CF9-80AFF4C2C443.png)

通过这张图可以看到，MCP 不是简单的“插件列表”，而是一套让 AI Agent 接入外部世界的标准协议。左侧是 AI Agent / Host，负责对话、推理和任务编排；中间是 MCP Client 和协议层，负责连接管理、初始化握手、能力发现、JSON-RPC 消息和传输方式；右侧是 MCP Server，把文件系统、数据库、API 服务和业务工具封装成可发现、可调用的能力。Agent 先知道有哪些 Tools、Resources 和 Prompts，再按权限调用对应 Server，并把结果带回上下文继续推理。

Close

Name cleared

Like the AuthorOther Amount

赞赏后展示我的头像

作品

暂无作品

Back

**Other Amount**

赞赏金额

¥

最低赞赏 ¥0

1

2

3

4

5

6

7

8


<!-- [摘要] 规则提取，如需全文请查看 vault 原始笔记 -->