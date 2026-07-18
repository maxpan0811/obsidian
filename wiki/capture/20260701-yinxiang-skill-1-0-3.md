---
title: 20260701-yinxiang-skill-1-0-3
type: capture
tags: [auto-capture, project]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


# 印象笔记Skill v1.0.3 安装记录

## 什么变了

### 安装来源
- **官方 ZIP**: https://cdn.yinxiang.com/ai/yinxiang-skill-v1.0.3.zip
- **安装到**: ~/.claude/skills/evernote-yinxiang/

### 认证方式
- **旧**: Developer Token（A=en-devtoken），存 .env 文件
- **新**: OAuth 授权，Token 存 ~/.config/yinxiang-skill/token 或环境变量 YX_AUTH_TOKEN
- OAuth 地址: https://app.yinxiang.com/third/skills-oauth/
- Token 前缀相同，但 A= 部分从 en-devtoken 变为 yinxiang-skill

### API 变更
- 创建笔记: createNoteFromMCP（原生 Markdown 支持）
- 网页剪藏: clipAndSaveNote 新增
- 搜索/列表: searchNotesByFilter / listNoteBooks / listTags / getNoteDetail
- 删除笔记: 官方 v1.0.3 未提供删除端点。旧 REST /deleteNote 返回无效权限

### 架构变化
- 旧: Python Thrift SDK（yinxiang.py），Python 3.14 兼容性问题
- 新: Shell 脚本 + curl（scripts/*.sh），轻量无依赖

## 已验证
- listNoteBooks API 返回 4 个笔记本 ✓
- 新 OAuth Token 可用 ✓
- 旧 Developer Token 备份到 evernote-yinxiang-backup-2026-07-01/ ✓
