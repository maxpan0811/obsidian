---
title: dashboard-html-build-pitfalls
type: capture
tags: [auto-capture, project]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


标签一致性看板（`~/Desktop/标签一致性看板.html`）反复白屏，三个独立根因叠加：

## 1. body HTML 被截断（最致命）

Python 构建脚本用字符串拼接操作 HTML 时，`<body>` 到 `<script>` 之间的 DOM 元素丢失（titleMenu 的 style 被截断在 `box-shadow:3px`，后续 `table`/`selbar`/`periodbar` 等全缺）。JS 执行 `document.getElementById('table').innerHTML=...` → null → TypeError → 白屏。

**Why**：字符串切片拼接 HTML 极易出错。`html.find('<script>')` 定位到的位置之前的内容，可能在之前的步骤中被修改过导致边界错位。

**How to apply**：
- 不要用字符串拼接改 HTML 结构，改用模板替换完整段落
- 验证时检查 body 里有哪些 div id：`python3 -c "... body_html = html[body_start:script_start]; print(body_html)"`
- 用 `grep -o 'id="[^"]*"' file.html` 列出所有 id

## 2. curPeriod() 在 LC 视图下崩溃

```js
const curPeriod = () => curView().periods[period]; // LC view 没有 periods → undefined
// init 时：resetPIdx() → curPeriod() → undefined.data → TypeError
```

**修复**：
```js
const curPeriod = () => curView().periods ? curView().periods[period] : null;
```
类似地 `curMatrix()` 和 `resetPIdx()` 都要处理 null。

## 3. mock DOM 测试陷阱

Node mock 用 `getElementById: (id) => ({...})` 按需创建元素 → 即使 HTML 缺元素也测不出 → 误判为 SYNTAX OK + RUNTIME OK。真实浏览器里不存在的元素返回 null。

**How to apply**：mock DOM 必须预定义所有期望的元素，对未定义 id 返回 null（模拟真实浏览器行为）。或者更好的方法：用 Playwright 直接在浏览器里测。

## 验证 checklist

修复后必须验证：
1. JS 语法（`new Function(js)`）
2. JS 运行时（null-returning mock DOM）
3. **HTML body 完整性**（`<body>` 到 `<script>` 之间必须包含所有 id 元素）
4. 真实浏览器刷新（Playwright 或 `open` + 用户确认）

⚙️ 总结看板白屏三因 | body截断+curPeriod崩溃+mock陷阱 | → 后续看板开发用模板化生成
