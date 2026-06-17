---

name: claude-code-ch3-modes-permissions
type: source
tags: [claude-code, tutorial]
source_path: 印象笔记管理工具/法律人的Claude Code教程（三）（教不会我吃民法典！）：工作模式、权限与配置管理.html

---

# 法律人的 Claude Code 教程（三）：工作模式、权限与配置管理

> 来源：智律积成（微信公众号）

## 三种工作模式

- **Default**：首次使用某类工具时弹出确认，安全稳妥
- **Plan**（`/plan`）：只读分析不动手，适合复杂任务前期规划
- **Auto Accept**（`Shift+Tab`）：自动接受文件编辑，适合批量处理

## 权限管理

- 三类工具确认机制：只读（免确认）、Bash（永久记忆）、文件编辑（仅当次会话）
- 四级配置：全局 / 全局本地 / 项目共享 / 项目本地
- allow/deny 白黑名单
- `--dangerously-skip-permissions` 极其危险，不可用于真实文件

## 实战场景

- 独立律师保护客户隐私：用 deny 禁止读取敏感文件
- 带助理模式：allow 放行文件操作，ask 管住 Bash 命令

[Related: [[features/工作模式与权限]]]
