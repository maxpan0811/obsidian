---
title: "PlotPilot 墨枢，让 AI 能写长篇小说了"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/PlotPilot 墨枢，让 AI 能写长篇小说了.md
tags: [印象笔记]
---

# PlotPilot 墨枢，让 AI 能写长篇小说了

# PlotPilot 墨枢，让 AI 能写长篇小说了 --- 原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzIwNjA1NjMyNQ==&mid=26491

---

# PlotPilot 墨枢，让 AI 能写长篇小说了

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzIwNjA1NjMyNQ==&mid=264911...](https://mp.weixin.qq.com/s?__biz=MzIwNjA1NjMyNQ==&mid=2649114532&idx=1&sn=d647b1a0383977b7aa1031ccf6dd4eda&chksm=8e71093ca56bc038108b2da429fc34efaf3aff5713954313d11698cf8799c15d8ca6dde30462&scene=90&xtrack=1&req_id=1783824101190009&sessionid=1783823291&subscene=93&clicktime=1783824249&enterid=1783824249&flutter_pos=43&biz_enter_id=4&ranksessionid=1783824101&jumppath=20020_1783824152684,1104_1783824222797,20020_1783824226525,1104_1783824245598&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b38&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQskXRCHhvzvATbvYuKmxkrxLTAQIE97dBBAEAAAAAAFAxF/e6MyMAAAAOpnltbLcz9gKNyK89dVj0jo/MT9RlPkjcFiBHhFIPVGIgpTnExaAU7uSmCNjo8bsULpEWP6HkLLbOT8Adbx5EsyVURjaZi4/vIOEvVebH4UGf/6L8tL++bwa2t9EQ5xe9s1djnHdM02jD36DaVAysgKTiU8LBrMlRsuoQEd65c64YacgTC9DrOaxegpsv6HH1dtxRYF+c/oOsoBMJRhkHCaso86XbmcrOrsIiSNcez6SfC0iwgKbe+7igrfk=&pass_ticket=OSIPB7nq6SSZVLhngpm1u5DXYfJBj8iIZWas4pBV7NuwJfombDTJtR1CXDYefVpH&wx_header=3)

OriginalAI智闻说AI智闻说

用 AI 写小说的人越来越多了，但几乎所有人都会撞上同一堵墙：写到十万字以后，人物性格飘了，伏笔忘了收。

这不是模型不够聪明。你让它续写一段话，它写得挺好；你让它记住二十章前埋的暗线，它做不到，因为根本没人替它记。

PlotPilot 墨枢就是来干这件事的。一个开源的剧情引擎内核，核心想做的事很简单：替 AI 管好叙事状态，让它能写一部完整的小说。

![](.evernote-content/83E5B22A-FE31-4FBE-948C-ADA1B2D5A75D/6C9ED587-6295-4F1E-B3F1-B8BF7951079C.png)![](.evernote-content/83E5B22A-FE31-4FBE-948C-ADA1B2D5A75D/33513BB7-8C5A-4A13-8921-ED2B802E23CD.jpg)

它到底是什么
------

PlotPilot 是一个剧情引擎内核（Narrative Engine Kernel），管的是叙事状态的持久化、检索和监控。

市面上大部分 AI 写作工具解决的是「生成」问题，没解决「连贯」问题。PlotPilot 走了另一条路，它不管生成本身，管的是生成之前和之后的状态。

和常见方案的区别：

| 方案 | 做什么 | 没做什么 |
| --- | --- | --- |
| 聊天式续写 | 「接着写第三章」 | 无跨章状态持久化 |
| 提示词模板 | 一组角色设定 | 无动态上下文装配 |
| 大上下文堆料 | 把全文塞进上下文 | 无叙事线索结构化追踪 |
| PlotPilot | 持久状态 + 结构化记忆 + 自动推进 | LLM 只负责在结构化上下文里写段落 |

LLM 负责生成文字段落，状态管理交给引擎——各干各的。

![](.evernote-content/83E5B22A-FE31-4FBE-948C-ADA1B2D5A75D/0F12AF7C-83AB-4BCC-9271-5ECB142D718A.jpg)

五个子系统怎么协作
---------

引擎在任意时刻都持有完整的叙事快照，每次生成新章节时，从快照里动态装配上下文窗口。

### 叙事状态机

引擎的「大脑」，维护五类结构化状态：

  
**Story Bible（故事设定集）**：人物档案（含 POV 防火墙、登场频率调度）、地点图、世界设定三元组  
**章级摘要链**：每章生成后自动提炼压缩摘要  
**叙事事件流**：关键事件的时序登记，支持因果链追溯  
**故事线 DAG（有向无环图）**：多故事线的分支与汇合可视化  
**伏笔注册表**：钩子的开启、悬置、消费状态完整追踪

### 向量语义检索层

两条并行索引：一条是基于 FAISS/ChromaDB 的语义切片索引，对所有已写章节做向量检索；一条是 `(主体, 关系, 客体)` 三元组索引，支持结构化与语义混合查询。

生成时，引擎通过当前场景语义自动召回相关历史内容注入上下文，解决模型「失忆」问题。嵌入服务支持 OpenAI 兼容 API 和本地 `bge-small-zh-v1.5` 模型。

### 引擎运行时

最核心的组件。代码入口在 `engine/runtime/engine_daemon.py`，EngineDaemon 管着守护进程，StoryPipelineRunner 跑十步管线：

1叙事治理预算2章节执行剧本准备3上下文装配（人物 / 世界观 / 记忆 / 伏笔）4LLM 调用5内容策略验证6文风漂移检测7章末管线（摘要 / 事件 / 三元组 / 伏笔）8向量索引更新9张力评分10状态落库 → 决定继续 / 重写 / 暂停

几个关键设计：熔断保护（连续失败自动暂停）、单写者路由（SQLite 串行写）、SSE 实时推流、检查点快照（可从任意检查点恢复）。

### 提示词策略层

引擎暴露 20+ 个独立提示接点，覆盖规划类、生成类、知识类、分析类四种类型。每个接点都能通过 `prompt_packages/` 下的 YAML 配置独立覆写。

可配置的内容很多：系统提示、声线锚点、节拍约束、字数层级，以及模型参数（temperature / top\_p / max\_tokens）。切换任务类型不需要改代码，换一套提示包目录就行。

### 质量监控子系统

叙事质量有三道防线：

  
**张力心电图**：每章生成后计算张力评分（0–10），历史曲线持久化，低谷自动触发诊断  
**文风漂移检测**：向量余弦相似度衡量偏离程度，超阈值触发定向修写——保留已有进度不回滚  
**陈词滥调扫描**：规则库 + 语义相似度双重检测，标记高频套路表达![](.evernote-content/83E5B22A-FE31-4FBE-948C-ADA1B2D5A75D/760AC3B3-D81E-4684-9D08-CDA3D9847E47.png)

和竞品有什么不同
--------

GitHub 上做 AI 长篇写作的开源项目不止一个。目前星数最多的是 AI-Novel-Writing-Assistant（1956 stars，TypeScript），定位「面向长篇小说的 AI Native 开源系统」，用 Agent + 世界观 + 写法引擎 + RAG 的路子。

两者的核心差异是出发点不同：AI-Novel-Writing-Assistant 产品化优先，UI 先行；PlotPilot 引擎优先，偏基础设施。

PlotPilot 目前有这些差异化能力：

  
张力评分曲线 + 低谷自动诊断——其他项目没看到类似机制  
文风漂移检测 + 定向修写——检测偏离后不回滚，触发修写保留进度  
伏笔注册表——从开启到悬置到消费，完整状态追踪  
POV 防火墙——人物视角不会串，写谁就是谁  
题材 Pipeline 扩展——武侠、仙侠、玄幻、都市、言情、悬疑、科幻、历史、游戏等 10 种题材，各有独立 Agent 和可选 Skills，比如战斗编排、修炼体系、推理逻辑、情绪节奏

PlotPilot 的出发点和市面上的写作工具不同：它用状态机、向量检索、质量监控来保证叙事连贯性，先把机制搭对，再让 LLM 在结构化上下文里生成文字。

上手试一下
-----

最小可跑流程（macOS / Linux）：

1克隆仓库，确认装了 Python 3.14（注意：3.14 是较新版本，系统没装的话需要单独下载）2`python3.14 -m venv .venv && source .venv/bin/activate`3`pip install -r requirements.txt`（国内可加 `-i https://pypi.tuna.tsinghua.edu.cn/simple` 换源）4`cp .env.example .env`，填写至少一个 LLM 凭证（OpenAI / Claude / 火山方舟 Doubao / Gemini 都行）5`uvicorn interfaces.main:app --host 127.0.0.1 --port 8005 --reload`6另开终端 `cd frontend && npm install && npm run dev`7打开浏览器访问 `http://localhost:3000`，走新书向导，设定世界观和人物，然后开启自动驾驶

Windows 用户更简单：双击 `plotpilot.bat`，自动创建虚拟环境、装依赖、启动服务、打开浏览器。

模型接入方面，PlotPilot 用了统一接口抽象，支持 OpenAI 兼容协议、Anthropic Claude、火山方舟 Doubao、Gemini。

另外能做的事还包括：长篇连续生产、世界观/人物/伏笔结构化管理、张力与文风质量监控、自动驾驶、10 种题材扩展、DOCX/EPUB/PDF 导出。

几个要注意的边界：

  
许可证含 Commons Clause：允许学习、修改、非商业内部部署，不允许封装成收费 SaaS  
完全离线需要额外配置：嵌入服务支持 OpenAI 兼容 API 和本地 `bge-small-zh-v1.5`，离线得装本地模型，额外装依赖  
macOS/Linux 体验不如 Windows：一键启动器目前只有 Windows 版（bat 脚本 + Tauri 安装包），macOS/Linux 需要手动走开发流程  
Python 3.14 依赖：这个版本比较新，部分系统默认的 Python 还是 3.11/3.12，需要单独安装

写在最后
----

PlotPilot 的核心思路是把「AI 写长篇」从「提示词怎么写」的问题，变成「状态怎么管」的问题。引擎管状态，LLM 管文字，长篇才写得完。

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzIwNjA1NjMyNQ==&mid=2649114532&idx=1&sn=d647b1a0383977b7aa1031ccf6dd4eda&chksm=8e71093ca56bc038108b2da429fc34efaf3aff5713954313d11698cf8799c15d8ca6dde30462&scene=90&xtrack=1&req_id=1783824101190009&sessionid=1783823291&subscene=93&clicktime=1783824249&enterid=1783824249&flutter_pos=43&biz_enter_id=4&ranksessionid=1783824101&jumppath=20020_1783824152684,1104_1783824222797,20020_1783824226525,1104_1783824245598&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b38&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQskXRCHhvzvATbvYuKmxkrxLTAQIE97dBBAEAAAAAAFAxF/e6MyMAAAAOpnltbLcz9gKNyK89dVj0jo/MT9RlPkjcFiBHhFIPVGIgpTnExaAU7uSmCNjo8bsULpEWP6HkLLbOT8Adbx5EsyVURjaZi4/vIOEvVebH4UGf/6L8tL++bwa2t9EQ5xe9s1djnHdM02jD36DaVAysgKTiU8LBrMlRsuoQEd65c64YacgTC9DrOaxegpsv6HH1dtxRYF+c/oOsoBMJRhkHCaso86XbmcrOrsIiSNcez6SfC0iwgKbe+7igrfk=&pass_ticket=OSIPB7nq6SSZVLhngpm1u5DXYfJBj8iIZWas4pBV7NuwJfombDTJtR1CXDYefVpH&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/c6c9a925-ca00-4d43-a646-259e7276e314/c6c9a925-ca00-4d43-a646-259e7276e314/)