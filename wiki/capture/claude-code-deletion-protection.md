---
title: claude-code-deletion-protection
type: capture
tags: [auto-capture, reference]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


# Claude Code 三层删除防护

## 三层结构

| 层 | 机制 | 文件 | 作用 |
|---|------|------|------|
| **模型层** | CLAUDE.md 引导 | `~/.claude/CLAUDE.md` | 让 Claude 生成阶段就写 `trash` 而非 `rm` |
| **工具层** | settings.json permissions.deny | `~/.claude/settings.json` | 执行引擎硬拦，模型绕不过 |
| **代码层** | PreToolUse hook | `~/.claude/hooks/block-dangerous.sh` | 补 deny 匹配不到的绕法 |

## 关键发现

### 1. Claude Code deny 通配比逐 flag 更简洁

Codex（Starlark `prefix_rule`）需要逐 flag 写：

```starlark
command_prefix_rule("rm", { ..., "allow_groups": [] })
command_prefix_rule("rmdir", { ... })
```

但 Claude Code 用的是 **glob 匹配工具调用字符串**，一行 `Bash(*rm *)` 就覆盖了所有变体（`rm -rf`/`sudo rm`/`command rm`/`/bin/rm`/`sh -c "rm..."`）。

### 2. PreToolUse hook 的 stdin 陷阱

**❌ 错误写法：**
```bash
tool_name=$(jq -r '.tool_name // empty')    # 读完 stdin
command=$(jq -r '.tool_input.command // empty')  # stdin 已空 → command=""
```

**✅ 正确写法：**
```bash
input=$(cat)  # 一次性读完 stdin
tool_name=$(echo "$input" | jq -r '.tool_name')
command=$(echo "$input" | jq -r '.tool_input.command')
```

### 3. grep 正则 \b 对 \-\- 不匹配

`--` 不是单词字符，`\b` 不匹配。用 `(\s|$)` 替代：
```bash
# ❌
grep -E 'git checkout --\b'
# ✅
grep -E 'git checkout --(\s|$)'
```

## 拦截清单

| 模式 | 拦截方式 |
|------|----------|
| `rm -rf` / `rm` / `rmdir` / `shred` / `unlink` | deny `Bash(*rm *)` + `*os.remove*` |
| `sudo rm` / `command rm` / `/bin/rm` | deny `*rm *` 隐式覆盖 |
| `find -delete` / `find -exec rm` | hook 第1条 |
| `git clean -fd` / `-fdx` | hook 第2条 |
| `git checkout --` | hook 第3条（注意 `--` 无 `\b`） |
| `git restore`（工作区） | hook 第4条；`git restore --staged` 放行 |

## 使用方式

```bash
# 删除一律用 trash
trash file.txt
trash dist/

# git 不可逆操作改用 stash
git stash        # 替代 git checkout -- / git restore
git stash pop    # 恢复
```

## 与 Codex 方案的对比
- [[20260715-codex-config-verbosity]]

**Why:** Claude Code 和 Codex 防护机制完全不同（Starlark prefix_rule vs glob deny + hook），不能套用同一写法。
**How to apply:** 以后给 Claude Code 配置防护时，用 `Bash(*rm *)` 一行，不用像 Codex 那样逐 flag 写。
