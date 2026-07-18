---
title: local-sync-discovered-20260702
type: capture
tags: [auto-capture, reference]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


2026-07-02 发现印象笔记 Mac 客户端将所有数据存储在本地，可直接读取导出到 Obsidian。

## 本地数据位置

```
~/Library/Application Support/com.yinxiang.Mac/accounts/app.yinxiang.com/207087/
├── localNoteStore/LocalNoteStore.sqlite  ← CoreData 数据库
│   ├── ZENNOTE       — 笔记（ZGUID, ZLOCALUUID, ZTITLE, ZNOTEBOOK）
│   ├── ZENNOTEBOOK   — 笔记本（Z_PK, ZGUID, ZNAME）
│   └── ZENRESOURCE   — 资源（ZGUID, ZMIME, ZFILENAME, ZDATAHASH, ZNOTE）
└── content/{ZLOCALUUID}/
    ├── content.enml         ← ENML 格式正文（和 Thrift 返回的完全一致）
    ├── {resource_guid}.jpg  ← 图片文件（直接是原始文件）
    └── snippet.txt / card.png / quickLook.png / snippet.tiff  ← 缩略图（忽略）
```

## 映射关系

| 概念 | Evernote API | 本地数据库 |
|------|-------------|-----------|
| 笔记唯一ID | GUID | `ZGUID` |
| 本地目录 | — | `ZLOCALUUID`（UUID 格式，内容目录名） |
| 标题 | title | `ZTITLE` |
| 正文 | getNote 返回的 ENML | `content/{uuid}/content.enml`（完全一致的 XML） |
| 资源 | getNote.resources[].data.body（二进制） | `content/{uuid}/{resource_guid}.ext`（原始文件） |
| en-media hash | `<en-media hash="...">` | `ZENRESOURCE.ZDATAHASH`（hex 编码） |
| 笔记本归属 | notebookGuid | `ZENNOTE.ZNOTEBOOK → ZENNOTEBOOK.Z_PK → ZGUID` |
| 活跃状态 | — | `ZACTIVE=1` 为活跃笔记 |

## 关键发现

- 本地 DB 中 Favorites 有 **17,183 条活跃笔记**（Thrift API 报 17,421，差异可能为同步延迟）
- 文件系统上 49,808 个 content 目录（含已删除和历史版本）
- `content.enml` 是完整的 ENML XML，包含 `<en-media>` 标签
- 图片文件以资源 GUID 命名，扩展名与原始文件一致
- `ZENRESOURCE.ZDATAHASH`（hex）与 en-media 的 `hash` 属性对应（小写）

## 优势

**不需要 Evernote Token、不调用云 API、不限流、不掉速**。直接从本地文件系统读取并复制到 Obsidian，机器速度。

## 局限性

- 无法将笔记移入 temp 笔记本（需要 Thrift API 的 updateNote）
- 仅限于已同步到本地的笔记（印象笔记 Mac 默认全量同步）

**Why：** 之前的 sync_favorites.py/fast_export.py 全部依赖 Thrift API，受限于约 700 次/窗口的限流。本地同步消除了这一瓶颈。

**How to apply：** 后续优先使用 local_sync.py，只在需要修改 Evernote 端数据（移动笔记本、删除）时才回退到 Thrift API。
