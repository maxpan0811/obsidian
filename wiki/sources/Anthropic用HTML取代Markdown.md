---
title: Anthropic 内部文档用 HTML 取代 Markdown
type: source
created: 2026-06-08
updated: 2026-06-08
sources: [https://mp.weixin.qq.com/s?__biz=Mzg3NzU0NzIxMA==&mid=224751...]
source_path: 印象笔记管理工具/Anthropic 宣布用 HTML ，这个项目也火了 。.md
tags: [anthropic, html, markdown, documentation, html-anything]
updated: 2026-06-27
---

---
title: "Anthropic 宣布用 HTML ，这个项目也火了 。"
source: evernote
type: note
export_date: 2026-06-27
guid: 6b632656-e66d-4324-8095-e04b5c3fdf1c
---

# Anthropic 宣布用 HTML ，这个项目也火了 。

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=Mzg3NzU0NzIxMA==&mid=224751...](https://mp.weixin.qq.com/s?__biz=Mzg3NzU0NzIxMA==&mid=2247512181&idx=1&sn=3d24f7266c5f876a2eb276ce284405fa&chksm=ce7c9f9d5632d8b2a80757a9fd94bd053e7c18951cfe96ccb7fa42770e2ac495d7deda518cd2&mpshare=1&scene=24&srcid=0518iOFWxZJ5ghxE06aJeA8z&sharer_shareinfo=d7f46e5850f80bcd1214bcf02180029f&sharer_shareinfo_first=d7f46e5850f80bcd1214bcf02180029f&clicktime=1779116254&enterid=1779116254&ascene=14&devicetype=iOS26.5&version=1800492d&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQUbyCkzvql0/zKBPpmxDaUBLTAQIE97dBBAEAAAAAAHTCD4xZnrUAAAAOpnltbLcz9gKNyK89dVj0LRht/H9+9BOOrdA7zfQHXwCQBtb9RxFh6RM364Y3kGTKRPw94tRC1FHHA4imcQ5HWN5oWxRqgQL4RYDg+HP5SvoGk/DQ/9xf4UwHVP40McxUEZcU/tkkIk26aJhnZmX56TarvbrLCBWj/uIbu0Kc8CH418i71YcogXf/yAQAn7EHb+kf4i4rZz0nf6e0A2GdfG1fdQ+TPzg2uNp+YNMaxUGwlWPH8+xsKJ7rkAo=&pass_ticket=ksKHYG/QajSEofxXz/eozl7RaD0q9RGmq2q74Z0ocHTSTmYg8g4oqq5Z30dwM72D&wx_header=3)

# Anthropic 宣布用 HTML ，这个项目也火了 。

Original开源日记开源日记

前几天在 X 上刷到一条有意思的消息：

Anthropic 的 Claude Code 团队宣布，他们内部文档不再写 Markdown 了，直接写 HTML。

理由是：Markdown 是写给作者看的，HTML 才是给读者看的。

然后。

一个叫 html-anything 的项目在 GitHub 上火了——**已经拿到 2500+ Star**。

**它能让本地 AI Agent 帮你写 HTML。不生成 Markdown 或 PPTX，直接输出纯静态的 HTML 文件。**

![](attachments/ad077ba5baf3b8d8.jpg)

左侧输入需求，中间选模板，右侧实时预览。

装好后你只需要做一件事：

```
做一份技术博客，暗色主题，要有代码示例和数据图表
```

AI 自动选模板、应用设计约束、输出完整 HTML 文件。

### 不提供 AI，只做调度

说到实现方式，html-anything 不自带模型，也不卖 API Key。

说白了就是**调用你电脑上已经装好的 AI 工具**。

Claude Code、Cursor、Gemini CLI、Copilot……只要你之前用过并且登录过，它直接拿来用。不需要额外注册或付费。

### 生成的每一页都是成品，不是半成品

自带 75 套精心设计的模板。

![](attachments/afcc6453eb33f9ac.png)

每个模版都有严格约束：

- CJK 优先字体栈。
- 8px 基线网格。
- 对比度 ≥ 4.5。
- 必须使用真实数据。
- 禁止占位文本。

这样做的好处就是确保输出契合专业规范。

覆盖 9 种常见场景:

**01 Web 原型。**

能够用来制作落地页、定价页以及后台管理、技术博客这些页面。

**02 演示文稿。**

有 20 套风格可以选用，下面我会单独拿出来说说。

![](attachments/573da679d8f96ebc.png)

演示文稿示例

**03 生成视频。**

写完一键导出渲染成 MP4 视频，下面我也会单独讲一下。

![](attachments/97e7dc3a0df0e878.png)

视频帧示例

**04 社交卡片。**

像小红书、推特以及 Spotify 风格的配图都能够借助它来一键生成。

**05 办公文档。**

日常办公要用到的周报、需求文档、财务报告等文档，都有相应模板。

![](attachments/addc75e212ee3d20.png)

办公文档示例

此外还囊括了简历此外海囊括了据报表等其它场景。

### 这 9 种场景里，演示文稿模板值得单独聊聊

足足有 20 套演示文稿。

做技术分享和产品路演的朋友，这部分会让你眼前一亮。

**01 瑞士国际主义风格。**

你用 16 列网格配一个主色调就行，克莱因蓝、柠檬绿这些随便挑，22 种固定布局直接套。打开就是那种「一看就贵」的冷峻感。

![](attachments/573da679d8f96ebc.png)

**02 杂志和电子墨水风。**

10 种布局搭配 5 套配色方案，墨水、靛蓝瓷、牛皮纸这些都有。看起来就像一本印刷精美的艺术杂志。

![](attachments/34e9fdfa9acfe705.png)

还有 deck-xhs-pastel 也就是小红书柔和风、deck-hermes-cyber 即爱马仕赛博霓虹风格、deck-replit 也就是 Replit 产品演示风格等。

![](attachments/de185653bfb0d177.png)

Deck 演示模式

### 视频帧脚本，可直接渲染成 MP4

除了静态页面和演示文稿，html-anything 还能生成视频内容。

它提供了 10 个遵循 heygen-com/hyperframes 规范的帧脚本，交给 Remotion 就能渲染成 .mp4。

**frame-glitch-title** — 故障艺术标题帧

青色/洋红色差偏移、CRT 扫描线、损坏数据字幕、段落 ASCII 噪声。赛博朋克专用。

![](attachments/137bd27b468600de.png)

frame-glitch-title

**frame-logo-outro** — 品牌 Logo 片尾帧

Logo 逐块组装 + 发光光晕、标语升起、CTTA 出现。产品发布的收尾卡。

![](attachments/9de3d25829b2ddd3.png)

**vfx-text-cursor** — 光标打字特效

每个字符以品红 × 青色色差轨迹显现。丢进一句引用，得到电影级开场帧。

![](attachments/f3c128e19ac9f266.png)

![](attachments/3c45846d746b076c.png)

Hyperframes 视频帧

### 一键导出到多个平台

内容生成好了，接下来就是发布。

html-anything 支持一键导出到多个主流平台，省去了手动排版的麻烦。

![](attachments/129847d834d5f425.png)

一键导出

- **微信公众号**：CSS 全部内联，粘贴进去直接用。
- **X / 微博 / 小红书**：自动渲染成 2× 高 DPI PNG，复制到剪贴板。
- **知乎**：LaTeX 公式自动处理成图片占位符。

如果你之前也经历过同一份内容在不同平台重新排版的痛苦，这个功能就很实用。

### 流式渲染 + 沙箱预览

生成过程中的体验同样重要。html-anything 采用了 SSE 流式渲染技术，让你能实时看到 AI 的创作过程。

![](attachments/85c8c6519d8f21c1.png)

SSE 流式渲染

你能看到页面被 AI 画出来的过程。发现方向不对可以马上中断、重新提示，避免浪费生成资源，也让创作过程更可控。

安全上有考虑，不是只顾功能的粗放实现。

所有生成的 HTML 都在沙箱 iframe 中进行预览，隔离本地存储Cookie。

### 看完这些功能，相信有些人已经迫不及待了。

注意本地至少安装了一个支持的 AI CLI，比如 Claude Code，要能正常用 。

传统手艺先用git把代码下载到你的电脑上。

```
git clone https://github.com/nexu-io/html-anything
```

进到目录，把依赖安装好。

```
cd html-anything  
pnpm install
```

最后一行命令启动。

```
pnpm dev
```

浏览器打开 http://localhost:3000 就能看到入口界面。

像看看每个模版长啥样，打开仓库里的 `skills/` 目录，每个模板都有 `example.html`，双击就能看到效果。

![](attachments/17f61c815016801b.png)

### 两个小问题

当然这个项目也不是完美的。目前有两个主要局限：

1. 目前只能输出 **HTML 和 PNG** 格式。如果你需要 PDF 或 PPTX 的话，得依靠浏览器打印或第三方工具来进行转换。
2. 修改内容需要通过 **AI Agent 重新生成**。没装过 AI CLI 的人上手门槛会偏高。

### 写在最后

说了这么多功能，回到最初的话题——HTML 还是 Markdown？

社区里争议挺大。

有人觉得 Markdown 够用了，简单直接，版本控制友好；也有人觉得 HTML 才是正解，排版自由，所见即所得。

两种观点都有道理。我觉得关键不在格式本身，而在于你所处的场景。

写笔记、做文档。

Markdown 就够了。

跨平台发布、需要精细排版。

HTML 的优势就出来了。尤其是现在 AI 能帮你写 HTML，格式门槛已经不是问题了。

你的看法呢 ？

项目基于 Apache-2.0  协议开放，感兴趣的同学可以去 GitHub 仓库看看源码和文档。

开源地址：https://github.com/nexu-io/html-anything

既然看到这了，欢迎随手点赞、在看、转发，也可以给我个星标⭐，接收最新的文章，我们下期见！
