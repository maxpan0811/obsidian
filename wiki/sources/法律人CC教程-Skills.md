---
title: 法律人的Claude Code教程（Skills）
type: source
created: 2026-06-08
updated: 2026-06-08
source_path: 印象笔记管理工具/法律人的Claude Code教程（六）（教不会我吃民法典！）：用Skills教Claude新本事.md
tags: [claude-code, tutorial, legal, series]
updated: 2026-06-27
updated: 2026-06-27
updated: 2026-06-27
updated: 2026-06-27
---

---
title: "法律人的Claude Code教程（六）（教不会我吃民法典！）：用Skills教Claude新本事"
source: evernote
type: note
export_date: 2026-06-26
guid: 5e1a37b5-ce06-47cd-9709-15a6ae031f4f
---

# 法律人的Claude Code教程（六）（教不会我吃民法典！）：用Skills教Claude新本事

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzkzMjg2NTcxNA==&mid=224748...](https://mp.weixin.qq.com/s?__biz=MzkzMjg2NTcxNA==&mid=2247485849&idx=1&sn=738935b09c0668910bf8d2d08317d041&chksm=c2547a44f523f352e3254b6408cf5f8aaa537ef8856b100ec02e9a251c1b21a652e7a1a78eee&cur_album_id=4406622888632549382&scene=189&ascene=3&devicetype=iOS26.4.1&version=18004725&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQi61r7iDjKRSXn8/Zu3i+0hLVAQIE97dBBAEAAAAAALBuCWo6WKUAAAAOpnltbLcz9gKNyK89dVj04yF39CwS32cqg0/tPfDIIVgopPFg+MZekKZri5csogQ2vrCeb1h3FWEZYRBpw8XPoncPjHo57oxj0mKKKFUkbw+8ffHxMclrZPMkdwpWoJPwRb1kFHu0FvgzXOUGPg4lAM+h21tibVDJhuNATqOJIKu1fbGSc+qqOrjcU4Npj8F5dtFCxzz3Uziw2zWuJaQ3+UdxnS0srKtIK95b32gBFq269z8HZl0QR6mND5C41w==&pass_ticket=x/O2PFTVenID1vLU1QRuXy/GiaHvx3jfFwtNfsgKtimIh1b4weMWBzBZukEgl4J5&wx_header=3)

# 法律人的Claude Code教程（六）（教不会我吃民法典！）：用Skills教Claude新本事

Original两眼一睁就是学呀 智律积成

经过了前五篇教程的学习，现在我们的 Claude Code 已经有了自己的"岗位说明书"（CLAUDE.md），也能使用外部工具（MCP）。是时候给它上点强度了。

回头看我们配置的 Claude Code，它确实可以完成一些简单工作。因为这些简单的工作，完全就是可以靠几百行的文字描述，就可以把整个工作给说清楚。

**但是我们实际上的工作会复杂的更多。**

---

## 一、为什么需要 Skill？

以合同审核为例。在教程四中，我们在 CLAUDE.md 里写了一个简单的合同审核流程。但实际场景中：

- **特定合同有特定审核要点** — 采购合同、服务合同、劳动合同，各有侧重
- **不同客户有不同标准** — 国企要合规、民企要效率、外企要严谨
- **文档格式要求不同** — 有的要 Word 修订模式，有的要批注，有的要单独出具意见书
- **需要调用外部资源** — 模板文件、检查清单、类似案例、背景知识
- **要验证准确性** — 主体资格查证、法条引用核对、格式规范检查

**所有这些东西**，以达成工作目的为核心，组成了你在某一方面的工作技能。

这东西就是 **Skill**。

---

## 二、先看一个实践：合同审核

想象一个比较通用的合同审核场景，就算是很通用的一个场景，也是没办法单靠 CLAUDE.md 就能够完成的。

我们会在文件夹里有一个待审合同 `样本合同.docx`。

### 我们希望 AI 做什么？

**第一步**：读取合同内容，生成一个业务流程图（可视化的图片，能直接打开看）

**第二步**：从基础条款、业务条款、法律条款三方面去审核，用 Word 批注的方式区分低中高风险，把风险内容批注出来

**第三步**：调用企业信息查询 MCP，核实主体名称的准确性和真实性

**第四步**：把合同内容、核心条款提取出来，形成简单的合同概要

### Skill 的作用

Skill 把前面提到的所有方面的工作流程、所依据的资源、所要用到的东西串联起来的流程全部放在一个文件夹里去实现。

当你真正要去审核合同的时候，就去调用这个 Skill，它就会按照既定的工作模式、资源等等，所有的东西全部去运行，最后给你稳定的输出。

你只需要一句话

![](attachments/48882019b2a3908d.png)

输出的结果就是这样的：

![](attachments/a4adc4ee6761aada.png)

其中业务流程图：

![](attachments/2a723708a294777c.png)

合同主体审核：

![](attachments/c9d251d545ecf963.png)

其他审核意见：

![](attachments/00e46e7cd2ba53d5.png)

这里不完全展开了。

我会提供我用的一些顺手的Skills，大家可以按需自取。

---

## 三、创建 Skills

为什么我们这篇文章的布置，不是说先了解 Skill 是什么、它的文档构成、里面的规则之类的？

因为整个 Skills 对于我们现阶段使用 Claude Code 以及使用其他的 AI 工具都是非常重要的，这个东西是非常流行和火爆的。而且它是我们真正意义上的工作经验和工作知识的沉淀。这样一个东西，理解是有一定难度的。

**我们先用官方的创建方式创建一个从我们法律人的视角去创建，过后再去理解。**

### 使用 skill-creator

在 Claude Code 中输入：

我想创建一个可以把法律文书转换成流程图的skill

skill-creator（本身就是一个skill）就 会引导你完成：

1. 询问 Skill 的用途
2. 询问具体的工作流程
3. 生成 SKILL.md 文件
4. 创建必要的目录结构

整个过程是交互式的，你只需要回答问题，不需要记住任何技术细节。

具体过程：

![](attachments/0c0b09bd9ad9390b.png)![](attachments/2a683ae9ff7dba26.png)![](attachments/4b20e687495e6a4e.png)![](attachments/3ed1f48debb5290d.png)![](attachments/da911ea6c005ba30.png)

---

## 四、使用 Skills

使用技能是非常核心的一环，因为它可以给你带来工作成果。但其实使用也是最简单的一环。

### 方式一：手动调用

通过一个斜杠指令就可以：

![](attachments/701b012818256820.png)

**特点**：精准、可控

### 方式二：自动调用

Claude 就是这么聪明，它可以识别到你当天的场景需要用什么，它就会自动调用什么。如果你不精准的话，很有可能是写的描述文件没有写对。

**示例**：

![](attachments/3c6dfe3e25ae97e6.png)

Claude 会自动匹配到 /legal-to-flowchart 并执行。

![](attachments/7203f71a521525b5.png)

---

## 五、简单了解 Skills

Skills 的创建、使用和优化是一个长期的过程，也是一个深刻的过程。这能够改变你的一些工作方式，显著提升你的工作效率。

我们刚刚使用 skill-creator 创建的过程里面就可以很清晰地看到它的整个结构。

### Skills 的最小结构

根据官方标准，一个 Skill 最简单的结构只需要：

skill-name/          ← Skill 文件夹（名称可自定义）
└── SKILL.md         ← 唯一必需的文件

### Skills 的完整结构

当 Skill 变复杂时，可以包含更多资源：

skill-name/                    ← Skill 根目录
├── SKILL.md                    ⭐ 必需：核心指令文件
│
├── assets/                     ← 可选：辅助资源文件
│   ├── template.md             ← 模板文件
│   ├── checklist.md            ← 检查清单
│   └── examples/               ← 示例
│       ├── good-case.md
│       └── bad-case.md
│
├── prompts/                    ← 可选：子提示词
│   ├── context.md              ← 背景知识
│   └── format.md               ← 输出格式
│
├── scripts/                    ← 可选：辅助脚本
│   └── helper.py               ← 可执行脚本
│
└── references/                 ← 可选：参考文档
    ├── civil-code.md           ← 法规文档
    └── standards.md            ← 标准规范

### Skills 的存放位置

官方规定 Skills 可以存放在四个位置：

| 位置 | 路径 | 适用范围 | 法律人用法 |
| --- | --- | --- | --- |
| **个人级** | `~/.claude/skills/<skill名>/` | 你的所有项目 | 个人通用模板 |
| **项目级** | `.claude/skills/<skill名>/` | 仅当前项目 | 特定案件的流程 |
| **插件级** | `<plugin>/skills/<skill名>/` | 启用插件的地方 | 律所标准模板（教程九讲） |
| **企业级** | 托管设置中 | 你的组织中的所有用户 | 律所统一分发（企业用户） |

### SKILL.md 的两部分

SKILL.md 文件包含两部分：

**1. Frontmatter（头部元数据）** - YAML 格式

yaml

---
name:legal-to-flowchart
description:将法律文书转换为Mermaid流程图。分析合同、判决书、法规条文、规章制度等法律文书中的程序性内容（履约流程、争议解决、审批程序、条件触发、权利义务流转等），自动生成结构化的Mermaidflowchart代码。支持直接输入文本、Markdown文件、PDF和DOCX格式。当用户要求"法律文书转流程图""合同转流程图""画流程图""生成流程图""法条可视化""flowchart""mermaid"，或提供法律文书要求可视化时使用此skill。
---

- `name`：Skill 的唯一标识名
- `description`：描述功能，Claude 据此自动匹配触发

![](attachments/b3e19d8b5355e5e6.png)

**2. Body（指令内容）** - Markdown 格式

markdown

# 法律文书转流程图
## 工作流程
1.\*\*读取文书\*\* → 确定文件格式，获取文本内容
2.\*\*识别流程要素\*\* → 提取步骤、条件、期限、主体、后果
3.\*\*构建逻辑结构\*\* → 确定节点关系、分支路径、回路
4.\*\*生成 Mermaid 代码\*\* → 输出 flowchart TD 格式
5.\*\*输出结果\*\* → 直接展示或写入 .md 文件

- 具体的工作步骤
- 只有被调用时才读取
- 可以很长很详细
- 但是，不要超过500行

### 为什么消耗很少 Token？

AI 启动时只会读取每个 Skill 的 **name** 和 **description**（大概 100 字左右）。

只有当 Skill 被调用时，才会读取 SKILL.md 的具体指令内容（Body 部分）。

这样设计的好处：

- **你可以有很多 Skills**（几十个甚至上百个）
- **不会占用太多上下文**
- **按需加载，效率很高**

---

## 六、如何开始你的 Skills

如果你想用好 AI 在这样一个时间点上，你肯定是要开始你的 Skills。

### 路线一：从零创建（自己动手）

根据自己的业务场景，使用 skill-creator 创建自己的 Skill。

然后在使用的过程当中，针对出现的问题，不断去优化提升，最终形成一个能够 80%-90% 匹配自己工作模式的 Skill。

我觉得这样一个匹配度就已经很夸张了。因为它意味着你在工作当中的时间消耗已经被压缩得很少了。你所要支付的只是说 AI 的一些费用，剩下的就可能是一些校对的工作。

### 路线二：站在别人的肩膀上（更推荐）

我更加推荐第二种方式。就是站在别人的肩膀上去做一些优化的工作。

**在哪里找？**

- GitHub 上搜索 `claude-code skills`
- 微信公众号上的开源分享
- 扣子等其他 AI 平台
- 法律人的社群

我相信很多法律人的工作和其他法律人的工作的重合度可能会很高。这种重合度就可以让你把别人的 Skills 拿来进行针对性的改造。

这个改造可能是一个相对较长的过程，也可能是一个反复的过程。但是这些努力都会是值得的。

**所以在优秀的例子里面去做一些尝试。这是我更加建议的一个路线。**

## 如何使用别人的 Skills

你在 GitHub 或其他地方找到了一个很棒的 Skill，怎么用它呢？这里主要介绍四种方式：

### 方式一：直接复制文件夹（最简单）

把别人的 Skill 文件夹直接放到你的 Skills 目录下：

![](attachments/86487f9c8542c7b1.png)

就可以开始用了

---

### 方式二：使用 CC Switch（推荐）

CC Switch 是一个桌面工具，可以管理 Claude Code 的配置、Skills、MCP 等。

**操作步骤**：

1. 打开 CC Switch
2. 进入 "Skills" 管理页面
3. 点击 "导入已有" 或 "发现技能"
4. 选择 Skill 来源（本地文件或 GitHub 仓库）
5. 安装skills

比如，你可以通过CC switch通过下图的方式安装我在文章开头演示的合同审核skill

![](attachments/26dee95e2a2078b6.png)![](attachments/0524eb6e16f59436.png)![](attachments/3348ee10bb6f0f58.png)

填写：https://github.com/zh-xx/legal-assistant-skills

![](attachments/9df293d82f6fc7b0.png)![](attachments/5cb3ffb1e78eb6d0.png)

大功告成！

接下来，就可以在Claude Code中使用了。

---

### 方式三：通过 Plugin 安装

有些优秀的 Skills 会打包成 Plugin，通过插件市场分发。

这里不展开啦。

---

### 方式四：直接让 Claude Code 学习

这个方式比较特别，你可以直接把别人的 Skill文件或地址发给 Claude Code：

**优点**：最省事，Claude 帮你搞定一切

![](attachments/7f6c62fc2b54202a.png)![](attachments/6cae12ecf4562824.png)

---

## 七、推荐一些 Skills 仓库/网址

这里整理了一些Skills 资源，推荐给大家：

### 官方资源

**Anthropic 官方 Skills 仓库**

- 地址：https://github.com/anthropics/skills
- 推荐理由：官方出品，质量有保证。包含一些通用型 Skills。适合了解官方的最佳实践。

### 社区资源

**Superpowers**

- 地址：https://github.com/obra/superpowers
- 推荐理由：由知名开发者创建的高质量 Skills 集合，包含多个实用型 Skills，代码质量高，文档清晰。

**SkillsMP**

- 地址：https://skillsmp.com/
- 推荐理由：Skills 分发平台，已有 36 万+ Skills，覆盖各个领域。可以像逛应用商店一样浏览和安装，"两眼一睁就是学"！

**JimLiu/baoyu-skills**

- 地址：https://github.com/JimLiu/baoyu-skills
- 推荐理由：包含多个实用型 Skills，比如文章配图、小红书图片生成等。适合有图文输出需求的场景。

### 法律人专用

**cat-xierluo/legal-skills**

- 地址：https://github.com/cat-xierluo/legal-skills
- 推荐理由：杨律出品，质量保证！专门针对法律工作场景设计，值得参考。

**zh-xx/legal-assistant-skills**（就是我在文章开头演示的那个）

- 地址：https://github.com/zh-xx/legal-assistant-skills
- 推荐理由：搭个便车。包含合同审核、法律文书转流程图等实用 Skills，可以直接用，也可以作为参考自己改造。

**法律 AI 相关社群**

- 各地的法律 AI 交流群
- 微信公众号上的开源分享
- 知乎、掘金等平台的技术文章

---

## 八、小结

### 核心概念

**Skill 是什么？**

Skill = 工作文件夹 + SKILL.md + 可选资源文件

它的核心价值是：工作经验和工作知识的沉淀。

### SKILL.md 的两个关键部分

1. **Frontmatter（头部元数据）**

- 包含 `name`（Skill 名称）和 `description`（功能描述）
- AI 读取这部分来决定何时调用这个 Skill

2. **Body（指令内容）**

- 具体的工作步骤和操作说明
- 只有当 Skill 被调用时才会被读取

### 为什么设计成这样？

AI 启动时只读取每个 Skill 的 name 和 description（大概 100 字左右），只有当 Skill 被调用时才读取完整的指令内容。这样你可以有很多 Skills（几十个甚至上百个），而不会占用太多上下文。

---

### 学习路径

**第一阶段**：使用 skill-creator 创建第一个 Skill

**第二阶段**：在实际使用中不断优化

**第三阶段**：尝试别人优秀的 Skills，改造适配自己的需求

**第四阶段**：形成自己的 Skills 体系

---

### 下一步预告

**Skill 是你主动调用的，Hook 是自动触发的。**

下一篇教程，我们会讲 **Hook** — 自动守护，让 Claude 在特定事件发生时自动执行某些操作，不需要你每次都去调用。

---

***💡 实践建议****：*

*今天就使用 skill-creator 创建你的第一个 Skill！从最简单的任务开始。*

*记住：Skills 是一个长期积累的过程，每次使用都是优化的机会。*

我也在持续分享更多法律 AI 的实践经验和工具，都会发布在公众号里。

如果你想一起交流、共建，

无论是使用、改进，还是自己动手做法律 AI 应用，都非常欢迎加入我们的群聊。
