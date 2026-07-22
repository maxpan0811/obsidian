---
name: agent-mail-cli-安装配置与邮件签名工具
type: source
tags: [邮件, AgentMail, CLI, 签名, 自动化]
source_path: /Users/panbo/Obsidian/程序开发/Agent Mail CLI 安装配置与邮件签名工具.md
---

[摘要]

本文档记录了Agent Mail CLI（@tencent-qqmail/agently-cli）的安装配置与邮件签名工具开发过程。安装步骤包括：npm全局安装CLI、可选安装skill、OAuth授权和验证。已验证邮箱为maxpan0811@agent.qq.com，权限范围包括读取别名、删除邮件、读取邮件和发送邮件。限制为每日发送50封、每小时200次请求、每分钟10次、单附件最大20MB。

邮件签名设计使用`ᓚᘏᗢ`（横躺猫咪小黑脸）作为视觉锚点，附带"邮件巡逻完毕，安稳着陆 ✦"文案，简洁但不啰嗦。

创建了agently-send助手脚本（位于`/Users/panbo/.claude/skills/agently-mail-tools/bin/agently-send`，软链至`~/.local/bin/agently-send`），自动在邮件正文末尾追加签名，保留agently-cli的两阶段确认机制，交互式提示确认发送。用法：`agently-send --to xxx@example.com --subject "标题" --body "正文"`。

关键规则：发正式邮件前必须用户确认——先展示完整邮件内容，等用户说"确认发送"后再投递，不经确认绝不直接发出。该规则已写入agently-mail-tools/SKILL.md的强制规则区。已成功发送测试邮件至myra.liu@trends.com.cn（笑话邮件）和panbo@hcgtravels.com（签名测试邮件）。

常用CLI命令包括查看用户信息（+me）、收件箱（message +list）、阅读邮件（message +read）、发送（message +send）、搜索（message +search）、回复（message +reply）、转发（message +forward）、移至废纸篓（message +trash）、下载附件（attachment +download）和OAuth管理（auth status/refresh）。

原文链接：/Users/panbo/Obsidian/程序开发/Agent Mail CLI 安装配置与邮件签名工具.md