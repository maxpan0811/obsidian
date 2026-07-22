---
name: yin-xiang-bi-ji-skill-v1-0-3-an-zhuang-yu-oauth-shou-quan
type: source
tags: [yinxiang, evernote, skill-install, oauth, claude-code]
source_path: /Users/panbo/Obsidian/程序开发/印象笔记Skill v1.0.3 安装与OAuth授权.md
---

[摘要]
本文记录了2026年7月1日印象笔记Skill v1.0.3的安装和OAuth授权过程。

v1.0.3主要改进：新增支持Claude Code、Codex、Cursor等开发工具；增强笔记写入能力，Markdown格式完整保留。从官方下载地址https://cdn.yinxiang.com/ai/yinxiang-skill-v1.0.3.zip安装到~/.claude/skills/evernote-yinxiang/，旧自定义skill备份到~/.claude/skills/evernote-yinxiang-backup-2026-07-01/。

文件结构包含：SKILL.md（7个场景）、_meta.json（版本1.0.3）、agents/openai.yaml（Codex/OpenClaw agent配置）、references/api-commands.md（7个API的curl命令参考）、9个shell脚本（_common.sh、create-note.sh、clip-url.sh、list-notes.sh、search-notes.sh、list-notebooks.sh、list-tags.sh、get-note-detail.sh、save-token.sh）。

OAuth授权流程：新skill使用OAuth方式替代旧的Developer Token。访问https://app.yinxiang.com/third/skills-oauth/完成授权获取S=s开头的Token，保存到~/.config/yinxiang-skill/token。Token验证通过，listNoteBooks API返回4个笔记本。

7个支持场景及触发词：授权引导（"授权印象笔记"）、创建笔记（"记一下""帮我记录"使用createNoteFromMCP Markdown API）、网页剪藏（URL+"保存"/"剪藏"使用clipAndSaveNote）、列出笔记（"列出笔记""有哪些笔记"）、搜索笔记（"搜一下""搜下"）、列出笔记本（"有哪些笔记本"）、列出标签（"有哪些标签"），均通过searchNotesByFilter和listNoteBooks/listTags API实现。

删除笔记调研：用户询问是否能删除笔记到垃圾箱，经深入调研发现v1.0.3未提供删除笔记端点。尝试过的路径包括旧REST deleteNote（Developer Token和OAuth Token均返回无效权限）、新gRPC deleteNoteFromMCP（只接受protobuf不支持JSON）、AI聊天笔记trashNote/deleteNote、旧Thrift SDK note_delete（Python 3.14兼容性问题）。可用变通是在Evernote客户端手动删除或通过搜索+更新笔记内容标记删除。

当前印象笔记相关技能共4个：evernote-yinxiang（AI Skill v1.0.3已更新）、印象笔记管理工具（Favorites导出管线旧Token）、印象笔记文章保存（微信公众号保存旧Token）、印象笔记去重（工作篮去重旧Token）。
[摘要]

原文链接: /Users/panbo/Obsidian/程序开发/印象笔记Skill v1.0.3 安装与OAuth授权.md