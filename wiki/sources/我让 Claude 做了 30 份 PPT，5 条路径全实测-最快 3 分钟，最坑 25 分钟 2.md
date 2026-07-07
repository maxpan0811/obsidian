---
title: 我让 Claude 做了 30 份 PPT，5 条路径全实测：最快 3 分钟，最坑 25 分钟 2
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/我让 Claude 做了 30 份 PPT，5 条路径全实测：最快 3 分钟，最坑 25 分钟 2.md
tags: [evernote, impression, yinxiang]
---

# 我让 Claude 做了 30 份 PPT，5 条路径全实测：最快 3 分钟，最坑 25 分钟

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzYzMjY1OTI0MA==&mid=224748...](https://mp.weixin.qq.com/s?__biz=MzYzMjY1OTI0MA==&mid=2247484628&idx=1&sn=5d5fc5f71d5e6c718c682d56e554ce7e&chksm=f1e3d32742056d89733621ae9911107024a1ad1b4345dabba31c670e7a9ba4b77534c81af52e&scene=24&xtrack=1&clicktime=1777365304&enterid=1777365304&ascene=14&devicetype=iOS26.4.2&version=1800472d&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ+O7N0aTAT//P4NV0V1Pj1RLVAQIE97dBBAEAAAAAADtyL/1FQ5oAAAAOpnltbLcz9gKNyK89dVj0GoWb0OU1C0a/ZIX7XB2l+/s/EzzaUb8bZY7o5CXod5CFrpji/Y8a0MFHBlJYiZLqVNVzJTRGj7tGRr6SlJTfqtQeGGI0Exzxd6ygtv5ENnWENSGdX2g5S7a2pQSpnUCNQYmusjPufyLvk6Rrjuho46fHw3//yGp/EVM1ncj29flpVQ+OhiRFq/A+Al9QrWCot/iQrE+502P2r85rjd/qu8H28EPxF/3VxV7rnf2VgA==&pass_ticket=ug+aduFgMiWj+4Kohrbsx8HUDfdV/G+pKeX/Qc3N94oKwI8buTxj/0nDzltexT/T&wx_header=3)

Original莲花明 AI落地手记

上个月我接了个家长讲堂的活，给二年级小朋友讲 AI 是什么。15 张 PPT，要彩色，要可爱，要小朋友坐得住。

我做完了。然后那个月又陆续做了 29 份其他的：客户月报、内部分享、行业方案、产品发布会复盘。

**全部用 Claude。一份没找设计师，一份没自己拖文本框。**

30 份做下来，5 条路径我全跑过一遍。今天交底。

结论先行：你以为的"Claude 做 PPT"是 1 件事，实际有 5 个完全不同的工具栈，差距能差到 8 倍。

选错那条，你 25 分钟交一份能被领导退回来的 60 分稿。选对那条，你 3 分钟出一份可以直接发的成品。

![](.evernote-content/BB4E9669-7168-46D8-985C-CDA8972992ED/F8BC5B09-B387-474B-B3A6-A85271167FCC.jpg)

---

一、5 条路径，先看全景图
-------------

![](.evernote-content/BB4E9669-7168-46D8-985C-CDA8972992ED/803866AD-0A8A-47D7-9013-311402AA763F.jpg)

▲ 5 条路径横评对照

快速对照表：

| 路径 | 门槛 | 出片速度 | 推荐度 |
| --- | --- | --- | --- |
| ① **Claude.ai 网页版** | 0 | 约 1 分钟 | ⭐⭐⭐ |
| ② **Claude for PowerPoint 加载项** | Pro 起步 | 约 2 分钟 | ⭐⭐ |
| ③ **Claude Code + 官方 PPTX Skill** | 中 | 15-25 分钟 | ⭐ |
| ④ **Claude Code + python-pptx** | 中 | 约 10 分钟 | ⭐⭐⭐⭐⭐ |
| ⑤ **Claude Code + Marp** | 中高 | 约 8 分钟 | ⭐⭐⭐⭐ |

---

二、路径①：Claude.ai 网页版（最低门槛）
-------------------------

打开 claude.ai，对着对话框说一句"做一份 12 页关于 AI 编排师的 PPT"。

Claude 自己写 Python 代码、自己跑、给你一个可下载的 .pptx。整个过程你只动嘴。

优点：0 操作成本，跟聊天一样；出片速度快，1 分钟左右；自带配色和图表能力。

缺点（致命）： ・不能读你的现有模板，配色全是 Claude 自己审美 ・风格固定，企业品牌色基本没戏 ・改一处要从头跑，没法精修

适合的场景就一个：临时救急，或者给一个不存在的项目做内部头脑风暴的雏形。给老板交活、发客户，建议绕开。

---

三、路径②：Claude for PowerPoint 加载项（官方解法）
-------------------------------------

Anthropic 今年 2 月 5 日发布的研究预览，2 月 20 日开放给所有 Pro 用户。

打开 PowerPoint，安装 Claude 加载项，右侧出现一个对话框。你说"在这个客户模板上做一份季度回顾"，它就在你的模板里改。

官方真有意思的点： ・能读你的母版页、字体、颜色、logo 位置，生成的内容会自动套 ・可以做局部精修，不破坏其他幻灯片 ・能把要点直接转成 PowerPoint 原生图表

官方写在帮助文档里的限制（要先知道）： ・不保存会话历史 ・数据 30 天后自动删除 ・暂不支持审计日志和合规 API ・官方明确不推荐用于"涉及高度敏感或受管制数据的最终客户交付物"

翻译一下：内部 PPT、模板内的精修、不涉密的对外稿，可以走这条。涉及合同金额、客户数据、合规材料的，自己掂量。

---

四、路径③：官方 PPTX Skill（最大坑）
------------------------

这条路径听起来最美：Anthropic 官方提供 Skill 文件，你在 Claude Code 里说一句"做 PPT"，Skill 自动激活、生成代码、输出文件。

我也是这么想的，直到看到少数派的实测。

少数派实测的数据（节选）： ・Claude Code + 官方 Skill 第一次跑：耗时 25 分钟，结果不可用 ・Sonnet 4.5 同一套流程：耗时 20 分钟，脚本校验失败 40 多次 ・优化后第二轮：3 分钟跑完，但作者评价"质量仍处于及格边缘"

同时段的对比组：

• Manus 跑同一个题目：4 分钟出片，作者打 85 分，称"最强王者"

• NotebookLM：设计最优但只能输出 PDF，无法迭代修改

**为什么官方 Skill 反而最坑？**

问题不在 Claude 模型本身，问题在 Skill 默认的 HTML→PPTX 转化链路。这个链路要求模型先生成 HTML，再校验，再栅格化图标，再转 PPTX。环节太多，任何一步抽风都会触发回滚。

我自己复测了一次，确认了少数派的结论：除非你愿意花时间魔改 Skill 文件本身，否则官方默认配置的 PPTX Skill 现阶段还在"看上去能用"的阶段。

结论：这条路目前不推荐普通人走。等官方迭代。

---

五、路径④：Claude Code + python-pptx（我的主路径）
--------------------------------------

4 月我做的 30 份 PPT 里，**22 份走的是这条**。

### 工作流（10 步）

• 1. 我跟 Claude Code 说"做一份关于 X 的 PPT，给 Y 看，重点讲 Z"

• 2. Claude 先反问 3-4 个问题：篇幅多长？目标受众什么背景？是否要带讲稿？

• 3. 我答完，Claude 出大纲，我看一眼，确认结构

• 4. Claude 写一段 python-pptx 代码，每一页一个函数

• 5. Claude 自己跑代码，输出 v1.pptx

• 6. 我打开看，挑出"这页字太多""那页配色丑"

• 7. Claude 改代码，跑出 v2.pptx，重复 2-3 轮

• 8. 配图环节：每张图的提示词交给 Gemini 3 Pro 出图，PNG 落到本地

• 9. Claude 把图片插到对应幻灯片的对应位置

• 10. 最终 vN.pptx 出片，整体 8-12 分钟

![](.evernote-content/BB4E9669-7168-46D8-985C-CDA8972992ED/9BC0D02E-4996-4C37-AD54-721B23FFD44D.jpg)

▲ 路径④的 4 节点循环工作流

### 为什么这条路最稳？

因为它把 PPT 拆成了"代码 + 图片"两个文件型产物。代码是文本，可以版本管理、可以 diff、可以被 Claude 反复改。图片是 PNG，可以用任意 AI 出图工具替换。

家长讲堂那份 PPT 我改了 5 版（v1 到 v5），每一版都能在 git 里 diff 出"这一版我改了哪 3 处"。这是网页版和加载项做不到的。

### 一句话 Prompt 模板（直接复制）

帮我做一份 N 页 PPT，主题 X，给 Y 看，要 Z 风格。**先反问我 3 个定位问题**，再出大纲让我确认，然后用 python-pptx 写代码生成。**每页一个函数**，配色用 #XXXXXX 主色。需要插图的位置标注 [图位置：XX]，配图我用 Gemini 自己出。

这条路有一个门槛：你要接受"PPT 是一段代码跑出来的"这件事。但你不需要自己写一行代码，所有代码 Claude 帮你写。

---

六、路径⑤：Claude Code + Marp（技术稿主选）
-------------------------------

Marp 是一个把 markdown 转成 HTML/PPTX 的开源工具。

你跟 Claude Code 说"做一份关于 K8s 排错的技术分享"，它出 markdown 草稿，每一页是一个 --- 分隔的小节。Marp 把这份 markdown 编译成 HTML 现场放，或者导出 .pptx。

**为什么技术稿要走 Marp 而不是 python-pptx？**

技术分享的内容生命周期长——一份关于"我们的微服务架构"的稿子，今年讲完明年还要讲，你要的是 markdown 这种纯文本载体，可以丢进 git 跟代码一起管。

python-pptx 路径出来的是二进制 .pptx，diff 不出有意义的内容；Marp 路径出来的是 markdown，可以 commit、可以 review、可以让团队提 PR。

小坑（freeCodeCamp 那篇文章里写的）：LibreOffice 把 markdown 转 PPTX 的时候，文本框默认偏窄，长文本会折行重叠。开源仓库里已经有一段 Python 后处理脚本能修，记得用。

---

七、5 选 1：你到底该走哪条？
----------------

按场景分流：

• 需求 = 临时一次性出片，不复用 → 走路径①（网页版）

• 需求 = 在企业现有模板里精修单页 → 走路径②（加载项），注意敏感数据别发

• 需求 = 深度定制 + 反复迭代 + 配图协作 → 走路径④（python-pptx），**大多数人的最优解**

• 需求 = 技术演讲、版本管理、跟代码一起管 → 走路径⑤（Marp）

• 需求 = 想试试官方 PPTX Skill → 等 Anthropic 下一版迭代再说，目前坑大于收益

**我自己怎么用？**

80% 走路径④（python-pptx），15% 走路径⑤（Marp），5% 临时救急走路径①。

路径②我装了，但 30 份 PPT 里只用过 2 次，都是给客户改单页用。路径③装了又卸了。

---

八、实战 SOP：路径④的完整配置（保姆级）
----------------------

### 环境准备（一次性，5 分钟）

• 1. 装 Claude Code（已经有的跳过）

• 2. 终端跑：`pip install python-pptx`

• 3. 申请 Gemini API key，配置到环境变量（用于配图）

• 4. 在项目目录新建 articles/ 文件夹，存 .py 脚本和 .pptx 输出

### 每次做 PPT 的标准流程

• 1. 我对 Claude Code 说"做一份 N 页 PPT，主题 X"

• 2. Claude 反问 3 个定位问题，我答

• 3. Claude 出大纲，我看一眼说"OK"或"第 5 页改成讲 XX"

• 4. Claude 写 gen\_ppt.py 脚本，里面有 N 个函数对应 N 页

• 5. Claude 自动 python3 gen\_ppt.py，输出 v1.pptx

• 6. 我打开看，标记问题（"第 3 页字太多""第 7 页配图位空着"）

• 7. 配图：Claude 写 gen\_images.py，调 Gemini 3 Pro 出 PNG

• 8. 把图插到 pptx，跑 v2、v3，迭代到满意

• 9. 全过程脚本在 articles/ 里，下次同主题直接改参数复用

### 关键 prompt 加固（这 3 句让效率翻倍）

① "**每页一个函数，函数名带页号**"——方便后续单独改某页

② "**需要插图的位置只放占位框，写明配图描述**"——Gemini 出图前先把版式定下来

③ "**脚本最后跑完自动 open 这个 .pptx**"——省掉每次手动找文件

---

九、写在最后
------

我做这 30 份 PPT 的目的从来不是"省事"，而是"**可控**"。

设计师能给我做出更漂亮的 PPT，但他没法在 5 分钟内把第 3 页的"上半年"改成"全年度"，再过 2 分钟把配色从蓝系改成绿系。

**Claude 可以。**

不是因为它比设计师强，是因为它和我是同一个工作站、同一份文件、同一个对话上下文。我说"再来一版"，10 秒后下一版就在我屏幕上。

这就是 AI 编排师真正在干的事：不是把人换成 AI，是把"反复迭代"这件事的成本压到接近 0。

PPT 只是一个具体的例子。同样的工作流我也用在文章、月报、研究报告、客户方案上。

---

**系列预告：**这是 Claude Code 五件套系列的**应用篇**。前面发过 Subagents / Hooks / MCP / 全家福地图 / Slash Commands。下一篇拆 Skills 本身——也就是路径③那个目前最坑、但未来最有想象力的能力。

**👆 这套工作流用得上的话，转发给一起做 PPT 的同事——**

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzYzMjY1OTI0MA==&mid=2247484628&idx=1&sn=5d5fc5f71d5e6c718c682d56e554ce7e&chksm=f1e3d32742056d89733621ae9911107024a1ad1b4345dabba31c670e7a9ba4b77534c81af52e&scene=24&xtrack=1&clicktime=1777365304&enterid=1777365304&ascene=14&devicetype=iOS26.4.2&version=1800472d&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ+O7N0aTAT//P4NV0V1Pj1RLVAQIE97dBBAEAAAAAADtyL/1FQ5oAAAAOpnltbLcz9gKNyK89dVj0GoWb0OU1C0a/ZIX7XB2l+/s/EzzaUb8bZY7o5CXod5CFrpji/Y8a0MFHBlJYiZLqVNVzJTRGj7tGRr6SlJTfqtQeGGI0Exzxd6ygtv5ENnWENSGdX2g5S7a2pQSpnUCNQYmusjPufyLvk6Rrjuho46fHw3//yGp/EVM1ncj29flpVQ+OhiRFq/A+Al9QrWCot/iQrE+502P2r85rjd/qu8H28EPxF/3VxV7rnf2VgA==&pass_ticket=ug+aduFgMiWj+4Kohrbsx8HUDfdV/G+pKeX/Qc3N94oKwI8buTxj/0nDzltexT/T&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/63abd128-162c-4241-a50d-b8fa4b05c3a5/63abd128-162c-4241-a50d-b8fa4b05c3a5/)
