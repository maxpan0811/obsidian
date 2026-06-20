---
title: GitHub 上 23 万 star 的 5 个 RAG，我替你卸了 2 个（项目经理只装这 3 个）
type: source
created: 2026-06-17
updated: 2026-06-17
source: 印象笔记管理工具
source_path: 印象笔记管理工具/GitHub 上 23 万 star 的 5 个 RAG，我替你卸了 2 个（项目经理只装这 3 个）.html
tags: [AI技术]
---

# GitHub 上 23 万 star 的 5 个 RAG，我替你卸了 2 个（项目经理只装这 3 个）

原文链接: https://mp.weixin.qq.com/s?__biz=MzYzMjY1OTI0MA==&mid=224748...

Original莲花明 AI落地手记 
上礼拜我干了件蠢事。
把手里攒的 47 份 PDF——合同模板、行业报告、产品手册、会议纪要的脱敏版——一股脑喂给了 5 个号称"最强"的开源 RAG 项目。想着测完写一篇"横向对比"，结果测到第三个我就想砸键盘。
不是 RAG 不行，是大部分项目根本没想清楚"谁在用"。
开发者做的 Demo 闪闪发光，项目经理拿去跑第一个 PDF 就卡死。文档解析报错、向量库崩掉、中文乱码、检索出来八竿子打不着的段落——我这一周踩的坑，比你想象的密集得多。
以下是我的"验尸报告"。star 数从高到低排列，真香和翻车都写得明明白白。
▲ 23 万 star 的 5 个开源 RAG，3 真香 2 翻车
一、RAGFlow：6.85 万 star，文档解析的真神✓ 真香 github.com/infiniflow/ragflow | 68.5k+ star，主仓今年仍在高频更新，社区活得很猛。
一句话定位：它不是"能聊天"，是"能看懂你的 PDF 长什么样"。
我塞了什么：一份 87 页的行业白皮书，带表格、带层级标题、带页脚注释；还有 6 份扫描版合同（图片 PDF）。
哪里真香：RAGFlow 的 DeepDoc 解析引擎确实离谱。表格没碎成文字渣，标题层级完整保留，扫描件居然也认出了八九成。它不像别的项目把 PDF 当成"一整坨文本"来切，是真的理解文档结构。

问"第三章提到的市场规模是多少"，它能定位到具体章节，不是全文瞎搜。最近还加了 Agent 能力和 MCP 支持——意味着它从"知识库"进化成了"能干活的知识库"。哪里翻车：Docker 镜像 9GB，低配机器根本跑不动。我第一次在 8G 内存的测试机上启动，直接 OOM。后来换了 16G 才勉强站起来。slim 版虽然小，但 embedding 模型要自己配，对非技术用户不友好。
一行装上：
git clone https://github.com/infiniflow/ragflow.git && cd ragflow/docker && docker compose up -d
二、AnythingLLM：5.97 万 star，5 分钟开聊的本地私域方案✓ 真香 github.com/Mintplex-Labs/anything-llm | 59.7k star，社区活跃得像个社群运营。
一句话定位：不想折腾的人，选它。
我塞了什么：12 份 Word 文档、3 个网页导出的 HTML、一个 200 行的 Excel 客户反馈表。
哪里真香：Desktop 版下载即装，Mac/Windows/Linux 全有。我拖进去 12 个文件，5 分钟后就能问"客户反馈里提到最多的三个问题是什么"。自动处理格式转换、自动切分、自动 embedding，全程不用我写一行配置。

...Workspace 隔离做得也好——项目 A 的文档不会污染项目 B 的问答。对怕数据上云的团队来说，本地跑 Ollama + AnythingLLM 是现成答案。哪里翻车：它太"傻瓜"了，导致高级功能藏得深。我想调 chunk size 和 overlap，找了 10 分钟才在设置里挖出来。免费版 embedding 质量一般，复杂文档的召回率不如 RAGFlow 精准。
一行装上：Mac/Win 直接去官网下 Desktop 安装包；服务器
