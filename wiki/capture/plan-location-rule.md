---
name: plan-location-rule
description: 所有程序开发相关文件必须保存到 Obsidian/程序开发/（根目录），严禁放入 20260520/程序开发/
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 3ff6f006-ddd5-4aff-ac56-d81cc59bd7fc
---

程序开发相关文件（设计文档、实施计划、优化记录、planning 产出等）必须放到 Obsidian 根目录的 `程序开发` 目录：**`~/Obsidian/程序开发/`**

## ❌ 绝对禁止

**`~/Obsidian/20260520/程序开发/`** ← 这个路径是错的！不要写！

大量 skill 的输出路径是 `~/Obsidian/20260520/xxx`，容易形成惯性自动加上 `20260520/`。
但程序开发目录在 Obsidian **根目录**，不在 `20260520/` 下面。

## 正确路径

```
~/Obsidian/程序开发/YYYYMMDD-feature-name.md   ✅
~/Obsidian/20260520/程序开发/...               ❌ 禁止
```

## 路径区分

| 目录 | 用途 |
|------|------|
| `~/Obsidian/程序开发/` | 开发文档、设计计划、优化记录、技术笔记 |
| `~/Obsidian/20260520/` | 管线输出（印象笔记/知乎/微信读书等 skill 的自动化输出） |

**Why:** 用户把所有开发相关的设计文档集中在 Obsidian 根目录的"程序开发"下统一管理。`20260520/` 是管线输出目录，程序开发笔记不属于管线输出。

**How to apply:**
- 任何要写"程序开发"相关文件的场景，路径都是 `~/Obsidian/程序开发/`
- writing-plans 技能产出计划后，直接写 `~/Obsidian/程序开发/YYYYMMDD-feature-name.md`
- 如果发现写到了 `20260520/程序开发/`，立即 mv 到正确位置
- 不要问"放哪里"——就是 `~/Obsidian/程序开发/`
