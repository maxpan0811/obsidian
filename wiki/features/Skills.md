---
name: Skills
type: feature
tags: [claude-code, skills]
---

# Skills

所属产品：[[products/Claude Code|Claude Code]]

## 概述

Skill = 工作文件夹 + SKILL.md + 可选资源文件。核心价值在于 **工作经验和工作知识的沉淀**。

区别于 CLAUDE.md：CLAUDE.md 是全局规则（岗位说明书），Skill 是特定场景的完整工作流（招式手册）。

## SKILL.md 结构

```yaml
---
name: legal-to-flowchart    # 唯一标识名
description: 将法律文书转换为Mermaid流程图...  # Claude据此自动匹配
---

# 工作流程
1. **读取文书** → 确定文件格式
2. **识别流程要素** → 提取步骤、条件、期限
3. **构建逻辑结构** → 确定节点关系
4. **生成 Mermaid 代码**
5. **输出结果**
```

- Frontmatter（name + description）：AI 启动时仅加载这部分，约 100 字
- Body（指令内容）：仅被调用时才加载，低 token 消耗

## 创建方式

1. **skill-creator**（内置 Skill）：说"我想创建一个可以把法律文书转换成流程图的 skill"，交互式完成
2. **手动创建**：在 skills 目录下创建文件夹 + SKILL.md

## 使用方式

- **手动**：输入 `/<skill-name>`
- **自动**：Claude 根据 description 自动匹配触发

## 学习路径

1. 使用 skill-creator 创建第一个 Skill
2. 在实际使用中不断优化
3. 尝试别人的优秀 Skills，改造适配
4. 形成自己的 Skills 体系

来源：[[sources/Claude Code教程-六-Skills]]
