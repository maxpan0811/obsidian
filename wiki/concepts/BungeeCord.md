---
name: BungeeCord
type: concept
category: technology
tags: [minecraft, server, proxy, bungeecord]
created: 2026-06-11
updated: 2026-06-11
---

# BungeeCord

Minecraft 多服务器代理端，将多个独立服务端连接成一个跨服网络，玩家通过单一入口访问不同子服务器。

## 配置要点

- **监听端口**: host: 0.0.0.0:25565（公开入口）
- **默认服务器**: default_server: lobby（新玩家入服第一个服务器）
- **服务器列表**: 每个子服务器指定不同端口（如 25566-25569）
- **安全**: spigot.yml 设置 bungeecord: true 防止直连；需额外验证机制防本地 BC 绕过

## 相关来源

- [[sources/BungeeCord跨服配置教程]]
