---
title: 掀Claude Code的桌子！Codex 一键搬家功能
type: source
created: 2026-06-27
updated: 2026-06-27
source_path: 印象笔记管理工具/掀Claude Code的桌子！Codex 一键搬家功能.md
tags: [evernote, impression]
---

---
title: "掀Claude Code的桌子！Codex 一键搬家功能"
source: evernote
type: note
export_date: 2026-06-22
guid: 7a5bd625-bd7e-458b-91fd-51e55e845611
---

# 掀Claude Code的桌子！Codex 一键搬家功能

来源：[打开原文](https://mp.weixin.qq.com/s/oT5wAI_zRZlX4ic4QftHEQ)

## 掀Claude Code的桌子！Codex 一键搬家功能

Codex CLI 0.140.0 做了一些比较重要的更新。

最重要的一条：Codex 同步在 CLI 和桌面 App 里上线了从 Claude Code 导入的功能。

CLI 端用 `/import` 触发，可以选择性导入 Claude Code 的 setup、项目配置和最近的聊天记录。

桌面 App 那边更完整更方便，进 Settings 点 "Import other agent setup"，Codex 自动扫描本机的 Claude Code 配置。

迁移的内容包含完整的skills、hooks、MCP servers、subagents、instruction files、30 天 session 历史，能自动转的直接转，转不了的可以开一个跟进对话让 AI 引导手动补齐。

连Claude Code 独占的`CLAUDE.md` 也会被直接识别成 `AGENTS.md` 导入进去。

新版本还增加了其他的有用功能：

用量可视化

新增 `/usage` 命令，支持查看每日、每周和累计的 token 消耗。重度用户之前对自己烧了多少 token 基本没感知，现在有了直接的数字参照。

@ 统一入口

输入 `@` 现在默认打开统一的 mentions 菜单，文件、插件、技能在一个入口里选，之前这三个入口是分散的。

`/goal` 增强

`/goal` 现在可以保留超大文本、大段粘贴内容和图片附件，包括在远程 app-server session 中也能保持。之前粘贴大块内容进 goal 容易丢失，这次补上了。

有关于 /goal 的详细使用，可以查看我的专栏AI编程高效开发指南中的Codex&Claude Code的 /goal 指令的高级进阶使用技巧

最后，大仓库和长 session 的响应速度也有提升，保留了 Git 内置文件系统监视器，避免重复读取历史记录。
