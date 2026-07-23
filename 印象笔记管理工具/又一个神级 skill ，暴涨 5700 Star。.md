# 又一个神级 skill ，暴涨 5700 Star。

---

来源：[打开原文](https://mp.weixin.qq.com/s/hTjvzwqcFzsJUPR6_skIQg)

做开发和架构设计的人一定会有这样的体会。

写技术方案、架构文档、README 文档，最费时间的不是理清逻辑，而是画图。

Draw.io、Visio 需要手动拖拽组件、连线、调整布局、修改颜色，一张复杂的微服务架构图要十几分钟。

Mermaid、PlantUML 要熟悉掌握很多语法，多分支流程、复杂的云架构很容易出错。

最近在 GitHub 上看到一个叫 Archify 的项目。

在 GitHub 上已经有 5700 个 Star 了。

一句话概括一下就是：

它就是用大白话来生成专业架构图的 Skill。

![](.evernote-content/9F6D1F46-4613-418D-BE76-0CBC219EC150/1D723B06-23BD-4127-B165-7A00D3E88FA8.png)

给你演示一下，你就知道它有多方便了
-----------------

我想给自己的微服务项目画一张架构图。

随手打开 Claude Code，说了一句:

画一个电商系统的架构，包含前端、API 网关、订单服务、支付服务、数据库、缓存。

它就开始生成图表。

Claude 先生成了一个结构化的 JSON 描述，其中包括了组件、连接和坐标等信息。

![](.evernote-content/9F6D1F46-4613-418D-BE76-0CBC219EC150/F4CF5333-20A9-4884-A9EC-B18BCF4BBDE4.png)

然后自动生成HTML。打开目录后。 我看到的是一个单独的HTML文件，可以直接在浏览器中打开。

![](.evernote-content/9F6D1F46-4613-418D-BE76-0CBC219EC150/5DEBB13E-0F46-4C23-9136-EEB141402DA2.png)

图表有深色和浅色两种主题，可以一键切换。

按下了T键之后，深色主题就变成了浅色主题。

![](.evernote-content/9F6D1F46-4613-418D-BE76-0CBC219EC150/11DD3D6C-DA5A-4C59-9117-62126EB55E02.gif)

然后点击导出菜单。

按下E键后会弹出一个导出菜单，可以将PNG格式的图片复制到剪贴板中，也可以选择下载为PNG、JPEG、WebP、SVG等格式。

在整个过程中我只说了一句话，后面生成JSON、渲染图表、切换主题、导出图片等工作都是它自己完成的。

有人会想，这是怎么做到的
------------

01 五种图表类型都包含在内。

Archify 一共支持五种常见的技术图表。

Architecture，系统架构图。

Workflow，泳道流程图。

Sequence，时序图。

![](.evernote-content/9F6D1F46-4613-418D-BE76-0CBC219EC150/97F8BB3E-AF3C-446E-85EE-A9E3298BE1C8.png)

Data Flow，数据流图。

![](.evernote-content/9F6D1F46-4613-418D-BE76-0CBC219EC150/7F706A17-FC38-4E61-B14D-F339A702F78A.png)

Lifecycle，状态机图。

这五种类型涵盖了开发者在技术文档、方案设计、架构评审、CI/CD 文档、API 文档等场景下的99%的绘图需求。

每种图表都有自己的 JSON Schema 和渲染器，保证输出的稳定性与可复现性。

02 自然语言驱动，零学习成本。

用户只需要用大白话来描述系统或者流程，比如画出一个 CI/CD 流程：

pull request -> tests -> approval -> build image -> staging -> smoke test -> production。

![](.evernote-content/9F6D1F46-4613-418D-BE76-0CBC219EC150/FD3FE60A-B64E-4D2B-8903-1D7F4DAA1970.png)

Archify可以生成相应的图表，不需要学习Mermaid语法，不需要拖拽组件，不需要调整布局。

03 双主题自适应切换。

每一个生成出来的图表都存在深色和浅色两种主题，用户可以通过按钮或者快捷键T来进行切换。

导出的SVG文件里有双主题CSS变量集以及prefers-color-scheme媒体查询。

当它被嵌入到 GitHub 的 README 或者博客中时，可以自动跟随读者的系统主题。

这就意味着你只需要维护一个SVG文件就可以同时适配深色和浅色两种阅读环境。

![](.evernote-content/9F6D1F46-4613-418D-BE76-0CBC219EC150/F209AC84-650F-48B6-A1C3-26EF17380149.png)

04 最高4倍高清导出。

所有的栅格导出（PNG、JPEG、WebP）都是以最高的安全分辨率来渲染，最高可以达到4倍，不会出现模糊或者锯齿。

![](.evernote-content/9F6D1F46-4613-418D-BE76-0CBC219EC150/AC4A7670-B2F0-46E8-A79F-E8C546E2FF4F.png)

并且可以一键将PNG复制到剪贴板中，可以直接粘贴到Slack、Notion、GitHub、Figma等工具里。

05 JSON IR + Schema 验证闭环。

Archify 并不是简单的 AI 生成器，而是一个有完整工程化闭环的工具。

每种图表类型都对应着一个 JSON IR 和一个 JSON Schema，Claude 先生成结构化的 JSON，然后由渲染器生成出 HTML/SVG。

渲染器在生成之前会做Schema校验、布局检查、HTML/SVG完整性检查，防止生成畸形图表。

![](.evernote-content/9F6D1F46-4613-418D-BE76-0CBC219EC150/FADDF3DD-307B-4412-BC61-E57CD6C6BEFA.png)

看完这些功能，相信各位已经迫不及待了
------------------

Archify 安装只需要一条命令：

npx skills add tt-a1i/archify -g

这个命令会通过开源的 skills CLI 安装 Archify，支持 Claude Code、Codex CLI、opencode 等多种 AI Agent 平台。

安装好之后，在Claude Code中说：

使用archify来绘制出该仓库的运行时架构图。

就可以画出结构图了。

如果只是试用的话，不需要永久安装，可以使用：

npx skills use tt-a1i/archify@archify --agent codex

将codex替换为claude-code或者opencode就可以适配不同的Agent。

到这里边界也给大家提提
-----------

Archify 并不是通用的绘图编辑器，不能像 Figma、Visio、Draw.io 一样自由拖拽编辑。

它所要做的就是把自然语言转换成成品图表，而不能像可编辑的画布那样。

如果要修改图表，只能通过对话或者编辑JSON IR来实现，不能直接在画布上拖动。

另外，在导出为PNG、JPEG、WebP格式的时候，会先使用系统自带的等宽字体。

只有在本地安装了JetBrains Mono之后，才能用。

另外一点是Archify没有使用自动布局，而是让 AI 自己来判断布局。

写在最后
----

我关注了Archify一段时间了。

今天抽空用了一下。

发现它有趣的地方是，它并不是要替代 Draw.io 或者 Figma。

它解决的是另外一个场景，即你已经有一个架构在脑子里了，但是要快速地把它可视化出来。

对于需要精确调节、多人配合的场景，还是交给专业的工具来处理。

但是快速出图、迭代验证，用Archify说一句话就成，节省下来的时间就可以专注于架构设计了。

项目基于 MIT 协议开放，感兴趣的同学可以去 GitHub 仓库看看源码和文档。

开源地址：https://github.com/tt-a1i/archify

既然看到这了，欢迎随手点赞、在看、转发，也可以给我个星标⭐，接收最新的文章，我们下期见！

[📎 在印象笔记中打开](evernote:///view/207087/s1/5fe97750-cbf1-4b1b-882b-8cec584cfc82/5fe97750-cbf1-4b1b-882b-8cec584cfc82/)