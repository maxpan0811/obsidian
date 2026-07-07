---
title: 一手实测 Claude Fable 5，手搓了个 Obsidian 的 Codex 插件
type: source
created: 2026-06-14
updated: 2026-06-14
source_path: 印象笔记管理工具/一手实测 Claude Fable 5，手搓了个 Obsidian 的 Codex 插件.md
tags: [印象笔记, AI/编程]
updated: 2026-06-27
updated: 2026-06-27
updated: 2026-06-27
---

---
title: "一手实测 Claude Fable 5，手搓了个 Obsidian 的 Codex 插件"
source: evernote
type: note
export_date: 2026-06-24
guid: c0821489-4e5e-4564-92b0-b44cad184454
---

# 一手实测 Claude Fable 5，手搓了个 Obsidian 的 Codex 插件

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzU4NTE1Mjg4MA==&mid=224749...](https://mp.weixin.qq.com/s?__biz=MzU4NTE1Mjg4MA==&mid=2247498742&idx=1&sn=3327c11465ee024d1a851b5048d0024d&chksm=fc2b6a6040ab7004f94da2dcdc1f337925aeb1c2a33b8ade979590e60fea3e45ef3fb67eac44&scene=90&xtrack=1&req_id=1781074854366963&sessionid=1781074846&subscene=93&clicktime=1781074866&enterid=1781074866&flutter_pos=3&biz_enter_id=4&ranksessionid=1781074854&jumppath=1001_1781074844630,1104_1781074847583,20020_1781074853606,1104_1781074856947&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004a2b&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQxdO5umw0SRyzsiIVb2P8nhLTAQIE97dBBAEAAAAAAH4FDboH7GIAAAAOpnltbLcz9gKNyK89dVj0Y01YUJvPx3dWek+7us0QJQWJ1SH2TJjkwgSuMNgxH+S6XwCH+ILOL0IuP/M6ZcrOqG4pcdkX2HEkrdc5PESx9KsBWQIJTHHrPix0iPJcP+QKauIFnT+NqWFyJsgvjdJuc9S4uJ6vyQXUn0T0SlfeRCVCpnAFQ0vsxP9khHT63CpPpohdJAUDfz7eDZrqhCQWzGqxyYsQsNFkSjNcaBGFIzD/m6K9tCIRs9u4oQU=&pass_ticket=s/cU0mWDstmC1tp82bz0HNlZIDH2/x6zqKXj1S1Zrceo5IWHWrcjnUEllxfT1bll&wx_header=3)

Original苍何苍何

这是苍何的第 545 篇原创！

大家好，我是人在广州的苍何。

就在昨晚 Anthropic 发布了他们迄今为止最强大的模型 Claude Fable 5。

![](attachments/edeb263a72a1b274.png)

说实话，每次出差都会赶上新模型发布，我其实一点儿也不想熬夜测模型。

今天一早，我就起来了，我把 WeSight 接入了 Claude Fable 5。

![](attachments/5b136698e7cf5f44.png)

并让 Fable 5 好好分析了下 WeSight 目前的引擎和模型等问题。

![](attachments/6c11eec5a3465cc4.png)

Fable 5 给出了详细的方案和建议，从功能性 BUG 到 UI 设计交互层面，仿佛是一个经验老道的程序员对着实习生写的代码，一顿分析。

![](attachments/8752aea17da30164.png)

这么多问题，我可不敢直接让 Claude Fable 5 直接帮我改，这玩意现在贵的离谱，随便改点小问题，额度就能直接用完。

不瞒你说，就分析完 WeSight 项目改了几个 bug，我的 5 小时额度就已经用完了。

![](attachments/dce97c2e3171fa16.png)

我看了下 Token 消耗及 TPS，不能说有多快，毕竟有见过像 glm-5.1-highspeed 这种 300-400 tokens/s 的高速模型， Claude Fable 5 的速度就比较一般。

![](attachments/cc3098987af6cb48.png)

但 Token 消耗是真的猛，几个简单任务，Token 就哗哗的用。

![](attachments/d0ca98ebed990a83.png)

有点难绷，我看国外不少人也反馈这个问题，或许简单任务就不该用这么贵的临神一脚的模型吧。

![](attachments/95404be8faa92c20.png)

第一个账号额度用完了，我迅速启动了第二个 Claude 账号，为了验证 Claude Fable 5 在编程及 Coding 上是不是大家吹的那么神。

于是我直接把 WeSight 的 GitHub 仓库代码丢给了它，然后让它帮我做一个基于 WeSight 的 Obsidian 插件。

它在收到指令后，几乎 2 个多小时，就帮我完成了需求。

![](attachments/3a2c62ac70205693.png)

这个插件完美的集成了 WeSight 的底层能力，它能识别你本地的 Claude Code、Codex、OpenCode 模型 cli，自动检测环境，同步到 Obsidian 中。

![](attachments/802e6abd35f3caae.png)

还支持自定义第三方模型，真正做到在 Obsidian 中 All in one 的使用 Claude Code、Codex、OpenCode，非常丝滑。

你不用像 Claudian 一样，每次切换 Claude Code 模型还需要打开 cc-switch 去配置模型，在 Obsidian 中，你就能指挥 Claude Code 帮你做很堵事情。

可以简单理解为这个插件做了 Claudian 和 cc-switch 组合的事情，一次打开一次配置，完美使用。

![](attachments/bf94c16fe7eeaf51.png)

这个插件后面我也会直接上架到 Obsidian 插件市场，感兴趣的可以评论区告诉我催催。

而这，是我在 WeSight 中接入 Claude Fable 5 模型，几乎一次性就完成的。

你要说震撼，说实话是真的挺震撼的，也难怪 Claude 官方说任务越长、越复杂，Fable 5 相对于其他模型的优势就越大。

也难怪 Claude Fable 5 在所有的维度全面碾压，全面 SOTA。

![](attachments/bc45a08d91ff6ab0.png)

Fable 5 在几乎所有测试基准测试中都达到了最先进的水平，在 Agent coding、知识工作、科学研究和视觉方面表现出色。

看到国外一个博主测试，Fable 5 能自动操作游戏，仅靠截图视觉推理，没有用任何辅助工具，在 50 分钟内就通关了这个《精灵宝可梦火红》游戏。

还有博主用 Fable 5  一个提示词出的「我的世界」游戏复刻场景。

甚至更绝的，有老哥，直接用 Fable 5  构建了一个 Windows 操作系统。

其实本来以为 Anthropic 会直接放出 Mythos，这个号称神话模型。

![](attachments/8e8c03cc71c80021.png)

要知道，当时在四月份的时候，Anthropic 发布 Claude Mythos Preview 就震惊了整个行业。

说是和 50 家左右公司合作，直接就找出了他们发现超过一万个高危或严重级别的漏洞，并导致了 zcash 漏洞的发现，进而导致加密货币的全线暴跌。

2 个月后的今天，他们并没有开放 Mythos，而是出了个 Fable 5，翻译过来叫「寓言」。

原因是怕发布如此强大的神话模型会伴随着风险。如果没有相应的安全措施，在网络安全等领域的功能可能会被滥用，造成严重损害。

![](attachments/e667b82638010a21.png)

所以，Fable 5 被加了约束，但凡是你问关于网络安全、漏洞相关的问题，它就会触发限制了。

比如我一开始想让它找下 WeSight 的漏洞，Fable 会直接拒绝掉请求。

![](attachments/4cd39c80dcf30919.png)

据 Anthropic 自己说，Fable 5 的安全防护机制能够检测与网络安全、生物学、化学和蒸馏相关的请求。每当发生故障时（平均发生率低于 5%），用户都会收到通知。

![](attachments/9680621cf2dfbd84.png)

但他们还是为一小部分网络防御者和关键基础设施提供商推出了 Claude Mythos 5，Mythos 5 与 Fable 5 共享相同的底层模型，但在某些方面取消了安全措施。

有点过于离谱

现在你在 Claude 应用端能直接使用 Fable 5 ，不过前提是要升级会员。

![](attachments/d812486b1daedf66.png)

当然如果你是 AI 先行者联盟成员可以联系我，账号和会员问题都有办法。

在 Claude Code 中也能直接使用 Fable 5 了，前提是用 Claude 账号登录，你的 Claude 账号充值了会员。

![](attachments/4db8c4674571dbc6.png)

当然你也可以直接选择把它接入到 WeSight 做统一管理，在 WeSight 中更方便的使用 Claude Code。

也可以在飞书中控制 WeSight 的 Claude Code、Codex 等。

![](attachments/ffe554299e26be81.jpg)

Anthropic 说从今天开始到6月22日，Fable 5 将免费包含在 Pro、Max、Team 及按席位计费的企业版方案中。

但之后就只能通过 API 使用，就很贵的那种。

和 Codex 比起来，多少还是有些小气了，现在 5 小时的用量也跑不了几个任务。

![](attachments/e06e9913aea2c2e7.png)

我简单试了下 Fable 5 的写作文字能力，比之前的 4.7、4.8 要好不少，有 4.6 那味了，除了贵，没别的毛病。

我感觉搞 Claude 那帮工程师也挺焦虑的，他们亲手造出了 Claude，或许他们某一天，也会亲眼看着 Claude 取代自己。

讲真的，这可能是人类离「造物主」最近的时代。

寓言从来不只是讲故事，它是借着故事，说一个道理。

而 Fable 想说的道理可能是：AI 离神，真的就差最后一步了。

这一步，连 Anthropic 自己都不敢迈。

但对我们普通人来说，与其焦虑他哪天封神，不如想想在它封神之前，你用它做点什么。

**工具永远在迭代，但用工具的人，才是最终的变量**。

你用上 Fable 5 了吗？体验如何，评论区聊聊。

共勉。
