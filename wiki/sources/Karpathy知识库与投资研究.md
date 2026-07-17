---

name: Karpathy知识库与投资研究
type: source
tags: [LLM Wiki, Karpathy, 投资研究, 知识复利]
source_path: RAW/PDF/最新研究报告.pdf

---


来源：微信公众号"曾敏敏老师"

原文链接：https://mp.weixin.qq.com/s?chksm=c05c743bf72bfd2d7336649aea74272...

## 核心内容

Andrej Karpathy（前特斯拉AI总监、OpenAI联创）在 GitHub 发布 `llm-wiki.md`（75行 markdown，一周 15000 star）。

### RAG vs LLM Wiki

- **RAG**：每次临时翻资料回答你，没有积累（像每次出门现查地图）
- **LLM Wiki**：持续维护知识库，新信息进来就整理，旧信息自动更新（像有一个助手每天更新你的私人地图）

### 三层架构拆解（投资视角）

1. **原始资料** — 财报、研报、新闻、电话会纪要（只读）
2. **知识库(Wiki)** — 公司档案页、主题页、策略页、论据页，互相链接。新财报不只是更新一个页面，而是沿着链接同步更新所有相关页面
3. **规则文件** — 告诉AI怎么维护知识库的说明书

### 三种核心操作

- **Ingest（入库）** — 读资料 → 提取

<!-- [摘要] 规则提取，如需全文请查看 vault 原始笔记 -->