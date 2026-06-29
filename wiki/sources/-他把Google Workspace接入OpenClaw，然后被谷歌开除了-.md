---
title: "他把Google Workspace接入OpenClaw，然后被谷歌开除了"
type: source
created: 2026-06-28
updated: 2026-06-28
source_path: 印象笔记管理工具/他把Google Workspace接入OpenClaw，然后被谷歌开除了.md
tags: [evernote, impression]
---
---
title: "他把Google Workspace接入OpenClaw，然后被谷歌开除了"
source: evernote
type: note
export_date: 2026-06-28
guid: 21289f1b-6d6d-4cef-8111-64004999c49f
---

# 他把Google Workspace接入OpenClaw，然后被谷歌开除了

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzA3MzI4MjgzMw==&mid=265104...](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&mid=2651041019&idx=1&sn=b533a9bce8f515dcece68765375638cf&chksm=8572f975ccedf607506c4b2efcd4b3eb9957285a1f5f30193eb8f776beffaebf4e0bef9d031c&scene=90&xtrack=1&req_id=1782307280907677&sessionid=1782304295&subscene=93&clicktime=1782307735&enterid=1782307735&flutter_pos=18&biz_enter_id=4&ranksessionid=1782307280&jumppath=WAWebViewController_1782307583083,WAWebViewController_1782307583588,20020_1782307610347,1104_1782307612648&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b2b&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQALjzdxTFHoanpRdzCmPzRxLTAQIE97dBBAEAAAAAAIhkMl5R6SYAAAAOpnltbLcz9gKNyK89dVj0BqdfYXE8lcFopA7OnfsdsIk+WBawVLhbxdz5vql/2ShjJmD28GvnONRlmbBV5wq22ur8MbuDemGxstvQnCV+z++c3j/d+UpJxl4GNtiHtN/YU06ppSXELynGVQ0Q9Bdl8CbEg73uZRXjKFgCgJug0NyV8OvXrw4gYck7INwiiZ1EYlrsZszSmqP/mZvjSre1nJ4HocBtURPrtsDTjwx9Gwm2IY3G/Y5ZQgO58ZM=&pass_ticket=OtrrnriuUUl3Rzf5wT1qMm0xGYx76BE3+QLBBdEFPS9Ops9RvjaRq8hvPv7z78i2&wx_header=3)

Original关注AI的 机器之心

![](attachments/8fa5d46bcd5ae8a5.png)

机器之心编辑部

什么？就因为做出了一个谷歌用户真正想要的工具，谷歌解雇了自家一位工程师。

这个项目叫「Google Workspace CLI」，上线之后迅速引爆了开发者社区，还一度冲上 Hacker News 第一，几天之内便在 GitHub 上拿下了数千 Star。

在项目刚出的时候，机器之心也对它进行了报道，详情可见：[一键接入 OpenClaw，谷歌开源 CLI 狂揽 15k Stars，Agent 开始接管 Workspace](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&mid=2651020388&idx=1&sn=deb1784bd1795c6a77b14d76851c9d8c&scene=21#wechat_redirect)。

截至目前，该项目的 Star 量已经近 3 万。

![](attachments/ed74fa567e4840af.png)

项目地址：https://github.com/googleworkspace/cli

按理说，这应该是一个典型的内部创新故事：工程师发现需求，快速做出产品，用真实用户验证价值，然后被公司吸收、放大、正式化。

但故事没有这样发展。

这位工程师 Justin Poehnelt 近日发推透露，两个月前，自己因为这个项目被谷歌解雇了。

更讽刺的是，就在他被解雇前两天，Google Cloud Next 刚刚宣布：官方版 Workspace CLI 要来了。

![](attachments/2a02628e4aa6e2ff.png)

在推文中，他表示，「那是一段不可思议、也让人困惑的经历。一边是一些总监和负责人来问我，他们能从这个工具里学到什么；另一边，我又被法务反复追问，为什么我项目的 GitHub 代码仓库里会出现谷歌的 Logo 和品牌配色。」

Justin Poehnelt 认为，真正的原因可能是 Workspace 以及某些项目及负责人，担心自己被冲击。但这种恐惧并不是专门针对我的 CLI，而是更广泛地来自他们对 Agent 会给 Workspace 带来什么变化的担忧。

因此，他想把这件事说出来，这样以后更容易向别人解释自己的经历。同时，这也是一段他真正拥有的经历，是自我修复的一部分。

翻开项目贡献者页面，排名第一的正是 Poehnelt，有 24 次 commits；排名第二的是 jpoehnelt-bot，有 20 次 commits。也就是说，他毫无疑问是这个项目的核心贡献者。

![](attachments/d04494029021b952.png)

OpenClaw 之父为 Justin Poehnelt 打抱不平，「谷歌把那个做出了 Google Workspace CLI 的人开了，原因就是他做出了这个项目。幸好，谷歌开不了我。」

![](attachments/896f98fabb4d5af2.png)

同时想要拉这位前谷歌工程师入伙，「Codex 团队一直在寻找那种主动性强、能把事情做成的人。欢迎私信我。」

![](attachments/9ffafad331ae0e18.png)

这具体是个啥项目？

有了 Google Workspace CLI 之后，人类开发者不再需要根据 REST 文档手写 curl 请求。它为每个资源都提供 --help 帮助信息，支持使用 --dry-run 预览请求，并自动处理分页。

对于 AI 智能体，所有返回结果都是结构化的 JSON。结合内置的 Agent 技能，你的 LLM 就可以在无需编写额外工具的情况下，直接管理 Google Workspace。

这意味着，该 CLI 将 Google Workspace API 变成了一个既适合人类，也适合 AI Agent 调用的统一接口。人类不用写 API 请求，AI 不需要写额外工具。

在架构层面，Google Workspace CLI 采用一种两阶段解析（two-phase parsing）策略：

- 读取 argv，以识别要调用的服务（例如 drive）。
- 获取该服务的 Discovery Document（API 发现文档），并进行缓存（缓存时间为 24 小时）。
- 根据文档中定义的资源（resources）和方法（methods），动态构建一个 clap::Command 命令树。
- 再次解析剩余的命令行参数。
- 完成身份认证，构建 HTTP 请求并执行。

所有输出，包括成功结果、错误信息以及下载相关的元数据，都会以结构化 JSON 的形式返回。

至于开发者关注的 AI Agent Skills 能力，Google Workspace CLI 内置 100 多个 Agent Skills（以 SKILL.md 文件形式提供），每个支持的 API 都对应一个技能，同时还包含一些用于常见工作流程的高层辅助技能，以及 50 个精选使用示例，覆盖 Gmail、Drive、Docs、Calendar 和 Sheets 等应用。

完整 Agent Skills 列表如下：

![](attachments/f5bfe39a6d01a6ec.gif)

*参考链接：*

*https://x.com/JPoehnelt/status/2069482265953087602?s=20*

© THE END
