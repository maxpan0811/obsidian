---
title: GLM 5.1 高速版实测
type: source
created: 2026-06-08
updated: 2026-06-08
sources: [https://mp.weixin.qq.com/s?__biz=MzU4NTE1Mjg4MA==&mid=224749...]
source_path: 印象笔记管理工具/实测 GLM5.1 高速版，快到离谱还不掉智商.md
tags: [glm, zhipu, model-review, speed]
updated: 2026-06-27
updated: 2026-06-27
updated: 2026-06-27
updated: 2026-06-27
---

---
title: "实测 GLM5.1 高速版，快到离谱还不掉智商"
source: evernote
type: note
export_date: 2026-06-24
guid: 4a198bb7-5264-442e-96d7-155832d3d8e1
---

# 实测 GLM5.1 高速版，快到离谱还不掉智商

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzU4NTE1Mjg4MA==&mid=224749...](https://mp.weixin.qq.com/s?__biz=MzU4NTE1Mjg4MA==&mid=2247498626&idx=1&sn=943aab0a86fb297ab490497d9a2d3927&chksm=fc1e33547d15e46a62f8b4e674d12b4e52a7929f5b5b20882c62ad5c310b4acd5e5c0a03a129&scene=90&xtrack=1&req_id=1779545244963818&sessionid=1779537340&subscene=93&clicktime=1779545579&enterid=1779545579&flutter_pos=16&biz_enter_id=4&ranksessionid=1779545245&jumppath=20020_1779545520139,WCWebImageBrowserViewController_1779545528161,20020_1779545534860,1104_1779545575324&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004932&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQbKryKZQg3eip8vbkAYfHhhLTAQIE97dBBAEAAAAAAFo5LW5pd64AAAAOpnltbLcz9gKNyK89dVj0QQAseC6zINh1CQE83g4ntvSqvz/BNxY/HwHuYvHPnqjBH8ChAc0gcela/wELH3LnPjHTda/v8griQN54ImOFdcqHz8vL4IhyOCHCrlqIPwZMKT39DreSGJA+s0MNXqNcrJYrchLj56SYI+Qf9gmdmwplO7C++OxjYraphSkdQJK437O+f5yBmJTfYSa6ZwjpLCJVQQo0F8cfyL1bgNuKEhEZcUNyjg6whRaHbEY=&pass_ticket=kGX9a5WxDuezZ4ilM4F2aqJ0GV0eu78xnNVD3JYuRnt3bSSa4nh3qZ62F0h2+EcZ&wx_header=3)

Original苍何苍何

这是苍何的第 537 篇原创！

大家好，我是苍何。

说实话，用 AI Coding 这么久来，最让我崩溃的一件事就是：等。

你让它改个组件，转圈圈十几秒；让它重构个模块，一分钟过去了还在吐字。思路早就跑到前面去了，AI 还在后面慢悠悠地挤牙膏。

直到前两天，智谱给了我一个 GLM-5.1 高速版的 API 内测，400 tokens/s。

什么概念？代码不是一行一行「写」出来的，是直接「喷」出来的。

我第一反应是：这速度，怕不是牺牲了效果吧？毕竟行业潜规则大家都懂，快的模型约等于小模型。

但实测下来，打脸了。

这玩意是旗舰级能力+极致速度，两个我全都要，还真让它做到了。废话不多说，直接上case。

我在 Claude Code 中配了 GLM 5.1 高速版，30 秒不到就给我整出了这个东西。

玩家控制一个角色在 3D 地图里移动。玩家可以输入自然语言，系统调用 GLM-5.1 高速版，将用户输入转换成结构化 JSON 场景指令，然后前端实时执行这些指令，让 3D 场景立即发生变化。

这个是我给的提示词：

![](attachments/c71b0563eb25107a.png)

```
你是资深全栈工程师与 3D Web 游戏开发专家，请从零实现一个「Text-to-World」Web Demo：玩家在 Three.js/R3F 的 3D 世界中移动，并通过自然语言实时改变场景。用户输入“在前方生成赛博朋克城堡并切换暴雨夜晚”等文本后，后端调用 GLM-5.1 高速版，  
将文本转换为结构化 JSON commands（spawn_object、set_environment、add_effect 等），前端 SceneCommandExecutor 实时解析并执行，让世界瞬时变化。技术栈要求 React + TypeScript + React Three Fiber + Tailwind + Node.js/Express，  
支持 WASD、鼠标视角、流式响应、环境天气、粒子特效、NPC、传送门等能力，且 API Key 不暴露在前端。  
请输出完整项目架构、前后端目录结构、JSON Schema、核心执行器设计、完整可运行代码、README、  
环境变量配置与启动命令，代码需模块化、类型清晰、具备错误处理与高实时交互体验。
```

这个喷代码的速度，服了，还没反应过来，就直接做完了，关键效果还很不错，还是那个 GLM 5.1，只是真的更快了。

为了更深入了解下，我又把分别搭载 GLM 5.1 高速版和 DeepSeek V4 Pro 的 Claude Code 接进 WeSight。

相同一个任务，我们来直观的对比下一些重要指标，比如输入输出 Token、TTFT、TPS 等。

这个是 DeepSeek V 4 Pro 的指标：

![](attachments/5a50a804a8694e9e.png)

估算 TPS 为 55.0，总耗时 2.3 分钟。

TPS 指的是模型每秒能生成多少 token，总耗时是指从发送到完整结束花了多久。

这里除去了模型内部推理、代理步骤做的估算 TPS，实际耗时为最终文本到达 WeSight 的时间。

![](attachments/239e6986f26b09a7.png)

相同的任务，我把 Claude Code 里面的模型替换为 GLM 5.1 高速版，TPS 直接就干到了 350，虽然离官方说的 400 还有一点点差距，但实际体感，无法表达，你还没反应过来就干完了。

![](attachments/9ce3ce2a54e13856.png)

实际耗时变为了 2.6 秒，这个体感还是非常明显的。在 WeSight 中你也能很直观的看到这个数据变化。

![](attachments/93c492f8b1058542.png)

相同的任务，这是 Codex 的数据，用的 GPT 5.5 high，TPS 是 153.1，这也符合基准网站 Artificial Analysis 给出的 OpenAI 高速模型 TPS 数据在 120~170 t/s。

侧面反应 WeSight 在预估 TPS 上还是做了很多功课的。

不瞒你说，WeSight 的这个监控能力也是通过 GLM 5.1 高速版开发的，前前后后几个小时就搞定了。

现在 WeSight 支持任务状态监控了。

这个是我在 WeSight 中用 Claude Code 配合 GLM 5.1 高速版 1.4 分钟就完成的宠物电商网站，功能完全可用。

这个视频是原速录制下来的，你看下这个喷代码的速度，有点可怕的，太快了吧。

数据详情：

![](attachments/58bce2c620976373.png)

TPS 在 300 左右，总计耗时 1.4 分钟。

什么概念，我打个水都没打完，就给我开发完了。

我同样的任务，用 DeepSeek V 4 Pro 试了一遍，就花了差不多 4.1 分钟，是 GLM 5.1 高速版耗时的十倍左右。

![](attachments/f29fe9a39c0fc7f5.png)

当你把 GLM 5.1 高速版接入 Claude Code 或者 Hermes Agent、OpenClaw，这才是你起飞的开始。

比如，你看我用飞书直接指挥搭载 GLM 5.1 高速版 Claude Code 和搭载 GPT 5.5 的 OpenClaw 同时做个爱心表白网页。

![](attachments/b9cf950455ab6e5c.jpg)

你可以看到 GLM 5.1 高速版几乎是秒出结果：

![](attachments/8480cae3a752bee1.png)

而 GPT 5.5 花费了 47.2 s，对比下来速度差了不是一点半点。

![](attachments/3e30d3b6671d0ff3.png)

而实际出来的效果是差不多的。

![](attachments/164d6f47b38dfc84.png)

## 为什么快这么多？

简单说下技术层面。

GLM-5.1 高速版背后是智谱自研的 TileRT 推理引擎，核心思路是把传统推理框架里那些零碎的算子调度、内存读写、同步等待全部干掉，编译期就把整个计算图编排成一个常驻 GPU 的 Engine Kernel。

通俗讲就是：传统方案每算一步都要「汇报一次」，TileRT 直接把整条流水线焊死在 GPU 上，中间不回头，一路算到底。

所以 400 tokens/s 不是峰值跑分，是稳定可用的生产级速度。

## 写在最后

说真的，这次体验完 GLM-5.1 高速版，我最大的感受是：速度本身就是一种能力。

以前我们评价模型，看的是跑分、看的是效果。但当你真正把模型接进工作流，每天跟它协作几十上百次的时候，你会发现速度才是决定体验的那个变量。

3 秒出结果和 30 秒出结果，不只是时间差了 10 倍，是你的心流状态完全不一样。快到一定程度，AI 真正变成了你的实时搭档，想到哪它就跟到哪。

看了下目前 GLM-5.1-HighSpeed 模型仅面向部分企业客户定向开放。

我是苍何，AI 时代的速度战争才刚刚开始，咱们下期见。
