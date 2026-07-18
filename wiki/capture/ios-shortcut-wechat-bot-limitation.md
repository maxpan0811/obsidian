---
title: ios-shortcut-wechat-bot-limitation
type: capture
tags: [auto-capture, reference]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


## iOS 快捷指令 + 微信 AI 机器人：能力边界

**场景**：从微信公众号文章复制链接，发送给微信内接入 Claude 的 AI 机器人。

### 核心限制

| 限制 | 原因 |
|------|------|
| ❌ 不能打开微信特定对话 | 微信不支持 `weixin://` scheme 带对话参数 |
| ❌ 不能向指定对话写入消息 | 微信未开放此 API 给 Shortcuts |
| ❌ Share Sheet 选不到 AI 机器人 | bot 不是普通联系人，不在分享列表 |
| ✅ 可以复制 URL 到剪贴板 | Shortcuts 基础能力 |
| ✅ 可以打开微信 app | `weixin://` URL scheme |

### 最优方案（半自动）

```
[Safari 分享菜单] 或 [公众号内...]
  → Shortcut 复制 URL 到剪贴板
  → 打开微信（weixin://）
  → 用户手动点到 bot 对话
  → 粘贴发送
```

### 关键认知

- 整个流程在微信**内部**发生（公众号→bot对话），Shortcuts 能做的很少
- 用户当前手动流程已经是：公众号文章→复制→切到 bot 对话→粘贴→发送
- **Shortcut 只能替代"复制"这一步**，其余都在微信内无法自动化
- 如果 bot 有外部 webhook/API，可以完全绕过微信 UI，这是真正的解法

### 适用场景判断

| 接收方类型 | 能否 Shortcut 自动发 |
|-----------|---------------------|
| 普通微信联系人 | ✅ Share Sheet 可选 |
| 微信群 | ✅ Share Sheet 可选 |
| 微信 AI 机器人 | ❌ 不在 Share Sheet |
| 企业微信机器人 | ✅ 有 webhook |
| iMessage 联系人 | ✅ 原生支持 |

**结论**：微信生态内，只有普通联系人和群可以被 Shortcuts 触达，bot/服务号/公众号均不可。
