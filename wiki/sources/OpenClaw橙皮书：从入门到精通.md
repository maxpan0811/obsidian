---
title: OpenClaw橙皮书：从入门到精通
type: source
created: 2026-06-27
updated: 2026-06-27
source_path: 微信读书管理工具/OpenClaw橙皮书从入门到精通.md
tags: [raw, md, reading-note, author-花叔]
---

# OpenClaw橙皮书：从入门到精通

**来源**: reading-note
**作者**: 花叔
**划线**: 25 条

**原始路径**: `微信读书管理工具/OpenClaw橙皮书从入门到精通.md`

---

# OpenClaw橙皮书：从入门到精通

**作者：** 花叔

**微信读书链接：** <https://weread.qq.com/web/bookDetail/3300199909>

---

## 划线笔记

### 09 设计哲学 Design Philosophy

> MCP（Model Context Protocol）是Anthropic提出的工具协议标准。几乎所有AI Agent框架都在集成MCP，但OpenClaw故意不支持

> 「CLI才是智能体连接世界的终极接口。」不需要为每个服务写一个集成，Agent只要能运行命令行，就能操作一切。

### 17 国内平台接入 Chinese Platforms

> 2026年3月22日，微信团队推出了ClawBot官方插件，这个问题终于有了正道解法。

> ClawBot的本质很简单：它不是一个新的龙虾产品，而是一条消息通道。你的微信通讯录里会多一个叫「微信ClawBot」的好友，你已有的任何OpenClaw实例（不管部署在哪里）都可以通过它和你的微信对话。[插图]1 安装ClawBot CLI在终端执行一条命令：npx -y @tencent-weixin/openclaw-weixin-cli@latest installnpm包在@tencent-weixin官方命名空间下，底层协议域名为ilinkai.weixin.qq.com，均为微信官方资产。

### 18 远程访问 Remote Access

> 安装Browser Relay扩展在Chrome网上应用店安装OpenClaw Browser Relay扩展（扩展ID: nglingapjinhecnfejdcpihlpneeadjp）。

> Dashboard Web UI（v2026.3.12全面升级）v2026.3.12 推出了Dashboard v2，控制台从功能型界面升级为完整的模块化管理中心：[插图]# Gateway 启动后默认可访问# 浏览器打开 http://127.0.0.1:18789openclaw gateway --port 18789 --verbose新增命令面板（Command Palette），按⌘K快速跳转。移动端新增底部标签栏，代替原来的悬浮按钮。

> v2026.3.13新增了最特别的一种「渠道」：直接附着到你正在使用的Chrome浏览器。Agent可以操控你已经登录的账号和页面——不需要另起账号，不需要API Key，直接接管你的浏览器会话。

### 20 ClawHub与技能生态 ClawHub & Skill Ecosystem

> ClawHub支持向量搜索，也就是说你可以用自然语言描述需求来搜索Skill，不必精确匹配名称。

> Vercel在2026年1月20日推出的Skills.sh是目前体量最大的跨平台技能市场。它的核心理念是：一个Skill应该能在任何Agent中运行，不绑定特定平台。

> ClawHub的质量问题非常严重。社区项目awesome-openclaw-skills（31.4K Stars）从13,729个技能中只精选了5,494个，剩下的大部分是垃圾、重复或低质量内容。安装任何第三方Skill前，务必查看源码

> 一个趋势正在形成：MCP负责「连接」（让Agent能调用外部工具），Skills负责「智慧」（教Agent如何高效使用工具）。两者互补而非竞争

> Skills本质上是结构化指令文件（SKILL.md），注入Agent的上下文窗口，提供特定领域的程序化知识。它坐在MCP之上：MCP解决「Agent怎么连工具」，Skills解决「Agent怎么用好工具」

### 21 热门Skills推荐 Top Skills

> 实用建议：不要一次性安装太多Skills。每个Skill都会增加system prompt的长度，占用上下文窗口。建议从Top 10中选择你真正需要的3-5个开始，用熟了再逐步扩展。

### 23 Skills安全 Skill Security

> 安全红线：拒绝任何要求你「下载zip文件」「执行shell脚本」「输入密码」的Skill。这些是恶意Skill最常见的行为模式。

> 关键认知：OpenClaw的Skill本质上是受信任代码。一旦安装，它就拥有和你的OpenClaw实例相同的权限。没有沙箱隔离，没有权限分级。这和npm生态早期面临的问题一模一样，但后果可能更严重，因为OpenClaw可以访问你的邮件、日历、消息和文件系统。

> 社区推出了开源安全工具SecureClaw，可以扫描已安装的Skills检查恶意内容。虽然不能100%防护，但能拦住已知的攻击模式。# 安装SecureClawnpm install -g secureclaw# 扫描已安装的skillssecureclaw scan ～/.openclaw/skills/

> 参考awesome-openclaw-skills项目（31.4K Stars）的精选列表，而不是直接在ClawHub上随意搜索。精选列表已经过滤掉了大量垃圾和恶意Skill。

> 社区推出了开源安全工具SecureClaw，可以扫描已安装的Skills检查恶意内容。虽然不能100%防护，但能拦住已知的攻击模式。

### 24 模型提供商总览 Provider Overview

> 设置models.mode: "merge"非常重要。它能保留所有内置Provider的同时叠加你的自定义配置。如果不设置，自定义配置会覆盖内置Provider。

> 设置models.mode: "merge"非常重要。它能保留所有内置Provider的同时叠加你的自定义配置。如果不设置，自定义配置会覆盖内置Provider。

### 26 国产模型配置 Chinese Models

> 相比按量付费的API，包月套餐的优势是成本可预期、无需管理API Key余额，尤其适合个人开发者和轻度到中度使用者。

### 30 成本控制 Cost Control

> 强烈建议所有用户都设置日预算上限。哪怕你不差钱，一个每日$5的上限也能在Agent进入循环推理时保护你的钱包

> • Skills的描述会注入system prompt，增加每次请求的输入token• 记忆系统（MEMORY.md+Daily Logs）会在每次请求中附带上下文• Agent 24/7运行，定时任务（cron）不断触发API调

### 33 vs Claude Code Comparison

> Claude Code管代码，OpenClaw管生活。两者是互补关系，不是替代关系。

### 附录A 常见问题FAQ Frequently Asked Questions

> 可以，而且是推荐用法。社区开发了openclaw-claude-code-skill，通过MCP协议桥接两者。OpenClaw负责消息平台接入和生活自动化，Claude Code负责编程任务。两者组合是2026年最完整的AI工作流。
