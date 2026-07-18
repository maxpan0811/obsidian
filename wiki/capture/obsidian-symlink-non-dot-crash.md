---
title: obsidian-symlink-non-dot-crash
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


Obsidian 1.12.7 在打开 vault 时白屏（全白无侧边栏），排查过程：

**排除了但非根因：**
- vault 内 .md 文件损坏（17K 篇全部排除）
- iCloud Drive 同步冲突
- Obsidian 应用数据损坏（`~/Library/Application Support/obsidian/`）
- GPU 渲染问题（`--disable-gpu` 无效）
- 社区插件冲突

**真正根因：** `_evernote-content.bak` 符号链接（非点号开头）指向 Evernote 本地 content 目录（约 50,000 个子目录）。Obsidian 在启动渲染时遍历了这个符号链接目标，5 万目录导致渲染进程崩溃，整窗白屏。

**修复：** 将符号链接名改为点号开头（`.evernote-content`），Obsidian 跳过点号文件/目录的遍历。vault 正常秒开。

**关键教训：**
- Obsidian 白屏不要只怀疑 vault 内容。符号链接目标遍历也会导致渲染崩溃
- 点号开头的文件/目录在 Obsidian 中既是"文件树隐藏"，也是"索引跳过"
- 17,220 个 .md + 点号符号链接 = **秒开** ✅
- 之前 Obsidian 卡 loading（而非白屏）是另一个问题——71GB attachments 导致索引遍历——已修复

**Why：** Obsidian（Electron）渲染进程在启动时遍历 vault 内所有非点号开头的文件/目录。符号链接被当作普通目录对待，其目标也被遍历。

**How to apply：** vault 内的所有符号链接必须用 `.` 开头命名，否则 Obsidian 会遍历其目标路径。不仅是文稿文件，目录和符号链接都适用。

参考：[[obsidian-loading-stuck-71gb-attachments]]
