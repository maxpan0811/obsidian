# Claude 把 HTML 玩明白了：从聊天框到命令行，3 条路一句话生成单文件网页（附选型表）

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzYzMjY1OTI0MA==&mid=224748...](https://mp.weixin.qq.com/s?__biz=MzYzMjY1OTI0MA==&mid=2247484889&idx=1&sn=2c9f95a30d16d095aebb2c2cebdd11b0&chksm=f1172e948f587eef7399ea06813e74acb4fa6c24da803fadf2fc883190c2d1d13aca1f4e5673&scene=126&sessionid=0&clicktime=1778947176&enterid=1778947176&ascene=3&devicetype=iOS26.5&version=18004929&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQg6JR/JiPuOXflTrqKIPD0xLTAQIE97dBBAEAAAAAAGktDM8F/kcAAAAOpnltbLcz9gKNyK89dVj0nDwaINjB9aMr8jvwGrI6B1/bkdFAZmET4KcCBRlNg+JX5WB+rj71WVqNH7YoOfvrRX94Y4dFJSdYvOxCNyTGRm3gZmO4vek+cJzxmnm1d/8yh9Fwy+Az7wTl1wqnWM1lM2rDpc6EgN2iV365i2Wr2AM7MIONP0tXsXQwFwYXA+xaOywQehFpMoQ0/FB2IPKLn3XBeH0jH/LuuD1zvd8rC9gZsV/LfJMoS9URTwY=&pass_ticket=9xjmrqfRB5Ad3PD0Jpgq1YVpdHYx+aGwZ0V8pSeHuir0webxj/rylRiMzH5OBTC0&wx_header=3)

Original莲花明 AI落地手记

你上一次手写 HTML 是什么时候？

我猜大部分人的答案是：从来没写过，或者很久很久以前。

HTML 1993 年就有了，今年 33 岁，比不少职场新人岁数都大。这么多年它一直是个「底层的东西」——网页背后那一层，普通人不用管，也管不着。

但最近两个月，**AI 圈最热的输出格式，恰恰就是它。**

而把这个老古董重新捧火的，是 Claude。

![](.evernote-content/C93572AA-C34D-4D4E-8277-4B53351EC405/FB26353F-BAA2-4DE7-B478-11B3B7B4AAF8.jpg)

这篇文章把「Claude + HTML」这个组合讲清楚：它为什么突然火，以及——更实用的——你想让 AI 替你生成一个能直接用的网页，到底有几条路、各走给谁。

---

一、为什么 AI 突然开始吐 HTML
-------------------

这事得从一个 Anthropic 工程师说起。

Claude Code 团队的 Thariq Shihipar 公开抛出一个主张：别再让 AI 用 Markdown 输出了，改用 HTML。

听着像个不起眼的技术细节，背后其实是一次挺大的转向。

### Markdown 是「小窗口时代」的产物

Markdown 当年为什么成了 AI 的默认输出格式？

因为 GPT-4 那个年代，模型的上下文窗口很小，每个 token 都金贵。Markdown 符号少、结构轻，省 token。它是被「省」出来的选择。

现在情况变了。Claude 的上下文窗口已经到了 100 万 token。AI 写的东西也越来越长——一份计划、一份报告动辄几百行。

问题来了：**超过 100 行的 Markdown，人基本不会看完。**一大坨纯文本堆在那，没有重点、没有层次，滑两下就划走了。

### HTML 是「给人看」的格式

HTML 不一样。它能做标签页、能折叠、能放目录、能塞图表、手机和电脑自动适配。

同样几百行内容，HTML 那一版你会愿意读完——因为它把结构做出来了。

Anthropic 自己已经把 HTML 设成了内部默认：写计划、做代码评审、出设计规范、生成报告，都用 HTML。5 月 8 号，开发者 Simon Willison 写了一篇《HTML 不合理的有效性》，把这个话题彻底推上了风口。

也有反对的声音。有人专门写了篇《HTML 不合理的「无」效性》怼回去，说这是为了视觉好看，牺牲了源码的可读性、安全性和可审查性。这个争论还没有定论。

但有一件事是确定的：不管你站哪一边，「让 AI 直接吐出能用的 HTML」这件事，现在已经有三条成熟的路了。

---

二、三条路：让 AI 替你写 HTML
-------------------

![](.evernote-content/C93572AA-C34D-4D4E-8277-4B53351EC405/C9833DA8-17C8-4EA7-BE2C-76D52D774E83.jpg)

### 路径一：Artifacts —— 聊天框里顺手出

这是门槛最低的一条，零成本，你现在就能用。

在 Claude 的网页或 App 里聊天，让它做个东西，它不会只回你一段文字——会在聊天窗口旁边直接开一块画布，把 HTML 渲染出来，能点、能玩。这块画布就叫 Artifact。

举个具体的：你说「帮我做一个房贷月供计算器，能输入总价、首付比例、贷款年限、利率，算出每月还多少」。Claude 会直接给你一个能用的网页计算器，输入框、按钮、结果区全有。不满意就接着说「把利率改成可以拖动的滑块」，它当场改给你。

**适合什么：**临时要个小工具、小游戏、一次性的数据看板。想完即用，用完即走。

### 路径二：Claude Design —— 专门的设计工作室

这是今年 4 月 17 号 Anthropic Labs 刚发布的新产品，目前是研究预览版，Pro 及以上会员可以用。

它跟 Artifacts 那种「聊天顺手出个东西」不一样。Claude Design 是个正经的设计台子，背后跑的是 Claude 最新的视觉模型。

你能用它做产品原型、线框图、提案 PPT、落地页、营销物料。做出来的东西不是死的——能可视化拖拽，能用滑块微调间距和配色，还能在上面直接写批注让它改。

出 HTML 这块：做完可以**一键导出成单文件 HTML**，也能导成 PDF、PPTX，或者直接推到 Canva 接着改，甚至打包丢给 Claude Code 继续开发。

效果有多省？Anthropic 公布的案例里，有个团队原来做一个复杂原型要来回 20 多轮对话，用上 Claude Design 之后压到了 2 轮。

**适合什么：**你要做的是「给人看的成品」——提案、原型、需要排版的页面。

一个提醒：Claude Design 跑的是重度视觉模型，token 烧得快。Pro 会员有周用量限制，悠着点用。

### 路径三：Claude Code + HTML 技能 —— 命令行里批量出

这条最重，但也最强，适合已经在用 Claude Code 的人。

Claude Code 本身是个命令行工具。它现在有一类专门出 HTML 的「技能」（Skill），装上之后，一句话就能出页面。

比如有个挺火的技能，专做横滑杂志风的网页 PPT：你给它一段内容，它直接生成一个单文件 HTML，十几种排版模板、五套配色、带 WebGL 动态背景，翻页像翻一本杂志。还有的技能能出高保真原型、带动画的幻灯片，甚至导出成 MP4 视频。

这条路的好处是能批量、能进版本管理、能跟你现有的开发流程接上。坏处也很直接——你得先会用 Claude Code。

**适合什么：**要一次出很多页面，或者这些页面是某个项目的一部分、需要长期维护。

---

三、为什么三条路出来的，都是「单文件」
-------------------

你可能注意到了：三条路径,落地的东西核心都是同一个——一个单文件的 HTML。

「单文件」这三个字，是整件事的关键。

![](.evernote-content/C93572AA-C34D-4D4E-8277-4B53351EC405/6B50EF97-B703-4036-A661-AFEF79556ECB.jpg)

单文件 HTML 意味着：所有的样式、所有的脚本、所有的内容，全打包在一个文件里，不依赖任何外部的东西。

它带来的好处特别朴素：你双击就能打开；发微信给同事，他点开也能直接看；丢到服务器上，它就是一个网页。

它不需要「安装」，不需要「配环境」，**浏览器就是它的运行时。**

这就是 HTML 在 AI 时代被重新捡起来的根本原因。它是少数几个 AI 写得出、人又愿意看的格式，而且机器拿到直接就能跑。中间不卡任何一环。

---

四、所以你该走哪条路
----------

三条路径并排放一起，长这样：

| 维度 | ① Artifacts | ② Claude Design | ③ Claude Code |
| --- | --- | --- | --- |
| 在哪用 | Claude 聊天框 | Design 工作室 | 终端命令行 |
| 门槛 | 零，会打字就行 | 低，会描述需求 | 中，要装 Claude Code |
| 适合谁 | 所有人 | 做设计、原型的人 | 开发者、重度用户 |
| 怎么改 | 接着对话让它改 | 拖拽 + 滑块 + 批注 | 改 prompt 或改代码 |
| 最适合 | 临时小工具、小页面 | 提案、原型、落地页 | 批量出页面、进项目 |

表：让 AI 替你写 HTML 的三条路径对比

如果不想记这么多，给你一个一句话版本的决策：

· 你只是偶尔要个小工具、小页面，不想装任何东西 → **走 Artifacts**，打开 Claude 聊天框就行。

· 你要做提案、原型、给人看的成品，希望能改得精细 → **走 Claude Design**。

· 你已经在用 Claude Code，要批量出页面、要进项目 → **装 HTML 技能**。

另外给你一段可以直接复制的 prompt。不管你在哪条路径上，想让 AI 吐出一个「拿来就能用」的单文件 HTML，这么说最稳：

把下面这件事做成一个单文件 HTML 页面：

【需求】（换成你自己的）：

做一个 \_\_\_ 工具 / 一份 \_\_\_ 报告页 / 一个 \_\_\_ 数据看板

【硬要求】：

- CSS 全部写进 style 标签，JS 全部写进 script 标签

- 不依赖任何外部文件、不引外部链接

- 响应式，手机和电脑都能正常看

- 配色干净，留白充足

做完直接给我完整 HTML 代码，我要双击就能打开。

「不依赖外部文件」这一句最重要——加上它，你才能拿到一个真正的单文件，而不是一堆散件。

---

五、写在最后
------

HTML 今年 33 岁了。这两个月没人给它加什么新功能，它还是那个老样子。

变的是 AI。

当 AI 要把工作成果交到人手里的时候，它需要一种格式：自己写起来顺手，人读起来舒服。最好，还能直接跑起来。

找来找去，最合适的居然是这个 30 多年前的老东西。

有人说这是 HTML 的文艺复兴。我觉得没那么浪漫——只是 AI 和人之间，需要一种通用语言。这一轮，HTML 正好被选中了。

你不用会写 HTML。你只需要知道一件事：**现在可以让 AI 替你写，而且有三条路。**

关注「AI 落地手记」，不见不散。

一个人 + AI 管 20 个项目的真实记录

原创扒一个工具，挺费功夫的。

觉得有用，点一下下面那个红色的「喜欢作者」就够了；不方便的话，转发给一个用得上的人 —— 对我一样是支持。

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzYzMjY1OTI0MA==&mid=2247484889&idx=1&sn=2c9f95a30d16d095aebb2c2cebdd11b0&chksm=f1172e948f587eef7399ea06813e74acb4fa6c24da803fadf2fc883190c2d1d13aca1f4e5673&scene=126&sessionid=0&clicktime=1778947176&enterid=1778947176&ascene=3&devicetype=iOS26.5&version=18004929&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQg6JR/JiPuOXflTrqKIPD0xLTAQIE97dBBAEAAAAAAGktDM8F/kcAAAAOpnltbLcz9gKNyK89dVj0nDwaINjB9aMr8jvwGrI6B1/bkdFAZmET4KcCBRlNg+JX5WB+rj71WVqNH7YoOfvrRX94Y4dFJSdYvOxCNyTGRm3gZmO4vek+cJzxmnm1d/8yh9Fwy+Az7wTl1wqnWM1lM2rDpc6EgN2iV365i2Wr2AM7MIONP0tXsXQwFwYXA+xaOywQehFpMoQ0/FB2IPKLn3XBeH0jH/LuuD1zvd8rC9gZsV/LfJMoS9URTwY=&pass_ticket=9xjmrqfRB5Ad3PD0Jpgq1YVpdHYx+aGwZ0V8pSeHuir0webxj/rylRiMzH5OBTC0&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/c81b3f60-72a6-4f0e-b40f-905854b4c3ca/c81b3f60-72a6-4f0e-b40f-905854b4c3ca/)