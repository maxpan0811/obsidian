---
title: local-sync-reconcile-complete-20260706
type: capture
tags: [auto-capture, project]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


**对账结果：** 2026-07-06 最终对账，Favorites 17231 篇 vs .md 文件 17231 篇，完全对齐。

**执行操作：**
1. 清理 16K 残留 `.md` 文件（文件重名 ` 2` 后缀的残留，来自 macOS iCloud 同步产生的重复）
2. 移除 6 篇不匹配的 .md（派评旧标题、济南未同步笔记残留、围棋证书旧标题）
3. 重复标题笔记全部移入 temp → 用户处理后移回 Favorites（重命名加 `-1`、`-2` 后缀）
4. "老婆的小贷问题汇总"从附件笔记恢复为普通笔记——本地 SQLite ZENRESOURCE 仍记录有 PDF 附件（未同步），需手动清除 local_db 状态后强制导出

**关键发现：**
- 本地 SQLite 中的 ZENRESOURCE 不会实时同步——用户在云端删除附件后，本地可能仍残存旧的资源记录。local_sync.py 的 doc 检测逻辑会误判。处理方式：清除 local_db 状态，手动导出嵌入文本内容（非附件部分）
- .md 文件数浮动原因：二进制搜索调试时 `/tmp/` 和 vault 间来回移动文件，部分文件残留

参考：[[evernote-deeplink-obsidian]]
