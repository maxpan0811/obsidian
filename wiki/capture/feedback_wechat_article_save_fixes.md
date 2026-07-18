---
title: feedback_wechat_article_save_fixes
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


2026-06-08 修复总结：

**1. walk() 重写：childNodes 遍历取代 children 遍历**
- 旧版用 `node.children`（仅元素节点）+ 复杂分支逻辑，深度嵌套的 SECTION > IMG 走丢
- 新版用 `childNodes`（含文本节点）+ 简化的递归，天然保持 DOM 顺序
- 图片和文本按 DOM 位置自然交错

**2. 标题检测恢复**
- 在递归前检测容器是否只含内联元素且文本 ≤40 字 → 输出为 `['h', ...]`
- 排除 `<p>` 和 `<body>` 避免误判
- 用 `window.getComputedStyle` 补全 text-align

**3. 图片兜底补漏**
- walk() 完成后用 TreeWalker 按 DOM 顺序收集全部 `<img>`
- 补充遗漏图片到 result 末尾（极少出现）

**4. Python 3.14 兼容**
- 添加 `inspect.getargspec` monkey-patch（thrift/evernote2 依赖）
- 移除 Python 3.9 site-packages 路径硬编码

**5. Playwright 风控绕过**
- `--disable-blink-features=AutomationControlled`
- 自定义 UA + viewport + locale
- `context.add_init_script` 隐藏 webdriver

**6. WebP → PNG 自动转换**（印象笔记不支持 webp）

**7. 纯文本文章自动保存**（0 图不强制退出）

**8. H1-H6 heading shortcut 吞内嵌图片（2026-06-11 新增）**
- 当 H6 含 img（如"△由Claude生成"配图），heading shortcut 直接返回不遍历子节点
- 修复：shortcut 前检查 `node.querySelector('img')`，有图则 fall through
- H1-H6 分支增加 img 子节点手动提取
- 详见 [[feedback_heading_image_swallowed]]

**Why:** 微信文章 DOM 结构多变，旧版 walk() 的复杂分支不适合处理深层嵌套。
**How to apply:** 后续如有图片/标题问题，先检查 `childNodes` 遍历是否覆盖了目标 DOM 结构。配图说明类文章优先检查是否命中 H6 img bug。
