---
title: "又一个神级 skill 开源 ! 好用很多。"
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/又一个神级 skill 开源 ! 好用很多。.md
tags: [evernote, impression, yinxiang]
---

# 又一个神级 skill 开源  !  好用很多。

---

20 天，2600+ Star。

又一个做PPT的项目在 GitHub 火了，叫 html-ppt-skill。

它做的事情听起来很简单：让 AI 帮你做 PPT。

自带 36 套主题、31 种布局、47 个动效，还有一个像素级精确的演讲者模式，后面我会详细讲讲。

html-ppt-skill不生成 PPTX 文件，而是直接输出一份纯静态的 HTML 文件，零构建、零依赖、AI 原生，双击打开浏览器就能演示。

它本质上是一个 AgentSkill——AI Agent 的插件。

装好后，直接告诉 AI 你要什么：AI 会自动选择模板、主题、布局，输出一个完整的 HTML 文件。

双击打开，按 F 全屏，直接演示。

![](.evernote-content/6FD2526E-C859-4254-8739-0AF705A17869/C8950EAD-99AD-4065-9075-AB9FDAA8FB8C.gif)

这个项目到底有什么特别之处 ？

它内置了 36 套。

覆盖了极简、暗色、渐变、科技、出版、柔和、商务、效果等不同风格。

从 minimal-white、editorial-serif 这种适合学术汇报的极简风，到 cyberpunk-neon、terminal-green 这种适合技术分享的赛博风。

再到 xiaohongshu-white、soft-pastel 这种适合小红书图文的柔和风，基本覆盖了常见场景。

按 T 键可以实时切换主题，方便快速对比效果。

![](.evernote-content/6FD2526E-C859-4254-8739-0AF705A17869/272D1D2C-10DE-44B5-ACE5-C6B499866FA1.png)

除了主题，它还提供了 15 套从真实项目里提炼出来的完整模板。

比如 tech-sharing 是 GitHub 暗底风格，专门给技术分享用的。

pitch-deck 是 YC 风格的融资路演模板。

![](.evernote-content/6FD2526E-C859-4254-8739-0AF705A17869/3F077075-1DCA-4A72-B2E6-E4F8A9216450.png)

xhs-post 是 3:4 竖版的小红书图文模板，直接对标小红书内容创作需求。

![](.evernote-content/6FD2526E-C859-4254-8739-0AF705A17869/372469F0-506D-413A-98F7-F41424A7B016.png)

还有一套 presenter-mode-reveal，每一页都带了 150-300 字的示例逐字稿，专门配合演讲者模式设计。

如果你要准备一场正式分享，直接拿这套模板改内容就行。

![](.evernote-content/6FD2526E-C859-4254-8739-0AF705A17869/D9618D01-B48B-480D-B80C-097B7597E0DA.png)

有了模板，接下来就是布局和动效了。

布局有 31 种之多。

从封面、目录、章节分隔，到文字排版、数据图表、代码展示，再到时间线、架构图、流程图，基本够用了。

每种布局都带真实的示例数据，复制粘贴就能用。

![](.evernote-content/6FD2526E-C859-4254-8739-0AF705A17869/15132C0F-CCD9-4594-A8E6-499D141B4132.gif)

动效也有 47 个，27 个 CSS 动画加上 20 个 Canvas FX。

前者轻量，适合常规入场。

后者是手写的 canvas 模块，粒子爆发、星空飞行、神经网络脉冲这种电影级效果，适合封面或关键时刻。

![](.evernote-content/6FD2526E-C859-4254-8739-0AF705A17869/8959B96A-71FA-4100-89BB-923052A0D1C4.png)

说到这里，你可能会好奇：为什么作者选择用 HTML 而不是传统的 PPTX？

为什么是 HTML 而不是 PPTX？

作者的想法很明确：零构建。

生成的文件不需要安装任何软件，双击用浏览器打开就能演示。

没有 node\_modules，没有构建步骤，只有 CDN 上的字体文件。

对于开发者来说，这种方式比打开 PowerPoint 顺滑太多。

除了技术选型，这个项目在演讲者模式上也下了不少功夫。

演讲者模式，真正用心的地方按 S 键，会弹出一个独立的演讲者窗口。

里面有四个可拖拽、可缩放的磁吸卡片：当前页预览、下一页预览、逐字稿、计时器。

每个预览卡片其实是一个 iframe，加载的是同一份 HTML 文件，只是 URL 多了一个 ?preview=N 参数。

这意味着预览和观众看到的是完全相同的 CSS、主题、字体、viewport——像素级精确。

不会出现"预览和实际不一样"的尴尬。

![](.evernote-content/6FD2526E-C859-4254-8739-0AF705A17869/04C31CE0-577C-4F95-82F9-7A6F73D202B6.jpg)

翻页的时候，演讲者窗口通过 BroadcastChannel 和主窗口同步，用 postMessage 通知 iframe 切换页面。

整个过程不重新加载页面，不白屏，不闪烁。

如果你也想试一下，最低门槛的打开方式是这样的：先运行 npx skills add https://github.com/lewislulu/html-ppt-skill 把它装成 AgentSkill，然后在你支持的 AI Agent 里直接说需求。

如果你用的是 Claude Code，它会自动调用这个 skill 生成 HTML 文件。

不想装 skill 的话，也可以直接 git clone 仓库，用 ./scripts/new-deck.sh my-talk 创建新项目，然后用浏览器打开生成的 HTML。

生成好 HTML 文件后，操作其实很简单。

用浏览器打开，按 ←→ 键翻页，按 F 进全屏，按 S 打开演讲者窗口。

![](.evernote-content/6FD2526E-C859-4254-8739-0AF705A17869/2E1DAE25-315A-4755-9ED1-768F78939546.png)

如果你想快速预览所有页面，按 O 键会弹出一个幻灯片网格，一目了然。

觉得当前主题不合适？

按 T 键循环切换，36 套主题挨个试，找到顺眼的为止。

![](.evernote-content/6FD2526E-C859-4254-8739-0AF705A17869/8D0E05C9-B85C-4E8F-AAEE-EF5BBFE0404E.png)

想在某一页加个动效？

按 A 键，它会在当前页循环演示各种入场动画，挑一个喜欢的记下来，回头改 HTML 加上就行。

如果你只是想先感受一下它的效果，可以直接打开仓库里的 templates/theme-showcase.html。

![](.evernote-content/6FD2526E-C859-4254-8739-0AF705A17869/F8DB6919-F69C-48F5-8DB0-6815D4D71FF4.png)

这是 36 套主题的展示页面，每一页用独立的 iframe 渲染，避免样式互相污染。

或者打开 templates/full-decks-index.html，浏览全部 15 套完整模板。

![](.evernote-content/6FD2526E-C859-4254-8739-0AF705A17869/B2D6190F-BE90-45FC-90C3-AA45ADA6922F.png)

这些都是现成的 HTML 文件，双击就能看。

想导出PDF就用浏览器的功能，用打印功能，选择另存为 PDF就行。

给你润色得更流畅、口语自然、逻辑通顺，直接可用：不过最后还有两个小问题想跟大家提一下。

目前它只能导出 PNG 图片格式，没法直接生成 PPTX。 只能先执行 ./scripts/render.sh 你的PPT文件.html，借助无头 Chrome 把每一页单独渲染成 PNG，之后再手动粘贴到 PPT 里，或者用别的工具批量转成 PPTX。

另外修改内容需要直接编辑 HTML 源码，对不懂前端、不会 HTML 的人来说，上手门槛会偏高。

写在最后以前做技术分享，光是排版、调样式就得耗一两个小时。现在简单跟AI说清楚需求，几分钟就生成好，省下的时间专心打磨内容就行。

就跟开车从手动挡换成自动挡一样，虽说少了点手动操控的感觉，但是真的省事、省心太多了。

项目基于 MIT 协议开放，感兴趣的同学可以去 GitHub 仓库看看源码和文档。

开源地址：https://github.com/lewislulu/html-ppt-skill

---

来源：<https://mp.weixin.qq.com/s/5xuQnjeESkJ1SdQVfk8aSw>

[📎 在印象笔记中打开](evernote:///view/207087/s1/3cd7facc-67db-4dc1-a52e-5447948e0a53/3cd7facc-67db-4dc1-a52e-5447948e0a53/)
