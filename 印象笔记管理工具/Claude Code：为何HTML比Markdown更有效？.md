# Claude Code：为何HTML比Markdown更有效？

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=Mzk0NjY0MTc0NA==&mid=224750...](https://mp.weixin.qq.com/s?__biz=Mzk0NjY0MTc0NA==&mid=2247500047&idx=1&sn=d70652d99ceb43512ceebca220953438&chksm=c2b1c7e1f76558da168db17de2a812cd8f34fc76463b9902737ed74e1c75ad132920894e8fee&scene=90&xtrack=1&req_id=1778309372841301&sessionid=1778311286&subscene=93&clicktime=1778311998&enterid=1778311998&flutter_pos=4&biz_enter_id=4&ranksessionid=1778311286&jumppath=1122_1778311899512,20020_1778311905879,1122_1778311985149,1104_1778311987863&jumppathdepth=4&ascene=56&devicetype=iOS26.4.2&version=18004922&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQf9sbik0No74F0XkEqzyk0RLVAQIE97dBBAEAAAAAABqtE7fHCSQAAAAOpnltbLcz9gKNyK89dVj0k7W7x8ZGOL8mhOpZdlV/icj41nxegcSZVA+84ixmuLp4MXSnzxeGG59RjlnzMOuqVG2/L4uD2aLZu+tmaUfgkxM0Mrkm2u8lcVOsv22HhWDe4VURXE0A8Jho5+7od2joAHftvsziqN4LP2sRxtE92TbO/MuoAdFHato1zrQIb1q8Zb6NUY2tGv9JjdfUlqcWDi7Y/js/AJ0Wp9AYpHDNpfVAHyaetC3WguLlHmESRw==&pass_ticket=3QLALp0+3PWDuy4a3nt4GUl+w1wlX4kN6fG1Dke23RKiJwCMAUmGlNHxW1f1IswW&wx_header=3)

Original一叶扁舟代码麻辣烫

![](.evernote-content/7A0A9902-5219-4AE7-BFA2-E225F020E82B/91012549-D1D6-4CA7-8364-B13AF9919BC7.jpg)

Markdown 已经成为代理与我们沟通时使用的主导文件格式。它简单、便携，具备一些富文本能力，并且易于编辑。Claude 甚至在 Markdown 文件中使用 ASCII 制作图表方面变得出奇地好。

但随着代理变得越来越强大，我感觉到 Markdown 变成了一种限制性格式。我发现阅读超过一百行的 Markdown 文件很困难。我想要更丰富的可视化效果、颜色和图表，并且我希望能够轻松地分享它们。

我也越来越多地不是自己编辑这些文件，而是将它们用作规范、参考文件、头脑风暴输出等。当我确实进行编辑时，我通常是提示 Claude 来编辑它们，这消除了 Markdown 的最大好处之一。

我开始更喜欢将 HTML 作为输出格式而不是 Markdown，并且越来越多地看到 Claude Code 团队中的其他人也在使用它，原因如下。

为什么选择 HTML？

**「信息密度」**
----------

![](.evernote-content/7A0A9902-5219-4AE7-BFA2-E225F020E82B/BDCF65D4-D6EB-442C-A6B3-0260C0FF5AF7.jpg)

HTML 能够传达比 Markdown 更丰富的信息。它当然可以像标题和格式化这样的简单文档结构，但它还可以表示其他类型的信息，例如：

* 使用表格表示表格数据
* 使用 CSS 表示设计数据
* 使用 SVG 表示插图
* 使用 script 标签表示代码片段
* 使用 HTML 元素与 JavaScript + CSS 表示交互
* 使用 SVG 和 HTML 表示工作流
* 使用绝对位置和画布表示空间数据
* 使用图像标签表示图像

我甚至敢说，几乎没有 Claude 可以阅读的信息集，你不能相当高效地用 HTML 表示。这使得它成为模型与你沟通深入信息的高效方式，以及你审查信息的方式。

我发现，在不能这样做的情况下，模型可能会在 Markdown 中做一些效率更低的事情，比如 ASCII 图表，或者我最喜欢的，用 Unicode 字符估计颜色，就像这张 Claude Code 在 Markdown 中显示颜色的截图。

![](.evernote-content/7A0A9902-5219-4AE7-BFA2-E225F020E82B/89A9F41C-C228-4AEB-BA8F-DD3EF9CE3C78.jpg)

Claude Code 尝试在 Markdown 中显示颜色

Claude Code 尝试在 Markdown 中显示颜色

**「视觉清晰度与易读性」**
---------------

![](.evernote-content/7A0A9902-5219-4AE7-BFA2-E225F020E82B/4528F0B3-70A7-4760-AA96-DD5EDD14EF00.jpg)

随着 Claude 能够做更复杂的工作，它也在编写越来越大的规范和计划。实际上，我发现我倾向于不阅读超过 100 行的 Markdown 文件，我当然也不能让我组织中的其他人阅读它。

但 HTML 文档更容易阅读，Claude 可以视觉上组织结构，使其理想地通过标签、插图、链接等进行导航。它甚至可以是移动响应式的，所以你可以根据你的形态因素以不同的方式阅读它。

**「易于分享」**
----------

Markdown 文件很难分享，因为大多数浏览器不会很好地原生渲染它们。你通常需要将它们作为附件添加到电子邮件或消息中。

有了 HTML，只要你上传文件（例如到 S3），你就可以轻松分享链接。你的同事可以在他们希望的任何地方打开它，并轻松参考它。

如果它是 HTML，那么有人实际阅读你的规范、报告或 PR 编写的可能性要高得多。

**「双向互动」**
----------

![](.evernote-content/7A0A9902-5219-4AE7-BFA2-E225F020E82B/3DA22C9C-5D5C-47E5-8F01-AF0B0061D8BC.jpg)

HTML 可以让你与文档互动，例如，你可能想要让它添加滑块或旋钮来调整设计，或者允许你调整算法中的不同选项以查看会发生什么。你还可以让它让你将这些更改复制到提示中，然后粘贴回 Claude Code。阅读更多关于我的游乐场帖子以查看这种双向互动的例子：https://x.com/trq212/status/2017024445244924382

**「数据摄取」**

为什么要使用 Claude Code 制作 HTML 文件，而不是 ClaudeAI 或 Claude Design 等？一个最大的原因是 Claude Code 能够摄取的所有上下文。例如，当我写这篇文章时，我要求 Claude Code 阅读我的代码文件夹，找到所有我生成的 HTML 文件，分组并分类，然后制作一个包含每种类型的图表的 HTML 文件。你在这篇文章中看到的图表是那的直接结果。

除了文件系统，Claude Code 还可以使用你的 MCP（如 Slack、Linear 等）、你的网络浏览器（带有 Chrome 中的 Claude）、你的 git 历史等找到额外的上下文。

**「它很有趣」**
----------

使用 Claude 制作 HTML 文档只是更有趣，让我感觉更参与和投入创作，这本身就是足够的。

如何开始
----

我有点担心人们会读这篇文章，然后将其变成一个 /html 技能或类似的东西。虽然这可能有一些价值，但我想强调你不需要做太多就能让 Claude 做到这一点。你可以只是要求它“制作一个 HTML 文件”或“制作一个 HTML 工件”。

诀窍在于知道你希望工件做什么以及你可能如何使用它。你可能会随着时间的推移制作一个技能，但现在我建议你从零开始提示，以了解如何在不同情况下使用它。

规范、计划与探索
--------

HTML 是 Claude 深入问题的丰富画布。当我开始处理一个问题时，与其是一个简单的 Markdown 计划，我期望制作一系列 HTML 文件。例如，我可能首先要求 Claude Code 进行头脑风暴，并创建一些不同选项的探索。然后我会要求它更深入地扩展其中一个，可能制作原型或代码片段。最后，当我感到满意时，我会要求它编写一个实施计划。当我对计划感到满意时，我会创建一个新的会话，并传入所有这些文件，以便它进行实施。

在验证时，我还会要求验证代理读取这些文件，它将对所需内容有更广泛的上下文。

![](.evernote-content/7A0A9902-5219-4AE7-BFA2-E225F020E82B/87E6ADF1-58BA-4F1A-AA87-7DF113620576.jpg)

**「示例提示：」**

* 我不确定要采取哪个方向的入门屏幕。生成 6 种截然不同的方法——变化布局、语气和密度——并将它们作为一个单一的 HTML 文件以网格形式排列，以便我可以并排比较它们。每个都用它所做的权衡标记。
* 在 HTML 文件中创建一个全面的实施计划，确保制作一些原型，显示数据流，并添加我可能想要审查的重要代码片段。确保它易于阅读和消化。

**「用例：」**

* 探索代码中的其他实现方式
* 探索多种视觉设计

代码审查与理解
-------

在 Markdown 文件中阅读代码可能很困难。但有了 HTML，我们可以渲染差异、注释、流程图、模块等。用这个来理解代理编写的代码，进行代码审查或向审查你代码的人解释 PR。我发现这通常比默认的 Github 差异视图工作得更好，我现在为每个 PR 附加一个 HTML 代码解释器。

![](.evernote-content/7A0A9902-5219-4AE7-BFA2-E225F020E82B/87F7C74D-DFD2-43DF-A11A-A3DC7CA9575E.jpg)

**「示例提示：」**

帮助我通过创建一个 HTML 工件来审查这个 PR。我对流媒体/背压逻辑不太熟悉，所以专注于那个。用内联边距注释渲染实际的差异，按严重程度用颜色编码发现，并做其他可能需要的事情来很好地传达概念。

**「用例：」**

* 创建一个 PR
* 审查一个 PR
* 理解代码中的主题

设计与原型
-----

Claude Design 基于 HTML，因为 HTML 在设计上非常富有表现力，即使你的最终表面不是 HTML。Claude 可以用 HTML 草拟一个设计，然后用你选择的语言编写，无论是 React、Swift 等。

你还可以原型化交互，如动画、动作等。考虑要求 Claude 制作滑块、旋钮等，以调整你正在寻找的确切内容。

![](.evernote-content/7A0A9902-5219-4AE7-BFA2-E225F020E82B/8E2546F2-E780-43C6-A3B1-ACE2EE8DE27A.jpg)

**「示例提示：」**

我想原型化一个新的结账按钮，当点击时它执行播放动画，然后很快变成紫色。创建一个 HTML 文件，有几个滑块和选项供我尝试这个动画的不同选项，给我一个复制按钮以复制工作良好的参数。

**「使用这个：」**

* 创建设计系统工件
* 调整组件
* 可视化组件库
* 原型化愉快的动画

报告、研究与学习
--------

Claude Code 在跨多个数据源综合信息并将其转换为可读报告方面非常出色。你可以提示 Claude 搜索你的 Slack、你的代码库、git 历史、互联网等，并用它生成非常容易阅读的报告，供你自己、领导或你的团队等使用。

你可以将这些以长 HTML 文档的形式组装，一个互动解释器，甚至是一个幻灯片/甲板。要求 Claude 使用 SVG 制作图表以帮助可视化它。例如，对于我关于提示缓存的帖子，我要求 Claude 为我准备一个深入的研究文件，以 HTML 形式阅读我们对提示缓存的所有更改，阅读 git 历史后。

![](.evernote-content/7A0A9902-5219-4AE7-BFA2-E225F020E82B/D094CA96-5D31-47C9-A79B-AFF899FB7982.jpg)

**「示例提示：」**我不明白我们的速率限制器实际上是如何工作的。阅读相关代码并生成一个单一的 HTML 解释页面：一个令牌桶流程的图表，3-4 个关键代码片段注释，以及底部的“陷阱”部分。优化它，以便某人一次阅读。

**「使用这个：」**

* 总结一个功能如何工作
* 向我解释一个概念
* 向你的老板提交每周状态报告
* 向你的领导提交事件报告
* SVG 图表、流程图、技术图表等

自定义编辑界面

有时很难仅在文本框中描述你想要的东西。在这种情况下，我会要求 Claude 为我构建一个一次性编辑器，用于我正在工作的确切事情。不是一个产品，或一个可重用的工具，而是一个单一的 HTML 文件，专为这一块数据量身定制。

诀窍总是以导出结束：一个“复制为 JSON”或“复制为提示”按钮，将我在 UI 中所做的任何操作转换回我可以粘贴到 Claude Code 中的东西。

![](.evernote-content/7A0A9902-5219-4AE7-BFA2-E225F020E82B/1F067F2C-F817-4C54-B026-C86ED241BB54.jpg)

**「示例提示：」**

* 我需要重新优先处理这些 30 个 Linear 票证。为我制作一个 HTML 文件，每个票证作为一个可拖动的卡片跨 Now / Next / Later / Cut 列。根据你的最佳猜测预排序。添加一个“复制为 Markdown”按钮，导出最终排序，并为每个桶提供一个简短的理由。
* 这是我们的功能标志配置。为其构建一个基于表单的编辑器，按区域对标志进行分组，显示它们之间的依赖关系，如果我启用了一个其先决条件关闭的标志，则警告我。添加一个“复制差异”按钮，只给我改变了的键。
* 我正在调整这个系统提示。制作一个并排编辑器：左侧是可编辑的提示，突出显示变量插槽，右侧是三个样本输入，它们重新渲染填充的模板。添加一个字符/令牌计数器和一个复制按钮。

**「使用这个：」**

* 重新排序、分类或分桶任何东西（票证、测试用例、反馈）
* 编辑结构化配置（功能标志、环境变量、有约束的 JSON/YAML）
* 使用实时预览调整提示、模板或副本
* 策划数据集，批准/拒绝行，标记示例，导出选择
* 注释文档、记录或差异并导出注释
* 选择难以用文本表达的值：颜色、缓动曲线、裁剪区域、Cron 时间表、正则表达式等。

常见问题解答
------

我告诉了很多人我已经转向 HTML，我看到了一些重复的问题。

**「它不是效率较低吗？」**虽然 Markdown 通常使用更少的令牌，但我发现 HTML 的表达性增加和阅读它的可能性大大增加意味着我得到了更好的输出。在 Opus 4.7 中的 1MM 上下文窗口中，增加的令牌使用在上下文窗口中并不明显。

**「你现在什么时候使用 Markdown？」**我老实说已经完全停止使用 Markdown 用于几乎所有事情，但我可能在 HTML 最大主义者方面走得很远。

**「我如何查看 HTML 文件？」**我倾向于在本地浏览器中打开它（你可以要求 Claude 打开它），或者如果你想要一个可共享的链接，就上传到 S3。

**「这不会比 Markdown 花更多时间生成吗？」**这确实需要更长的时间！HTML 可能需要比 Markdown 长 2-4 倍的时间，但我发现结果值得。

**「关于版本控制呢？」**这确实是 HTML 的最大缺点之一，HTML 差异很嘈杂，很难审查，与 Markdown 相比。

**「如何让 Claude 符合我的品味/不制作丑陋的东西？」**前端设计插件有助于 Claude 制作好的 HTML 文件。但要符合你自己公司的样式，你可以通过指向你的代码库创建一个单一的设计系统 HTML 文件。然后你可以使用该设计系统文件作为其他 html 文件的参考。

结语
--

所有上述都是说我使用 HTML 的真正原因是我感觉与 Claude 的联系更紧密。我开始担心因为我不再深入阅读计划，我将不得不让 Claude 做出它的选择。

但我很高兴地说，使用 HTML 时，我感觉比以往任何时候都更在循环中。

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=Mzk0NjY0MTc0NA==&mid=2247500047&idx=1&sn=d70652d99ceb43512ceebca220953438&chksm=c2b1c7e1f76558da168db17de2a812cd8f34fc76463b9902737ed74e1c75ad132920894e8fee&scene=90&xtrack=1&req_id=1778309372841301&sessionid=1778311286&subscene=93&clicktime=1778311998&enterid=1778311998&flutter_pos=4&biz_enter_id=4&ranksessionid=1778311286&jumppath=1122_1778311899512,20020_1778311905879,1122_1778311985149,1104_1778311987863&jumppathdepth=4&ascene=56&devicetype=iOS26.4.2&version=18004922&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQf9sbik0No74F0XkEqzyk0RLVAQIE97dBBAEAAAAAABqtE7fHCSQAAAAOpnltbLcz9gKNyK89dVj0k7W7x8ZGOL8mhOpZdlV/icj41nxegcSZVA+84ixmuLp4MXSnzxeGG59RjlnzMOuqVG2/L4uD2aLZu+tmaUfgkxM0Mrkm2u8lcVOsv22HhWDe4VURXE0A8Jho5+7od2joAHftvsziqN4LP2sRxtE92TbO/MuoAdFHato1zrQIb1q8Zb6NUY2tGv9JjdfUlqcWDi7Y/js/AJ0Wp9AYpHDNpfVAHyaetC3WguLlHmESRw==&pass_ticket=3QLALp0+3PWDuy4a3nt4GUl+w1wlX4kN6fG1Dke23RKiJwCMAUmGlNHxW1f1IswW&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/4421164e-4664-4630-8f28-da551f036c1f/4421164e-4664-4630-8f28-da551f036c1f/)