---
title: evernote-yinxiang-skill-upgrade
type: capture
tags: [auto-capture, project]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


# 印象笔记 Skill 升级 v1.0.4

2026-07-18 从官方 `https://cdn.yinxiang.com/ai/yinxiang-skill-v1.0.4.zip` 升级。

**Why：** 用户看到印象笔记公众号文章，确认有新版本没有自动同步到本地。

**新增能力：**
- 更新笔记（updateNoteFromMCP）— 改标题/正文/笔记本/标签
- 创建标签（createTagFromMCP）
- 创建笔记本（createNotebookFromMCP）
- 搜索增强 — keyword + tagNames + notebookGuid + startTime/endTime + title 组合过滤
- 创建笔记支持 `tagNames` 参数，一键创建带标签的笔记
- 搜索增加「最近3天」快捷筛选、总数≥100条话术、时间范围处理规则
- 批量操作支持（批量创建笔记本、批量移动笔记、批量管理标签）
- PowerShell + bash 双平台支持

**How to apply：** 下次用户提到印象笔记相关操作时，skill 已自动加载新版。注意新的触发词：更新笔记、修改笔记、创建标签、创建笔记本、批量创建笔记本等。

**升级方式：** 下载官方 zip → 覆盖 SKILL.md + references/api-commands.md + 全部 scripts/*.sh。备份保留到 `~/.Trash/evernote-yinxiang.bak`。
