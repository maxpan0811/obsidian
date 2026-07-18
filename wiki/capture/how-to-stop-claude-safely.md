---
title: how-to-stop-claude-safely
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


用户问如何安全地阻止正在执行破坏性操作（如删除文件）的 Claude Code。

**停止方式优先级（从快到慢）：**

| 方式 | 延迟 | 说明 |
|------|------|------|
| **Ctrl+C** | 立即 | 中断当前 Bash 进程，`os.remove` 等循环当场终止 |
| `!pkill -f <script_name>` | ~1秒 | 从外部杀掉进程 |
| 发"停下" | 当前 Bash 调用结束后 | 工具调用是原子操作，循环跑完才收到消息 |
| 关窗口重开 | 几秒 | 会话自动恢复，但操作终止 |

**致命教训（2026-07-01）：** sync_favorites.py 的 checkpoint bug 导致 10,743 个 .md 文件被 `os.remove` 永久删除，原因是：
1. checkpoint 从 batch 141（offset 14100）恢复，只拉了最后 3,321 篇
2. reconcile 发现 DB 里 10,820 篇不在 batch → 误判为 orphan → 全删
3. 用户连发多条"停下来"但当前 Bash 调用未结束，无响应
4. 操作不可逆（`os.remove` 不走 Trash）

**事后措施：**
- 全局 deny 规则已加入 `~/.claude/settings.json`：`Bash(*os.remove*)`、`Bash(*os.unlink*)`、`Bash(*shutil.rmtree*)`
- `reconcile.py` 已改为 `shutil.move` 到 `~/.Trash`
- 记忆文件 `feedback-delete-move-to-trash.md` 记录规则

**Why：** "停下来"发了几次都没截停，因为 Bash 调用是原子操作。用 Ctrl+C 打断最可靠。

**How to apply:** 此记忆仅供回顾。实际防护已写入全局 deny 规则和 reconcile.py 代码修复。
