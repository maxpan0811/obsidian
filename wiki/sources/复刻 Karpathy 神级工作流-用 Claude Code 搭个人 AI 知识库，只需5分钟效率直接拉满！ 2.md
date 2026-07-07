---
title: 复刻 Karpathy 神级工作流：用 Claude Code 搭个人 AI 知识库，只需5分钟效率直接拉满！ 2
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/复刻 Karpathy 神级工作流：用 Claude Code 搭个人 AI 知识库，只需5分钟效率直接拉满！ 2.md
tags: [evernote, impression, yinxiang]
---

# 复刻 Karpathy 神级工作流：用 Claude Code 搭个人 AI 知识库，只需5分钟效率直接拉满！

---

Andre Karpathy 最近发布了一种使用 LLM 构建知识库的方法，这种方法相比传统方法有了巨大突破，因为 AI 可以持续记忆并帮你整理信息。小林我已经在自己的电脑上搭建了，使用claude code +obsidian,感觉很牛，分享给大家。

![](.evernote-content/E3A8B7AE-B407-451E-B4BB-45A1D6153A0E/03658749-7A48-4CB7-95EF-7FDEF55A2FCF.png)

这个核心流程是：输入原始数据 → 自动整理 → 建立关系 → 支持查询。同时还能发现知识缺口，并进行补充研究。传统 AI 对话是短暂的，记忆不会保留，而这种方式可以让知识持续积累。

整个搭建过程约 5 分钟，不需要复杂架构，只需要和claude code对话。

Karpathy 方案的灵魂，就是把「原始资料、处理过程、成品 Wiki」彻底分开，避免混乱。

这种方式在成本和 token 使用上更高效。有用户将 383 个文件和 100 多份会议记录整理为 Wiki，token 使用降低了 95%。此外，不需要复杂配置，只需让 Cloud Code 按照该思路实现即可。

Karpathy 提供了一个说明文档，解释了整体架构和原理，文档地址为：https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

下面是操作步骤：

首先下载 Obsidian，官网链接：https://obsidian.md/创建一个新的 vault文件夹，并选择保存位置。

![](.evernote-content/E3A8B7AE-B407-451E-B4BB-45A1D6153A0E/991AC3EF-6AAD-4B76-839E-D9C9D97CB8F4.jpg)

![](.evernote-content/E3A8B7AE-B407-451E-B4BB-45A1D6153A0E/61BD47DC-68F2-40CE-A385-63E98BD82520.png)

然后在 VS Code 中打开该文件夹，启动 Claude（通过终端运行）。

![](.evernote-content/E3A8B7AE-B407-451E-B4BB-45A1D6153A0E/0135E40B-C39E-4EF5-9473-E7680925E113.png)

![](.evernote-content/E3A8B7AE-B407-451E-B4BB-45A1D6153A0E/C81B9FBE-CABD-4CAC-8F55-9BD1C18E7541.png)

将 Karpathy 的文档网址复制到 Cloud Code 对话框中，让它自己学习。

https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

再补充一段指令，让其作为 LLM wiki agent，构建完整的第二大脑并进行引导。

![](.evernote-content/E3A8B7AE-B407-451E-B4BB-45A1D6153A0E/0FDCF8FF-5968-4157-8E9C-A4093EA11E03.png)

指令为：你现在是我的 LLM Wiki 代理。请将这个完整的想法文件实现为我的第二大脑。请一步一步引导我：创建包含完整规则的 CLAUDE.md 结构文件，设置 index.md 和 log.md，定义文件夹规范，并向我展示第一个数据导入（ingest）示例。从现在开始，所有交互都遵循该结构。

执行后，claude code 会帮你自动创建 raw 和 wiki 文件夹。

默认会生成 analysis、concepts、entities、sources 等结构，也可以根据需要调整。系统还会生成 index、log 和 claw.md。

接下来提示导入第一个数据源。

可以通过复制网页内容，或使用 Obsidian Web Clipper 插件将文章导入 vault，并存入 raw 文件夹。

插件安装地址：https://obsidian.md/clipper

![](.evernote-content/E3A8B7AE-B407-451E-B4BB-45A1D6153A0E/5F1DE484-5F1E-4746-8D01-FB6D5197F5B0.png)

导入后，通知 Claude Code 执行 ingest。

可以提前说明项目用途，例如个人知识库或研究项目。

系统会自动解析内容，并将其拆分为多个 Markdown 文件，同时建立关联。这些内容会形成结构化关系，而不是单一文件。系统可能会提出问题，以优化结构和重点。可以在 Graph View 中观察关系生成过程。

![](.evernote-content/E3A8B7AE-B407-451E-B4BB-45A1D6153A0E/9277C1C3-68FF-4CF7-AF42-AA7D4C6A1D23.png)

示例中生成了多个节点，包括人物、组织、AI 系统、概念和分析内容。整个过程自动完成结构构建和关系连接。

Karpathy 会对 Wiki 运行 LLM 健康检查，用于发现数据不一致，通过网络搜索补全缺失数据，挖掘潜在关联以生成新的文章候选等。这就保证了你的个人ai知识库始终有序。

你只要在 Claude Code 里说一句：帮我检查一下 Wiki 的健康状况。就可以做到了。

如果觉得这个教程有用就转发或者点赞。自己的AI知识库早一天搭就早一天开始积累。

我是小林，我自己也是慢慢从“用AI聊天”，走到“用AI干活”的。一开始也踩过很多坑。后来才发现很多机会，不在工具本身。而在你能不能用它持续做事。

如果你最近在折腾 Claude Code，这个工具真的值得试一下。

---

来源：<https://mp.weixin.qq.com/s/QJhXJwpnNTotroAMA-abZw>

[📎 在印象笔记中打开](evernote:///view/207087/s1/934cb44c-66ec-4899-b3f5-92540cb4cbf8/934cb44c-66ec-4899-b3f5-92540cb4cbf8/)
