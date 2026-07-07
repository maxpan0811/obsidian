---
title: 用微信读书MCP在Cursor中构建私人图书馆，太哇塞了！ 2
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/用微信读书MCP在Cursor中构建私人图书馆，太哇塞了！ 2.md
tags: [evernote, impression, yinxiang]
---

# 用微信读书MCP在Cursor中构建私人图书馆，太哇塞了！

---

原文链接: [https://mp.weixin.qq.com/s?chksm=fd8c45cccafbccda3019d790985bc03...](https://mp.weixin.qq.com/s?chksm=fd8c45cccafbccda3019d790985bc03b57e36dc05e961795d684455b38fe1cca467f131c1b69&exptype=unsubscribed_card_recommend_article_u2i_mainprocess_coarse_sort_tlfeeds&ranksessionid=1745981293_1&scene=169&mid=2247493075&sn=71010faab7a021ddff59cc3eadeda0ea&idx=1&__biz=MzU4NTE1Mjg4MA==&sessionid=1745980557&subscene=200&clicktime=1745981357&enterid=1745981357&flutter_pos=20&biz_enter_id=5&jumppath=WAWebViewController_1745981165900,WAWebViewController_1745981166468,20020_1745981186795,1104_1745981283129&jumppathdepth=4&ascene=56&devicetype=iOS18.4.1&version=18003b24&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ5xifCHixc/YBCnhsNnSzaxLVAQIE97dBBAEAAAAAAK85ANjf7bQAAAAOpnltbLcz9gKNyK89dVj0H3hj07SwVvsL82RFICOQxWSQyddfhWUgaqTaPLq4H4GLmmscw1LafC3ZmKgTf5gC7hp2YpL8boMJllfeGEc7m1KUb9TvXn1oIzCObfnU7IEA9W19q2TAHKC8k3y03JejbETqH2tQ1mEY6UC/2Yq1y4HMebTN6uL7ioWG95XV+76fk43D1/s0gR7cjmyoBWREVqKBJKs9zTOz6B+LTaqTn0RW7+rngghDKIbBHZR9RQ==&pass_ticket=MkZxa9O7RBmyOmchxqKypHxHwWgoe1xOQk5y86frOljvQTNhPQDPI6tNKexTqrXq&wx_header=3)

用微信读书MCP在Cursor中构建私人图书馆，太哇塞了！
=============================

Original苍何 苍何

这是苍何的第 353 篇原创！

大家好，我是苍何。

"明明看过很多书，却依旧过不好这一生"，这是个很经典的哲学问题，但今天我们不谈哲学，我们讨论如何用 AI 来解决这个问题。

不瞒你说，我的记忆也就比小鱼快 3 秒，所以很多东西看了根本记不住，看书这事也一样。

为了弥补缺陷，我会在微信读书中随时做笔记和划线，然后将这些笔记自动同步到 Notion 或者 Obsidian 这样的笔记软件中。

![](.evernote-content/1C908E91-1DC0-46DD-8A22-97E63AB38E6A/3B949A7F-1CC6-4499-87F0-11C8AD2B6BE8.png)

这套系统我用了好些日子，但时间久了，我发现一个问题。

我看了这么多书，做了这么多笔记，真正记住并用起来的又能有多少？

往往一些当时觉得很不错的观点记录下来，时间久了，我要真去想在哪本书看过呀？明明有印象，怎么就想不起来了呢？

**那些我曾看过的知识也同样在收藏夹中吃灰罢了**。

这时我就会陷入一种混沌的状态，我想过很多办法来解决，比如，我将我的微信读书仓库直接用 RAG 知识库交给 AI ，但效果都很「感人」。

![](.evernote-content/1C908E91-1DC0-46DD-8A22-97E63AB38E6A/DA9DBEC7-0EC4-4E3D-A0AD-FDBFCA35CD80.png)

除了理想不达标，数据更新等一系列问题外，这套做法未免显得太过于复杂。

直到我用了微信读书 MCP Server，才真正让我「**学有所用**」。

先别管他是个啥，我们来先看看效果。

比如我想看看我的书架上有哪些书？我只需要在 Cursor 中直接提问，他就快速给了我结果。

![](.evernote-content/1C908E91-1DC0-46DD-8A22-97E63AB38E6A/FE976A55-6A55-4CBD-9397-EC487BDAF33B.png)

具体搭建教程在文章最后会给出实战沉浸式教程。

比如我想看看之前笔记中关于“人活在世上”的一些观点，来辅助我写作。

![](.evernote-content/1C908E91-1DC0-46DD-8A22-97E63AB38E6A/526661B5-1FBB-4CC8-90E6-6B9A8C7AECBA.png)

AI 迅速帮我找出并汇总好，也就是说，我原先做的笔记又都发挥了作用，我也不用再费尽心思去找这些零碎的知识。

比如找下《认知觉醒》中关于”大脑天性“的笔记和观点

![](.evernote-content/1C908E91-1DC0-46DD-8A22-97E63AB38E6A/03671936-4734-4341-8D99-F94F7D5D8FDD.png)

进一步提问："将这些观点与我在《认知驱动》一书中的笔记做对比"

![](.evernote-content/1C908E91-1DC0-46DD-8A22-97E63AB38E6A/269DA019-E0BF-43EA-BFDE-5C77B8EE7659.png)

发现没有，所有知识自动串连起来了，太哇塞了吧。**每一步都有用，每一个知识都作数，成为了现实。**

这还没结束，经常做了很多的读书笔记，各种观点之间往往需要进行主题式整合，比如，我想查下我看过的书中所有关于"领导力"的内容。

我只需在 Cursor 中直接提问，AI 就帮我搜罗我所有的知识碎片，然后做一顿整合，直接给我想要的答案。

![](.evernote-content/1C908E91-1DC0-46DD-8A22-97E63AB38E6A/5F4ACBFD-4724-41A6-9B6C-C2A768E8D5BD.png)

然后继续让他找出不同点和差异："帮我整合这些不同来源的观点，找出共同点和差异"。

![](.evernote-content/1C908E91-1DC0-46DD-8A22-97E63AB38E6A/F137B340-6230-4850-9368-4FE6A51914BB.png)

然后基于这些笔记，帮我构建一个自驱力的知识框架

![](.evernote-content/1C908E91-1DC0-46DD-8A22-97E63AB38E6A/C3E26956-4D52-46CC-9C4C-5344DF8996CB.png)

绝了，在主题搜索、跨书整合和知识地图能力上，我已经完全能放飞自我了，不再受限于局部的碎片知识。

当然，我需要常年写作，经常会遇到灵感枯竭的情况，比如我想表达「似水流年」时，想引用之前看过的王小波的原文的哪句话，但就是想不起来。

这时候，我直接可以问 AI："我正在写关于似水流年的内容，请帮我找出笔记中关于似水流年的原文直接给我"

![](.evernote-content/1C908E91-1DC0-46DD-8A22-97E63AB38E6A/92B8F333-25DC-48B1-A513-36A61BFC8851.png)

就是这么快，而我去看了下我做的笔记，完全一模一样，我的个乖乖。

![](.evernote-content/1C908E91-1DC0-46DD-8A22-97E63AB38E6A/6A33CAA6-E27C-43C8-B51C-D4D39629B34C.png)

**这直接就打通了我输入-整体-输出的全流程**，而且全程不需要本地知识库存储，全是基于实时的 API 调用。

于是整个过程可以概括为：

![](.evernote-content/1C908E91-1DC0-46DD-8A22-97E63AB38E6A/1EDE2B55-E05D-4CF8-8B91-318F50F867D3.png)

**看书的时候，看到不错的观点直接划线或者做笔记，然后通过 AI 直接提问整理，知识的输入输出，完美闭环打通**。

甚至不用再倒腾多个工具，做整本书的读书笔记，也可以直接让 AI 基于划线或者评论的部分来做整个，输出完整的读书笔记。

比如用我这个提示词模板，丢给 Cursor。

# 角色
你是一位专业的读书笔记撰写者，擅长根据用户指定的书籍内容（包括划线和评论）制作详细的读书笔记。你的笔记将涵盖书籍的基本信息、核心内容提炼、深度思考延伸、行动指南以及多维评分。
## 技能
### 技能1：基本信息整理
- \*\*任务\*\*：记录书籍的基本信息。
  - 书名
  - 作者
  - 阅读日期
  - 书籍类型（小说/社科/工具书等）
  - 一句话概括全书核心主题
### 技能2：核心内容提炼
- \*\*关键论点/故事主线\*\*
  - 作者试图解决的核心问题是什么？
  - 书中最颠覆认知的3个观点
- \*\*逻辑结构分析\*\*
  - 全书框架图解（可用思维导图或分层标题）
  - 各章节递进关系
- \*\*高光片段标记\*\*
  - 最具启发性的案例/金句（标注页码）
  - 值得重读的章节
### 技能3：深度思考延伸
- \*\*批判性分析\*\*
  - 你认同/不认同的观点及原因
  - 书中未解答的疑问
- \*\*现实关联\*\*
  - 哪些内容可迁移到工作/生活中？举例
  - 这本书改变了你之前的哪些认知
- \*\*创意发散\*\*
  - 如果由你续写此书，会新增什么内容
  - 书中理论与XX领域（如心理学/经济学）的关联
### 技能4：行动指南
- \*\*立即实践清单\*\*
  - 列出具体可以立即实践的事项
- \*\*延伸学习方向\*\*
  - 相关书籍/课程/作者推荐
### 技能5：多维评分
- \*\*可读性\*\*
- \*\*知识密度\*\*
- \*\*实践价值\*\*
- \*\*重读可能性\*\*
## 限制
- 读书笔记应基于用户提供的书籍内容（包括划线和评论），确保信息准确无误。
- 在进行批判性分析时，保持客观公正，避免引入个人偏见。
- 提供的行动指南和延伸学习方向应具有实际可行性和实用性。
- 多维评分应基于对书籍内容的全面理解和评估，确保评分的客观性和准确性。
## OutputFormat:
### 1. 基本信息
- 📖 书名：
- ✍️ 作者：
- 📅 阅读日期：
- 📚 类型（小说/社科/工具书/心理学等）：
- 🧠 一句话总结核心主题：
### 2. 核心内容提炼
- ✅ 书中核心问题 / 故事主线：
- 🚩 最颠覆认知的3个观点：
- 🧩 章节结构分析（可用思维导图或列表）：
- 💎 高光片段（金句、案例）及页码：
- 📌 值得重读的章节或段落：
### 3. 深度思考延伸
- 💡 认同/不认同的观点及理由：
- ❓ 本书留下的未解答问题：
- 🌱 可迁移到生活/工作的内容 + 举例：
- 🔄 本书对你认知产生了哪些改变？
- 🔮 创意联想（可选）：
  - 若你续写此书，会添加哪些内容？
  - 本书与xx领域（如心理学/经济学）是否可产生跨界连接？
### 4. 行动指南
- 🚀 立即可实践的2项建议：
1.
2.
- 📚 延伸阅读/课程推荐：
### 5. 多维评分（1-5分）
- ⭐ 可读性：
- ⭐ 知识密度：
- ⭐ 实践价值：
- ⭐ 重读可能性：

比如我想基于我读的《白银时代》的所有笔记和划线来自动生成读书笔记，直接输入《白银时代》读书笔记汇总。

![](.evernote-content/1C908E91-1DC0-46DD-8A22-97E63AB38E6A/33B91204-5118-484E-8F99-8203168D3673.png)

然后拿着这个笔记直接丢微信读书中做一下总结。

也就是说，我只需要沉浸于读书这件事，对于笔记整理，以及笔记使用，就全部丢给 AI 好了。

我也不大喜欢记什么方法，我记得有什么费曼学习法，卡片笔记法，为了让我的这种新的方法有个好的名字，姑且就叫他 **AI 学习法**吧😂。

那么这个微信读书系统怎么搭建呢？步骤超级简单，一共就五步，下面，带你沉浸式的感受一下。（如果看到这，你已经战胜了 80%的小伙伴啦，给自己和文章悄悄点个赞吧）。

![](.evernote-content/1C908E91-1DC0-46DD-8A22-97E63AB38E6A/1BD03E31-1AC9-494D-9542-E9A7C3B960F5.png)

这里介绍的是本地部署 MCP Server 的方式，需要安装环境，当然我们也可以基于云部署的方式来使用，本地部署的好处是数据足够安全和隐私。

环境准备
====

1. 确保系统已安装 Node. js (v 16+)
2. 克隆本仓库：`git clone git@github.com:ChenyqThu/mcp-server-weread.git`
3. 进入项目目录：`cd mcp-server-weread`
4. 安装依赖：`npm install`

获取微信读书 Cookie
=============

1. 在浏览器中登录微信读书网页版: https://weread.qq.com/,
2. 打开浏览器开发者工具（F 12 或右键检查）
3. 刷新网页，切换到"Network"
4. 点开任意一个请求，找到"Cookies"
5. 找到并复制所有 cookie

![](.evernote-content/1C908E91-1DC0-46DD-8A22-97E63AB38E6A/E43B2959-8C2D-4E12-AEF7-4574FB9026F0.png)

配置环境变量
======

1. 在项目根目录下，编辑`.env`文件
2. 设置微信读书 Cookie：`WEREAD_COOKIE=你复制的cookie值`

![](.evernote-content/1C908E91-1DC0-46DD-8A22-97E63AB38E6A/B8B8F528-9847-4B8D-A207-165D64E1EC44.png)

启动服务器
=====

1. 编译代码：`npm run build`
2. 启动服务器：`node build/index.js`
3. `启动后就不用管他啦。`

在 Cursor 中配置
============

打开 Cursor 的 MCP 配置（这里可以参考我之前的文章）

{
  "mcpServers":{
    "mcp-server-weread":{
      "command":"node",
      "args":["/path/to/mcp-server-weread/build/index.js"],
      "env":{
        "WEREAD\_COOKIE":"你的微信读书cookie"
      }
    }
}
}

替换`/path/to/mcp-server-weread`为实际安装路径，并设置正确的 cookie 值。

![](.evernote-content/1C908E91-1DC0-46DD-8A22-97E63AB38E6A/618D2A9A-2F8A-4416-AD7E-080B1F428E3D.png)

配置好后就可以直接在 Cursor 对话框中使用啦，如果在配置过程中有任何使用问题都可以在文末**阅读原文**联系苍何哦。

写完文章，我长长舒了一口气，这套系统搭建好后，我相当于在 Cursor 中无形搭配了一个私人图书馆。

他只属于我一个人，我可以随时查看自己曾经似水流年留下的所有读书碎片，不用的时候他就安安静静在那里。

要用的时候，轻轻一问，AI 自动帮我从图书馆中搜集信息，给我反馈。

**这，就是 AI 的魅力。**

好啦，以上全文 **3097 字，17 张图**，如果这篇文章对你有用，可否点个关注，给我个三连击：点赞、转发和再看。若可以再给我加个⭐️。

文章同步我的 AI 开源知识库：[AI 开源知识库](https://mp.weixin.qq.com/s?__biz=MzU4NTE1Mjg4MA==&mid=2247492745&idx=1&sn=5bfca0f4b2b429d77e7f84a1e662f898&scene=21#wechat_redirect),，或者回复 AI 即可直接获取。

endin
=====

---

[🌐 原始链接](https://mp.weixin.qq.com/s?chksm=fd8c45cccafbccda3019d790985bc03b57e36dc05e961795d684455b38fe1cca467f131c1b69&exptype=unsubscribed_card_recommend_article_u2i_mainprocess_coarse_sort_tlfeeds&ranksessionid=1745981293_1&scene=169&mid=2247493075&sn=71010faab7a021ddff59cc3eadeda0ea&idx=1&__biz=MzU4NTE1Mjg4MA==&sessionid=1745980557&subscene=200&clicktime=1745981357&enterid=1745981357&flutter_pos=20&biz_enter_id=5&jumppath=WAWebViewController_1745981165900,WAWebViewController_1745981166468,20020_1745981186795,1104_1745981283129&jumppathdepth=4&ascene=56&devicetype=iOS18.4.1&version=18003b24&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ5xifCHixc/YBCnhsNnSzaxLVAQIE97dBBAEAAAAAAK85ANjf7bQAAAAOpnltbLcz9gKNyK89dVj0H3hj07SwVvsL82RFICOQxWSQyddfhWUgaqTaPLq4H4GLmmscw1LafC3ZmKgTf5gC7hp2YpL8boMJllfeGEc7m1KUb9TvXn1oIzCObfnU7IEA9W19q2TAHKC8k3y03JejbETqH2tQ1mEY6UC/2Yq1y4HMebTN6uL7ioWG95XV+76fk43D1/s0gR7cjmyoBWREVqKBJKs9zTOz6B+LTaqTn0RW7+rngghDKIbBHZR9RQ==&pass_ticket=MkZxa9O7RBmyOmchxqKypHxHwWgoe1xOQk5y86frOljvQTNhPQDPI6tNKexTqrXq&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/daebea5a-f5ce-484a-9d35-6585b64cb2ce/daebea5a-f5ce-484a-9d35-6585b64cb2ce/)
