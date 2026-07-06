# Get笔记 CLI 安装与认证

> 日期：2026-06-30
> 标签：#Get笔记 #得到大脑 #CLI #认证

## 背景

用户询问能否对接"得到大脑"的 CLI，经确认后发现"得到大脑"即 **Get笔记**（getnote CLI），目前已通过 npm 全局安装。

## 安装情况

- 工具名：`getnote` CLI（npm 包：`@getnote/cli`）
- 版本：v1.1.8
- 位置：`~/.npm-global/bin/getnote`
- 安装方式：`npm install -g @getnote/cli`

## 认证流程

```bash
getnote auth login
```

认证方式为 OAuth 设备码授权：
1. CLI 向 Get笔记服务器请求设备码
2. 输出浏览器授权 URL 和确认码
3. 用户在浏览器中打开 URL、确认码完成授权
4. API Key 自动保存，有效期 1 年

实际认证结果：✅ 成功，API Key 有效期至 2027-06-30

## 功能限制

⚠️ **Get笔记 OpenAPI 仅对会员开放**。免费账号无法通过 CLI 执行搜索、创建、读取笔记等操作。

错误信息：
```
Error: OpenAPI 仅对会员开放
```

会员开通链接：https://www.biji.com/checkout?product_alias=6AydVpYeKl

## 已有 Skill 覆盖

Get笔记的相关 skill 已安装在 `~/.claude/skills/getnote/` 下，支持以下功能：
- 保存文本/链接/图片笔记
- 语义搜索
- 知识库管理
- 标签管理

Skill 的 description 已补充"得到大脑"别名，方便后续会话自动匹配触发。

## 经验

- 用户说的"得到大脑"= Get笔记，属同一产品不同称呼
- CLI 可以正常认证，但 API 级别操作需要会员身份
- 建议需要 CLI 操作时先升级会员
