---
title: 深度测评 MiniMax M3，能打但不贵 2
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/深度测评 MiniMax M3，能打但不贵 2.md
tags: [evernote, impression, yinxiang]
---

# 深度测评 MiniMax M3，能打但不贵

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzU4NTE1Mjg4MA==&mid=224749...](https://mp.weixin.qq.com/s?__biz=MzU4NTE1Mjg4MA==&mid=2247498785&idx=1&sn=d7266d060dbf8ea11ef770a25999fdb6&chksm=fc7b0a8e4aa714c65e999f780d9d2c0ec13c855075377fe5ce572ff488400b51e0f7bf198ec6&scene=90&xtrack=1&req_id=1781527553758468&sessionid=1781527535&subscene=93&clicktime=1781528247&enterid=1781528247&flutter_pos=7&biz_enter_id=4&ranksessionid=1781527553&jumppath=WAWebViewController_1781528210804,WAWebViewController_1781528211309,20020_1781528230793,1104_1781528241379&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004a2f&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQRUIOGmzJtC3SEhMeopNOQBLTAQIE97dBBAEAAAAAAHeUD8NzWh8AAAAOpnltbLcz9gKNyK89dVj0kFJyDVc9DcLF8mpbQvYYHRjlH3yF1u6H1fBc6jCTjBkeV5q1koXdvuqTmn3pce/hihIIZGtLV4322fQwmlCOLIEGWAJgNtw/OF0yRxdfzjUOs1RVx3dN5MVWqwtLZiB/ulX+REpOTWlW+/dzgJw3M4Y7Ewjb8zqVzIM6ePzFQIxgSymxJcmQzppJy+3GPcJ+du4C4PbTUTq6RLJqntzC3TKbh8h+ZCpUmMwOAoY=&pass_ticket=QmNEeJtlYO+wFVrCDmmXF54ePaelR5lbZmz9jEwYQc0Ornr8X10ugCEpxNsec7Pt&wx_header=3)

深度测评 MiniMax M3，能打但不贵
=====================

Original苍何苍何

这是苍何的第 548 篇原创！

大家好，我是苍何。

其实在 MiniMax M3 模型刚发布的时候就看到 Vercel CEO 发过一条帖子，说 M3 在 Next.js 的 AI Coding Agent 评测中仅次于 Opus 和 GPT5，但价格便宜了 10 倍。

![](.evernote-content/CED00DCE-F495-4F85-8ED4-9422D1C81FFD/5E15E80B-B362-49A0-80E8-7AEA9788F19B.png)

当时就一直想做下测试，但后来出差加一堆的事情就没来得及，所以这篇文章也拖到现在才发。

我上来就用自己的开源项目 WeSight 里的 Claude Code 快速接入了 MiniMax M3。

![](.evernote-content/CED00DCE-F495-4F85-8ED4-9422D1C81FFD/7E3E3BCC-6FDB-40F5-94E2-6E050DA694AD.png)

刚好最近 WeSight 积了不少 issue，干脆先让 M3 试试能不能自主修复。

![](.evernote-content/CED00DCE-F495-4F85-8ED4-9422D1C81FFD/33B8D54C-2F40-41DF-BF15-E65A43554981.png)

说一下背景，WeSight 目前有 954 个工程文件，16 万多行代码，是个真实的工程化项目，不是那种 demo 级别的玩具仓库。

配置好 M3 后，我直接把 issue 链接丢给它，开启 plan 模式，先让它分析项目代码，再想办法修复。

![](.evernote-content/CED00DCE-F495-4F85-8ED4-9422D1C81FFD/63DD7168-10F0-4CFA-B8D6-D418B9909181.png)

M3 花了一些时间获取项目上下文后，开始自行调用技能去拉 GitHub issue 信息。

![](.evernote-content/CED00DCE-F495-4F85-8ED4-9422D1C81FFD/AB2D142C-FEE7-4B63-9EA8-FAD2A4AA063B.png)

这里有个小细节值得单独说。M3 拿到 Issue 后没有上来就蛮干，而是先做了**任务分解**，判断当前有哪些工具可用，然后定了一套降级策略，gh CLI 优先，失败走浏览器抓取，都不行再向用户要内容。这其实就是 Agent 领域里的 **Plan-then-Execute** 范式，先规划再执行，遇到阻塞还能自己绕路。

![](.evernote-content/CED00DCE-F495-4F85-8ED4-9422D1C81FFD/116CA728-4A9C-444F-9D06-83B2F74C8EFB.png)

这种能力在简单任务里看不出差距，但任务链一旦拉长，模型会不会主动规划、能不能自己做容错，直接决定了最终产出能不能一次跑通。

而且你会发现，M3 最终选择的是浏览器抓取，而不是 gh CLI。因为这个 issue 里有附件，gh issue view 对附件和 Markdown 渲染的支持不如网页直观，M3 自己判断出来并切换了方案。

![](.evernote-content/CED00DCE-F495-4F85-8ED4-9422D1C81FFD/DE654944-E9D7-4332-BF37-E3C0BFF3F6B9.png)

耗时 9.5 分钟后，bug 修复完成，修改 12 个文件及 2 个核心文件。

![](.evernote-content/CED00DCE-F495-4F85-8ED4-9422D1C81FFD/3D4B47E1-ED02-4E92-B73A-4CBDE47A36DE.png)

修改完代码 diff 后，完成了 449 测试用例的验证通过。

![](.evernote-content/CED00DCE-F495-4F85-8ED4-9422D1C81FFD/B4BBB141-DC5C-4887-997B-20F40E2397D1.png)

然后我还让 Codex 的 GPT 5.5 做了下 Code Review。指出了一两个小问题，我又让 M3 来修复。

![](.evernote-content/CED00DCE-F495-4F85-8ED4-9422D1C81FFD/A43358F3-315A-4E69-AB86-3D1209BEAB44.png)

经过 1 轮的 Code Review 和修改后，重新打包，发现已经修复这个 bug 了。

然后让 M3 自己推送代码到 GitHub，然后自动回复和关闭 issure。

![](.evernote-content/CED00DCE-F495-4F85-8ED4-9422D1C81FFD/FE3FAD44-B25D-4941-809E-2E9F0157A759.png)

我发现用 M3 来写代码，然后用 Claude Opus 和 GPT 5.5 来做对抗式 Code Review，效果很不错，而且还省 token 啊，性价比拉满，毕竟后两玩意太贵。

聊完 Coding Agent，咱换个赛道。

听说 M3 的 3D 效果挺猛，我顺手把它和 DeepSeek-V4-Pro 都接进了 Hermes，丢同一个 Prompt，让它们用 Three.js 各自渲染一版 3D 城市街道。

Prompt 是这个。

```
●●●

生成一个单文件 HTML 页面，使用 Three.js（通过 CDN 引入），渲染一个 3D 可交互的城市街道场景。

要求：

1. 有一条可行驶车辆的沥青马路，包含车道线、斑马线；

2. 马路两侧有多层建筑，建筑窗户有纹理和灯光效果；

3. 人行道上有路灯、树木、长椅等街道设施；

4. 有环境光和定向阳光，并开启阴影；

5. 支持鼠标拖拽旋转视角（OrbitControls），滚轮缩放；

6. 所有几何体和纹理必须程序化生成，不能使用外部图片资源；

7. 画面要有科技感，夜晚/白天模式可切换。
```

![](.evernote-content/CED00DCE-F495-4F85-8ED4-9422D1C81FFD/33735751-3A87-4C29-9DCD-685E3F903966.png)

先来看 MiniMax M3 的效果。

  

不瞒你说，M3 第一眼给我的感觉就是，交互做得到位。

昼夜联动、小车速度交互、时间、车速、雾气、昼夜四个控制按钮一个不落。左下角还贴心地放了实时 FPS、建筑数量、光源数量的状态面板。

更细的地方还在后面。

车头灯用了 SpotLight + target 做真实投射光，尾灯是 emissive 红色，建筑天线点缀着红色闪烁灯。路灯做了点光源加微闪烁，模拟那种真实路灯的不稳定感。树冠用三层球体堆叠，加了随机偏移防对称。

不过建筑细节和阴影比较粗糙，天空和夜晚效果一般，算是个小遗憾。

再来看 DeepSeek-V4-Pro 的效果。

![](.evernote-content/CED00DCE-F495-4F85-8ED4-9422D1C81FFD/C9491C87-4D0C-4C8A-B1F9-BB232A8E8EE6.png)  

DeepSeek-V4-Pro 这版完成度也能打。

道路、建筑、灯光、树木、长椅、霓虹牌和昼夜切换全都搭起来了，视觉氛围拉满，程序化纹理让细节加分不少。

它更偏视觉呈现，交互上相对克制，能调的参数有限。白天光照有点过曝，我翻了下代码，部分函数参数没真正用起来。

我看大家都在说 M3 的原生多模态表现不错，我测试了一个 Sketch-to-UI 的场景。

我随手画了一张电商商品详情页的草图，塞了商品图轮播、价格区、规格选择、加购按钮、详情 Tab 这些常见模块。

![](.evernote-content/CED00DCE-F495-4F85-8ED4-9422D1C81FFD/236044BC-50A7-49FD-9DFF-DF4DA1990BD7.png)

然后给两个模型发了同样的 Prompt。

```
●●●

我画了一张电商商品详情页的草图，请根据这张图片生成一个可运行的单文件 HTML 页面。

要求：

1. 识别草图中的所有组件和布局；

2. 使用 TailwindCSS 美化，尽量还原草图结构；

3. 商品图支持轮播切换，规格选择有选中状态反馈；

4. 加入购物车按钮需要有交互反馈（例如点击后数量变化或提示）；

5. 页面需要是响应式的；

6. 所有资源内联，单文件即可运行。
```

MiniMax M3 的输出。

![](.evernote-content/CED00DCE-F495-4F85-8ED4-9422D1C81FFD/D6EB0C81-DB15-4DE8-9A7F-705F12DF54C0.gif)

M3 对草图的理解依然在线。

商品图轮播、价格标题、规格选择、加购按钮、详情 Tab、底部推荐，全都识别到位。轮播切换、规格高亮、加购提示条这些交互也顺手补齐了。

最让我意外的是，它把我画得很潦草的背包，直接给还原成了实际效果。

这种「看懂线条 + 补全行业默认交互」的能力，做前端原型真的省心。

![](.evernote-content/CED00DCE-F495-4F85-8ED4-9422D1C81FFD/2F7D8E97-3BBC-4836-9928-AF82E731DC32.gif)

最后一个 case，压一压极限，超长上下文 + Agent 长任务。

我直接搬来一份 ZF 工作报告，让两个模型跑同一个多步骤的政策分析任务。

Prompt 是这个。

```
●●●

你是一名顶级产业分析师。请对我提供的政策文件进行对比分析，重点识别与上一版本相比的新增内容、删减内容、表述变化和政策升级方向，找出真正的边际变化。随后从投资视角推演政策影响路径：**政策变化 → 行业影响 → 产业链传导 → 细分赛道 → 受益公司**，分析哪些赛道获得增量支持、哪些机会存在预期差、哪些公司可能受益最大。不要复述文件内容，而要解释政策变化背后的意图、市场容易忽略的信号以及未来可能产生的产业影响，并以图表和HTML方式呈现结论。
```

MiniMax M3 的输出报告。

  
可以看到 M3 在这个任务上的表现很不错，细节处理相当到位。  
拿 2026 年和 2025 年两版报告做了逐条对比，识别出 13 个维度的边际变化，推演了完整的投资传导路径，还附带 9 张可视化图表和四层受益标的矩阵，30+ 标的逐一拆解。从核心判断到 13 个细分维度的边际变化，5 个市场容易忽略的隐性信号，再到 12 个赛道的政策红利强度评分，最后落到风险提示和操作建议。一份能直接给投研团队参考的报告，它一次就跑出来了。再看 DeepSeek-V4-Pro。  
  
DeepSeek-V4-Pro 也拆得不错，速度还更快，政策边际变化对比表、产业链传导路径图、细分赛道受益热力图该有的都有。只是维度上没 M3 铺得开，一些细分赛道的深度拆解也相对浅一些。金融长文档 + Agent 长任务这种场景，M3 在输出结构和引用规范上更稳，几百页文档多步骤提取一次跑通的概率更高。DeepSeek-V4-Pro 的优势在速度，响应更跟手。

金融场景天然就是长文档、多步推理、高频跑量，模型需要做「边际变化识别→产业链传导→细分赛道映射」，M3 的细节表现会更好一些。

所以，对于需要高频处理研报、招股书、政策文件的金融场景来说，M3 更为适合，性价比更高。

几个 case 跑完，我整体感受是，M3 和 DeepSeek-V4-Pro 各有侧重，但 M3 在多模态理解、Agent 长任务稳定性和交互细节上，确实有自己的东西。

瞅一眼官方的 OSWorld，M3 在 Computer Use、多模态这几个评测里，成绩还真不赖。

![](.evernote-content/CED00DCE-F495-4F85-8ED4-9422D1C81FFD/DAEE6F32-61E2-4434-9BA7-4B9DE384789E.png)

而且 M3 还是开源的。

价格这块也值得提一嘴。从 M2 到 M3，MiniMax 在定价上一直很克制，同等能力水平下基本是全球旗舰模型里最实惠的那个。对开发者来说，这意味着你可以放心地把它塞进生产环境跑量，不用一边调 API 一边心疼账单。

一边是大洋彼岸的闭源模型死贵还各种限制，一边是国内团队在卷能力卷开源，想办法让更多人用上好模型。讲真的，AI 不应该是少数人的特权，它应该是所有人的工具。

![](.evernote-content/CED00DCE-F495-4F85-8ED4-9422D1C81FFD/25E8D972-F2B1-4F72-885D-17469068A35A.png)

国产开源模型，是真在卷出花来了。

你跑过 M3 没？效果咋样，评论区唠唠。

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzU4NTE1Mjg4MA==&mid=2247498785&idx=1&sn=d7266d060dbf8ea11ef770a25999fdb6&chksm=fc7b0a8e4aa714c65e999f780d9d2c0ec13c855075377fe5ce572ff488400b51e0f7bf198ec6&scene=90&xtrack=1&req_id=1781527553758468&sessionid=1781527535&subscene=93&clicktime=1781528247&enterid=1781528247&flutter_pos=7&biz_enter_id=4&ranksessionid=1781527553&jumppath=WAWebViewController_1781528210804,WAWebViewController_1781528211309,20020_1781528230793,1104_1781528241379&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004a2f&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQRUIOGmzJtC3SEhMeopNOQBLTAQIE97dBBAEAAAAAAHeUD8NzWh8AAAAOpnltbLcz9gKNyK89dVj0kFJyDVc9DcLF8mpbQvYYHRjlH3yF1u6H1fBc6jCTjBkeV5q1koXdvuqTmn3pce/hihIIZGtLV4322fQwmlCOLIEGWAJgNtw/OF0yRxdfzjUOs1RVx3dN5MVWqwtLZiB/ulX+REpOTWlW+/dzgJw3M4Y7Ewjb8zqVzIM6ePzFQIxgSymxJcmQzppJy+3GPcJ+du4C4PbTUTq6RLJqntzC3TKbh8h+ZCpUmMwOAoY=&pass_ticket=QmNEeJtlYO+wFVrCDmmXF54ePaelR5lbZmz9jEwYQc0Ornr8X10ugCEpxNsec7Pt&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/da4b6e65-a4d5-41e7-9ebb-9b838e3d12d5/da4b6e65-a4d5-41e7-9ebb-9b838e3d12d5/)
