---
name: icloud-jiu-lu-jing-qing-li-20260717
type: source
tags: [obsidian, icloud, path-migration, skills-fix, cleanup]
source_path: /Users/panbo/Obsidian/程序开发/iCloud旧路径清理_20260717.md
---

[摘要]
本文记录了2026年7月17日Obsidian vault从iCloud路径迁移到本地后，处理旧iCloud路径被重建问题的完整过程。

问题根因：vault已从iCloud路径(/Users/panbo/Library/Mobile Documents/iCloud~md~obsidian/Documents/20260520/)迁移到本地路径(/Users/panbo/Obsidian/20260520/)，但11个skill脚本仍硬编码旧iCloud路径。运行时脚本写回旧路径，导致iCloud判定vault活跃并重建目录树。

侦查过程：通过grep -rn "iCloud.*md~obsidian" ~/.claude/skills/发现14处引用；检查iCloud残留目录发现84篇微信读书笔记+1篇程序开发笔记+.obsidian配置；排除cron/launchd/git hooks等自动触发机制；确认新vault正常运转。

修复涉及4个工具共14个文件：印象笔记管理工具（7脚本+SKILL.md共8个）、知乎管理工具（3脚本）、LLM-Wiki管理工具（1脚本）、知识库管理工具（SKILL.md路径）、每日选股分析（SKILL.md路径）。每个文件将硬编码的iCloud旧路径全部替换为新本地路径。

残留清理：iCloud旧目录（87个.md文件+.obsidian配置）移入废纸篓~/.Trash/icloud-obsidian-20260520_20260717_124840。

关键经验：vault路径迁移后必须全局grep iCloud.*md~obsidian检查所有.claude/skills/下的.py/.sh/.md文件；skills脚本路径常被忽视（AI不会主动告诉有旧路径残留）；可使用sed -i '' 's|旧路径|新路径|g'批量替换后再逐文件核查。
[摘要]

原文链接: /Users/panbo/Obsidian/程序开发/iCloud旧路径清理_20260717.md