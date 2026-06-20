---
title: MCP 协议大改版：无状态化来了
type: source
created: 2026-06-17
updated: 2026-06-17
source: 印象笔记管理工具
source_path: 印象笔记管理工具/MCP 协议大改版：无状态化来了.html
tags: [AI技术]
---

# MCP 协议大改版：无状态化来了

原文链接: https://mp.weixin.qq.com/s?__biz=Mzk0NjY0MTc0NA==&mid=224750...

MCP 协议大改版：无状态化来了Original一叶扁舟 代码麻辣烫 
MCP 刚发布了 2026-07-28 版本的 Release Candidate 。说实话，看完 changelog 我愣了一下——这不是小修小补，是把协议的地基给换了。

核心变化： MCP 协议层变成无状态的了。

什么意思？以前你部署一个远程 MCP Server ，需要 sticky session 、共享 session store 、网关做深度包检测。现在？普通的 round-robin 负载均衡就行，流量按 Mcp-Method header 路由，客户端可以缓存 tools/list 响应。

跟你说以前的流程。客户端要调一个 tool ，得先发 initialize 请求握手：

POST /mcp HTTP/1.1
{"jsonrpc":"2.0","id":1,"method":"initialize",
 "params":{"protocolVersion":"2025-11-25","capabilities":{},
           "clientInfo":{"name":"my-app","version":"1.0"}}}

服务端返回一个 Mcp-Session-Id，后面每个请求都得带着这个 ID 。客户端被钉死在发出 session 的那个实例上。

想水平扩展？要么搞 sticky routing ，要么所有实例共享一个 session store 。 Redis 集群、一致性哈希、故障转移——为了一个协议层的 session ，你得搭一套分布式基础设施。

这不是工程问题，是设计问题。协议本身不应该强制你为了横向扩展去搞这些东西。

POST /mcp HTTP/1.1
MCP-Protocol-Version: 2026-07-28
Mcp-Method: tools/call
Mcp-Name: search

{"jsonrpc":"2.0","id":1,"method":"tools/call",
 "params":{"name":"search","arguments":{"q":"otters"},
           "_meta":{"io.modelcontextprotocol/clientInfo":
             {"name":"my-app","version":"1.0"}}}}

握手没了。 Session 没了。协议版本、客户端信息全塞到每个请求的 _meta 里。任意一个 Server 实例都能处理任意一个请求。

六个 SEP （ Specification Enhancement Proposals ）配合完成了这件事。 SEP-2575 干掉了 initialize/initialized 握手， SEP-2567 移除了 Mcp-Session-Id header 。

如果你的 Server 需要跨请求维护状态怎么办？做 HTTP API 一直在做的事：从 tool 里返回一个显式 handle （一个 basket_id、一个 browser_id），让 model 在后续调用里把它当普通参数传回来。

...说白了，就是把状态从"传输层偷偷藏着"变成"让 model 明确看到并管理"。 model 可以跨 tool 
