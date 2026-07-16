---
title: "当 AI 浏览器走向「原生」，AI 侧栏会被吞并还是与之共存？"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/当 AI 浏览器走向「原生」，AI 侧栏会被吞并还是与之共存？.md
tags: [印象笔记]
---

# 当 AI 浏览器走向「原生」，AI 侧栏会被吞并还是与之共存？

# 当 AI 浏览器走向「原生」，AI 侧栏会被吞并还是与之共存？ --- 原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzA3MzI4MjgzMw==&mid

---

# 当 AI 浏览器走向「原生」，AI 侧栏会被吞并还是与之共存？

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzA3MzI4MjgzMw==&mid=265104...](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&mid=2651043883&idx=1&sn=64ed5207f9643eb63b56805834d7355b&chksm=8537e6d3e84bf6884e92c5bfdbf1e3c4ea00b9adfd9140c0b982747a413ced6eb2c207c6f4ce&scene=90&xtrack=1&req_id=1783823855236204&sessionid=1783823291&subscene=93&clicktime=1783823933&enterid=1783823933&flutter_pos=31&biz_enter_id=4&ranksessionid=1783823855&jumppath=20020_1783823854764,1122_1783823870504,20020_1783823871944,1104_1783823919001&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b38&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQmNdzIl9Z9RBvLLJYngaMThLTAQIE97dBBAEAAAAAANvVJTxZ1JMAAAAOpnltbLcz9gKNyK89dVj0xc08ovZfVRpzdVby8gs36OBn84g5ha4it0f7CCWW4B1Y4s16N7+8XyvhO6sZpZewJihyHwihLpI7/rESqiiJ9My1C0MebsXdlZH4BctGHPELfj7p5Qx7JQl9wgleh/Q99sMSytUCmxe8Asz/9RhWa+uNMEP3Wsqw4hs4WBYWl84u0NFT30tmAN7VDvfn8oPl1uMZXx8ncDpx1XwYEDJBzYx+IgnbQlVoouYUzV0=&pass_ticket=zKXtKbaGIpdFeL6gFwoVgDzrPfPBXVFkSeVb7Q8GOHvHCyqDGDbwvf8DCD5r1Ete&wx_header=3)

Pro会员通讯机器之心

本文来自PRO会员通讯内容，文末关注「机器之心PRO会员」，查看更多专题解读。

![](.evernote-content/5E4C0153-AF5A-4D8B-B201-B3A977252AFE/E337DE10-EAAC-466C-9328-03F9F9B5C86E.png)

2026 年 6 月，美团旗下 GN06 团队宣布 AI 原生浏览器「Tabbit 1.0」上线，以此为契机审视当前 AI 浏览器的发展格局，三条技术路线已逐渐清晰，其一，「传统内核+AI 侧栏」路线延续既有浏览架构，以插件或侧栏形式将 AI 功能附加于浏览器边缘；其二，「研究/Agent 向（Research & agent）」路线基于 Chromium 内核，将视觉多模态理解与全局上下文记忆嵌入浏览体验；其三，「AI 原生」路线以「Browser + Agent + Workflow」架构将 Agent 调度能力写入浏览器运行时。三条路线在架构融合度、模型绑定策略、自动化执行深度三个维度上呈现出不同的设计取向与技术特征。

**目录**

**01. AI 浏览器分出了哪三类？**

AI 浏览器的三条路线是演进阶梯还是平行范式？三类 AI 浏览器的分水岭在哪？...**02.当 AI 从侧栏「搬进」浏览器内核，Agent 的执行范围会发生什么变化？**架构融合度能否成为划分 AI 浏览器发展阶段的标尺？...**03.AI 浏览器会继续分化还是走向大一统？**业界对AI浏览器的未来发展方向有哪些看法？...

****AI 浏览器分出了哪三类？****

1、美团旗下 GN06 团队（原光年之外）近日发布 AI 原生浏览器 「Tabbit 1.0」。该工具的开发过程经历了从「地址栏」到「搜索框」，再到「对话框」，最终进化为「智能体」的跨越，因而其演进过程带动了业界对 AI 浏览器交互形态变迁的讨论。[1-1]

① 「Tabbit 1.0」是一款将 AI 能力深度嵌入浏览器内核的产品形态，其定位是大模型问答、全网搜索与 Agent 任务执行融为一体的 AI 工作入口。

② Tabbit 负责人刘炯称「Tabbit 1.0」的交互入口在公测 100 天内完成了四阶迭代，从最初传统网址输入，到融合全网搜索能力，接着接入大模型实现自然语言对话，最终升级为可自主跨网页执行信息采集、表单填写与文件生成的 Agent。[1-1]

③ 公测的 100 天周期中，Tabbit 1.0 内置 Agent 的任务成功率从 53.1%拉升到 91.8%的速度，单用户月均 Token 消耗量达 853 万。[1-1]

2、Tabbit 1.0 引起的话题在于，其形态的变迁不局限于单一产品的迭代，同时反映了当前行业在 AI 浏览器底层架构选择上的探索路径，各阶段所侧重的场景与相应设计，以及 AI 浏览器产品的能力边界。

① 参照 Tabbit 演进的各个阶段，当前 AI 浏览器在模型调度、上下文调用与任务执行权限等方面呈现出明显差异。当前，行业 AL 浏览器可分为三种，即「传统内核叠加 AI 侧栏」、「研究/Agent 向（Research & agent）浏览器」和「AI 原生浏览器」。[1-2]

3、传统内核+AI 侧栏路径以 Edge+Copilot 和 Brave+Leo 为代表，架构上保留完整的 Chromium 或自研内核，AI 以侧边栏插件或实验性模块的形式接入。

① Edge+Copilot 和 Brave+Leo 的共同点在于，AI 主要作为浏览器之外或浏览器边缘的辅助层存在，更多承担问答、总结、检索与内容生成等任务，并未改变浏览器原有的页面加载、权限管理与安全隔离机制。

4、第二类以研究和智能体（Research & agent）为核心的 AI 浏览器以 Perplexity Comet 和 ChatGPT Atlas 为代表，仍然建立在 Chromium 等成熟浏览器内核之上，但将 AI 从侧栏移入核心功能模块，这类产品更强调由用户意图触发连续操作，使浏览器从「显示网页」进一步转向「协助完成网页中的任务」。[1-2]

① 该类浏览器的突破在于视觉多模态理解与全局上下文记忆的嵌入，使浏览器具备跨标签页的关联分析能力，但在模型策略上仍表现为单一厂商深度绑定，用户缺乏切换弹性。

5、AI 原生浏览器（AI Native Browser）以 Tabbit、Dia、Fellou 为代表，其架构特征在于利用 AI 从底层构建标签页、输入框和智能体，在浏览器框架（Shell）中整合 Agent 调度、多模型协作与 Workflow 编排，以实现多步骤任务的执行。[1-1]

① 以 Tabbit 1.0 为例，其内置了 LongCat、DeepSeek、智谱 GLM、Kimi 等多款大模型，并会实时接入新模型 API（应用程序接口）。

② 相较于绑定单一模型体系的产品形态，这种多模型接入方式使模型能力以可切换、可调度的形式存在，浏览器可根据任务类型、响应效果或成本条件，在不同模型之间进行配置与调用。

表：三类 AI 浏览器的代表产品及特征[1-3]-[1-9]

![](.evernote-content/5E4C0153-AF5A-4D8B-B201-B3A977252AFE/60F7EFC2-B89D-4B59-A693-D2053AEAFD5A.png)

当 AI 从侧栏「搬进」浏览器内核，Agent 的执行范围会发生什么变化？

1、AI 与浏览器的集成深度带来了不同层面的架构约束，进而影响 Agent 在任务执行上的能力边界。不同集成深度对应了 Agent 不同的执行范围与环境感知水平，其能力边界呈现为从单页内嵌式信息处理到跨页面工作流状态调度的不同配置水平...

**关注👇🏻「机器之心PRO会员」，前往「收件箱」查看完整解读**![](.evernote-content/5E4C0153-AF5A-4D8B-B201-B3A977252AFE/25C56EF7-4A94-4636-82C5-A4133B015DCD.png)  
更多往期专题解读内容，关注「机器之心PRO会员」服务号，点击菜单栏「收件箱」查看。

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&mid=2651043883&idx=1&sn=64ed5207f9643eb63b56805834d7355b&chksm=8537e6d3e84bf6884e92c5bfdbf1e3c4ea00b9adfd9140c0b982747a413ced6eb2c207c6f4ce&scene=90&xtrack=1&req_id=1783823855236204&sessionid=1783823291&subscene=93&clicktime=1783823933&enterid=1783823933&flutter_pos=31&biz_enter_id=4&ranksessionid=1783823855&jumppath=20020_1783823854764,1122_1783823870504,20020_1783823871944,1104_1783823919001&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b38&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQmNdzIl9Z9RBvLLJYngaMThLTAQIE97dBBAEAAAAAANvVJTxZ1JMAAAAOpnltbLcz9gKNyK89dVj0xc08ovZfVRpzdVby8gs36OBn84g5ha4it0f7CCWW4B1Y4s16N7+8XyvhO6sZpZewJihyHwihLpI7/rESqiiJ9My1C0MebsXdlZH4BctGHPELfj7p5Qx7JQl9wgleh/Q99sMSytUCmxe8Asz/9RhWa+uNMEP3Wsqw4hs4WBYWl84u0NFT30tmAN7VDvfn8oPl1uMZXx8ncDpx1XwYEDJBzYx+IgnbQlVoouYUzV0=&pass_ticket=zKXtKbaGIpdFeL6gFwoVgDzrPfPBXVFkSeVb7Q8GOHvHCyqDGDbwvf8DCD5r1Ete&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/ad7dc636-14eb-41f1-87fc-57b4a827f1c2/ad7dc636-14eb-41f1-87fc-57b4a827f1c2/)