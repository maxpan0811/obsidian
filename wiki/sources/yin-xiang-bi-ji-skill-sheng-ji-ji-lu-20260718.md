---
name: yin-xiang-bi-ji-skill-sheng-ji-ji-lu-20260718
type: source
tags: [claude-code, yinxiang, evernote, skill-upgrade]
source_path: /Users/panbo/Obsidian/程序开发/印象笔记Skill升级记录20260718.md
---

[摘要]
本文记录了2026年7月18日印象笔记evernote-yinxiang skill从v1.0.3升级到v1.0.4的完整过程。

触发流程：用户看到印象笔记公众号文章（2026-07-18）宣称新版Skill新增更新笔记、创建标签、创建笔记本、按时间/标签/笔记本搜索等能力，要求核实本地skill是否有新版。核实发现本地_meta.json中版本为1.0.3（部分标记为1.1.0），官方最新v1.0.4（7月15日打包），references/api-commands.md从3.2KB暴涨至24KB，新增3个API端点：updateNoteFromMCP、createTagFromMCP、createNotebookFromMCP。

官方升级包信息：下载地址https://cdn.yinxiang.com/ai/yinxiang-skill-v1.0.4.zip，官方文档https://guide.yinxiang.com/docs/yxai/skill.html，打包时间2026-07-15。

新增能力清单7项：updateNoteFromMCP更新笔记（改标题/正文/笔记本/标签）、createTagFromMCP创建独立标签、createNotebookFromMCP创建笔记本（支持批量）、searchNotesByFilter搜索增强（keyword+tagNames+notebookGuid+startTime/endTime+title组合过滤）、createNoteFromMCP创建笔记增强（新增tagNames参数一键创建带标签笔记）、最近3天搜索（用户说最近固定按3天筛选）、批量操作（批量创建笔记本/移动笔记/管理标签）。

升级操作三步：先cp -r备份到~/.Trash/evernote-yinxiang.bak；从官方zip下载到/tmp/；逐个cp -f覆盖14个文件（SKILL.md 22KB场景从7扩至10、references/api-commands.md 24KB含bash+PowerShell双平台、11个shell脚本新增create-notebook.sh/create-tag.sh/update-note.sh/search-notes.sh增强版、save-token.sh、_common.sh）。全量校验14个文件字节数与官方zip一致。

SKILL.md关键变化：description大幅扩展新增更新笔记/创建标签/创建笔记本/批量操作等触发词；新增平台检测（bash vs PowerShell）；新增复合任务与批量操作规则章节；新增3个独立场景（场景二更新笔记/场景八创建标签/场景九创建笔记本）；新增Cursor使用说明；所有API请求体必须传source:"skill"；搜索结果展示规则细化（≥100条话术、时间处理、最近3天）。

重要结论：AI无法自动监控印象笔记Skill更新，官方渠道为公众号+GitHub Release+官网，无RSS/Webhook。下次看到更新公告时告诉Claude即可。本次升级不影响已有的Token配置。
[摘要]

原文链接: /Users/panbo/Obsidian/程序开发/印象笔记Skill升级记录20260718.md