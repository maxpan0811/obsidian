---
title: obsidian-blank-screen-gpu
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


Obsidian 启动后一片白色空白（无侧边栏、无按钮）。排查步骤：

**第一步：排除 vault 内容**
- 新建空库（`--new-vault /tmp/test-vault`）→ 同样白屏 → 确认不是 vault 问题
- 删除 `.obsidian` 配置 → 白屏依旧
- 删除 `~/Library/Application Support/obsidian` 全部数据 → Obsidian 恢复正常
- 恢复旧配置后再次白屏 → 确认是 Obsidian 配置损坏

**第二步：结论**
根因是 `~/Library/Application Support/obsidian/` 中的配置数据损坏（可能是旧版 Obsidian 的缓存/插件状态/GPU 缓存损坏导致渲染进程崩溃）。只清空 vault 内的 `.obsidian` 不够，必须删除应用级的 `~/Library/Application Support/obsidian/`。

**修复方法：**
```bash
mv ~/Library/Application\ Support/obsidian ~/Library/Application\ Support/obsidian.bak
```
然后重启 Obsidian，应用数据会自动重建。

**Why：** Obsidian 基于 Electron，应用级缓存（GPU Cache、Local Storage、IndexedDB 等）存储在 `~/Library/Application Support/obsidian/` 中。某个缓存损坏会影响所有 vault，不限于单个 vault 的 `.obsidian` 配置。

**How to apply：** 以后遇到 Obsidian 白屏/崩溃，先排除应用级缓存再怀疑 vault 内容。删除应用缓存后 Obsidian 会恢复出厂状态但 vault 数据无损。

参考：[[obsidian-loading-stuck-71gb-attachments]]
