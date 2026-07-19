---
name: evernote-dedup-before-save
description: 保存信息到印象笔记前必须先搜索已有笔记——对比内容是否重复，新资料才保存，已有则跳过或追加
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d2b21803-0b6a-4389-bc5e-65e82e404e5f
---

# 印象笔记保存前必须去重

## 规则
1. 保存前先用 `search-notes.sh` 搜索关键词，查看已有笔记
2. 用 `get-note-detail.sh` 检查内容（字段名是 `content`，不是 `noteContent`）
3. 如果内容已存在 → 跳过或追加到已有笔记
4. 如果是新内容 → 保存到新笔记
5. AI 整理的总结笔记命名加 `[Claude总结]` 前缀，与原始资料区分

## 踩坑
- get-note-detail 的 content 字段在 `data.dataDetail.content`，不是 `noteContent`
- 之前误以为11篇NeXTSTEP文章全是空的，实际是字段名搞错了
- 必须用完整 GUID（带连字符的36位），不能用截断的8位

**Why:** 避免重复保存，保持印象笔记整洁。用户明确说了"跟已有的做比较，没有的才保存"。

**How to apply:** 任何保存到印象笔记的操作，先搜索→对比→决定保存/追加/跳过。
