---
title: JS变量清理陷阱
type: capture
tags: [auto-capture, 看板, JavaScript, 调试]
source: "Claude Code 会话 2026-07-19"
created: 2026-07-19
---

修改 JS 变量名后必须 grep 模板中所有引用位置，漏改一个就会导致整个看板白屏。

**案例1**：删除 `bTotal25f` 变量时漏改合计行引用 → 白屏。
**案例2**：新建 `bTotal26f` 但引用处写成 `bCt26f`（拼写错）→ 白屏。

**规则**：删除/新建变量前，先 `grep` 找所有引用。变量命名统一：`bCt`=携程, `bNct`=非携程, `bTotal`=合计, 后缀 `f`=full全年。
