---
name: get笔记-cli-安装与认证笔记
type: source
tags: [Get笔记, 得到大脑, CLI, 认证, 笔记工具]
source_path: /Users/panbo/Obsidian/程序开发/Get笔记 CLI 安装与认证笔记.md
---

[摘要]

本文档记录了Get笔记（原称"得到大脑"）CLI工具的安装与认证过程。Get笔记CLI（npm包@getnote/cli v1.1.8）已通过`npm install -g @getnote/cli`全局安装，位置在`~/.npm-global/bin/getnote`。

认证流程使用OAuth设备码授权：CLI向Get笔记服务器请求设备码→输出浏览器授权URL和确认码→用户在浏览器完成登录授权→API Key自动保存，有效期1年（至2027-06-30）。实际认证结果成功。

功能限制：Get笔记OpenAPI仅对会员开放，免费账号无法通过CLI执行搜索、创建、读取笔记等操作，错误信息为"Error: OpenAPI仅对会员开放"。会员开通链接已记录。

Get笔记的相关skill已安装在`~/.claude/skills/getnote/`下，支持保存文本/链接/图片笔记、语义搜索、知识库管理和标签管理。Skill的description已补充"得到大脑"别名以便自动匹配触发。

经验总结：用户说的"得到大脑"即Get笔记，属同一产品不同称呼；CLI可以正常认证但API级别操作需要会员身份；建议需要CLI操作时先升级会员。

原文链接：/Users/panbo/Obsidian/程序开发/Get笔记 CLI 安装与认证笔记.md