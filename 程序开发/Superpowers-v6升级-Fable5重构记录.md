---
date: 2026-07-09
tags: [superpowers, fable5, codex-plugin, upgrade, skill-framework]
---

# Superpowers v6.1.1 升级记录：Fable 5 重构

## 背景

Superpowers v6 用 Fable 5 完全重构。核心优化：构建耗时降约 50%，token 消耗降约 60%。

文章原文提到的关键改进：
- Fable 5 内置 autoresearch loop，用 Opus 当协调者，批量跑 25 组以上的实验，持续 36 小时，烧掉约 650 美元的算力
- 发现反直觉结论：精简 reviewer 指令让输出压缩 41% 且判断质量不受影响；去掉流程步骤旁白再省 54% 且零方差
- 按任务复杂度动态分配模型（简单任务 haiku，复杂自动拒绝降级）
- 去 Claude Code 方言化，技能描述用通用表达
- 新增 Kimi Code、Pi、Antigravity 三个 harness
- brainstorming 可视化配套功能换了更安全的实现方式

## 升级前状态

| 组件 | 版本 | 来源 |
|------|------|------|
| Codex 官方市场版 | v5.1.3 | openai-api-curated |
| git repo | v5.1.0 | github.com/obra/superpowers |
| 旧 Claude CLI 插件 | v5.1.0 | obra/superpowers-marketplace |

## 升级过程

```bash
# 1. 拉取最新代码
cd ~/.superpowers && git pull

# 2. 移除旧 Codex 官方市场版
codex plugin remove superpowers@openai-api-curated

# 3. 添加本地 git repo 为 marketplace 源
codex plugin marketplace add /Users/panbo/.superpowers

# 4. 安装 v6.1.1
codex plugin add superpowers@superpowers-dev
```

## 升级后状态

| 组件 | 版本 | 来源 |
|------|------|------|
| Codex 插件 | v6.1.1, installed, enabled | superpowers-dev（本地 repo） |
| git repo | v6.1.1 | ~/.superpowers/ |
| 运行时路径 | `~/.codex/.tmp/plugins/plugins/superpowers/skills/` | Codex 缓存 |
| 技能数 | 14 | brainstorming, subagent-driven-development, executing-plans 等 |

## 后续更新

```bash
cd ~/.superpowers && git pull
codex plugin add superpowers@superpowers-dev  # 会自动重新安装到最新版本
```

## 关键补记：skills 软链接

Codex 插件安装（`codex plugin add`）仅安装到 `~/.codex/plugins/` 插件缓存，但 **CLI agent 读取的技能来自 `~/.codex/skills/`**，而该目录下全是到 `~/.claude/skills/` 的软链接。

所以插件安装后还需要：

```bash
# 1. 替换 .claude/skills/ 下的旧版技能目录为 v6.1.1 的软链接
for d in ~/.superpowers/skills/*/; do
  name=$(basename "$d")
  rm -rf ~/.claude/skills/"$name"
  ln -s "$d" ~/.claude/skills/"$name"
done

# 2. 在 .codex/skills/ 下创建对应软链接（指向 .claude/skills/）
for d in ~/.superpowers/skills/*/; do
  name=$(basename "$d")
  ln -s ~/.claude/skills/"$name" ~/.codex/skills/"$name"
done
```

最终链路：

```
.codex/skills/brainstorming → .claude/skills/brainstorming → .superpowers/skills/brainstorming/
```

共 14 个技能，下次会话生效。

## 验证清单

| 验证项 | 结果 |
|--------|------|
| `task-reviewer-prompt.md` 合并 | ✅ 替代旧 spec-reviewer-prompt + code-quality-reviewer-prompt |
| 参考文件修剪 | ✅ 仅保留 codex-tools.md / pi-tools.md / antigravity-tools.md |
| using-superpowers 引导压缩 | ✅ 3063 字节 |
| 14 个技能软链接 | ✅ 两端（claude + codex）全部就位 |
| 本地 marketplace | ✅ superpowers-dev，来源 ~/.superpowers |
