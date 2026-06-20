---
title: 又一个神级 skill 开源  !  好用很多。
type: source
created: 2026-06-17
updated: 2026-06-17
source: 印象笔记管理工具
source_path: 印象笔记管理工具/又一个神级 skill 开源  !  好用很多。.html
tags: [AI技术]
---

# 又一个神级 skill 开源  !  好用很多。

又一个做PPT的项目在 GitHub 火了，叫 html-ppt-skill。

它做的事情听起来很简单：让 AI 帮你做 PPT。

自带 36 套主题、31 种布局、47 个动效，还有一个像素级精确的演讲者模式，后面我会详细讲讲。

html-ppt-skill不生成 PPTX 文件，而是直接输出一份纯静态的 HTML 文件，零构建、零依赖、AI 原生，双击打开浏览器就能演示。

它本质上是一个 AgentSkill——AI Agent 的插件。

装好后，直接告诉 AI 你要什么：AI 会自动选择模板、主题、布局，输出一个完整的 HTML 文件。

覆盖了极简、暗色、渐变、科技、出版、柔和、商务、效果等不同风格。

从 minimal-white、editorial-serif 这种适合学术汇报的极简风，到 cyberpunk-neon、terminal-green 这种适合技术分享的赛博风。

再到 xiaohongshu-white、soft-pastel 这种适合小红书图文的柔和风，基本覆盖了常见场景。

按 T 键可以实时切换主题，方便快速对比效果。

除了主题，它还提供了 15 套从真实项目里提炼出来的完整模板。

比如 tech-sharing 是 GitHub 暗底风格，专门给技术分享用的。

pitch-deck 是 YC 风格的融资路演模板。

xhs-post 是 3:4 竖版的小红书图文模板，直接对标小红书内容创作需求。

还有一套 presenter-mode-reveal，每一页都带了 150-300 字的示例逐字稿，专门配合演讲者模式设计。

如果你要准备一场正式分享，直接拿这套模板改内容就行。

从封面、目录、章节分隔，到文字排版、数据图表、代码展示，再到时间线、架构图、流程图，基本够用了。

每种布局都带真实的示例数据，复制粘贴就能用。

动效也有 47 个，27 个 CSS 动画加上 20 个 Canvas FX。

后者是手写的 canvas 模块，粒子爆发、星空飞行、神经网络脉冲这种电影级效果，适合封面或关键时刻。

说到这里，你可能会好奇：为什么作者选择用 HTML 而不是传统的 PPTX？

生成的文件不需要安装任何软件，双击用浏览器打开就能演示。

没有 node_modules，没有构建步骤，只有 CDN 上的字体文件。

对于开发者来说，这种方式比打开 PowerPoint 顺滑太多。

除了技术选型，这个项目在演讲者模式上也下了不少功夫。

演讲者模式，真正用心的地方按 S 键，会弹出一个独立的演讲者窗口。

里面有四个可拖拽、可缩放的磁吸卡片：当前页预览、下一页预览、逐字稿、计时器。

每个预览卡片其实是一个 iframe，加载的是同一份 HTML 文件，只是 URL 多了一个 ?preview=N 参数。

这意味着预览和观众看到的是完全相同的 CSS、主题、字体、viewport——像素级精确。

翻页的时候，演讲者窗口通过 BroadcastChannel 和主窗口同步，用 postMessage 通知 iframe 切换页面。

如果你也想试一下，最低门槛的打开方式是这样的：先运行 npx skills add https://github.com/lewislulu/html-ppt-skill 把它装成 AgentSkill，然后在你支持的 AI Agent 里直接说需求。

如果你用的是 Claude Code，它会自动调用这个 skill 生成 HTML 文件。

...不
