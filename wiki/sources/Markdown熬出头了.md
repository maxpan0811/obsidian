---
title: Markdown 终于熬出头了——HTML 的回归
type: source
created: 2026-06-08
updated: 2026-06-08
sources: [https://mp.weixin.qq.com/s?__biz=MzI0NDQ0ODU3MA==&mid=224754...]
source_path: 印象笔记管理工具/Markdown，终于熬出头了.md
tags: [markdown, html, writing, tool]
updated: 2026-06-27
---

---
title: "Markdown，终于熬出头了"
source: evernote
type: note
export_date: 2026-06-26
guid: 2ccb5b97-5976-4f1f-a895-7b7c3d8b471b
---

# Markdown，终于熬出头了

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzI0NDQ0ODU3MA==&mid=224754...](https://mp.weixin.qq.com/s?__biz=MzI0NDQ0ODU3MA==&mid=2247547687&idx=1&sn=8f02ae6bcc5a3d0674f6b53525b2d3b8&chksm=e81bba153c9fe48e69dd0bb9f0d8214bfd959fd5824218ef7dbb397fafbceb49a29b7863a1f8&scene=90&xtrack=1&req_id=1779603601102156&sessionid=1779603405&subscene=93&clicktime=1779603830&enterid=1779603830&flutter_pos=8&biz_enter_id=4&ranksessionid=1779603601&jumppath=WAWebViewController_1779603608428,WAWebViewController_1779603608928,20020_1779603644192,1104_1779603803016&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004933&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ0rRGaAXAJWS8sHVA89UKGBLTAQIE97dBBAEAAAAAAE5YJ9utTOkAAAAOpnltbLcz9gKNyK89dVj08Z3sqoQ4MWLTzmq+01+SEoa0/67S7F1orcvHgRqLKVyk7P4d8mpbr07szzOIkSO7FDg3Ff9z0bIURpSFnIgsTEd+/8huRl+zXUEeJz8+O9vA9n/nPoZxRJx8EifP90otaVUl4SIfnhw4yuYly+VeIvoyAuhSnZX07mB3T0O30fXDNsPXsjpy3c/fuhyCK2XFXkeAFe4nxO/WeACJw7BtGvQgPc981BlEhozxLZU=&pass_ticket=4HgLZzc4cg+Hwo1I67Wm/IJ/yYk7YyweAlw6qN16VzpOO/8KXqe2nzlp3gxNXRsK&wx_header=3)

Originaldev 大迁世界

很长一段时间里，我都觉得 Markdown 编辑器已经没什么新东西可聊了。

那些曾经很受欢迎的“优雅写作”应用，慢慢淡出了大家的视野。很多只支持 macOS，有些甚至还搞过众筹，后来却陷入交付延期、沟通混乱之类的问题。现在回头看，真的有点难想象：曾经一个 Markdown 编辑器，居然也能在 Kickstarter 上募到钱。

如果你今天只是想写一篇文章，Typora 当然还够用。

很多年前，每次换新设备，第一件事就是装付费版 Typora。那时候它几乎是我写 Markdown 的默认选择。可后来，我慢慢转向了免费的 MarkText。MarkText 做得很好，而 Typora 几乎已经从我的日常工具里消失了。

再后来，大家的注意力转向了“笔记库”。

Obsidian 崛起，并且建立起了完整的生态。如果你要处理代码和文档，VS Code 也完全能胜任。于是很容易得出一个结论：Markdown 工具这条赛道，似乎已经没什么新空间了。

但最近，试了一批新的 Markdown 应用，尤其是在我上次写到 Tolaria 工作流之后，我开始觉得事情正在发生变化。

新一代小而美的 Markdown 编辑器，已经不只是用来“写 Markdown”了。

它们正在变成本地纯文本工作台。

更准确地说，是一种可以让 AI Agent 安全操作的本地工作台。

也就是说，你的文件依然是 `.md`。 它们依然保存在你的硬盘上。 它们依然可以通过 Git、Syncthing、iCloud、Dropbox 或任何你喜欢的方式同步。

真正变化的是编辑器旁边多了一层能力：AI 可以搜索、总结、改写、整理、生成任务，甚至在很多情况下，通过 MCP 直接读写同一个笔记库。

这和那些把所有东西上传到云端，然后在云端调用 AI 的工具，完全不是一条路线。

分享一个正版GPT5.5 目前 0.2 倍率,  关注公众号后，在后台回复：airealy 即可自动获取兑换码及使用方式。

## 别再把它们当成 Typora 替代品

下面这些新工具，第一眼看上去很容易被误认为“又一个 Typora”。

但它们并不是。

Clearly，也就是 clearly.md，把自己的范围控制得很克制：打开一个 `.md` 文件，写作，获得语法高亮，然后切换到漂亮的预览模式。

它是原生 Mac 和 iPhone 应用，免费、开源。试过之后，我觉得它非常清爽，是 macOS 上少见的轻量级好选择。

![](attachments/8025d4a36b160748.png)

Cogito，也就是 Cogito.md，更像一个“文件夹优先”的原生 Mac 笔记应用。

你可以添加本地文件夹，使用 `[[Wiki links]]`，也可以用 Obsidian 风格的 `![[embeds]]`。它支持可点击的任务复选框，还能导出排版不错的 PDF。

更有意思的是，它的定位是“为 Agent 和人类共同设计”。它提供 AI 生成的文档摘要，也有原生、快速的预览体验。你可以把它理解成一个更轻、更精致的 Obsidian。

Writer，也就是 writer.computer，则走了一条更偏工程师的路线。

它基于 Tauri v2、React、CodeMirror 和 Rust 构建。文档保存在本地磁盘上，会尊重工作区里的 `.gitignore`，支持多窗口，也能渲染表格和 Mermaid。

它给人的感觉是快、稳、务实，非常适合开发者。

Quarkdown 值得单独拿出来说。

它不是传统意义上的编辑器，而是一个基于 Markdown 的排版系统。

通过 doctype 预设，同一份源文件可以输出分页文章、书籍、文档站点，甚至交互式幻灯片。

它有点像“Markdown 遇上 LaTeX”。它支持响应式预览、脚本能力和可复用组件。如果你想用 Markdown 生成更正式、更稳定、更高质量的内容，Quarkdown 很值得看。

![](attachments/85542184176d6193.png)

你当然可以把这些工具看成经典 Markdown 编辑器的演进版本。

但真正有意思的变化，其实发生在另一组工具身上。

## Markdown 正在变成 Agent 控制台

VMark、ZenNotes 和 SoloMD，并不想靠“更漂亮的预览”或者“更多主题”取胜。

它们真正想回答的问题是：

AI Agent 能不能在你的本地文本库里，安全、直接、可控地工作？

我之前写过的 Tolaria，也属于这个方向。

VMark 把自己定义成一个人类和 AI 协作的纯文本工作区。

它支持 Markdown、YAML、JSON、TOML、Mermaid、SVG、HTML 和代码。更关键的是，它原生支持 MCP，所以 Claude、Codex 或 Gemini 可以和你读写同一批文件。

它还提供 schema-aware previews，也就是针对 GitHub Actions、package manifests 等结构化文件，提供更懂内容的预览体验。

ZenNotes 的方向更明确。

它强调键盘优先、本地 Markdown vault、内置 MCP server，以及一个 zen CLI。

它可以和 Claude Code、Claude Desktop、Codex 干净地集成，让这些 AI 工具直接编辑同一批保存在磁盘上的 Markdown 文件。

它还支持 Mac、Windows 和 Linux。如果你更喜欢浏览器环境，也可以自托管它的 Web 应用。

![](attachments/c4177154e0a5acb8.png)

SoloMD 则更有野心。

它想做一个全能型 Markdown 编辑器，同时也是连接 LLM 的桥梁。

它是 local-first 的，支持 AutoGit 版本管理，可选端到端加密 vault，本地语义搜索和 RAG，还内置 MCP server，可以让 Claude Desktop、Cursor 等工具操作你的笔记库。

它支持 14 个 BYOK AI 提供商，包括 Ollama，也就是说你可以完全本地运行。

不过说实话，我个人觉得它有点重。测试之后，我没有特别想把它留下来。相比之下，我更喜欢 Tolaria 的风格。

但如果你想要一个“所有东西都放在一起”的方案，SoloMD 确实很好地展示了这种思路。

## 如果让我选，我会这样看

如果只是简单编辑单个文件，或者日常写作，我不会把事情搞复杂。

Clearly 足够轻巧，Cogito 和 Writer 都很舒服，也都做得很完整。MarkText 依然是一个靠谱的免费选择。

至于 Typora，对我来说，它已经不是第一选择了。

时代确实变了。

如果你要处理正式文档和长期笔记，Obsidian 仍然是默认答案。

如果你希望 AI 参与进来，把 Obsidian 和 Claude Code、Codex、OpenCode 这类工具搭配起来，依然是一条非常实用的路线。

如果你关心更前沿的 Agent 工作流，又喜欢一体化的本地工作台，那么 VMark、ZenNotes、SoloMD 和 Tolaria 都值得认真看看。

Markdown 工具会来来去去，但 Markdown 本身并没有过时。

恰恰相反，在 AI 时代，它可能变成了人类和机器都最容易理解的本地数据层。

## 还有一些候选工具

Moraya：Tauri + WYSIWYG + AI Agent，方向和 SoloMD 有点像，但成熟度还需要观察。

Otterly：更像轻量版 Obsidian / Cogito，重点放在本地 vault 上。

Marko：Tauri、文件夹、Wiki links、Git，走的是极简但实用的路线。

Inkwell：便携、离线、不需要账号。如果你只是想打开文件然后写东西，它很合适。

MerMark Editor：专门面向 Markdown + Mermaid 技术文档。

Nimbalyst：它不是纯 Markdown 编辑器，更像 Claude Code / Codex 的可视化控制台，但它指向的也是 Agent workspace 这个趋势。

MarkEdit：不算新工具，但它依然是小而精的 Mac Markdown 编辑器代表。

![](attachments/8f5d3f52a915d177.png)

## 最后

过去，判断一个 Markdown 工具，主要看三个维度：

写作体验。 预览效果。 导出能力。

但现在，这些基础功能已经被重复造了太多遍。

同时，AI 编程也带来了大量低成本工具。很多工具注定不会长期存在，但其中一些想法会留下来。

未来我会重点关注几个方向：

安全和隐私是否扎实。 信息架构是否合理。 是否能接入 MCP、CLI、Git 和快速本地搜索。

这也是为什么我越来越确信一件事：

到了 2026 年，小而美的 Markdown 编辑器，正在悄悄变成 AI Agent 的本地工作台。

最可靠的工作流，未必是把所有东西都推到云端。

更好的方式可能是：保留一组你能打开、能同步、能备份、能审计的纯文本文件，同时让 AI Agent 以安全的方式参与进来。
