---
name: zhihu-guanli-gongju-tongbu-yu-bug-xiufu
type: source
tags: [知乎, 收藏夹, Obsidian, bug修复, 同步工具]
source_path: /Users/panbo/Obsidian/程序开发/知乎管理工具同步与Bug修复_2026-07-14.md
---

[摘要]
2026年7月14日执行知乎管理工具技能——同步知乎收藏夹（510261837）到Obsidian。同步状态：64篇待处理全部成功导出，0失败，0登录墙。最终对齐结果为知乎收藏夹153篇 = Obsidian 152篇 + 1篇无内容。

修复了两个关键Bug：

Bug 1（pending检测机制错误）：fetch_batch.py第352行用a['status'] == 'pending'判断待处理文章，但fetch_collection.py每次运行生成全新progress.json，所有文章status被重置为'pending'，之前已导出的'done'状态丢失。结果每次同步都重新导出所有文章，产生大量重复.md文件。修复为改用processed.json（URL持久化字典）查表判断：pending = [a for a in progress['articles'] if a['url'] not in processed_urls]。

Bug 2（Obsidian路径未迁移）：同步后文章被导出到旧的iCloud目录而非当前使用的/Users/panbo/Obsidian/目录。修复为fetch_batch.py默认路径从iCloud旧目录改为/Users/panbo/Obsidian/20260520。

清理因Bug1累积的14个重复.md文件至废纸篓。

原文链接: /Users/panbo/Obsidian/程序开发/知乎管理工具同步与Bug修复_2026-07-14.md