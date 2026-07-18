---
title: network-escalation-rule
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


用户明确要求：以后每次需要网络访问时（Thrift API、gh CLI、GitHub API、任何远程服务），
必须主动使用 sandbox_permissions: require_escalated 请求提权。

涉及场景：印象笔记 Thrift API、GitHub CLI、任何 API/远程服务。
