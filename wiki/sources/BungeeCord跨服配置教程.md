---
title: BungeeCord跨服配置教程
type: source
created: 2026-06-11
updated: 2026-06-11
source_path: 印象笔记管理工具/BungeeCord跨服配置教程 - 联机教程 - Minecraft(我的世界)中文论坛 -.html
tags: [minecraft, bungeecord, server, tutorial]
---

**摘要**: Minecraft BungeeCord 跨服配置教程，讲解如何将多个 MC 服务端通过 BungeeCord 连接成跨服网络。包括准备条件（服务器/VPS/带宽/内存）、BungeeCord 运行配置（config.yml 详解）、多服务端关联（server1-4 示例端口 25566-25569）、安全防护（防止绕过登录服务器）。

## 核心观点

- BungeeCord 是独立服务端（不是插件），作为多服务器中转站
- config.yml 配置：监听端口(host)、默认服务器(default_server)、服务器列表(servers)
- 安全要点：spigot.yml 的 bungeecord: true 仅限制直连，本地搭 BC 可绕过

## 相关页面

- [[concepts/BungeeCord]]
