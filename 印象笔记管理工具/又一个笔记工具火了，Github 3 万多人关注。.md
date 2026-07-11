# 又一个笔记工具火了，Github 3 万多人关注。

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=Mzg3NzU0NzIxMA==&mid=224751...](https://mp.weixin.qq.com/s?__biz=Mzg3NzU0NzIxMA==&mid=2247512135&idx=1&sn=b915ae797c338f3ad276c45e5d211a8e&chksm=ce39c26d674060070e99f23810ac3359d4dbc8e8eca21afb27c88f34428f08089b4ae979b9a5&scene=90&xtrack=1&req_id=1778928837201035&sessionid=1778928814&subscene=93&clicktime=1778929178&enterid=1778929178&flutter_pos=15&biz_enter_id=4&ranksessionid=1778928837&jumppath=20020_1778929129883,1104_1778929142487,20020_1778929146394,1104_1778929166423&jumppathdepth=4&ascene=56&devicetype=iOS26.4.2&version=18004929&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ2LevqKigSC2QL04qm2w7bRLVAQIE97dBBAEAAAAAALVaEigrL50AAAAOpnltbLcz9gKNyK89dVj09cXwTKnSu1TXYTGeHhv/sJtBHLndQyoNrQN0UGXhq+npkiCMPK+Tsz1mJwRaw/DtotN1yJAMYt0P+i/vYOCH33ZXV2+xDzSNd7KEVATaepXOcOjsWoXClgb1+s3W6eL9Pc8iWQQYifHp8fC05irYJMaMiDGScrvZg438xv8CqN0PYPj8x9guXKdIZrw1K0IYQpzGOaf3ZA2xr47vTRJMzO6ue45/gyANS692QnkqVw==&pass_ticket=i8z4+aU74ia6MlXZXvlNgLIV++BRdp9CaCm/cuIOQTnLbWVpePySsCOgBPZuyW+V&wx_header=3)

Original开源日记开源日记

好久没有分享关于写作的工具了。

最近刷到一个叫 Tolaria 的写作工具。有点意思 。

短短 3 个月，GitHub Star 破万，发布后两周成为全球增长第 10 快的仓库。

![](.evernote-content/A1DBF258-BE7A-423D-9863-763B24A91D31/DE355BF9-7C70-4450-9AC3-54CD0D23E420.png)

一说到写作，知识管理，很多人会无脑推 Notion 和 Obsidian 。

一个新玩家，数据为啥如此爆 ？

也许和作者的背景有关：

一个写了 5 年技术博客的人，积累了 9000 多条笔记，最后发现市面上的工具都不顺手，干脆自己动手写了一个。

**Tolaria 是一个桌面应用，用来管理 Markdown 知识库，本地优先、Git 原生集成、AI 可直接读写笔记**。

![](.evernote-content/A1DBF258-BE7A-423D-9863-763B24A91D31/DB233D14-0B2C-441C-825A-30D75861A64A.png)

采用 Tauri+React+Rust 技术栈，包体小巧、启动迅速、内存占用极低。

它把 Notion 的编辑体验和 Obsidian 的本地理念缝合在一起。
-------------------------------------

**01 本地 Markdown 存储。**

所有笔记都存成纯 Markdown 文件，配合 YAML frontmatter 来描述结构化元数据。

你在电脑硬盘看到的就是一推.md 结尾的文件。

![](.evernote-content/A1DBF258-BE7A-423D-9863-763B24A91D31/7F1584AE-3517-4CC2-8A6A-FC8BA572F4A7.png)

你可以用任何编辑器打开，甚至可以借助 `grep` 命令行来搜索。

要是哪天 Tolaria 倒闭了，或者你不想用了，你的数据还在，不会跟着平台一起消失。

**02 Notion 风格块编辑器。**

这一点和 Notion 一样 。

Tolaria 也提供了一个类似 Notion 的块编辑器，支持斜杠命令、拖拽操作、实时预览。

![](.evernote-content/A1DBF258-BE7A-423D-9863-763B24A91D31/79597453-DE64-467E-88E2-27182BC547A8.png)

写起来有 Notion 那种德芙般丝滑的快感，但所有操作都在本地完成，没有云端同步的延迟感。

**03 wikilinks 双向链接。**

让我惊喜的是，它还支持 wikilinks 双向链接，借助 `[[笔记名]]` 就能关联其他笔记，构建知识网络。

![](.evernote-content/A1DBF258-BE7A-423D-9863-763B24A91D31/92D89037-ED77-4E0D-8E4E-43A2F1B1C1F1.png)

**04 实时预览。**

编辑 Markdown 时，右侧同步渲染出最终效果，所见即所得。

![](.evernote-content/A1DBF258-BE7A-423D-9863-763B24A91D31/D60369D2-115B-4CAB-B5E4-512F6058A1B4.png)

真正的差异性，是它的 Git 原生集成。
--------------------

这是 Tolaria 以及 Obsidian 拉开差距的地方。

**01 Git 仓库管理。**

它把每个知识库都当成了一个 Git 仓库。

内置的有 Git 工具，可以在里面存版本、同步内容、查历史、对比哪些地方有修改。

![](.evernote-content/A1DBF258-BE7A-423D-9863-763B24A91D31/B23500A9-2F15-49E3-8A6F-4954381A59CC.png)

还有一个好处是能用GitHub管理你的知识库，自带版本记录，不小心删错改错，随时一键恢复回来。

也许有朋友会说 Obsidian 也可以啊。

可以是可以 ，但要通过装插件，配置 Git实现，门槛稍高那么一点。

**02 可视化 Git 操作。**

另外它把 Git 操作做成了可视化界面。

![](.evernote-content/A1DBF258-BE7A-423D-9863-763B24A91D31/01DA6B85-938E-4DB5-8F4B-9FAF1EF744A3.png)

你不需要记命令行，点几下按钮就能完成 commit、push、查看历史。

对于不熟悉 Git 的用户，这大大降低了使用门槛。

![](.evernote-content/A1DBF258-BE7A-423D-9863-763B24A91D31/0F72F591-1143-4218-B21F-051EC399D2D8.png)

AI功能也不能少 。
----------

这不是简单地在侧边栏加个 AI 聊天窗口。

![](.evernote-content/A1DBF258-BE7A-423D-9863-763B24A91D31/3E64B333-85D5-4538-A9FE-D947CECA19C1.png)

**01 MCP 服务器。**

Tolaria 内置了一个 MCP服务器，把你的知识库变成了一个 AI 可以直接操作的结构化数据源。

具体来说，当你连接 Claude Code、Codex CLI 或 Gemini CLI 这些 AI 编程工具时，它们可以直接搜索你的笔记、读取内容、甚至创建新笔记。

![](.evernote-content/A1DBF258-BE7A-423D-9863-763B24A91D31/9062B6D6-7E89-43F5-BBC5-9BFF63A5AC05.png)

**02 AGENTS.md 文件。**

Tolaria 还会自动生成一个 `AGENTS.md` 文件，告诉 AI 你的知识库是怎么组织的，有哪些约定和结构。

这相当于给你的 AI 助手装上了记忆芯片，让它真正基于你的私人知识体系工作，而不是每次都从零开始。

举个例子。

你在知识库里积累了大量技术笔记，包括 React 组件设计模式、性能优化技巧、测试最佳实践。

当你让 AI 帮你写代码时，它会先读取你的知识库，理解你的编码风格和偏好，然后生成符合你习惯的代码。

而不是每次都给你一个通用的、可能不符合你项目规范的答案。

社区里有人把 Tolaria 称为Notion 的皮，Obsidian 的心。

这个比喻挺准，但还不够完整。

它更像是把 Notion 的编辑体验、Obsidian 的本地理念，再加上一层 AI 原生设计，缝合成了一个新物种。

到这有几个问题我也说一下。
-------------

它不是 Notion 那样的团队协作平台，没有实时协作、权限管理这些功能。

插件生态也不如 Obsidian 丰富，毕竟是个新项目。

移动端目前还没有，这点确实不方便。

看完这些功能，相信各位已经迫不及待了。
-------------------

最简单的方式：

去 GitHub Release下载最新的安装包就可以了。

![](.evernote-content/A1DBF258-BE7A-423D-9863-763B24A91D31/1587A422-596D-44CD-9C31-41E827C2ACA8.png)

下一步一直装到最后。

![](.evernote-content/A1DBF258-BE7A-423D-9863-763B24A91D31/8D9A98DF-D6E9-4EAB-8112-8311DA6A8E9C.png)

写在最后
----

Notion 数据在云端，协作功能强；Obsidian 数据在本地，插件生态丰富。

Tolaria 也是本地存储，但多了 Notion 风格的编辑体验，以及 Git 和 AI 的深度集成。

如果你已经在用 Notion 或 Obsidian，用得顺手，其实没必要换。

但如果你想试试本地存储 + Notion 编辑体验 + Git + AI 这套组合，Tolaria 可以看看。

Tolaria 基于 AGPL-3.0 协议开放，感兴趣的同学可以去 GitHub 仓库看看源码以及文档。

开源地址：https://github.com/refactoringhq/tolaria

既然看到这了，欢迎随手点赞、在看、转发，也可以给我个星标⭐，接收最新的文章，我们下期见！

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=Mzg3NzU0NzIxMA==&mid=2247512135&idx=1&sn=b915ae797c338f3ad276c45e5d211a8e&chksm=ce39c26d674060070e99f23810ac3359d4dbc8e8eca21afb27c88f34428f08089b4ae979b9a5&scene=90&xtrack=1&req_id=1778928837201035&sessionid=1778928814&subscene=93&clicktime=1778929178&enterid=1778929178&flutter_pos=15&biz_enter_id=4&ranksessionid=1778928837&jumppath=20020_1778929129883,1104_1778929142487,20020_1778929146394,1104_1778929166423&jumppathdepth=4&ascene=56&devicetype=iOS26.4.2&version=18004929&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ2LevqKigSC2QL04qm2w7bRLVAQIE97dBBAEAAAAAALVaEigrL50AAAAOpnltbLcz9gKNyK89dVj09cXwTKnSu1TXYTGeHhv/sJtBHLndQyoNrQN0UGXhq+npkiCMPK+Tsz1mJwRaw/DtotN1yJAMYt0P+i/vYOCH33ZXV2+xDzSNd7KEVATaepXOcOjsWoXClgb1+s3W6eL9Pc8iWQQYifHp8fC05irYJMaMiDGScrvZg438xv8CqN0PYPj8x9guXKdIZrw1K0IYQpzGOaf3ZA2xr47vTRJMzO6ue45/gyANS692QnkqVw==&pass_ticket=i8z4+aU74ia6MlXZXvlNgLIV++BRdp9CaCm/cuIOQTnLbWVpePySsCOgBPZuyW+V&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/13a8f42a-b4b2-4ed7-98c4-8d33458e552b/13a8f42a-b4b2-4ed7-98c4-8d33458e552b/)