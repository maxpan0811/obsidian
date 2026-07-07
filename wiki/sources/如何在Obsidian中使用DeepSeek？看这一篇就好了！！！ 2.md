---
title: 如何在Obsidian中使用DeepSeek？看这一篇就好了！！！ 2
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/如何在Obsidian中使用DeepSeek？看这一篇就好了！！！ 2.md
tags: [evernote, impression, yinxiang]
---

# 如何在Obsidian中使用DeepSeek？看这一篇就好了！！！

---

原文链接: [https://mp.weixin.qq.com/s?chksm=c0f531ecf782b8fa6918c5f11328632...](https://mp.weixin.qq.com/s?chksm=c0f531ecf782b8fa6918c5f11328632021344a728e302346d8a9c6bed7a167cf3a0ab845a8f4&exptype=unsubscribed_card_recommend_article_u2i_mainprocess_coarse_sort_tlfeeds&ranksessionid=1746195939_2&scene=169&mid=2247484684&sn=c82780b80dcde47795da3ace2639cdac&idx=1&__biz=MzkwNTY1MTU5OQ==&sessionid=1746195110&subscene=200&clicktime=1746197164&enterid=1746197164&flutter_pos=34&biz_enter_id=5&jumppath=WAWebViewController_1746196924570,WAWebViewController_1746196925108,20020_1746196936440,1104_1746197155805&jumppathdepth=4&ascene=56&devicetype=iOS18.4.1&version=18003b25&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQk1Jal5qzCTu97KSklBg4sRLVAQIE97dBBAEAAAAAAOSNGi++cJMAAAAOpnltbLcz9gKNyK89dVj0F39qZ6JwEDwigYBpJNR02Fns0gXaPj+VimGkdGXwyimZsTRiTBhSbzF5tzMzBCNJxWhPMABXtcjPUh0DVfZY2fFVZE57A25/FkmecozcCVPYLklWW+093sibqhXdSiy5kZsmVgpMymrUfs39BBXvszs8zfL1MKz2evCnl6nGR6OpOsMX7MrCbq3bfaAEvmCVvk4357Zc9ye58cJyhygqn+ePU6Eb9w2MnY3WI72Gpw==&pass_ticket=R1mQSmCMdoOBbMNHtcsincy2MeKDyk/tL4u5/2JKrjPi4Ecl+nCvw+nf8EgzLMaD&wx_header=3)

Original 拾柒  DUNDUN册页

在之前系列文章中我们介绍过[Obsidian-一款强大的知识管理工具](https://mp.weixin.qq.com/s?__biz=MzkwNTY1MTU5OQ==&mid=2247483744&idx=1&sn=deaf8c7fe33f67395ad2c79ecc11e859&token=4788213&lang=zh_CN&scene=21#wechat_redirect)，本文通过介绍Deepseek和如何与Obsidian结合，打造一个个人人工智能知识管理平台。

### 一、DeepSeek是什么？

**DeepSeek**

是一款基于人工智能的知识挖掘与分析工具。它能够通过自然语言处理（NLP）和机器学习技术，帮助用户从海量文本中提取关键信息、生成摘要、发现知识关联，甚至提供智能推荐。无论是学术研究、商业分析，还是个人学习，DeepSeek都能帮助你快速捕捉核心内容，节省大量时间。

![](.evernote-content/812EE5ED-EF07-41FA-99A6-24A72AF3F154/405B6B0B-B793-4643-8DC0-91FC8E0FF015.png)

#### 核心功能

DeepSeek的核心功能包括：

* **智能摘要**：自动生成文本的摘要，提炼核心观点。
* **知识图谱**：构建知识点之间的关联，形成可视化网络。
* **语义搜索**：通过理解语义，快速定位相关内容。
* **智能推荐**：根据你的阅读习惯和兴趣，推荐相关文献或资料。

#### 同类型产品对比

| **产品名称** | **特点** | **应用场景** | **性能表现** |
| --- | --- | --- | --- |
| **DeepSeek-V2** | 高效推理、长上下文支持、多语言优化 | 智能客服、内容创作、教育辅助 | 推理速度快，资源消耗低 |
| **GPT-4** | 强大的生成能力和广泛的应用场景 | 内容创作、代码生成、学术研究 | 英文任务表现优异，但资源消耗高 |
| **LLaMA3 70B** | 多语言处理，适用于广泛的NLP任务 | 多语言文本处理、多任务处理 | 性能稳定，资源消耗低 |
| **Mixtral 8x22B** | 灵活的多任务处理能力 | 多任务处理、复杂对话 | 性能灵活，适合多任务场景 |
| **QWen1.5 72B Chat** | 中文和英文对话优化 | 实时对话、多语言对话应用 | 对话流畅，适合实时应用 |

#### DeepSeek的优势

1. **性价比高**：DeepSeek在训练和推理效率上表现优异，适合资源有限的环境。
2. **多语言优化**：尤其在中文和英文对话中表现出色，适合多语言应用场景。
3. **长上下文支持**：支持128K的上下文长度，适用于长文本生成和复杂对话场景。

---

### 二、Obsidian的特色功能

![](.evernote-content/812EE5ED-EF07-41FA-99A6-24A72AF3F154/29C019A5-FE85-4A9E-B339-389819A7A5A9.png)

Obsidian

**Obsidian**是一款以本地存储为核心的笔记软件，以其强大的链接和可视化功能著称。它采用“双向链接”和“图谱视图”的设计理念，帮助用户构建个人知识库。Obsidian的特色功能包括：

1. **双向链接**：通过`[[ ]]`语法，轻松链接不同笔记，形成知识网络。详细可参考[【Obisidian】- 链接与反向链接](https://mp.weixin.qq.com/s?__biz=MzkwNTY1MTU5OQ==&mid=2247483826&idx=1&sn=12aa15dd451fc9138a9602aa624d3bf3&token=4788213&lang=zh_CN&scene=21#wechat_redirect)
2. **图谱视图**：以可视化的方式展示笔记之间的关系，帮助你发现隐藏的知识结构。详细可参考[【obsidian】核心插件篇 - 关系图谱：构建你的知识网络可视化利器](https://mp.weixin.qq.com/s?__biz=MzkwNTY1MTU5OQ==&mid=2247484593&idx=1&sn=ad029a85786be0687c51b0a8793351d5&scene=21#wechat_redirect)
3. **本地存储**：所有数据都存储在本地，确保隐私和安全。
4. **插件生态**：支持丰富的插件扩展，满足个性化需求。详细可参考[【Obsidian】- 插件](https://mp.weixin.qq.com/s?__biz=MzkwNTY1MTU5OQ==&mid=2247483785&idx=1&sn=43935502bec2a641fa8da63ae1106bbd&scene=21#wechat_redirect)
5. **Markdown支持**：采用简洁的Markdown语法，方便编辑和排版。详细可参考[【Obsidian】- Markdown 介绍](https://mp.weixin.qq.com/s?__biz=MzkwNTY1MTU5OQ==&mid=2247483766&idx=1&sn=e80736d02090f474508c30ee44763e4b&token=4788213&lang=zh_CN&scene=21#wechat_redirect)Obsidian的设计理念是“让你的知识像大脑一样工作”，它不仅仅是一个笔记工具，更是一个个人知识管理系统（PKMS）。

---

### 三、DeepSeek与Obsidian联用的效果

当**DeepSeek**与**Obsidian**结合使用时，两者的优势互补，能够显著提升知识管理的效率和深度。以下是它们联用的几大效果：

1. **智能摘要与笔记整合**

   DeepSeek可以自动为你阅读的文献、文章生成摘要，并将这些摘要直接导入Obsidian中。你无需手动整理，就能快速捕捉核心内容，并将其整合到个人知识库中。
2. **知识图谱的增强**

   DeepSeek的知识图谱功能可以与Obsidian的双向链接和图谱视图结合，帮助你更清晰地看到知识点之间的关联。例如，DeepSeek可以自动识别文本中的关键概念，并在Obsidian中生成相应的链接和图谱。
3. **语义搜索与快速定位**

   DeepSeek的语义搜索功能可以帮助你在Obsidian中快速找到相关内容。即使你忘记了具体的笔记标题，只需输入相关的关键词或概念，DeepSeek就能帮你定位到相关的笔记。
4. **智能推荐与知识扩展**

   DeepSeek可以根据你现有的笔记内容，推荐相关的文献、文章或知识点。这些推荐可以直接导入Obsidian，帮助你不断扩展和深化知识库。

---

### 四、如何在Obsidian中使用DeepSeek？

要将DeepSeek与Obsidian结合使用，可以按照以下步骤操作：

1. **注册硅基流动账号**

   由于Deepseek官网的API已经暂停服务，但依旧可以通过第三方在obsidian中嵌入Deepseek。搜索并点击进入硅基流动官网，点击右上方的注册;

![](.evernote-content/812EE5ED-EF07-41FA-99A6-24A72AF3F154/2E411269-EC2C-4B6A-A015-103B5B41F210.png)

1. **配置API密钥**

   点击左侧API密钥，点击新建API密钥，可以给这个密钥任意取一个名字，再点击新建即可，新建密钥之后复制密钥，这在之后的插件设置中有用；

![](.evernote-content/812EE5ED-EF07-41FA-99A6-24A72AF3F154/1B226243-3CD9-45D7-B1EF-D5972412B71A.png)

1. **下载copilot插件**

   在插件市场中下载并打开copilot插件；

![](.evernote-content/812EE5ED-EF07-41FA-99A6-24A72AF3F154/C1F52A67-8987-465E-AD7E-D648D13B8751.png)

1. **设置插件**

   打开copliot插件设置，点击Model，将所有勾选取消，点击Add Custom Model，可以按照图示设置，设置完之后点击verify，此时右上角会弹出成功提示，通过后点击Add Model ，仅勾选大模型Deepseek为正确；

![](.evernote-content/812EE5ED-EF07-41FA-99A6-24A72AF3F154/B80609A7-88CB-4909-91EB-F8C30A3F0D23.png)

1. 继续下滑到Embedding Models，点击Add Custom Model，可以按照图示设置，这两次设置中的密钥都是之前创建的，设置完之后点击verify，多次尝试直至右上角弹出成功提示，通过后点击Add Model ，仅勾选BAAI为正确；

![](.evernote-content/812EE5ED-EF07-41FA-99A6-24A72AF3F154/7737E1C3-B3C7-421C-91C0-D7AEF671917D.png)![](.evernote-content/812EE5ED-EF07-41FA-99A6-24A72AF3F154/428F4E5B-ADA4-42E3-B8EF-E12659CF9876.png)

1. 回到Basic页面，找到 General，第一个选择Deepseek，第二个选择BAAI，此时可能会跳出提示框更换后需要重新读取笔记内容，点击Continue即可，此时右上角会加载笔记库；

![](.evernote-content/812EE5ED-EF07-41FA-99A6-24A72AF3F154/1BCFC93F-0BFE-495B-859A-2CC6670CB47C.png)![](.evernote-content/812EE5ED-EF07-41FA-99A6-24A72AF3F154/2126F370-43E6-4A77-82B6-41C1BE2E6E68.png)![](.evernote-content/812EE5ED-EF07-41FA-99A6-24A72AF3F154/7280CC74-EFF8-41A8-A0B7-82AE55FFD4E9.png)

1. **使用搜索**

   在左侧工具栏中找到聊天图标，单击打开，页面右侧出现聊天框，将左下角改为Deepseek即可

![](.evernote-content/812EE5ED-EF07-41FA-99A6-24A72AF3F154/F3CB2AA1-0E23-4030-9F2F-7371CC80FA2F.png)

---

### 结语

DeepSeek与Obsidian的联合使用，为知识管理带来了全新的可能性。无论是学术研究者、内容创作者，还是终身学习者，都可以通过这两款工具的结合，实现更高效、更智能的知识管理。如果你正在寻找一种方式来提升你的知识管理效率，不妨试试DeepSeek与Obsidian的组合，开启你的智能知识管理之旅吧！

个人观点，仅供参考

---

[🌐 原始链接](https://mp.weixin.qq.com/s?chksm=c0f531ecf782b8fa6918c5f11328632021344a728e302346d8a9c6bed7a167cf3a0ab845a8f4&exptype=unsubscribed_card_recommend_article_u2i_mainprocess_coarse_sort_tlfeeds&ranksessionid=1746195939_2&scene=169&mid=2247484684&sn=c82780b80dcde47795da3ace2639cdac&idx=1&__biz=MzkwNTY1MTU5OQ==&sessionid=1746195110&subscene=200&clicktime=1746197164&enterid=1746197164&flutter_pos=34&biz_enter_id=5&jumppath=WAWebViewController_1746196924570,WAWebViewController_1746196925108,20020_1746196936440,1104_1746197155805&jumppathdepth=4&ascene=56&devicetype=iOS18.4.1&version=18003b25&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQk1Jal5qzCTu97KSklBg4sRLVAQIE97dBBAEAAAAAAOSNGi++cJMAAAAOpnltbLcz9gKNyK89dVj0F39qZ6JwEDwigYBpJNR02Fns0gXaPj+VimGkdGXwyimZsTRiTBhSbzF5tzMzBCNJxWhPMABXtcjPUh0DVfZY2fFVZE57A25/FkmecozcCVPYLklWW+093sibqhXdSiy5kZsmVgpMymrUfs39BBXvszs8zfL1MKz2evCnl6nGR6OpOsMX7MrCbq3bfaAEvmCVvk4357Zc9ye58cJyhygqn+ePU6Eb9w2MnY3WI72Gpw==&pass_ticket=R1mQSmCMdoOBbMNHtcsincy2MeKDyk/tL4u5/2JKrjPi4Ecl+nCvw+nf8EgzLMaD&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/b20ac8e9-003f-41dc-88cd-dbe067d024d7/b20ac8e9-003f-41dc-88cd-dbe067d024d7/)
