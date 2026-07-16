---
title: 装了Gemini CLI后，Claude Code我一个月没打开过
type: source
created: 2026-06-14
updated: 2026-06-14
source_path: 印象笔记管理工具/装了Gemini CLI后，Claude Code我一个月没打开过.md
tags: [印象笔记, AI/编程]
updated: 2026-06-27
updated: 2026-06-27
updated: 2026-06-27
updated: 2026-06-27
---

---
title: "装了Gemini CLI后，Claude Code我一个月没打开过"
source: evernote
type: note
export_date: 2026-06-27
guid: 79003b88-8274-417e-8d2d-1b9d5a40b838
---

# 装了Gemini CLI后，Claude Code我一个月没打开过

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzU2MTA2NTIyNg==&mid=224748...](https://mp.weixin.qq.com/s?__biz=MzU2MTA2NTIyNg==&mid=2247485174&idx=1&sn=b8c9c915f1e434b297c882b6306f8c32&chksm=fd62c26b69e31e1fb02642e3e54b2f3ac0ced0e95b3a87bc14ad8003d08ff0d5357e13a921c7&mpshare=1&scene=24&srcid=0608ALon9WiBTz72o7OWuseG&sharer_shareinfo=a65f71617ee74c10fefe00888aa3716d&sharer_shareinfo_first=a65f71617ee74c10fefe00888aa3716d&clicktime=1780890669&enterid=1780890669&ascene=14&devicetype=iOS26.5&version=18004a29&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ3DXoOi6jZqpr07ePfrqU6xLGAQIE97dBBAEAAAAAAJyyNmna+hEAAAAOpnltbLcz9gKNyK89dVj06N4EKB7USJxkyqqrrZUjHXLYTlMDHK8zXTBkwLFuag6Qzd9xQfsft1FlXPa7lrvF1EXtfYDk5y63dfkpOrOQkSB8pfVxpKrRPCxTJLONLPiujpGV4xPN+ddxcIchI4LLMbW04NrnMKR5AtGRQlEg/9/ko3XygpxWI9lr6lN4RlSoKEZf98hi7bejm2blh8g/dxAy1v9SVJE6Lx2DCEtAhA==&pass_ticket=FkB4tLBqrlr44Co9/w0bzXA9ntMRaH71LNgCzZnB8c7NbHJsiZvcAPSH4Ps6gr9j&wx_header=3)

# 装了Gemini CLI后，Claude Code我一个月没打开过

Original留明 AI硅基指南

👆 **「关注」·「星标」**，第一时间收到推送

![](attachments/9370d06960ec4ecc.jpg)

Claude Code挺好，但每月20美元。Gemini CLI直接免费，100万token上下文随便塞。一个用了一个月，我选后者。

---

## Claude Code vs Gemini CLI：差距没你想的那么大

先上个对比：

|  | Claude Code | Gemini CLI |
| --- | --- | --- |
| 价格 | 每月20美元 | 完全免费 |
| 上下文窗口 | 20万token | **100万token** |
| 模型 | Claude 3.7 | Gemini 3（稳定版） |
| 生态 | Anthropic闭源 | Google开源 |
| 安装方式 | 官方包 | **npm install** 一行 |

差距就两点：钱，和上下文。

100万token能做什么？直接丢一个中型代码库进去让它分析架构。同样东西塞给Claude Code，早超了。

Google AI CLI免费这件事，确实有诚意。Gemini 3现在稳定可用，核心功能该有的都有：代码生成、调试解释、Git操作、文件批量处理。

Claude Code功能深度确实更强，工具链也更完善。

但说实话：我每天真的需要那么深吗？

---

## 3分钟装好：npm install，然后没了

先确认电脑装了Node.js。没装的去 https://nodejs.org 装一个，装完打开终端：

# 全局安装 Gemini CLI
npm install -g @google/gemini-cli
# 验证安装
gemini --version

看到版本号就算成功。

接下来登录Google账号：

# 启动登录
gemini auth

浏览器会自动弹出来，跟着走就行。用自己的Google账号登录授权。

然后设一下默认模型：

# 使用 Gemini 3 稳定版
gemini config set model gemini-3.0-flash

整个过程，3分钟到顶了。

![](attachments/a8046f9ae32a1be7.jpg)

---

## 7个高频技巧，用过就回不去

### 1. 批量重命名文件：说句话的事

以前批量重命名要写Python脚本或者find命令。现在：

gemini "把这个文件夹下所有 .jpeg 改成 .jpg"

它先列出改动预览，你确认后才执行。

### 2. Git相关操作：解释PR比人快

gemini "帮我解释一下这个PR改了什么"

扔一个diff进去，直接给你中文总结。不用自己看几十行改动。

### 3. 代码调试：报错信息直接贴

gemini "这段报错是什么意思：paste your error here"

不用再复制去Google搜，终端里直接出结果。

### 4. 本地部署AI助手：直接调教

想本地部署AI助手做私有知识库问答？Gemini CLI配合MCP扩展可以连上各种数据源：

gemini "读取当前目录下的README，然后生成安装文档"

文档、代码、配置文件都可以直接扔给它处理。

### 5. 快速生成Shell命令

想写一个复杂的find命令？直接：

gemini "写一个命令，查找所有大于100MB的日志文件"

秒出，复制执行就行。

### 6. 批量处理图片元数据

gemini "把这个文件夹下所有图片重命名成 拍摄日期\_序号 格式"

整理照片的时候特别实用。

### 7. 一键生成项目README

gemini "根据这个项目结构生成README.md"

它会扫描整个目录，生成一个像样的说明文档。

![](attachments/3ead0a006140ff1f.jpg)

---

## 什么人适合，什么人不适合

**适合的人：**

- • 学生党：预算有限，免费是真香
- • 独立开发者：不需要重度功能，够用就行
- • 写脚本党：经常需要写Shell命令、处理文件的
- • AI工具尝鲜者：想体验Google生态的

**不适合的人：**

- • 需要深度代码重构：Claude Code工具链更成熟
- • 企业级项目管理：需要更强的审计和安全合规
- • 已经订阅Claude Pro：换过来意义不大

---

## 最后

Gemini CLI不是Claude Code的替代品，它是一个免费够用的选择。

预算充足、追求功能深度，Claude Code依然是更好的选择。想省点钱，或者需要一个本地AI助手处理日常杂活，Gemini CLI完全能打。

我的用法：Gemini CLI当日常主力，Claude Code留着处理复杂任务。一个月下来，20美元省了，效率没掉。

**去试试吧，npm install只要一行。**

如果觉得有用，点个**在看**和**赞**吧 👍

关注公众号「AI留明」，持续输出有价值的 AI 内容


---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzU2MTA2NTIyNg==&mid=2247485174&idx=1&sn=b8c9c915f1e434b297c882b6306f8c32&chksm=fd62c26b69e31e1fb02642e3e54b2f3ac0ced0e95b3a87bc14ad8003d08ff0d5357e13a921c7&mpshare=1&scene=24&srcid=0608ALon9WiBTz72o7OWuseG&sharer_shareinfo=a65f71617ee74c10fefe00888aa3716d&sharer_shareinfo_first=a65f71617ee74c10fefe00888aa3716d&clicktime=1780890669&enterid=1780890669&ascene=14&devicetype=iOS26.5&version=18004a29&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ3DXoOi6jZqpr07ePfrqU6xLGAQIE97dBBAEAAAAAAJyyNmna+hEAAAAOpnltbLcz9gKNyK89dVj06N4EKB7USJxkyqqrrZUjHXLYTlMDHK8zXTBkwLFuag6Qzd9xQfsft1FlXPa7lrvF1EXtfYDk5y63dfkpOrOQkSB8pfVxpKrRPCxTJLONLPiujpGV4xPN+ddxcIchI4LLMbW04NrnMKR5AtGRQlEg/9/ko3XygpxWI9lr6lN4RlSoKEZf98hi7bejm2blh8g/dxAy1v9SVJE6Lx2DCEtAhA==&pass_ticket=FkB4tLBqrlr44Co9/w0bzXA9ntMRaH71LNgCzZnB8c7NbHJsiZvcAPSH4Ps6gr9j&wx_header=3)
[📎 在印象笔记中打开](evernote:///view/207087/s1/79003b88-8274-417e-8d2d-1b9d5a40b838/79003b88-8274-417e-8d2d-1b9d5a40b838/)
