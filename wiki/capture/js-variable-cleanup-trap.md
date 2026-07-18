---
title: js-variable-cleanup-trap
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


# JS 变量清理陷阱

删除模板中的变量时，必须 `grep` 确认**所有引用**都已替换，缺一处 = 整个页面白屏。

**案例**：删除 `bTotal25f`/`bCt25f`/`bNct25f` 变量时，合计行的 `fmtCap(bTotal25f)` 漏改，导致 `bTotal25f is not defined` → JS 崩溃 → 表格空白。

**How to apply**：删除变量前，先 `grep` 找所有引用，全部替换后再删除声明。不要假设"应该都改完了"。
