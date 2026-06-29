---
title: Mac mini 一夜爆单，Clawdbot 什么来头？
type: source
created: 2026-06-14
updated: 2026-06-14
source_path: 印象笔记管理工具/Mac mini 一夜爆单，Clawdbot 什么来头？.html
tags: [印象笔记, 其他]
updated: 2026-06-27
---

---
title: "Mac mini 一夜爆单，Clawdbot 什么来头？"
source: evernote
type: note
export_date: 2026-06-24
guid: 0ec0fc60-92f2-4c50-a0ad-c698696f4434
---

# Mac mini 一夜爆单，Clawdbot 什么来头？

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MjgzMTAwODI0MA==&mid=265244...](https://mp.weixin.qq.com/s?__biz=MjgzMTAwODI0MA==&mid=2652442455&idx=1&sn=649ba13bbc81fd8111591a99d9d3e8cb&chksm=9a5e586212305710994836ec55f6192e42cecf2e5421db410f748d54ee5632d8fa3297fbd8c5&scene=90&xtrack=1&req_id=1769508003893461&sessionid=1769507995&subscene=93&clicktime=1769508118&enterid=1769508118&flutter_pos=6&biz_enter_id=4&ranksessionid=1769508003&jumppath=WAWebViewController_1769508094069,WAWebViewController_1769508094556,20020_1769508107830,1104_1769508108428&jumppathdepth=4&ascene=56&devicetype=iOS26.2&version=1800442a&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQq2nS2NmZkBdvVjdIlH1qNhLTAQIE97dBBAEAAAAAALVrAx+DZAwAAAAOpnltbLcz9gKNyK89dVj0V2Jykh7H/gDPpHmrIgVLChtH7Z3pcTR5GrwjGjBTfeWlmQDcOKthU9aJfBFcgdp+PV5W7a/wNjiknaQG/gMurc+9XYfJawj4gZ6BkzmmodNzvirsHujcJz9/Y4hWfFC3NCO+Nf9GyEWqEehMdlf4bgstVdcI4IxtFXf/EQkJoykJXJGFCZZhg3qRPeRu/AQec8SI76HPb0N08xNJMQzfyYD6Ytzu3nC+GSyOUnA=&pass_ticket=0qseYMvFgsF8FIywSQJlZYP3MOGFMC9j3NPJj2A47jtLOAp0X/+AVYuCBkFYIVJV&wx_header=3)

发现明日产品的 爱范儿

一夜之间，Mac mini 爆单了，连苹果的销售部门都有点懵。既没有开发布会，春节降价好像也只看到 iPhone Air 大跳水，但 Mac mini 的讨论度却在各大社交平台上突然诡异地飙升。如果你打开 X 或者 Reddit，会发现到处都有 Mac mini 订单截图和各种梗图。就连 Google AI Studio 的负责人，Logan Kilpatrick 都发 X 说，「我已经下单了 Mac mini」。

![](attachments/dbdd92d5516a064f.png)

但是你能想到，让网友们疯狂掏腰包的，只是一个 GitHub 上突然爆火的开源项目 Clawdbot 吗？这是一个自部署的 AI 助手项目，只是因为网上的攻略都在说，用 Mac mini 来搭建是最好的选择，于是，Mac mini 就这样火了。

![](attachments/dcb484766187e314.jpg)

不得不说，今年一开始，各种 AI 产品的爆发前所未有，**前有狂揽 4800 万浏览的 Claude Cowork**，顺势催生了 Skills、Claude Code 的爆火，X 上的信息流，都是它们的教程。现在又来了个 Clawdbot，号称是一个真正的 AI 个人助手，可以运行在自己的设备上。然后 GitHub 的 Star 数量在这两天，**突然就直线飙升，从五千到两万**，这在开源项目里面应该算是比较少见的存在。

![](attachments/3b0b6ef18c8e563e.png)

有网友发梗图说，自己的 2026 才刚刚开始，就已经被这些东西「夺舍」了，这样的日子什么时候才能结束。

![](attachments/3af16a2e03e863ac.jpg)

刚学会了 Claude Code ，又说 OpenAI 的 Codex 更好，用了 Cowork，又还有 Skills，还有乱入的 Mac mini｜图片来源：x@riomadeit不过，倒没有必要对这些 AI 工具产生焦虑，APPSO 就来帮你扒扒这个 Clawdbot 到底是个什么东西，怎么就引起了大家的关注，还有 Mac mini 又是怎么回事。

![](attachments/5afd9ef2b956a6cf.jpg)

希望这是读完之后的你｜图片来源：x@OanaGogeClawdbot 是一个手机端的 CoworkSiri 喊了这么多年智能助手，结果在大多数的用户手里，还是个定闹钟的；Clawdbot 要做的，就是实现「Siri 本该有的样子」。

![](attachments/b24d37383397bdab.png)

Clawdbot 官网：https://clawd.bot/而要做到一个理想的「Siri」，Clawdbot 在某种程度上，是复刻了 Cowork 那一套，并且联动了更多的手机本地内容。具体来说，Clawdbot 是一个自部署的 AI 助手，它的理念是消息优先。我们不需要下载新的客户端，Clawdbot 就是聊天列表里的一个头像，像给同事发微信一样给它发消息，它也在同一个对话框里回复。这听起来很像早期的「聊天机器人」？在 Telegram 上部署一个这样的机器人早已不是什么新鲜事，甚至 ChatGPT 刚出来那会儿，还有人在微信部署过类似的 AI 助手。但是，Clawdbot 的不同，**在于「Gateway（网关）」这个概念。**普通的 Chatbot 只是模型的一个传声筒，而 Clawdbot 是一个中枢（Gateway）。**它一边连接着常用的聊天软件（WhatsApp/Telegram/iMessage 等），另一边连接着最强的 AI 大脑（我们可以自由切换 Claude、ChatGPT、DeepSeek、MiniMax 或本地模型），中间还挂载了无数个包含不同 Skills 的智能体工具。**

![](attachments/7e5177ddba973461.jpg)

图片来源：https://youtu.be/SaWSPZoPX34就像这个架构图所描述的，以前的 Chatbot，我们只是能和他说几句话，或者生成几张图片。**但是 Clawdbot 的架构，是由 Gateway 网关、Agent 智能体、Memory 记忆，以及 Skills 技能共同组成。**我们可以在不同的聊天工具里面部署一个 Clawdbot，常见的配置是使用 Telegram。这也是上图 User 部分，我们与 Clawdbot 进行交互的界面。接着，Clawdbot 会利用网关，连接不同的聊天软件和 AI 机器人。例如，项目提到能支持 iMessage 发送和接收消息，使用的是 GitHub 上一个开源项目，steipete/imsg，它可以在 macOS 上提供一个命令行（CLI），用来「列出/读取/监听/发送」Messages.app（iMessage/SMS）的消息。

![](attachments/5cb4b40ab5da4368.png)

图片来源：https://docs.clawd.bot/channels/whatsapp针对其他的即时通讯工具，Clawdbot 也会采用官方 API、模拟网页端等标准接口的方式，来获取聊天软件接收的信息。在他们的官方文档中，给出了连接到不同聊天应用的详细设置。这些信息会进一步交给 AI 大语言模型处理，**即图中的 Agent 部分，这也是 Clawdbot 的大脑**，我们可以设置不同大语言模型的 API，使用 Claude、ChatGPT 等不同的模型来处理。Agent 还连接了丰富的 Skills 来增强智能体的能力。Skills 最近也是大热门，Clawdbot 提供了常见的网页浏览、连接日历和邮箱、搜索 X 帖子、连接 Excel、设置清单到手机备忘录等等多个技能。

![](attachments/0221d09becfcd46a.png)

Clawdbot 的官方 Skills 库：https://clawdhub.com/skills值得一提的是，Clawdbot 的大脑，其中思考和记忆部分是分开的，思考是由第三方的 AI 模型支持，但是记忆不会随着大模型的更换而消失，记忆的存储完全在部署 Clawdbot 的平台，即本地或云服务提供商。因此，一般来说，Clawdbot 的记忆容量是无上限的。这套架构，也给了 Clawdbot 一些其他 Agent 触及不到的能力。1. 它有记性了，我们上周告诉它「我只喝燕麦奶拿铁」，下周让它帮忙点咖啡时，它不会再问我们要什么奶。因为它有持久化记忆。对话不再是「用完即走」的一次性抛弃品，而是像和朋友聊天一样，有着连续的上下文。而且，这份上下文，还不会因为我们跟另一个朋友聊天，就被忘记。

![](attachments/63ed1d6f2728c114.png)

2. 主动性，这是最像真人的地方。目前的 AI 都是被动的，我们不问，它永远不说话。 Clawdbot 支持主动性。我们可以设定它每天早上 8 点，把未读邮件摘要发给我们；或者在监测到服务器宕机时，第一时间发弹窗。 从「人找 AI」变成了「AI 找人」，这是质变。3. 它真的在干活。通过丰富的工具连接和 Skills 引入，它不再只是陪聊。连接 Notion，它可以帮我们整理笔记；连接日历，它可以安排会议；连接浏览器，它可以去网上搜集资料并总结成文档。想象一下，周五下午 4:55，你的手机震动了一下。 不是老板催命，而是 Clawdbot 发来一条消息：「这是你本周完成的 5 项主要工作摘要，以及下周一上午 10 点的会议提醒，需要我把它们整理成周报发给团队吗？」很明显，这才是我们想要的「助理」，而不是那个只会写诗作画的搜索框。X 上已经有网友拿 Clawdbot 来炒股、购物、做生意、还有 Vibe Coding 也是同样不在话下。这位网友使用 Claude Opus 4.5 部署好 Clawdbot 之后，直接给了它 2000 美元的交易钱包，让它每隔 4 小时使用多种 API 进行市场研究，不断提出新的交易思路，然后重新评估未平仓位。虽然还不知道 Clawdbot 能不能帮它自己赚到买 RTX 4090 的钱，但这种跨平台、能真的放手让 AI 去做的场景，确实在变多。

![](attachments/56207d3ad305f7f7.png)

还有网友用它来买车，帮他省了 4200 美元。具体是怎么做的呢，基本上是 Clawdbot 揽了全部的工作。它先通过 Browser Use 之类的工具，浏览网页上的优惠政策和贷款利率，帮助博主找到合适的汽车型号之后；继续通过 Clawdbot 来联系供应商，要它来跟经销商讲价；一来一回，Clawdbot 还真的帮他谈下来了。

![](attachments/12db35831da7636c.png)

不只是能在买东西的时候，帮我们讲价省钱，还有人直接部署它来运营一个茶叶公司。这回真的是一台 Mac mini 就是一家公司了。

![](attachments/cf3d78dc10addb17.png)

还有 Vibe coding，直接做出一个游戏界面。

![](attachments/39504ad901a57228.png)

更多玩法，可以在官方案例展示查看，https://clawd.bot/showcase不要被网上的 Mac mini 欺骗了随着 Clawdbot 的走红，在 X 上到处都是这种照片，桌面上堆叠着好几台 Mac mini，配文是「打造我的私人 AI 算力中心」。

![](attachments/fff0d67462d8064e.jpg)

未来的 CEO 和他的员工｜图片来源：X@birdabo看起来很极客，很赛博朋克，但其实并没有说 Mac mini 是运行这个项目的标配。Clawdbot 官方直接发文说，「别再给苹果公司送钱了，能运行 Node.js 的设备，都可以拿来部署 Clawdbot。」

![](attachments/9bac54ea953aa85a.png)

因为 Clawdbot 本质上是一个「路由」。繁重的推理计算依然是在云端（OpenAI 或 Anthropic 之类的大模型服务器）完成，或者由本地电脑偶尔承担。Clawdbot 运行的地方，只需要负责收发消息、调用 API 和运行一些简单的脚本。对于 90% 的用户来说，一台每月 5 美元的廉价 VPS 云服务器，或者家里那台 24 小时开机的旧电脑，就足以让这个 AI 助手跑得飞起。

![](attachments/69f79d60568f90a1.jpg)

Clawdbot 配置流程｜图片来源：X@minchoi但无论是用 Mac mini 还是自己找一个云服务器，要搭建一个 Clawdbot 都不是一件容易的事情。Clawdbot 目前还是一个开源项目，安装它需要我们懂一点终端的知识，其实就是复制粘贴一行代码的事。此外，它也并不总是完美，偶尔会报错，配置起来也有门槛。既然都能看到，用起来这么麻烦，为什么大家还如此痴迷？因为它解决了一个巨大的痛点，割裂。现在的软件生态是割裂的，笔记在 Notion，沟通在微信之类的即时通讯软件，待办在 Things，AI 在浏览器网页里。我们每天就在这些 App 之间反复横跳，精疲力竭。Clawdbot 提供的是一种「大一统」的解法，以「对话」为界面，整合所有服务。

![](attachments/a24dc9d6f02698ae.png)

上下滑动查看更多内容根据官方的介绍，在选择 AI 聊天平台上，Clawdbot 就提供了 WhatsApp、Telegram、Discord、Slack、iMessage / Messages、Microsoft Teams 等数十种聊天工具服务。AI 模型也支持 Anthropic (Claude)、OpenAI (ChatGPT models)、Google (Gemini)、xAI (Grok)、DeepSeek、MiniMax、智谱 GLM、Perplexity 以及 OpenRouter 和本地模型等。在具体连接的服务上，它能连接到 Notion、Things 3、Obsidian 等多个生产力工具、Spotify、Shazam 等音乐流媒体、Home Assistant 智能家居控制、以及生图、网络浏览等各种各样的工具集成。

![](attachments/495248e76f6c0c38.png)

上下滑动查看更多内容｜网友分享的 Clawdbot 玩法，几乎能在数字世界里面，帮助他完成全部的任务说实话，最近接连看到 Cowork 、 Clawdbot 这种产品的爆发，我发现 AI 产品新的主线似乎开始显现。自从 Agent（智能体）概念提出来，大家就在喊「App 已死」。但直到今天，Clawdbot 这种形态的出现，才让我们真正看到了一角未来。我们不再需要为了看天气打开天气 App，不再需要为了记账打开记账 App。**所有的交互，回归到了人类最原始、最自然的本能——对话。**虽然现在的 Clawdbot 还是个需要敲代码配置的「极客玩具」，偶尔还会报错发疯。但别忘了，两三年前的 GPT-3.5 和 AI 视频，看起来就像个简陋的玩具，充满各种槽点。从 Cowork 接管电脑文件， 到 Clawdbot 接管生活琐事，这种能深度连接本地生活的 AI Agent，如果再联合更多的终端，或许能把 AI 应用落地从 ChatBot 突破到一个新的阶段。说起来这也是苹果等硬件厂商在这上面也有着巨大的优势，只是留给苹果挤牙膏的时间，真的不多了。说在最后：心动了是不是？最后给你一些提醒。Clawdbot 的行为是很大程度上「不可控」的。如果你在主力机上安装了它，还给了足够权限，它趁你不注意删除有用的文件，也是有可能的。

![](attachments/6a2a07a09c761bc4.png)

以及，别以为买一台 mac mini 就完事了：Clawdbot 运行仍然需要后端的大模型 API 去提供「算力」，而网友已经试过，让它做一些简单的操作，轻轻松松就能烧掉几十块美刀的 token……——如果你缺乏足够的「科技素养」，也没有便宜的大模型 API 方案，最好还是暂时别碰它。

🔗 相关参考信息：https://ucstrategies.com/news/what-is-clawdbot-and-why-everyone-is-suddenly-obsessed-with-it/Clawdbot GitHub 地址：https://github.com/clawdbot/clawdbot

![](attachments/750ef3665a68d8d5.png)
