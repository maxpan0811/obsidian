---
title: 给 Claude 添加永久记忆 2
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/给 Claude 添加永久记忆 2.md
tags: [evernote, impression, yinxiang]
---

# 给 Claude 添加永久记忆

---

来源：[打开原文](https://mp.weixin.qq.com/s/TRiygaw8lLTQllarjGp3aQ)

每一次和 Claude 开新对话，默认都是从一片空白开始。

它不记得你昨晚调试过什么，不记得你已经解释过三遍的代码风格，也不记得你认真写下来的项目决策。

过去几年，这种“无状态”几乎就是使用大语言模型必须接受的代价。

但到了 2025 年，并延续到 2026 年，Anthropic 开始悄悄拆掉这堵墙。

不是靠一个简单的“记忆开关”，而是用一套分层架构，把 Claude 的记忆能力一点点搭起来。问题是，大多数开发者到现在都还没有真正用满它。

不管你只是想让 Claude 别每次都重新问你的偏好，还是你在构建生产级 Agent，或者你的工程团队已经厌倦了反复上传上下文文件，这里都有一套适合你的记忆策略。

为什么Claude总是忘？但现在变了

大语言模型在设计上，本来就是无状态的。

每一次 API 调用，都是一张白纸。模型接收一段上下文窗口里的 token，然后生成回答。

不会存储。

不会延续。

不会天然保留上一轮之外的东西。

这种架构带来了很强的扩展性，也能保证隐私隔离。但对任何做长期项目的人来说，它的体验都很崩溃。

过去的解决办法很笨：

反复粘贴超长 system prompt。

每次上传参考文档。

把 Claude Projects 当成手动文件柜。

说到底，记忆这件事，还是人在干。

Anthropic 从 2025 年 9 月开始逐步解决这个问题。最早是 Team 和 Enterprise 计划，之后在 2025 年 10 月扩展到 Pro 和 Max 用户。到了 2026 年初，某种形式的记忆综合能力已经面向所有用户开放，只是最强的功能仍然留在付费层级里。

问题从来不是 Claude 不够聪明。

问题是，每一次新对话，它都像第一次见你。

接下来出现的，是一套四层记忆系统。每一层都对应不同使用场景、不同用户类型，以及不同控制程度。

我们一层一层看。

分享一个正版GPT5.5 目前 0.2 倍率，claude-code-4.8 0.4倍率,  关注公众号后，在后台回复：airealy 即可自动获取兑换码及使用方式。

Claude的四层记忆系统

第一层：所有用户可用

Chat Memory Synthesis

Claude 会自动读取你的对话历史，并提炼出一份关键事实摘要。

比如：

• 你的职业。

• 你常用的工具。

• 你的沟通风格。

• 你反复讨论的话题。

• 你明确表达过的偏好。

这份综合记忆大约每 24 小时更新一次，并会注入到每一个新的独立对话里。

你也可以不用等它自动更新。只要直接用自然语言告诉 Claude：

“请记住我以后更喜欢简洁的技术解释。”

它就能立刻更新记忆。

内置能力。 自动更新。

第二层：Pro / Max / Team / Enterprise

Project Memory Spaces

每一个 Claude Project 都有自己的独立记忆空间。

它和你的全局聊天记忆是分开的。

当你在某个项目里工作时，Claude 只会综合这个项目内的对话，不会把你的产品发布计划和客户项目混在一起，也不会把个人学习内容塞进工作上下文里。

Projects 还支持历史聊天搜索。你可以让 Claude 检索几周前的某个决策、数字、代码片段，或者之前讨论过的细节。

有范围。 相互隔离。

第三层：Claude Code用户

CLAUDE.md文件记忆

对 Claude Code 用户来说，CLAUDE.md 是最直接、最稳定的记忆方式。

它本质上是一个 markdown 文件，Claude Code 会在每次会话开始时读取它。

不需要检索。

不需要等待综合。

不靠模型“想不想起来”。

和综合记忆不同，CLAUDE.md 会被无条件加载。

你可以把它理解成项目宪法：那些不会随便被临时 prompt 推翻的规则。

它可以放在全局范围：

~/.claude/CLAUDE.md

也可以放在项目范围、目录范围，甚至作为 gitignore 掉的个人覆盖文件存在。

Claude Code v2.1.59+ 还提供 Auto Memory。它可以让 Claude 自己跨会话写入记忆笔记。

始终加载。 基于文件。

第四层：API / 开发者

API Memory Tool

API Memory Tool 给 Agent 开发者提供了一个客户端读写文件系统，路径是：

/memories

Claude 可以跨会话创建、读取、更新、删除记忆文件。

和更高层的消费级记忆功能不同，这个工具完全由你控制。

你拥有存储。

你定义 schema。

你决定什么该持久化。

它是构建真正有长期召回能力 AI 助手的底层原语，也非常适合和 context compaction 搭配，用在长时间运行的 Agent 工作流里。

可编程。 完全控制。

Chat Memory Synthesis到底怎么工作？

很多指南会简单说：

“Claude 会记住你。”

但这句话其实说得太粗了。

Claude 并不是把你的聊天记录原封不动存起来。

它更像是在你的历史对话上运行了一次抽取式总结，识别其中未来可能有用的信息：

• 模式。

• 偏好。

• 反复出现的话题。

• 事实背景。

重点是，普通问答不会被保留。

如果你只是问 Claude：

“解释一下光合作用。”

这段内容通常不会进入记忆综合。

但如果你告诉 Claude：

“我是机器学习工程师，主要用 PyTorch。”

这个事实就很可能被提炼并保留下来。

模型会判断什么值得记住。它更偏向保留有用的职业、个人和工作偏好，而不是短暂的一次性任务内容。

高级用法

不要傻等 24 小时的综合周期。

你可以直接告诉 Claude：

Remember that I prefer concise technical explanations with code examples rather than long prose.

也就是：

“记住，我更喜欢简洁的技术解释，最好带代码示例，而不是长篇大论。”

然后，你还可以这样验证它到底记住了什么：

Write out your memories of me verbatim, exactly as they appear.

当 Claude 引用过去对话里的内容时，它会显示一个可点击引用，链接回原始交流。

你也可以随时删除那段历史聊天。下一次记忆综合时，它就会被移除。

这里的隐私控制不是装饰。

你确实能管理 Claude 知道你什么。

怎么写一个真的有用的CLAUDE.md？

如果你用 Claude Code，CLAUDE.md 是回报最高的投资。

它不是锦上添花。

它直接决定 Claude 是把你的代码库当成陌生人的项目，还是像已经在里面工作了几个月一样理解它。

它的架构是分层的。

全局文件控制所有项目。 项目根目录文件控制整个仓库。 子目录文件控制代码库里的特定部分。

规则冲突时，越具体的文件优先级越高。

还有一个很重要的实践建议：

CLAUDE.md 最好控制在 200 行以内。

超过这个范围后，Claude 对指令的遵守程度会明显下降。

如果上下文越来越大，可以用 .claude/rules/ 目录做模块化规则管理。

~/.claude/CLAUDE.md：全局规则

# Global Claude Preferences

## Communication Style

Prefer concise technical answers over verbose explanations

Always include runnable code examples in Python responses

Use type hints in all Python function signatures

## Tooling Preferences

Python stack: PyTorch, Polars, FastAPI, Pydantic v2

Avoid pandas unless explicitly requested

Use uv for dependency management, not pip

## Code Style

Ruff for linting, Black for formatting (line length: 88)

Never generate placeholder comments like "# TODO: implement"

All functions must have docstrings

/project-root/CLAUDE.md：项目规则

# VidSynth AI — Project Context

## What This Is

RAG-powered video summarization service. FastAPI backend,

Qdrant vector store, Whisper transcription, LangChain pipeline.

## Architecture Decisions (do not reverse)

Use async throughout — no sync DB calls in route handlers

Chunk size: 512 tokens with 64-token overlap (tested, do not change)

Models live in /app/models/, never inline in routes

## Naming Conventions

Services: {name}\_service.py

Schemas: {name}\_schema.py

Use "workspace" not "project" in user-facing strings

## Current Sprint Focus

Implementing multi-language transcript support (Spanish, Hindi priority)

![](.evernote-content/F527E5DF-ADFD-45CA-AF38-E551A43FED4B/70993CE8-6364-480D-8882-A708C3FAB206.png)

API Memory Tool：给真正做Agent的开发者

如果你在 Claude API 上构建应用，Memory Tool 是目前最强的选择。

它和面向普通用户的综合记忆不一样。

API Memory Tool 是一个客户端文件系统。

数据存在哪里，由你控制。 结构怎么设计，由你决定。 什么时候读写，也由你的应用负责。

Claude 只会发起工具调用，比如 create、read、update、delete，然后你的应用在本地执行这些操作。

实际效果就是：

Agent 真的可以从上次中断的地方继续。

一个 coding agent，可以记住第一轮会话里做出的架构决策。

一个研究助手，可以持续积累它已经确认过的事实知识库。

一个项目管理 agent，可以跨几十次会话维护结构化进度日志。

Python：给长期运行Agent接入Memory Tool

import anthropic

import json

from pathlib import Path

client = anthropic.Anthropic()

MEMORY\_DIR = Path("/memories")

MEMORY\_DIR.mkdir(exist\_ok=True)

# Memory tool definition

memory\_tool = {

"name": "memory",

"description": "Read and write persistent memory files",

"input\_schema": {

"type": "object",

"properties": {

"command": {

"type": "string",

"enum": ["read", "create", "str\_replace", "insert", "delete"]

},

"path": {"type": "string"},

"file\_text": {"type": "string"},

},

"required": ["command", "path"]

}

}

def agent\_session(user\_message: str) -> str:

# Load existing memory as system context

memory\_context = ""

notes\_path = MEMORY\_DIR / "notes.md"

if notes\_path.exists():

memory\_context = notes\_path.read\_text()

response = client.messages.create(

model="claude-opus-4-5",

max\_tokens=2048,

system=f"""You are a persistent agent. Your memory from prior sessions:

{memory\_context}

Always check memory before starting. Update memory at session end.""",

tools=[memory\_tool],

messages=[{"role": "user", "content": user\_message}]

)

return response.content[0].text

架构提示

Memory Tool 很适合和 Anthropic 的 context compaction 搭配使用。

当上下文窗口快满时，compaction 会在服务端总结整段对话。

而 Memory Tool 能确保关键内容不会在压缩边界处丢失。

一个负责长上下文压缩。

一个负责跨会话持久化。

这两个系统本来就适合一起用。

不同记忆方式怎么选？

![](.evernote-content/F527E5DF-ADFD-45CA-AF38-E551A43FED4B/6075E081-583D-498B-AD97-C6C6D7FECCDB.png)

简单理解：

如果你是普通用户，用 Chat Memory Synthesis。

如果你在处理明确项目，用 Project Memory Spaces。

如果你写代码，用 CLAUDE.md。

如果你在构建自己的 Agent，用 API Memory Tool。

别把所有东西都塞进同一个地方。

记忆越分层，Claude 越稳定。

你必须知道的限制

Claude 的记忆系统很强，但它不是魔法盒子。

理解它的边界，才能设计出不撞墙的工作流。

第一，项目记忆和独立聊天记忆是隔离的。

如果你一会儿在 Claude Project 里工作，一会儿又在普通聊天里继续同一个项目，那么你的记忆上下文也会被拆开。

项目内的记忆不会自动流入普通聊天。

普通聊天里的综合记忆，也不会自动进入项目。

所以，同一个工作流最好选择一个固定位置。

第二，记忆更擅长保存偏好和事实，不擅长自动保存决策链。

Claude 可能会记住你偏好 PostgreSQL。

但它不会自动记住：

为什么这个项目选 PostgreSQL 而不是 MySQL。 当时 schema 长什么样。 你们权衡了哪些 trade-off。

这种重量级决策，必须明确写进 CLAUDE.md，或者放进 API Memory Tool。

第三，聊天搜索是付费功能。

免费用户可以用记忆综合，但不能搜索过去对话，精确找回之前某次交流。

Pro 及以上才有完整检索能力。

如果你是免费用户，又需要引用某个历史对话，只能手动找。

第四，记忆不会跨平台旅行。

Claude 的记忆存在 Anthropic 的服务里，只在 Claude 内部生效。

你切到 ChatGPT、Gemini 或 Cursor，就又从零开始。

不过，Anthropic 现在已经支持记忆导入和导出，也包括从 ChatGPT 和 Gemini 迁移的路径。

现在就该怎么做？

不要停留在概念上。

根据你的情况，直接照下面做。

如果你只是普通 Claude 用户：

打开 Settings → Capabilities，启用 memory。

然后在下一次会话开头花 5 分钟，明确告诉 Claude 你希望它永远知道的五件事：

• 你的工作。

• 你的沟通风格。

• 你的主要工具。

• 你正在进行的项目。

• 你的硬性约束。

比如：

不要写废话。 总是使用公制单位。 回答代码问题时给可运行示例。

这些信息会被综合并带到未来对话里。

如果你使用 Claude Code：

今天就创建一个全局文件：

~/.claude/CLAUDE.md

控制在 200 行以内。

写入你的语言偏好、技术栈、代码风格规则，以及任何你已经重复解释超过两次的东西。

启用 Auto Memory。

在 v2.1.59+ 中，它默认开启。

然后运行：

/memory

检查 Claude 已经积累了什么，并删掉过期内容。

如果你在 API 上构建应用：

在你的 Agent 里创建一个 /memories 目录。

会话开始时加载：

progress.md

preferences.md

会话结束时更新它们。

如果工作流要跨几十次会话，就搭配 context compaction 使用。

如果你需要更丰富的语义搜索，也可以考虑 claude-mem 这类方案。

CLAUDE.md 最大的好处，是它绕开了检索问题。

它不是 Claude “可能会想起来”的记忆。

它是每次会话启动时，Claude 一定会读的文件。

最后

值得退一步看一下 Anthropic 到底在构建什么。

很多 AI 助手把记忆当成一个单一功能：

要么有。

要么没有。

但 Claude 的方式是分层的。

每一层都在便利性和控制权之间做不同交换。

Synthesis 很省事，但不够精确。

CLAUDE.md 很精确，但需要手动维护。

API Tool 完全可控，但需要工程实现。

Anthropic 文档里的核心理念其实很简单：

让 AI 适应你，而不是让你反复适应 AI。

记忆最好的状态，不是让 Claude 看起来更聪明。

而是消除你每次开新会话都要付出的那笔“重新介绍自己”的税。

你是谁。 你在做什么。 你喜欢怎么工作。 这个项目有哪些不能改的规则。

这些东西每次都重新解释，其实非常浪费。

而且这种浪费积累得比你想象中快。

每一次重复说明。 每一次重新上传上下文。 每一句“就像我之前说过的”。

都是摩擦。

Claude 的记忆系统，如果四层都用对了，就能把这种摩擦几乎降到零。

你终于可以把时间花在真正的工作上。

[📎 在印象笔记中打开](evernote:///view/207087/s1/3584a574-a146-43bf-a822-1b8871086e04/3584a574-a146-43bf-a822-1b8871086e04/)
