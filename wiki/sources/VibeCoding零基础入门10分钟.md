---
title: Vibe Coding 零基础入门指南：10 分钟学会 AI 编程
type: source
created: 2026-06-08
updated: 2026-06-08
source_path: 印象笔记管理工具/Vibe Coding 零基础入门指南：10分钟学会AI编程.md
tags: [vibe-coding, ai-programming, tutorial]
updated: 2026-06-27
---

---
title: "Vibe Coding 零基础入门指南：10分钟学会AI编程"
source: evernote
type: note
export_date: 2026-06-27
guid: 6e3b9a2b-733f-4721-95bd-76ba73fe4ced
---

# Vibe Coding 零基础入门指南：10分钟学会AI编程

原文链接: <https://mp.weixin.qq.com/s?__biz=MjM5OTQ0MjU2Mw===2651699568=1=595539c36a9ed8c68457f9445307c4bf=bd7f4726d89e750b3e1fe0bd4f901d87c5e6d4980a60c490c9c7b13e4f4cd7bbe914dd906497=en-US=159#rd>

![](attachments/2afb46566a5d415d.jpg)

## 前言：什么是 Vibe Coding？

如果您听说过用自然语言编程或AI 自动编码，那么 **Vibe Coding** 就是这个概念的最新实现。

### **简单来说**

传统编程就像用外语写说明书——需要学习语法、记住命令。

**Vibe Coding 就像用中文说话，AI 自动给你翻译成代码**。

---

## 为什么要学 Vibe Coding？

### **对普通人的意义**

![](attachments/1103de2ef385eea7.jpg)

传统编程与 Vibe Coding 对比

| 传统编程 | Vibe Coding |
| --- | --- |
| 需要学 Python/JavaScript 等语言 | 用日常中文描述想法 |
| 学习周期：数月到数年 | 学习周期：几天到几周 |
| 门槛：高中级数学 + 逻辑思维 | 门槛：会用电脑就行 |
| 创意实现：70% 时间在调试 | 创意实现：90% 时间在创意 |

### **你可以用 Vibe Coding 做什么？**

✅ 写一个 AI 聊天机器人

✅ 创建一个个人网站

✅ 开发一个数据分析工具

✅ 制作一个自动化脚本

✅ 构建一个智能应用

**关键是**：你只需要描述你想要什么，AI 帮你写代码。

---

## 🚀 准备工作：6 个简单步骤

### **步骤 1：安装 Node.js（5 分钟）**

![](attachments/7f3ac9fcdb756a2c.jpg)

Vibe Coding 工具链图解

Node.js 是什么？简单说，它是让 JavaScript 代码能在您的电脑上运行的工具。

**Windows 用户**：

1. 1. 打开浏览器，访问 nodejs.org
2. 2. 点击绿色的 **LTS** 按钮（长期稳定版）
3. 3. 下载后，双击安装程序
4. 4. 一直点击Next和Install即可
5. 5. 安装完成后，重启电脑

**Mac 用户**：

1. 1. 访问 nodejs.org
2. 2. 点击绿色的 **LTS** 按钮
3. 3. 下载后，按照提示安装
4. 4. 安装完成后，重启电脑

![](attachments/61d99343a7311674.png)

**验证安装成功**：

- • Windows：打开 PowerShell（搜索 PowerShell）
- • Mac：打开 Terminal（搜索 Terminal）
- • 输入这行命令：`node --version`
- • 如果显示版本号（比如 `v20.10.0`），说明安装成功！

---

### **步骤 2：安装 Claude Code（3 分钟）**

**Claude Code 是什么？** 它是 Anthropic 提供的 AI 编程工具，是 Vibe Coding 的核心运行环境。

#### **安装步骤**

**第 1 部分：打开命令行工具**

- • **Windows**：搜索并打开 **PowerShell**
- • **Mac**：打开 **Terminal**

**第 2 部分：安装 Claude Code**

在命令行工具中，复制下面这行，粘贴后按 Enter：

npm install -g @anthropic-ai/claude-code

等待 1-2 分钟，您会看到类似这样的提示：

added XX packages

说明安装成功了！

**第 3 部分：验证安装**

在同一个命令行工具中，输入：

claude --version

如果显示版本号，说明 Claude Code 安装成功！

---

### **步骤 3：开通 MiniMax 会员（3 分钟）**

**MiniMax** 是提供 AI 能力的服务商。简单说，就像您需要电话卡才能打电话一样，Vibe Coding 需要 MiniMax 的服务。

#### **怎么开通？**

1. 1. **打开官网**：访问 www.minimaxi.com

![](attachments/0deb8350c06959e4.png)

1. 2. **注册账号**

- • 点击注册或Sign Up
- • 用邮箱或手机号注册
- • 完成邮箱验证

1. 3. **选择套餐**

   MiniMax 提供六种套餐（包括标准版和极速版）：

#### **标准版套餐**

| 套餐 | 价格 | 每月额度 | 特点 | 适合用途 |
| --- | --- | --- | --- | --- |
| **Starter** | ¥29/月 | 40 次 prompts/5小时 | 基础功能 | 初学者学习和试验 |
| **Plus** | ¥49/月 | 100 次 prompts/5小时 | 2.5 倍 Starter 额度 | 日常开发使用 |
| **Max** | ¥119/月 | 300 次 prompts/5小时 | 7.5 倍 Starter 额度 | 高级开发场景 |

#### **极速版套餐**（推荐！MiniMax-M2.5-highspeed 模型，3倍生成速度）

| 套餐 | 价格 | 每月额度 | 特点 | 适合用途 |
| --- | --- | --- | --- | --- |
| **Plus-极速版** | ¥98/月 | 100 次 prompts/5小时 | 100 TPS 极速推理 | 专业开发场景 |
| **Max-极速版** | ¥199/月 | 300 次 prompts/5小时 | 100 TPS 极速推理 | 高级开发场景 |
| **Ultra-极速版** | ¥899/月 | 2000 次 prompts/5小时 | 100 TPS 极速推理 | 硬核开发者 |

**推荐**：

- • 🎯 **初学者**：选择 **Starter** (¥29/月) 或 **Plus** (¥49/月)
- • ⚡ **追求速度**：选择 **Plus-极速版** (¥98/月)，3倍生成速度，专业开发更高效

1. 4. **支付方式**

✅ **完成后，您会看到一个控制面板。**

![](attachments/4e93a43059191fd2.png)

---

### **步骤 4：获取 API Key（2 分钟）**

**API Key 是什么？** 简单说，就像您的账户密码，Claude Code 需要用它来确认这是您的 MiniMax 账户。

#### **获取步骤**

1. 1. **登录 MiniMax 控制面板**

- • 访问 www.minimaxi.com/console
- • 用您刚才注册的账号登录

1. 2. **找到 API Key**

- • 左侧菜单 → API Keys 或 密钥管理
- • 点击创建新密钥
- • 复制显示的 **API Key**

2. 3. **保存这个 Key**

- • 打开记事本（Windows）或 TextEdit（Mac）
- • 粘贴 API Key
- • 保存为 `minimax-api-key.txt`
- • **重要**：不要分享这个密钥给任何人！

✅ **现在您已经有了 API Key，进入下一步。**

**注意：MiniMax的API key会分为常规充值的API和套餐的API，不要搞错，否则一直在用充值的余额。**

---

### **步骤 5：下载安装 CC-Switch 工具（3 分钟）**

**CC-Switch 是什么？** 它是一个开源工具，让您能轻松使用 Vibe Coding。可以理解为配置中心 —— 它帮您配置 MiniMax 的 API Key，连接 Claude Code 和 MiniMax。

#### **安装步骤**

**第 1 部分：下载安装程序**

1. 1. **访问 GitHub 官方仓库**：https://github.com/farion1231/cc-switch
2. 2. **选择对应版本下载**

- • **Windows**：下载 `cc-switch-windows-x64.exe` 或类似名称的 Windows 安装程序
- • **Mac**：下载 `cc-switch-macos-x64.dmg` 或 `cc-switch-macos-arm64.dmg`（M1/M2 芯片选择 arm64）
- • 在 GitHub 页面中，点击右侧的 **Releases** 或 **发行版**
- • 选择最新版本（Latest Release）
- • 根据您的系统选择对应的安装程序（不用下载 .zip 文件）：

**第 2 部分：安装程序**

**Windows 用户**：

1. 1. 找到下载的 `cc-switch-windows-x64.exe` 文件
2. 2. 双击该文件
3. 3. 按照安装向导完成安装（一直点Next或确定即可）
4. 4. 安装完成后，CC-Switch 会自动添加到系统路径

✅ **安装完成！**

**Mac 用户**：

1. 1. 找到下载的 `cc-switch-macos-x64.dmg` 或 `cc-switch-macos-arm64.dmg` 文件
2. 2. 双击打开 DMG 文件
3. 3. 将 CC-Switch 图标拖到 Applications（应用程序）文件夹中
4. 4. 等待复制完成

**如果 Mac 提示无法打开或安装不了**：

- • 这是 macOS 的安全机制
- • 打开 **系统设置** → **隐私与安全性**
- • 在页面下方找到 **允许以下来源的应用程序**
- • 点击 **允许** 按钮
- • 再次双击 CC-Switch 安装程序
- • 按照提示完成安装

✅ **安装完成！**

---

### **配置 API Key**

现在配置 MiniMax 的 API Key，让 CC-Switch 能够连接到您的 MiniMax 账户。非常简单，只需三步！

**步骤 1：打开 CC-Switch 应用**

- • **Windows**：在开始菜单中找到 CC-Switch，双击打开（或在桌面找到快捷方式）
- • **Mac**：在 Applications（应用程序）文件夹中找到 CC-Switch，双击打开

![](attachments/187d0d13b4b98071.png)

**步骤 2：添加 API Key**

1. 1. 在 CC-Switch 窗口中，点击右上角的 **+（加号）** 按钮
2. 2. 在弹出的菜单中，选择 **MiniMax** 或对应的模型名称
3. 3. 将您刚才保存的 API Key 粘贴到输入框中（例如：`abc123xyz789`）/注意：也必须是套餐的API
4. 4. 点击 **启用** 或 **确定** 按钮

✅ **配置完成！CC-Switch 现在已经连接到您的 MiniMax 账户了。**

![](attachments/565eb4a87497a7f3.png)

---

## 🚀 启动 Claude Code：进入 Vibe Coding 环境（1 分钟）

所有配置都完成了！现在我们要启动 Claude Code 来开始进行 Vibe Coding。

### **启动步骤**

打开命令行窗口，输入”claude“，按 Enter 键。

✅ **看到 Config saved successfully 就表示成功了！**

---

## 🚀 步骤 6：启动 Claude Code：进入 Vibe Coding 环境（1 分钟）

所有配置都完成了！现在我们要启动 Claude Code 来开始进行 Vibe Coding。

### **启动步骤**

**在命令行工具中输入**：

claude

然后按 Enter 键。

**您会看到这样的欢迎界面**：

![](attachments/5434692c3e68a94e.png)

✅ \*\*看到这个界面就说明成功了！您现在已经进入了 Claude Code 的 Vibe Coding 环境。\*\*
### \*\*环境说明\*\*
此时，您的电脑已经：
- ✅ 安装了 Claude Code（步骤 2）
- ✅ 开通了 MiniMax 账户（步骤 3）
- ✅ 配置了 API Key（步骤 5）
- ✅ 连接到 Claude Code 的 AI 编程环境
- ✅ 可以开始进行自然语言编程
现在您可以：
- 用中文自然语言描述您的编程需求
- Claude Code 会自动为您生成和调试代码
- 实时看到代码生成和执行的过程
---
## 🎉 开始 Vibe Coding：你的第一个 AI 程序
现在您已经进入了 Claude Code 环境，可以开始您的第一个 Vibe Coding 项目了！
### \*\*示例 1：创建一个简单的网页\*\*
在 Claude Code 中直接输入类似以下的文字需求即可：

创建一个简单的网页，有标题 '欢迎来到我的网站'，背景是蓝色，中间有一个红色的按钮说'点击我'

然后按 Enter。
AI 会自动为您生成 HTML 代码。您会看到类似这样的输出：
```html
html
  head
    title欢迎来到我的网站/title
  /head
  body style=background-color: blue;
    button style=color: red;点击我/button
  /body
/html

---

### **示例 2：创建一个数据处理脚本**

在 Claude Code 中输入：

写一个程序，读取一个 CSV 文件，计算每一列的平均值，然后输出结果

Claude Code 会自动为您生成 Python 或 JavaScript 代码，并且您可以看到实时的代码生成过程。

---

### **示例 3：创建一个 AI 聊天机器人**

在 Claude Code 中输入：

创建一个简单的聊天机器人，用户输入问题后，AI 回答。要求支持中文

Claude Code 会为您生成完整的聊天程序代码，您可以看到实时生成的过程。

---

## 💡 Vibe Coding 的核心技巧

### **技巧 1：描述得越详细，结果越好**

❌ 不好（在 Claude Code 中）：

写一个程序

✅ 更好：

写一个 Node.js 程序，接收用户输入，计算输入数字的阶乘，然后显示结果

### **技巧 2：一步步来，不要一口气要求太多**

❌ 不好：

创建一个完整的电商网站，包括支付、库存、用户系统、推荐算法

✅ 更好（第一步）：

创建一个简单的产品列表网页，显示产品名称、价格、图片

然后等 Claude Code 生成代码后，继续提出下一个要求：

给上面的产品列表添加一个搜索功能

### **技巧 3：充分利用自然语言的灵活性**

您可以：

- • 用比喻：「就像 Excel 里的 SUM 函数」
- • 用例子：「比如输入 5，输出 '五'」
- • 用修饰词：「简洁的设计」「深色主题」「移动友好」

---

## 🎓 学习路径：从入门到精通

### **第 1 周：熟悉基础**

**目标**：能用自然语言描述简单需求

**练习**：

- •创建一个显示 Hello World 的网页
- •创建一个计算器程序
- •创建一个简单的表单

**命令模板**：

直接在 Claude Code 中输入（启动后，输入 `claude` 进入）：

创建一个 [类型] 程序，功能是 [描述]

---

### **第 2-3 周：尝试实际项目**

**目标**：完成一个小项目（不超过 100 行代码）

**项目建议**：

- • 个人博客系统
- • 待办事项应用
- • 天气查询工具
- • 个人简历网站

**关键**：

- • 把大项目分成小步骤
- • 每个步骤在 Claude Code 中用自然语言描述
- • Claude Code 会实时显示生成过程，您可以看到代码如何演变

---

### **第 4 周+：融合多个模块**

**目标**：创建综合项目

**项目建议**：

- • 集成数据库的应用
- • 调用外部 API 的工具
- • 多页面网站
- • 自动化脚本

---

## ❓ 常见问题解答

### **Q1：我不会编程，能学 Vibe Coding 吗？**

**A**：完全可以！这就是 Vibe Coding 的核心优势。您甚至不需要理解代码长什么样，只需要能用中文描述您的想法。

---

### **Q2：生成的代码是否一定能运行？**

**A**：Claude Code 生成的代码 95% 以上都能直接运行。但如果有问题，您可以：

1. 1. 在 Claude Code 中告诉 AI 上面的代码有错或这个功能不对
2. 2. Claude Code 会实时修改代码
3. 3. 您可以看到修改过程，然后重新测试

---

### **Q3：我可以免费使用吗？**

**A**：MiniMax 的 Starter 套餐每月 ¥29，包含一定的免费额度。如果您只是学习，这个价格是合理的（比一杯咖啡贵一点点）。

---

### **Q4：生成的代码我可以商用吗？**

**A**：可以。生成的代码属于您。但建议阅读 MiniMax 的服务条款确保了解细节。

---

### **Q5：如果我的电脑是 Linux 系统呢？**

**A**：步骤完全相同。打开 Terminal，然后执行相同的命令即可。

---

## 🎯 快速开始清单

在开始之前，确保您已完成以下步骤：

- •✅ 安装了 Node.js（验证：`node --version` 显示版本号）
- •✅ 安装了 Claude Code（验证：`claude --version` 显示版本号）
- •✅ 注册了 MiniMax 账号并开通了会员
- •✅ 获取了 API Key 并保存在本地
- •✅ 从 GitHub 下载安装了 CC-Switch（https://github.com/farion1231/cc-switch）
- •✅ 验证了 CC-Switch 安装（Windows: `.\cc-switch.exe --version` 或 Mac: `./cc-switch --version`）
- •✅ 配置了 API Key（Windows: `.\cc-switch.exe config --set minimax.api-key=YOUR_KEY` 或 Mac: `./cc-switch config --set minimax.api-key=YOUR_KEY`）
- •✅ 启动了 Claude Code（输入 `claude` 并回车）

**全部完成？恭喜！您现在可以在 Claude Code 中开始 Vibe Coding 了！**

---

## 🚀 你的第一个真实项目

### **项目：创建一个日常提醒助手**

这是一个完全适合初学者的项目。

**步骤 1**：启动 Claude Code

claude

**步骤 2**：创建基础结构

在 Claude Code 中输入：

用 Node.js 创建一个程序，功能是存储用户的待办事项，并且能显示列表

看着 Claude Code 为您生成代码...

**步骤 3**：添加删除功能

在 Claude Code 中继续输入：

在上面的基础上，添加删除待办事项的功能

Claude Code 会为您更新代码...

**步骤 4**：保存到文件

最后，输入：

修改程序，使得待办事项能保存到一个文本文件中，程序重启后能读取

**完成！** 您现在有了一个实用的待办事项工具，整个过程中您只需要用中文描述需求，Claude Code 会自动为您完成所有编程工作。

---

## 📚 进阶资源

当您完成入门教程后，可以继续学习：

- • **Claude Code 官方文档**：Anthropic Claude Code Docs
- • **MiniMax 文档**：MiniMax 官方文档
- • **CC-Switch GitHub**：CC-Switch Repository
- • **社区讨论**：在 GitHub 的 Issues 中提问

---

## 💡 Claude Code 的优势

现在您已经完全启动了 Claude Code 的 Vibe Coding 环境，您会发现它的强大之处：

✨ **实时代码生成** - 看着代码实时生成，理解每一步是怎样完成的

✨ **自然语言交互** - 用中文表达您的需求，不需要任何编程知识

✨ **智能调试** - 如果代码有问题，直接告诉 Claude，它会修改代码

✨ **项目可视化** - 您可以看到整个项目的结构和演变过程

---

## 💬 最后的话

**Vibe Coding 代表了编程的未来**——

- • 不再需要记住复杂的语法
- • 不再需要花数年学习编程基础
- • 任何有想法的人都可以将其变成现实

这不是说编程的重要性降低了。相反，**创意和问题解决的能力变得更重要了**。

如果您有一个想法，现在您有了工具来实现它。

**现在就开始吧！** 🎉

---

**遇到问题？**

- • 检查 API Key 是否正确配置
- • 确保网络连接正常
- • 尝试用更详细的描述重新 prompt
- • 在官方社区提问

**祝您使用愉快！**

---

*本教程针对 2026 年 2 月的最新 Vibe Coding 工具链编写。由于技术快速发展，某些步骤可能需要更新。*


---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MjM5OTQ0MjU2Mw==&mid=2651699568&idx=1&sn=595539c36a9ed8c68457f9445307c4bf&chksm=bd7f4726d89e750b3e1fe0bd4f901d87c5e6d4980a60c490c9c7b13e4f4cd7bbe914dd906497&app_lang=en-US&app_status_bar_height=159#rd)
[📎 在印象笔记中打开](evernote:///view/207087/s1/6e3b9a2b-733f-4721-95bd-76ba73fe4ced/6e3b9a2b-733f-4721-95bd-76ba73fe4ced/)
