---
title: 用 Claude Code 搭一套 7×24 工作环境
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/用 Claude Code 搭一套 7×24 工作环境.md
tags: [evernote, impression, yinxiang]
---


来源：[打开原文](https://mp.weixin.qq.com/s/8e15DME8RMYMWzj0YvsG_g)

装好了 CLAUDE.md、Skills、Hooks，AI 能帮你干活了，但每次还得你先开口。7×24 的关键是你不在的时候它还能自己跑。

早上到公司，打开电脑，发现昨晚定的代码审查已经跑完了、PR 也提了、CI 也过了。你走之前设好了 5 层配置：cron 定时跑、Hooks 监听事件、Memory 记住了上次审到哪、tmux + SSH 让你在地铁上用手机看了一眼结果。5 层拼起来，Claude Code 就从"你叫才动"变成"自己会跑"。

这篇讲的方案全部基于 CLI + API key，不需要 claude.ai 账号登录。Routines、Remote Control、Channels 这些需要官方认证的功能，文末统一提一笔。

5 层都是什么，一张图看全
-------------

| 层 | 解决什么问题 | API key 用户能用的方案 |
| --- | --- | --- |
| 定时触发 | AI 自己醒来干活 | claude -p

<!-- [摘要] 规则提取，如需全文请查看 vault 原始笔记 -->