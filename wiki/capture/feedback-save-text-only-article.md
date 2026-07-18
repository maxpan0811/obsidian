---
title: feedback-save-text-only-article
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


# 保存纯文本公众号文章（已修复）

`save_article_playwright.py` 原先有两个检查点在 0 图片时强制退出，**已永久修复**：
- ~~`len(img_srcs) == 0 → sys.exit(1)`~~ → 改为 `print("⚠️ 未找到图片（纯文本文章，继续保存）")` 
- ~~`enmedia_count == 0 → sys.exit(1)`~~ → 当 `len(img_srcs)==0` 且 `enmedia_count==0` 时视为纯文本文章正常保存

不再需要临时修改脚本。

**Why**：纯文本文章（如 PDF 下载链接、纯文字长文）无图片是正常情况，不应阻止保存。
**How to apply:** 脚本已内置此逻辑，直接运行即可。
