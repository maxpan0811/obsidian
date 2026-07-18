---
title: feedback-evernote-token-7day
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


# 印象笔记 Token 7天更新周期

上次更新：2026-06-13（周日），下次过期：2026-06-20

印象笔记 Developer Token 有效期为 7 天，到期后必须手动刷新。

**更新地址**：https://app.yinxiang.com/api/DeveloperToken.action

**需要更新的位置**：
1. `~/.claude/skills/印象笔记管理工具/.env` — `EVERNOTE_TOKEN`
2. `~/.claude/skills/evernote-yinxiang/.env` — `YINXIANG_TOKEN`

**为什么**：Token 过期后保存笔记会报 `EDAMUserException(errorCode=9, parameter='authenticationToken')`，文章内容虽能正常抓取但无法保存到印象笔记。

**如何应用**：Token 过期前 1 天应主动提醒用户刷新。可用 `E=` 字段值（hex timestamp）解码判断剩余天数。
