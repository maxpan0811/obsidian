---
title: "[TITIAN TOOL] 备份 LaunchBar Actions"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/[TITIAN TOOL] 备份 LaunchBar Actions.md
tags: [印象笔记]
---


[TITIAN TOOL] 备份 LaunchBar Actions
----------------------------------

LaunchBar 没有自动备份 Actions 的功能。好在这些 Actions 可以在 Finder 里找到源文件，我们备份源文件就实现了 Actions 的备份。

基本的原理，还是借助一个命令行工具 rsync，将 Actions 文件夹增量同步到指定位置（我选的是 iCloud）。

手动备份：用 LaunchBar
----------------

首先想到的是手动备份 Actions，可以用 LaunchBar 自身来实现。创建一个动作，粘上下面的 shell 脚本：

```
# backup LaunchBar Action
rsync -av /Users/apple/Library/Application\ Support/LaunchBar/Actions/ /Users/apple/Library/Mobile\ Documents/com\~apple\~CloudDocs/Automation/Launchbar\

<!-- [摘要] 规则提取，如需全文请查看 vault 原始笔记 -->