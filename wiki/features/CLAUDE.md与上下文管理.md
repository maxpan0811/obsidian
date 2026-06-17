---
name: CLAUDE.md与上下文管理
type: feature
tags: [claude-code, configuration]
---

# CLAUDE.md 与上下文管理

所属产品：[[products/Claude Code|Claude Code]]

## 记忆系统

| 层级 | 位置 | 作用域 | 共享 |
|------|------|--------|------|
| 用户级 | `~/.claude/CLAUDE.md` | 所有会话 | 仅自己 |
| 项目级 | `./CLAUDE.md` | 当前项目 | 团队（git） |
| 本地级 | `./CLAUDE.local.md` | 当前项目 | 仅自己（gitignore） |
| Auto Memory | `~/.claude/projects/<project>/memory/` | 当前项目 | 仅自己 |

## 大型代码库的分层策略

从子目录启动时，Claude 沿目录树向上查找 CLAUDE.md，逐层叠加加载：

```
repo/
├── CLAUDE.md                   # 全局约定：代码风格、提交规范、关键路径
├── services/payments/
│   └── CLAUDE.md               # 支付服务专属：测试命令、部署流程
└── infra/
    └── CLAUDE.md               # 基础设施专属：terraform 规范
```

- **根目录 CLAUDE.md**：只放真正全局的内容
- **子目录 CLAUDE.md**：只放局部的东西，专项知识放 Skills
- **原则**：内容越多噪声越大，性能下降。只放广泛适用的内容
- **推荐用法**：从子目录 `cd services/payments && claude` 启动，根级配置自动向上加载

### 排除噪音

在 `.claude/settings.json` 中配置（可提交进版本库，团队共享）：

```json
{
  "permissions": {
    "deny": [
      "Read(.next/**)", "Read(dist/**)", "Read(node_modules/**)",
      "Read(vendor/**)", "Read(generated/**)", "Read(**/*.pb.go)"
    ]
  }
}
```

### 代码库地图

根目录放一个简单 markdown 做索引，格式越简单越好。

## CLAUDE.md 写作四原则

1. 控制在 200 行以内
2. 结构清晰、分点列举
3. 指令要具体、可验证（"必须标注风险等级高/中/低"而非"注意风险"）
4. 避免矛盾规则

## 保持简洁

`@path` 语法导入外部文件：
```
@案件说明.md
@docs/合同审查清单.md
@~/.claude/个人工作习惯.md
```

## 上下文管理

| 命令 | 用途 |
|------|------|
| `/context` | 查看 token 用量 |
| `/compact` | 压缩上下文 |
| `/clear` | 清空重开 |
| `/resume` | 恢复历史会话 |

来源：[[sources/Claude Code教程-四-CLAUDE.md与上下文管理]] · [[sources/Claude Code大型代码库最佳实践]]
