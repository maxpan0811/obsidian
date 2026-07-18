---
title: rename-delete-old
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


重命名文件后，旧的原始文件不会自动删除，需要手动清理。

**场景：** 英语错题本的微信图片（Weixin Image_xxx.jpg）重命名为有序名称（英语-2026年-新东方Think2三阶段测试-P1~P7.jpg）后，老文件还留着，导致目录混乱且文件翻倍。

**Why:** 改名操作只是创建了新文件，原文件还在原位置，不会自动消失。

**How to apply:** 每次重命名一组文件后，确认原文件名已被新名覆盖，再删除原文件。核对文件大小可以帮助确认新旧是否同一批。
