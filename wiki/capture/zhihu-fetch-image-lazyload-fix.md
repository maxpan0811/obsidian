---
title: zhihu-fetch-image-lazyload-fix
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


知乎文章中的图片通过 `data-actualsrc` 属性实现懒加载：`<img src="data:image/svg..." data-actualsrc="https://real-url.jpg">`。初始时 `src` 是 SVG 占位图。

**根因（两处咬合 bug）：**

1. `clean_html()` 先尝试用 `data-actualsrc→src` 替换，但这个替换是字符串级别的——如果 `data-actualsrc` 出现在 SVG `src` 之前，替换后 img 同时有 `src="real"` 和 `src="data:image/svg..."`，HTML 只认第一个；如果出现在之后，替换根本没命中。
2. 更致命的是，`clean_html()` 最后一行删除所有 `src="data:image/svg..."` 的 `<img>` 标签——无论它是否已被注入真实链接，整行删除。

结果：22 张图最多抓 6 张。旧的 HTML 管线也受影响。

**正确做法（在浏览器端解决）：**
```js
document.querySelectorAll('.Post-RichText img, .RichText img').forEach(img => {
    const real = img.getAttribute('data-actualsrc')
        || img.getAttribute('data-lazy')
        || img.getAttribute('data-original')
        || img.getAttribute('data-src');
    if (real && img.src !== real) img.src = real;
});
```
在取 innerHTML 之前执行，确保所有图片的 src 已是真实 URL。

**教训：** HTML 字符串级别的 `data-actualsrc→src` 替换不可靠。懒加载图片的修复应该在 **浏览器 DOM 层** 做，取到 HTML 后 `clean_html` 只做属性清理，不做图片删除。

**How to apply:** 任何涉及知乎/类似懒加载机制的网页抓取，优先在浏览器端注入真实 src，不要依赖字符串替换。

**Related:** [[reference_zhihu_pipeline]]
