---
title: evernote-deeplink-obsidian
type: capture
tags: [auto-capture, project]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


在 `local_sync.py` 的 `build_md()` 中新增了 `guid` 参数，每篇笔记末尾追加 `[📎 在印象笔记中打开]` 链接。

**链接格式：**
```
evernote:///view/{userId}/{shardId}/{guid}/{guid}/
```
其中 userId 是 `207087`（从印象笔记账户目录名获得），shardId 为 `s1`。

**验证结果：** 两种格式均经过测试：
- 短格式 `evernote:///view/{guid}` — 点击后打开印象笔记但未跳转到具体笔记 ❌
- 完整格式 `evernote:///view/207087/s1/{guid}/{guid}/` — 正确跳转到对应笔记 ✅

**效果：** 17,235 篇笔记末尾新增 `[📎 在印象笔记中打开]` 链接，与已有的 `[🌐 原始链接]` 并列。点击可直接从 Obsidian 跳转到印象笔记的原始笔记。

**Why：** 用户需要从 Obsidian 快速回到印象笔记查看原始内容（含图片、附件等），此前图片引用方案因 Obsidian 遍历符号链接导致白屏，折中方案是提供跳转链接而非直接显示图片。

**参考：** [[local-sync-symlink-image-pattern]]
