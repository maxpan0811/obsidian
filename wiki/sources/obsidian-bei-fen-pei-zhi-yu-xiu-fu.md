---
name: obsidian-bei-fen-pei-zhi-yu-xiu-fu
type: source
tags: [obsidian, git, backup, github, gitee]
source_path: /Users/panbo/Obsidian/程序开发/Obsidian备份配置与修复.md
---

[摘要]
本文记录了Obsidian vault通过Git备份到GitHub和Gitee镜像的完整配置与修复过程。

最终架构采用三仓库方案：笔记库(github.com/maxpan0811/obsidian.git)存放全部vault笔记（印象笔记35K篇、知乎130篇、程序开发等）、配置库(github.com/maxpan0811/obsidian-config.git)存放.obsidian配置（插件/主题/设置）、Gitee镜像(gitee.com/maxpan0811/obsidian.git)通过GitHub Actions自动同步，防止GitHub被墙导致无法访问。备份方案选型排除了百度云盘（无官方CLI），确认Git+GitHub为首选。

Obsidian Git插件配置要点：Base path指向20260520子库仓库，自动commit和push间隔均为15分钟。GitHub Token通过gh auth refresh --scopes repo授权。纳入备份的关键决策包括：从.gitignore移除印象笔记管理工具/目录（35K文件/563MB）、知乎笔记仅跟踪.md文件排除attachments/（129篇~2MB/排除233MB附件）、使用git filter-branch移除vector_store/chroma.sqlite3（242MB大文件）。还处理了6个超长文件名（超过Linux ext4的255字节上限），截短至50字符+...后缀。

Gitee镜像同步问题修复（2026-07-14）：workflow连续2天同步失败，根因有两个——fetch-depth:0被误删导致shallow clone无法push，以及Gitee拒绝默认分支的force-push。修复方案是恢复fetch-depth:0、升级actions/checkout从v4到v5、通过delete+push绕过Gitee的force-push保护（git push remote :refs/heads/main删除分支后再git push remote main）。最终验证两端提交完全一致，0 ahead/0 behind。

关键经验：GitHub→外部Git仓库push必须完整历史不能省fetch-depth:0、delete+push走不同协议路径绕过force-push保护、GitHub Actions annotation只显示exit code实际错误在step日志里。
[摘要]

原文链接: /Users/panbo/Obsidian/程序开发/Obsidian备份配置与修复.md