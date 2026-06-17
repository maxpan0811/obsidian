---
name: DNS over HTTPS (DoH)
type: concept
category: technology
tags: [dns, doh, security, privacy]
created: 2026-06-11
updated: 2026-06-11
---

# DNS over HTTPS (DoH)

利用 HTTPS/TLS 协议加密 DNS 查询流量，防止运营商或第三方窥探、篡改 DNS 解析结果。

## 相关技术

- **DoH** (DNS over HTTPS): 通过 HTTPS 协议传输 DNS 查询
- **DoT** (DNS over TLS): 通过 TLS 协议传输 DNS 查询
- **ECS** (EDNS Client Subnet): 帮助 CDN 返回更准确的节点

## 平台设置

| 平台 | 推荐方案 |
|:----|:---------|
| iOS | Cloudflare App (1.1.1.1) 或 Adguard |
| Android 9+ | 设置→私人 DNS |
| macOS/Win | Firefox 网络设置→启用基于 HTTPS 的 DNS |
| 全部平台 | DNScrypt 本地 DNS 客户端 |

## 相关来源

- [[sources/DNS安全设置-DoH-DoT指南]]
