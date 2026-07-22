---
name: yinxiang-biji-tongbu-guangxian
type: source
tags: [印象笔记, 同步管线, Obsidian, 笔记管理]
source_path: /Users/panbo/Obsidian/程序开发/印象笔记同步管线.md
---

[摘要]
印象笔记同步管线完整的开发记录，涵盖从2026年6月23日至7月14日的多次迭代。最初采用Thrift API的sync_favorites.py四步管线（List→Reconcile→Export→Verify），通过SQLite追踪状态、两阶段写入确保崩溃不丢状态。但Thrift API限流严重（约700次/15分钟），全量导出17k篇笔记需24-40小时。

2026年7月2日取得关键突破——发现印象笔记Mac客户端本地存储了完整的数据副本。本地SQLite（LocalNoteStore.sqlite）含17,183条活跃笔记的元数据，content/目录含49,808个子目录的完整ENML正文和图片文件。据此开发的local_sync.py纯本地读取，5分钟完成17k篇导出，零网络零限流。

后续迭代包括：符号链接引用图片（避免71GB附件拖垮Obsidian）、点号开头的符号链接避免Obsidian渲染崩溃、iCloud冲突副本保护（写入前退出Obsidian）、safe_title零宽字符修复等。最终实现Favorites 47,660篇 = .md文件完全一致。

另外记录了公众号文章通过CDP（Chrome DevTools Protocol）保存到印象笔记工作篮的方案，以及多个bug修复经验（ENML截断假阳性、update_note只UPDATE不INSERT、时间戳同步安全加固等）。

原文链接: /Users/panbo/Obsidian/程序开发/印象笔记同步管线.md