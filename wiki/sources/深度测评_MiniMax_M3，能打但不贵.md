---
title: 深度测评 MiniMax M3，能打但不贵
type: source
created: 2026-06-17
updated: 2026-06-17
source: 印象笔记管理工具
source_path: 印象笔记管理工具/深度测评 MiniMax M3，能打但不贵.html
tags: [AI技术]
---

# 深度测评 MiniMax M3，能打但不贵

原文链接: https://mp.weixin.qq.com/s?__biz=MzU4NTE1Mjg4MA==&mid=224749...

...深度测评 MiniMax M3，能打但不贵Original苍何 苍何 
这是苍何的第 548 篇原创！大家好，我是苍何。
其实在 MiniMax M3 模型刚发布的时候就看到 Vercel CEO 发过一条帖子，说 M3 在 Next.js 的 AI Coding Agent 评测中仅次于 Opus 和 GPT5，但价格便宜了 10 倍。
当时就一直想做下测试，但后来出差加一堆的事情就没来得及，所以这篇文章也拖到现在才发。
我上来就用自己的开源项目 WeSight 里的 Claude Code 快速接入了 MiniMax M3。
刚好最近 WeSight 积了不少 issue，干脆先让 M3 试试能不能自主修复。
说一下背景，WeSight 目前有 954 个工程文件，16 万多行代码，是个真实的工程化项目，不是那种 demo 级别的玩具仓库。
配置好 M3 后，我直接把 issue 链接丢给它，开启 plan 模式，先让它分析项目代码，再想办法修复。
M3 花了一些时间获取项目上下文后，开始自行调用技能去拉 GitHub issue 信息。
这里有个小细节值得单独说。M3 拿到 Issue 后没有上来就蛮干，而是先做了任务分解，判断当前有哪些工具可用，然后定了一套降级策略，gh CLI 优先，失败走浏览器抓取，都不行再向用户要内容。这其实就是 Agent 领域里的&#xa0;Plan-then-Execute&#xa0;范式，先规划再执行，遇到阻塞还能自己绕路。
这种能力在简单任务里看不出差距，但任务链一旦拉长，模型会不会主动规划、能不能自己做容错，直接决定了最终产出能不能一次跑通。
而且你会发现，M3 最终选择的是浏览器抓取，而不是 gh CLI。因为这个 issue 里有附件，gh issue view 对附件和 Markdown 渲染的支持不如网页直观，M3 自己判断出来并切换了方案。
耗时 9.5 分钟后，bug 修复完成，修改 12 个文件及 2 个核心文件。
修改完代码 diff 后，完成了 449 测试用例的验证通过。
然后我还让 Codex 的 GPT 5.5 做了下 Code Review。指出了一两个小问题，我又让 M3 来修复。
经过 1 轮的 Code Review 和修改后，重新打包，发现已经修复这个 bug 了。
然后让 M3 自己推送代码到 GitHub，然后自动回复和关闭 issure。
我发现用 M3 来写代码，然后用 Claude Opus 和 GPT 5.5 来做对抗式 Code Review，效果很不错，而且还省 token 啊，性价比拉满，毕竟后两玩意太贵。
聊完 Coding Agent，咱换个赛道。
听说 M3 的 3D 效果挺猛，我顺手把它和 DeepSeek-V4-Pro 都接进了 Hermes，丢同一个 Prompt，让它们用 Three.js 各自渲染一版 3D 城市街道。
Prompt 是这个。
●●●生成一个单文件 HTML 页面，使用 Three.js（通过 CDN 引入），渲染一个&#xa0;3D&#xa0;可交互的城市街道场景。要求：
1.&#xa0;有一条可行驶车辆的沥青马路，包含车道线、斑马线；
2.&#xa0;马路两侧有多层建筑，建筑窗户有纹理和灯光效果；
3.&#xa0;人行道上有路灯、树木、长椅等街道设施；
4.&#xa0;有
