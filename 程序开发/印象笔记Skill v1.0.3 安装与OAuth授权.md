# 印象笔记Skill v1.0.3 安装与对话记录

## 背景

2026-07-01，印象笔记发布了 Skill v1.0.3 更新，主要改进：
- 新增支持 Claude Code、Codex、Cursor 等开发工具
- 增强笔记写入能力，Markdown 格式完整保留

## 安装过程

从官方下载地址安装：`https://cdn.yinxiang.com/ai/yinxiang-skill-v1.0.3.zip`

### 安装到
`~/.claude/skills/evernote-yinxiang/`

### 备份
旧自定义 skill 已备份到 `~/.claude/skills/evernote-yinxiang-backup-2026-07-01/`

### 文件结构
```
evernote-yinxiang/
├── SKILL.md              — 主 skill 文件（7 个场景）
├── _meta.json            — 版本 1.0.3
├── agents/openai.yaml    — Codex/OpenClaw agent 配置
├── references/
│   └── api-commands.md   — 7 个 API 的 curl 命令参考
└── scripts/
    ├── _common.sh        — Token 加载公共脚本
    ├── create-note.sh    — 创建笔记（Markdown）
    ├── clip-url.sh       — 网页剪藏
    ├── list-notes.sh     — 列出最近笔记
    ├── search-notes.sh   — 搜索笔记
    ├── list-notebooks.sh — 列出笔记本
    ├── list-tags.sh      — 列出标签
    ├── get-note-detail.sh— 获取笔记详情
    └── save-token.sh     — 保存 OAuth Token
```

## OAuth 授权

新 skill 使用 OAuth 授权方式，替代旧的 Developer Token：
1. 访问 https://app.yinxiang.com/third/skills-oauth/
2. 完成授权，获取 `S=s` 开头的 Token
3. Token 保存到 `~/.config/yinxiang-skill/token`

Token 验证通过 ✓ — `listNoteBooks` API 返回 4 个笔记本。

## 7 个支持场景

| 场景 | 触发词 | API 端点 |
|------|--------|----------|
| 授权引导 | "授权印象笔记" | — |
| 创建笔记 | "记一下"、"帮我记录" | `createNoteFromMCP` (Markdown) |
| 网页剪藏 | URL + "保存"/"剪藏" | `clipAndSaveNote` |
| 列出笔记 | "列出笔记"、"有哪些笔记" | `searchNotesByFilter` |
| 搜索笔记 | "搜一下"、"搜下" | `searchNotesByFilter` (带 keyword) |
| 列出笔记本 | "有哪些笔记本" | `listNoteBooks` |
| 列出标签 | "有哪些标签" | `listTags` |

## 删除笔记调研

用户询问是否能删除笔记到垃圾箱，经过深入调研：

### 结论
官方 v1.0.3 未提供删除笔记端点。

### 尝试过的路径

| 路径 | 结果 |
|------|------|
| 旧 REST `/deleteNote` (Developer Token) | 返回 `{"code":1001,"message":"无效权限"}` |
| 旧 REST `/deleteNote` (OAuth Token) | 同样返回"无效权限" |
| 新 gRPC `deleteNoteFromMCP` | 只接受 protobuf (grpc-web)，不支持 JSON |
| AI 聊天笔记 `trashNote` / `deleteNote` (JSON) | 415 Unsupported Media Type |
| AI 聊天笔记 `trashNote` / `deleteNote` (protobuf) | 需要反编 proto schema |
| 旧 Thrift SDK `note_delete` | Python 3.14 兼容性问题（decode 属性错误） |

### 可用变通
- 在 Evernote 客户端手动删除
- 通过搜索 + 更新笔记内容"标记删除"

## 相关 Skill

当前印象笔记相关技能清单：
- **evernote-yinxiang** (AI Skill, v1.0.3，已更新) — 创建/搜索/剪藏
- **印象笔记管理工具** — Favorites 导出到 Obsidian 管线（旧 Developer Token，不受影响）
- **印象笔记文章保存** — 微信公众号文章保存到工作篮（旧 Developer Token，不受影响）
- **印象笔记去重** — 工作篮去重（旧 Developer Token，不受影响）
