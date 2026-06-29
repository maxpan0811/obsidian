---
title: Codex visio paper figure skill：将生成图转化为visio可编辑图！
type: source
created: 2026-06-17
updated: 2026-06-17
source: 印象笔记管理工具
source_path: 印象笔记管理工具/Codex visio paper figure skill：将生成图转化为visio可编辑图！.html
tags: [AI技术, 教育]
updated: 2026-06-27
---

---
title: "Codex visio paper figure skill：将生成图转化为visio可编辑图！"
source: evernote
type: note
export_date: 2026-06-24
guid: b93f18a3-3942-40d0-86bd-0cb345f5b3fa
---

# Codex visio paper figure skill：将生成图转化为visio可编辑图！

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=Mzg3MjYzMDk0Nw==&mid=224750...](https://mp.weixin.qq.com/s?__biz=Mzg3MjYzMDk0Nw==&mid=2247503981&idx=1&sn=8a312eb0e3cea3611572cdbc27f3c9ee&chksm=cf402626ad66c1d0f3e444b8e90868f7386cd4ae92e8b3e805728bfe403f6d68586b484357a2&scene=90&xtrack=1&req_id=1781530026634194&sessionid=1781527535&subscene=93&clicktime=1781530325&enterid=1781530325&flutter_pos=33&biz_enter_id=4&ranksessionid=1781530026&jumppath=WAWebViewController_1781530202500,WAWebViewController_1781530202995,20020_1781530213421,1104_1781530214010&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004a2f&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQZs6R5CoBGMxgP0bYcjxB4hLTAQIE97dBBAEAAAAAAIKIDqOfbCYAAAAOpnltbLcz9gKNyK89dVj0vyv09FGMnQHF9OkQZ2cMpulH4L0tPuvHxXXMZ7Rxr8XQn4aq/uDw2lGPi5osUrX/qQgCTg1JH2EaXwcT65qK4RjZk/InDWh8PWrmImtVPa9Xxqq7wwYOEIurCkNjp6MsOmlrxQOSkRPX/O69Zy239ew6gTh8pmBzSnDvav7MQnAvCCfHUK6zsg7YNiDF+3S1mLThtxtk41XHViasQTpmqBwvqk6na5FXmRWqf7M=&pass_ticket=yD7bZ6uKobeS1oUZX/iOcw7WOOeOmoJIoO1LWnK2mYAME4erifbWHb01KpP0y/pH&wx_header=3)

AI学术圆桌派

做科研的人都知道一个残酷的事实：

很多时候，做实验只占工作量的一半。

另一半，花在了画图上。

实验跑完了，结果出来了，接下来要开始：

- 调 Matplotlib 参数
- 改字体大小
- 调整图例位置
- 统一配色
- 修改线条粗细
- 导出 PDF
- 再被导师要求重画一遍

尤其是准备论文投稿的时候，经常会出现一种情况：

数据分析用了半小时，画图用了两天。

最近在逛 GitHub 的时候，我发现了一个挺有意思的项目：

**codex-visio-paper-figure-skill**

这是一个专门给 Codex 使用的 Skill，目标非常明确：

**把实验结果自动转换成可以直接放进论文里的图表和 LaTeX 表格。**

它并不是一个新的绘图库，也不是可视化平台，而更像是一个专门为科研场景定制的 AI 绘图助手。

**一**

**科研绘图最大的痛点是什么？**

很多人以为科研绘图的问题是不会画。

其实恰恰相反。

会画的人更痛苦。

因为真正耗时间的不是生成图，而是反复调整。

举个例子。

你完成了一组模型对比实验，需要展示：

- Accuracy
- F1 Score
- Recall
- Precision

如果手工处理，通常流程是：

读取 CSV → 写 Matplotlib → 调参数 → 调颜色 → 调图例 → 导出 → 插入论文。

一张图还好。

如果论文里有：

- 训练曲线
- 消融实验
- 参数敏感性分析
- 方法对比
- 热力图
- 散点图

十几张图下来，基本能让人怀疑人生。

更麻烦的是：

很多图虽然画出来了，但并不符合论文规范。

例如：

- 字体不统一
- 分辨率不够
- 颜色不适合打印
- 图例遮挡数据
- 不符合期刊格式

最后还是得返工。

**二**

**这个 Skill 到底能干什么？**

根据项目介绍，它的核心能力主要集中在两件事：

***1. 自动生成论文级图表***

支持的图表类型非常丰富：

- Line Plot（折线图）
- Bar Chart（柱状图）
- Scatter Plot（散点图）
- Heatmap（热力图）
- Box Plot（箱线图）
- Violin Plot（小提琴图）

只要你的实验结果已经保存在：

- CSV
- JSON
- Log 文件

里面的数据都可以直接读取并生成图表。

对于机器学习、深度学习研究来说，基本覆盖了绝大部分实验展示需求。

***2. 自动生成论文表格***

很多论文中的表格其实比图更折磨人。

尤其是：

- 消融实验
- Baseline 对比
- Benchmark 结果

经常需要手工调整：

- 对齐方式
- 粗体标记
- Top-1 高亮
- LaTeX 格式

这个 Skill 可以直接生成对应的 LaTeX 表格代码。

对于经常写论文的人来说，这个功能其实比自动画图更有价值。

因为表格排版真的是一个纯体力活。

**三**

**它和普通 AI 绘图工具有什么区别？**

现在很多 AI 都能画图。

但科研图和宣传图完全不是一个东西。

科研图最重要的不是好看，而是：

**规范、统一、可复现。**

项目作者在设计时专门强调了几个原则：

- 所有图统一风格
- 使用论文级排版参数
- 输出矢量格式 PDF
- 保证可复现
- 图和生成脚本一起保存

也就是说：

不仅给你结果。

还给你生成结果的方法。

这一点其实非常符合科研工作的要求。

因为论文里的每一个结果，理论上都应该能够重新生成。

**四**

**最实用的功能：批量生成整篇论文的图**

很多人第一次看到这个 Skill 时会觉得：

“不就是帮我画个图吗？”

实际上并不是。

它更大的价值在于：

**统一管理整篇论文的所有图表。**

项目支持 Multi-panel Figure。

简单理解就是：

AI 可以帮你把多个实验结果自动组织成论文里的 Figure 1、Figure 2、Figure 3。

例如：

Figure 3：

- (a) Accuracy
- (b) F1 Score
- (c) Recall
- (d) Precision

统一布局。

统一字体。

统一风格。

这类工作如果手工处理，往往要花掉几个小时。

**五**

**特别适合哪些人？**

我觉得主要有三类。

***第一类：机器学习研究生***

这是最直接的受益群体。因为日常工作本身就是：训练模型 → 导出结果 → 画图 → 写论文。整个流程几乎完美匹配。

***第二类：经常写 SCI 的老师***

很多老师并不缺实验能力。缺的是时间。如果能把重复性的绘图工作交给 AI，效率提升非常明显。

***第三类：用 Codex 做科研自动化的人***

最近越来越多人开始搭建自己的科研 Agent 工作流。例如：文献检索、自动阅读、实验规划、代码生成、论文写作。而科研图表一直是自动化链条里比较难补齐的一环。这个 Skill 本质上是在填补这块空白。

**六**

**我觉得它最大的意义是什么？**

不是替代科研人员。

而是把科研人员从重复劳动里解放出来。

说实话：

没人读博是为了每天调 Matplotlib 参数。

也没人做研究是为了花一下午调整图例位置。

真正值得投入时间的部分应该是：

- 提出问题
- 设计实验
- 分析结果
- 形成观点

而不是：

plt.legend(loc='upper right')

改了二十遍。

AI 最适合做的，本来就应该是这种标准化、重复性强的工作。

**七**

**写在最后**

过去几年，AI 在科研领域最先改变的是：

- 文献阅读
- 代码编写
- 论文润色

而现在，我们开始看到越来越多细分 Skill 的出现。

它们不再试图解决所有问题。

而是专门解决某一个具体痛点。

对于科研工作来说，这种工具往往比“大而全”的平台更有价值。

如果你平时经常需要：

- 画实验结果图
- 做模型对比图
- 整理消融实验
- 生成论文表格

那么这个 **codex-visio-paper-figure-skill** 值得收藏试试。

也许下一次投稿前熬夜改图的人，就不是你了。

—— ✦ ——

Codex Skill · 让科研绘图回归表达本身
