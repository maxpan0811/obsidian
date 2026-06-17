---

name: claude-code-ch6-skills
type: source
tags: [claude-code, tutorial]
source_path: 印象笔记管理工具/法律人的Claude Code教程（六）（教不会我吃民法典！）：用Skills教Claude新本事.html

---

# 法律人的 Claude Code 教程（六）：用 Skills 教 Claude 新本事

> 来源：智律积成（微信公众号）

## 核心概念

- **Skill** = 工作文件夹 + SKILL.md + 可选资源文件，是工作经验和工作知识的沉淀
- 区别于 CLAUDE.md：CLAUDE.md 是全局规则，Skill 是特定场景的完整工作流

## SKILL.md 结构

- **Frontmatter**：`name`（唯一标识）+ `description`（描述，Claude据此自动匹配触发）
- **Body**：具体工作步骤，仅被调用时才加载（低 token 消耗）

## 存储位置

| 层级 | 路径 | 适用范围 |
|------|------|----------|
| 个人级 | `~/.claude/skills/<skill名>/` | 所有项目 |
| 项目级 | `.claude/skills/<skill名>/` | 当前项目 |
| 插件级 | `<plugin>/skills/<skill名>/` | 启用插件处 |
| 企业级 | 托管设置 | 组织全体用户 |

## 使用方式

- **手动**：输入 `/skill-name`
- **自动**：Claude 根据 description 自动匹配

## 推荐仓库

- anthropics/skills（官方）
- obra/superpowers
- skillsmp.com（36万+ Skills）
- cat-xierluo/legal-skills（杨律法律专用）
- zh-xx/legal-assistant-skills（合同审核、法律文书转流程图）

[Related: [[features/Skills]]]
