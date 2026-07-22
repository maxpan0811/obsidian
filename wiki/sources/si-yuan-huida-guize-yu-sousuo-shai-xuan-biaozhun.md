---
name: si-yuan-huida-guize-yu-sousuo-shai-xuan-biaozhun
type: source
tags: [AI交互规范, 信息检索, 方法论, Claude配置]
source_path: /Users/panbo/Obsidian/程序开发/四源回答规则与搜索筛选标准.md
---

[摘要]
记录四源回答规则的建立过程和搜索筛选标准的确立。起因是Claude Code回答NeXTSTEP操作系统设计风格问题时100%仅使用了训练数据，用户要求以后所有信息类问题必须从四个来源并行查证并明确标注。

四源规则：Claude训练数据（🧠）、Obsidian Wiki知识库（📓）、Tavily搜索（🌐）、FAISS向量数据库（📊）。每个信息点必须标注来源，搜不到的要明确写"该来源无相关记录"。多个来源一致时标注"交叉验证一致"。闲聊/问候/简单确认不触发。

Tavily搜索采用四维过滤标准（按优先级降序）：来源权威度（Wikipedia/官方文档优先）、内容类型（教程/综述优先）、交叉验证（多源一致取最权威）、时效性（技术类3年内）。Tavily score仅作参考，不唯score论。

实践记录展示了四源回答NeXTSTEP问题的结果：训练数据有丰富知识、Wiki仅有一篇简引、Tavily搜索4篇交叉验证一致、FAISS无相关记录。交付动作包括写入Wiki页面、印象笔记剪藏4篇文章、保存规则文件和记忆文件。

原文链接: /Users/panbo/Obsidian/程序开发/四源回答规则与搜索筛选标准.md