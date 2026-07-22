---
name: mubu-quanliang-daochu-dao-obsidian
type: source
tags: [幕布, 笔记迁移, Obsidian, 工具使用]
source_path: /Users/panbo/Obsidian/程序开发/幕布全量导出到Obsidian_20260718.md
---

[摘要]
将幕布（mubu.com）全部文档迁移到Obsidian的操作记录。方案选型对比了手动导出OPML再转换和skillhub mubu-integration skill v1.3.6两个方案，最终采用后者。

mubu-integration skill自带CLI工具，支持API批量拉取和双层往返（Markdown↔幕布大纲），省去手动导出OPML再转换的步骤。安装后配置凭据文件~/.workbuddy/.env.mubu，使用Python CLI列出文档并批量导出。

导出结果：137个.md文件，分布在根目录（28个）、个人娱乐学习（13个）、孩子学习相关（6个）、华程工作资料存档（85个）、动漫视频+音乐（5个）。每个文档带YAML frontmatter（title + source: 幕布），幕布大纲的层级结构保持完整。

最终路径为用户手动从程序开发/随笔/幕布存档/移入~/Obsidian/20260520/幕布存档/。如需后续增量同步，可复用mubu-integration skill的API接口，该skill也支持Markdown到幕布的导入（双向）。

原文链接: /Users/panbo/Obsidian/程序开发/幕布全量导出到Obsidian_20260718.md