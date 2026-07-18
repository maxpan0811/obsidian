---
title: feedback_heading_image_swallowed
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


2026-06-11 修复：walk() heading shortcut 吞掉 H6 内嵌图片

**Bug 现象：**
- 文章标题含"△由Claude生成"或"△图片由AI生成"等配图时，图片被丢失
- walk() 输出计数比实际少，用户反馈"少了一张claude生成的图"
- TreeWalker 补漏虽能找回图片，但会追加到末尾破坏图文穿插

**根因：**
`walk()` 函数（约 L169-179）对所有容器做 heading shortcut 检测：
```js
if (!hasBlock && txt.length > 0 && txt.length <= 40) {
    result.push(['h', {text: txt, align: align}]);
    return;  // ← 直接返回，跳过子节点
}
```
当 H6 内含 `<img>` 且无 block 子元素时：
- img 的 `alt="图片"` 属性使 `textContent` 长度=2，满足 shortcut 条件
- shortcut 直接 return，img 子节点被跳过
- 此情况在"图片说明"配图结构中常见：`<h6><strong><span leaf=""><img></span></strong></h6><h6>△由Claude生成</h6>`

**修复（两处）:**

1. heading shortcut 入口（L174-177）：
```js
const hasImgInside = node.querySelector && node.querySelector('img');
if (!hasImgInside) {
    // 正常走 shortcut
    result.push(['h', {text: txt, align: align}]);
    return;
}
// 含图片则 fall through 继续遍历子节点
```

2. H1-H6 分支（L193-205）额外处理内嵌 img：
```js
if (cn.querySelector('img')) {
    for (const sub of cn.childNodes) {
        if (sub.nodeType === Node.ELEMENT_NODE && sub.tagName === 'IMG') {
            const src = sub.getAttribute('data-src') || sub.getAttribute('src') || '';
            if (src && src.startsWith('http')) result.push(['i', src]);
        }
    }
}
```

**Why:** 微信文章常用 H6 包裹"△由Claude生成"/"△图片由AI生成"等配图说明，结构为 `h6 > strong > span > img`，img 被 deep 嵌套在 heading 容器内。heading shortcut 未考虑容器含 img 的情况。

**How to apply:** 看图配 caption 类的文章优先检查是否有图片在 H1-H6 内。如果再有类似"少了一张图"的反馈，先跑 DOM 检查 `document.querySelectorAll('h1 img, h2 img, ... h6 img')` 确认是否命中此 bug。
