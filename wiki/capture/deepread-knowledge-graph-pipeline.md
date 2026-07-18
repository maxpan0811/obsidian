---
title: deepread-knowledge-graph-pipeline
type: capture
tags: [auto-capture, reference]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


# DeepRead：用 AI 把书变成可交互知识图谱

从 GitHub 项目 [liujuntao123/DeepRead](https://github.com/liujuntao123/DeepRead) 和其网站 [deepread.aizhi.site](https://deepread.aizhi.site) 学到的经验。

## 管线的四步流程

1. **格式转换** — EPUB 用 BookTools 一键转换，PDF 用 MinerU 智能解析，TXT 直读
2. **AI 宏观分析** — Gemini 识别全书结构，自动划分维度（人物/事件/概念/地点/组织），生成任务清单
3. **批量填充** — AI 按任务清单逐个生成知识节点，同时自动建立双向链接（如"孙悟空"→"如意金箍棒""花果山""大闹天宫"）
4. **发布上线** — Obsidian 本地使用（图谱视图+笔记），或 Quartz 部署 GitHub Pages

核心工具组合：**Gemini CLI + BookTools**。一个人+几小时可完成一本书。

## 分类体系设计（可迁移）

不是固定模板，每本书自定义维度。以《西游记》为例分了7个维度：
- 主要人物、神佛仙圣、妖魔鬼怪、法宝兵器、地名仙府、重要事件、八十一难
- 192 个节点覆盖原著几乎全部关键信息

## 值得借鉴的工程思路

- **先规划再填充**（宏观分析 → 任务清单 → 批量生成），比一锅炖更可控
- **Markdown 文件存储** — 人类可读、可手动编辑、可版本控制、可被 Obsidian 消费
- **双向链接自动建立** — 生成节点时就关联相关节点，而非事后手动链接
- **人机分工清晰** — AI 做提取和结构化，人做校验和补充

## 对我当前工作的启发

LLM Wiki 知识库管线和 DeepRead 思路相通，可借鉴：

1. 双向链接自动建立机制可在 wiki pipeline 里复用——ingest 时识别实体间关系
2. "先规划再填充"比当前 wiki ingest 的一锅炖更可控——先做全书结构分析，再分批填充
3. 可以给 wiki query 管线增加知识图谱视图，不只是文本搜索
4. 格式转换阶段选成熟工具（BookTools/MinerU）而非造轮子——印证了"先确认 repo 里有没有现成的"原则

## 局限认识到（预防踩坑）

- 技术门槛：需要 CLI 工具和大模型配置——后续若做类似工具可优先考虑降低门槛
- AI 准确率：复杂人物关系和隐喻可能漏掉——节点用 Markdown 可手动修正的设计是对的
- 覆盖面只有 26 本——但 26 本经典书已经足够建立公信力
