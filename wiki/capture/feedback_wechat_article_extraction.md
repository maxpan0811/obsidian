---
title: feedback_wechat_article_extraction
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


## save_article_playwright.py 的 walk() 函数已知陷阱（2026-06-04 修复）

### 1. `<section><span leaf="">text<span textstyle="">...</span></span>` 结构文字丢失

**症状：** 文章段落文字没有保存下来（内容块数异常少）。  
**原因：** 原来只处理了无子节点的叶子节点（`children.length === 0`），但这种结构的 `<span>` 有 inline 子节点，`children.length > 0`，被递归跳过。  
**修复：** walk() 入口加判断——若节点没有块级子节点（BLOCK_TAGS 外），直接提取 `textContent`。

### 2. `<ul><li>` 列表内容丢失（如"模式。偏好。反复出现的话题。"）

**症状：** 原文用列表分行展示的内容，保存后合并成一行或消失。  
**修复：** for 循环里加 `UL/OL` 分支，用 `querySelectorAll('li')` 取每项，加 `• ` 前缀。

### 3. `<section>` 内的 `<PRE>` 代码块变成普通文本（无黑色底纹，无分行）

**症状：** 代码块保存为普通文本，丢失格式。  
**根因（两层）：**
- walk() 入口的 monospace 检测在 `node`（父节点）上判断，但代码块容器是 for 循环里的 `c`（子节点），父节点已被判断为"有块级子节点"绕过了 monospace 检测。
- 文章所有内容在一个大 `<SECTION>` 里，该 SECTION 有直接 `<p>` 子节点，走了 `childNodes` 迭代路径，PRE 作为 `childNodes` 里的节点被 `walk(cn)` 递归，但 walk() 把 PRE（子节点是 CODE，非块级）误判为"只含内联元素"→ 提取文本。  
**修复：** 在 childNodes 迭代里专门处理 `cn.tagName === 'PRE'` → `['p', innerText]`（不走 walk(cn)）。

**Why:** 这三个 bug 在不同账号文章里触发，很难从单一测试发现，需要对照原文段落逐条检查。  
**How to apply:** 修改 walk() 时注意这三条路径，不要破坏已有修复逻辑。每次改完后用真实文章验证内容块数和关键段落是否完整。
