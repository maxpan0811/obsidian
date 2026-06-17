---
title: Claude Code 在大型代码库里的最佳实践
type: source
created: 2026-06-08
updated: 2026-06-08
sources: [https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=224751...]
source_path: 印象笔记管理工具/Claude Code 在大型代码库里的最佳实践.html
tags: [claude-code, best-practice, monorepo, large-codebase, architecture]
---

## 一句话摘要

Anthropic 官方发布的 Claude Code 在企业级大型代码库（百万行 monorepo、遗留系统、多微服务仓库）中的精细化管理策略。

## 核心最佳实践

### 1. CLAUDE.md 分层，不要全堆根目录

```
repo/
├── CLAUDE.md                   # 全局约定：代码风格、提交规范、关键路径
├── services/payments/
│   └── CLAUDE.md               # 支付服务专属：测试命令、部署流程、特殊约束
└── infra/
    └── CLAUDE.md               # 基础设施专属：terraform 规范、云账号信息
```

- **根目录 CLAUDE.md**：只放真正全局的内容（提交规范、测试要求、关键路径标注）
- **子目录 CLAUDE.md**：只放局部的东西（测试命令、部署方式、注意事项）
- **原则**：只放广泛适用的内容，专项知识放 Skills。内容越多噪声越大，性能反而下降

### 2. 从子目录启动，不要从 repo 根目录启动

```bash
# ❌ 不推荐
cd ~/projects/myrepo && claude

# ✅ 推荐
cd ~/projects/myrepo/services/payments && claude
```

根级 CLAUDE.md 会自动向上加载，不会丢失全局约定。

### 3. 用 .ignore 排除噪音

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

配置在 `.claude/settings.json` 里提交进版本库，团队共享。

### 4. 写一份代码库地图

根目录放一个简单 markdown 当索引：

```markdown
# 代码库地图
- services/api/      — REST API 网关
- services/payments/ — 支付处理
- services/notify/   — 消息推送
```

## 适合谁

- 面对百万行 monorepo 的开发团队
- 几十个微服务分散在不同仓库的团队
- 需要精细化控制 Claude Code 上下文范围的人

## 相关页面

- [[products/Claude Code]]
- [[features/CLAUDE.md与上下文管理]]
- [[features/工作模式与权限]]
- [[sources/claude-code-best-practice-工作流指南]]
- [[sources/Claude Code七层约束-Hook-Skill-CLAUDE]]
