---
title: "别再用云会议工具了！24k Star 开源神器，录音、转录、AI摘要全本地搞定"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/别再用云会议工具了！24k Star 开源神器，录音、转录、AI摘要全本地搞定.md
tags: [印象笔记]
---


大家好，我是小黑，今天我们聊聊最近有点火的 Meetily，目前在 GitHub 24k Star，这个是 Zackriya Solutions 开源的 AI 会议助手，MIT 协议。

[🔗 原文链接](https://mp.weixin.qq.com/s/GldHdr7OJAmY2ZerVNPOrg)

它干的事很简单：录你电脑上的声音，本地转成文字，再用 AI 出摘要，所有东西都存在你自己机器上，不需要同意什么乱七八糟的隐私政策，数据不会跑到别人的服务器。

![](.evernote-content/CD7394F7-5132-4BC7-A5C5-AFE6BCFA631A/4242062D-2877-4EC7-B0D4-AB810E9C3E15)

简介

Meetily 是一个桌面端应用，macOS 和 Windows 有安装包，Linux 需要源码编译。它直接抓取系统音频和麦克风，本地完成转录和摘要，转录引擎用 Whisper.cpp 或 NVIDIA Parakeet，摘要接 Ollama 本地模型。数据存在本地 SQLite，向量检索用 VectorDB。

市面上类似

<!-- [摘要] 规则提取，如需全文请查看 vault 原始笔记 -->