---
title: save-to-evernote
type: capture
tags: [auto-capture, reference]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


## When to use

Save a wechat public account article to Evernote inbox when the user explicitly asks. This is a one-off operation — don't auto-trigger.

## 当前实现（2026-06-03 更新：Playwright + cleanParagraph 方案）

脚本位置：`~/.claude/skills/印象笔记管理工具/scripts/save_article_playwright.py`

### 核心算法

`walk()` DFS 遍历 `#js_content`，`<p>` 元素走 `cleanParagraph()`，其余容器递归。

**`cleanStyle(styleStr)`**：保留印象笔记 ENML 支持的标准 CSS，过滤垃圾属性：
- 保留：`text-align`, `color`, `font-size`, `font-weight`, `font-style`, `text-decoration`, `line-height`, `letter-spacing`, `margin-top`, `margin-bottom`, `text-indent`, `vertical-align`, `background-color`
- 过滤：`mso-*`, `layout-*`, `-webkit-*`, `text-autospace`, `font-family` 等

**`cleanParagraph(pEl)`**：递归生成干净 HTML：
- 文本节点：转义 `&`、`<`、`>`
- `<img>`：单独 emit `['i', src]`，不嵌入 HTML 片段
- `<span>/<b>/<em>/<a>` 等内联元素：用 `<span style="cleanStyle">` 保留格式
- `text-align` 用 computed style 补充：`<p>` 自身 inline style 没有时，用 `window.getComputedStyle(pEl).textAlign` 检查，继承自父 SECTION 的居中也会输出
- 返回 `<div style="cleanStyle">...</div>` 或空字符串（无文本内容时）

**容器递归规则**：没有直接 `<p>` 子元素的容器，直接用 `walk(c)` 递归——原来用 TreeWalker 只收文本，嵌套多层 SECTION 里的 `<p>` 格式会丢失（三联等排版复杂的号用此嵌套结构）

### 输出类型

- `['html', htmlStr]`：`<p>` 生成的带格式 HTML，Python 端直接插入 ENML 不 escape
- `['t', text]`：纯文本（容器内游离文本节点等）
- `['h', text]`：H1-H6 标题
- `['i', src]`：图片 URL
- `['p', text]`：`<pre>` 代码块
- `['table', html]`：表格 HTML

### 验证条件

`en-media 数量 == resources 数量`

## 旧方案（已废弃）

早期用 TreeWalker 只提取纯文本 + 图片，`<p>` 的 `text-align`/`color`/`font-weight` 等样式全部丢失。

## 笔记保存目标

- 笔记本：工作篮（GUID: `5a87b643-d40a-4d96-8999-e9d2aaf94b4f`）
- Token：`.env` 中 `EVERNOTE_TOKEN`（每 7 天过期，参见 [[feedback_evernote_token_7day]]）

## URL 格式陷阱

追踪参数（`scene=24`、`mpshare=1`）触发验证码，必须用 `/s/XXXX` 直链。

## 2026-07-01 更新：click_id 追踪参数兼容性

通过 CDP 路线验证，URL 含 `?click_id=XXX` 等追踪参数不再触发验证码，CDP 可正常保存。这改写了对"只有 `/s/XXXX` 直链可靠"的早期判断——该限制仅适用于 Playwright launch 路线（某些追踪参数确实会触发验证码），CDP 路线不受影响。
