---
title: skills-audit-backup
type: capture
tags: [auto-capture, reference]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


# Skills 盘点与自定义技能备份

**盘点时间**：2026-06-12

## 架构梳理

| 目录 | 数量 | 角色 |
|------|------|------|
| `~/.claude/skills/` | 165 | 活跃 Skills 池 |
| `~/.agents/skills/` | 165 | 镜像池（28 个 symlink 自 .claude） |
| `~/.openclaw/workspace/peter/skills/` | 177 | OpenClaw 主角色 Peter 的源（唯一真实源头） |
| `~/.openclaw/workspace/skills/` | 79 | 通用技能（58 个与 Peter 完全重复，待清理） |
| `~/.openclaw/skills/` | 6 | 专用技能（getnote*, weread-official） |

## 已完成操作

### 1. 替换 self-improving-agent（2026-06-12）

- 旧版 `self-improving-agent-skill`（workspace 理论包装版）→ 删除
- 新版 `self-improving-agent`（Peter 实用版）→ 部署到 `.claude/skills/` + `.agents/skills/`
- Peter 版特色：`.learnings/LEARNINGS.md / ERRORS.md / FEATURE_REQUESTS.md` 三文件方案、OpenClaw 原生集成、Pattern-Key 重复检测、Hook 支持

### 2. 5 个自定义技能注册到 Peter 源（无备份风险消除）

| 技能 | 类型 | Peter 源已注册 |
|---|---|---|
| `delegate-task` | 轻量（纯 SKILL.md） | ✅ |
| `skill-discovery` | 轻量（纯 SKILL.md） | ✅ |
| `llm-wiki-karpathy` | 重型（含项目文件） | ✅ |
| `华程达成率分析工具` | 重型（6 个 Python 脚本） | ✅ |
| `四川省联盟包团分析工具` | 重型（3 个 Python 脚本） | ✅ |

所有 5 个技能已获得 OpenClaw 标准元数据（_meta.json + .clawhub/origin.json）。

## 待办

- P1：清理 `workspace/skills/` ✅ **已完成**
  - workspace/skills 从 79 → 12 → **0**（全部删除，包括 12 个独有项）
    - 过时/被替代：clawphone-wechat-control, wechat-automation, wechat-hot-trend, wechat-mp-cn, wechat-mp-reader
    - 重复/有替代：deepread-ocr, netease-mail, ocr-skill-test
    - 非 skill 文件：openclaw-wechat-mp-guide
    - 已替换：self-improving-agent-skill → self-improving-agent
    - 无用：slack-gif-creator, web-artifacts-builder
  - 清空了空的 document-skills/ 目录
  - 28 个 symlink 全部转为硬拷贝，`.claude/skills/` 自包含 ✅ **已完成**
  - 5 个自定义技能注册到 Peter 源（无备份风险消除）✅ **已完成**
- P2：docx 和 weread-analyzer 内容差异合并 ✅ **已完成**
- P3：评估未部署的 OpenClaw 技能 ✅ **已完成**
  - 已部署：openclaw-control-center, openclaw-tavily-search, openclaw-with-apple
  - 已删除（废弃）：processon-diagram-generator, processon-mindmap-generator, openclaw-backup-safe, openclaw-oa-operator, ai-pulse, ima-skills, simple-file-backup, simple-file-tree
  - 已部署：openclaw-control-center, openclaw-tavily-search, openclaw-with-apple, 腾讯ima-skills
- 自部署 Peter 源替换旧 workspace 版 self-improving-agent ✅ **已完成**

**Why:** 避免自定义技能损坏丢失（含生产级业务分析工具），统一 OpenClaw 和 Claude Code Skills 的源头。
**How to apply:** Peter 源是唯一真实来源。新增技能优先注册到 `~/.openclaw/workspace/peter/skills/`，然后同步到 `.claude/skills/` + `.agents/skills/`。
