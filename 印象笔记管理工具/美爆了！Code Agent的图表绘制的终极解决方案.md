# 美爆了！Code Agent的图表绘制的终极解决方案

---

来源：[打开原文](https://mp.weixin.qq.com/s/gb_Bprf0kz29TsBb1J7VAw)

一图胜千言，使用图表可以非常清晰地展示代码逻辑架构以及各种流转的状态。但在有AI之前，画架构图这类东西，真的是一件非常麻烦的事情。

打开 Visio 或者 draw.io，拖半小时方块和箭头，改一个字段名又要重新拖。这种工具和 AI agent 的工作流完全不兼容，一个靠鼠标，一个靠文本。

Mermaid 是这个矛盾的解法。

它是一套纯文本语法，用来描述图表结构，然后由工具渲染成图。不用再拿着鼠标去描图了，直接用AI来写文本的描述就可以。

以一张前后端分离时序图为例，文本内容如下：

sequenceDiagram

前端->>后端: POST /login

后端->>数据库: 查询用户

数据库-->>后端: 返回结果

后端-->>前端: 200 OK + token

最后渲染的结果：

![](.evernote-content/E6867C5B-26A5-47C8-B17B-AEF7A21C0FA0/979394C2-BAED-42D5-B9B4-81877E62C514.png)

但是原生的Mermaid图表有几个问题。首先是千篇一律的丑，你看到的很多原生Mermaid图表大概率都长这样的红配绿：

![](.evernote-content/E6867C5B-26A5-47C8-B17B-AEF7A21C0FA0/25379A6E-67EA-4BF9-B9A0-2B6B0499CFC9.png)

再就是要渲染和展示它，还需要专门的插件和工具。针对这些问题，Craft.do团队终于下手了，专门打造了一个更快更好用的Mermaid美化引擎，更加贴合在Code Agent中使用。

它解决了 Mermaid 默认渲染器的 4 个痛点：

1. 超颜值 — 默认风格丑，不够专业

2. 多主题 — 改颜色要折腾 CSS class

3. 终端输出 — 支持 ASCII 纯文本渲染

4. 依赖重 — 原来简单图表拖一堆代码

5. 零工具 — 在Code Agent 中直接展示使用

Mermaid 是文本，AI 最擅长生成的就是文本，用 Claude Code 或者Codex三秒就能给你一段语法正确、结构清晰的 Mermaid。

零 DOM 依赖。

纯 TypeScript，不依赖浏览器环境,，Node 里直接跑。Claude Code 的 bash 工具可以直接执行，不需要起任何浏览器进程。

ASCII 终端输出。

不用开浏览器，renderMermaidASCII() 直接输出 Unicode 字符画,在终端里就能看架构图。

Skill的支持。

文章的结尾提供了Skill的下载。放进 Claude Code 的 Skill 路径，它就直接具备生成并渲染 Mermaid 图的能力，不需要你写任何胶水代码。

直接用自然语言就可以完成图表的生成和修改。

安装完成之后，我们就可以使用下面的提示词来生成任意的图表：

“画一个 sequenceDiagram，描述用户登录流程，渲染成 SVG 保存到本地”

Claude Code 自动识别 Skill，调用 beautiful-mermaid 渲染，SVG显示，全程不需要你解释用哪个库、怎么写脚本。

beautiful-mermaid提供了六大类，覆盖日常开发文档里最常见的需求:

Flowchart 流程图

![](.evernote-content/E6867C5B-26A5-47C8-B17B-AEF7A21C0FA0/D6FDFC3B-D9A6-4E42-828D-91A5F9B0B9D5.png)

Sequence Diagram 时序图

![](.evernote-content/E6867C5B-26A5-47C8-B17B-AEF7A21C0FA0/9A5EB248-DCF4-4C9C-81EA-20E94693698D.png)

State Diagram 状态机图

![](.evernote-content/E6867C5B-26A5-47C8-B17B-AEF7A21C0FA0/1AE81647-D98B-490C-B102-C72295992B8F.png)

Class Diagram 类图

![](.evernote-content/E6867C5B-26A5-47C8-B17B-AEF7A21C0FA0/C3EF343F-E1E0-4508-8B73-C66CD2BCFD07.png)

ER Diagram 实体关系图

![](.evernote-content/E6867C5B-26A5-47C8-B17B-AEF7A21C0FA0/EB607558-B3A2-4BFF-B338-28BA14D957F5.png)

XY Chart 柱状图、折线图、组合图

![](.evernote-content/E6867C5B-26A5-47C8-B17B-AEF7A21C0FA0/83E20414-6C11-4E81-95C4-9CBABE40D6D0.png)

更多图表的展示：ttps://agents.craft.do/mermaidSkills下载：https://link.bytenote.net/note

[📎 在印象笔记中打开](evernote:///view/207087/s1/9e35dfba-ecba-4f96-9710-7a232a691006/9e35dfba-ecba-4f96-9710-7a232a691006/)