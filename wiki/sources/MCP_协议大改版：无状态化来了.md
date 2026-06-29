---
title: MCP 协议大改版：无状态化来了
type: source
created: 2026-06-17
updated: 2026-06-17
source: 印象笔记管理工具
source_path: 印象笔记管理工具/MCP 协议大改版：无状态化来了.html
tags: [AI技术]
updated: 2026-06-27
---

---
title: "MCP 协议大改版：无状态化来了"
source: evernote
type: note
export_date: 2026-06-26
guid: bfb15625-ffdd-4036-8845-cfe0838a4dc6
---

# MCP 协议大改版：无状态化来了

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=Mzk0NjY0MTc0NA==&mid=224750...](https://mp.weixin.qq.com/s?__biz=Mzk0NjY0MTc0NA==&mid=2247500336&idx=1&sn=07ea1122d72df2ee9595d0e6280cda01&chksm=c20bcba6446898440fa8ce8ed0de07728c7b8c6f165b3a383a949ca007ad86f010652f851fba&scene=90&xtrack=1&req_id=1780013094977203&sessionid=1780012596&subscene=93&clicktime=1780013382&enterid=1780013382&flutter_pos=13&biz_enter_id=4&ranksessionid=1780013095&jumppath=20020_1780013209414,1104_1780013211380,20020_1780013231589,1104_1780013245792&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004935&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ3YqaiE8tX4xOqvTe8JEvuhLTAQIE97dBBAEAAAAAANGlEoGjw6QAAAAOpnltbLcz9gKNyK89dVj0t6xtF1Ag/hK/myputjkcLqR7Rlv5dENTE3lUvlBasMpnbe7ak1QnBBK3/a+rktIjDwyT5tZ5fd7M8p6MxgwL7nUWz9XNv72ffKOOKT6qFaPQIfxpSWZxWiV+xjZnOcNwSfJrNyL7WJQS+IdPn+EkfD2sAzlLHrlW/uojr1II2g3Vg8sh2YOfzYX81zWsw4BDef8VzN/1sIXIg7Wdv7eikumq6bhJdMlCVnbVcyA=&pass_ticket=ZMR4B6sKtQDU1LYt65tUbk3w4YBk2QQJMX9fJfaFth2CNfk3cS/JH4oy0lVljyLr&wx_header=3)

# MCP 协议大改版：无状态化来了

Original一叶扁舟 代码麻辣烫

MCP 刚发布了 `2026-07-28` 版本的 Release Candidate 。说实话，看完 changelog 我愣了一下——这不是小修小补，是把协议的地基给换了。

## 一句话说清楚这次改了什么

核心变化： MCP 协议层变成无状态的了。

什么意思？以前你部署一个远程 MCP Server ，需要 sticky session 、共享 session store 、网关做深度包检测。现在？普通的 round-robin 负载均衡就行，流量按 `Mcp-Method` header 路由，客户端可以缓存 `tools/list` 响应。

就这一个改动，运维复杂度直接砍掉一半。

## 以前有多痛苦

跟你说以前的流程。客户端要调一个 tool ，得先发 `initialize` 请求握手：

POST /mcp HTTP/1.1
{"jsonrpc":"2.0","id":1,"method":"initialize",
 "params":{"protocolVersion":"2025-11-25","capabilities":{},
           "clientInfo":{"name":"my-app","version":"1.0"}}}

服务端返回一个 `Mcp-Session-Id`，后面每个请求都得带着这个 ID 。客户端被钉死在发出 session 的那个实例上。

想水平扩展？要么搞 sticky routing ，要么所有实例共享一个 session store 。 Redis 集群、一致性哈希、故障转移——为了一个协议层的 session ，你得搭一套分布式基础设施。

这不是工程问题，是设计问题。协议本身不应该强制你为了横向扩展去搞这些东西。

## 现在一个请求搞定

新版本里，同样调一个 tool ：

POST /mcp HTTP/1.1
MCP-Protocol-Version: 2026-07-28
Mcp-Method: tools/call
Mcp-Name: search
{"jsonrpc":"2.0","id":1,"method":"tools/call",
"params":{"name":"search","arguments":{"q":"otters"},
           "\_meta":{"io.modelcontextprotocol/clientInfo":
             {"name":"my-app","version":"1.0"}}}}

握手没了。 Session 没了。协议版本、客户端信息全塞到每个请求的 `_meta` 里。任意一个 Server 实例都能处理任意一个请求。

六个 SEP （ Specification Enhancement Proposals ）配合完成了这件事。 SEP-2575 干掉了 initialize/initialized 握手， SEP-2567 移除了 `Mcp-Session-Id` header 。

但——等一下。

## "无状态不代表我的业务不需要状态"

对，协议层无状态不等于应用层不能有状态。

如果你的 Server 需要跨请求维护状态怎么办？做 HTTP API 一直在做的事：从 tool 里返回一个显式 handle （一个 `basket_id`、一个 `browser_id`），让 model 在后续调用里把它当普通参数传回来。

说白了，就是把状态从"传输层偷偷藏着"变成"让 model 明确看到并管理"。 model 可以跨 tool 组合这些 handle 、推理它们的关系、在步骤之间传递——这些是以前 session state 做不到的。

协议不再帮你管状态，但也不拦着你自己管。只是现在状态对 model 可见了，不再是藏在 header 里的暗箱操作。

## 运维侧的三个利好

除了无状态核心，有三个小改动对运维非常友好：

**1. Header 路由**

Streamable HTTP 现在强制要求 `Mcp-Method` 和 `Mcp-Name` header （ SEP-2243 ）。负载均衡器、网关、限流器可以直接按 header 路由，不用解包 JSON body 。如果 header 和 body 不一致， Server 直接拒绝。

**2. 客户端缓存**

List 和 resource read 响应现在带 `ttlMs` 和 `cacheScope`（ SEP-2549 ），对标 HTTP Cache-Control 。客户端精确知道 `tools/list` 响应能缓存多久、能不能跨用户共享。不用再靠一条 SSE 长连接来监听列表变化了。

**3. 分布式追踪**

`_meta` 里的 W3C Trace Context 传播现在写进规范了（ SEP-414 ）。`traceparent`、`tracestate`、`baggage` 的 key name 固定了。一个 trace 从 host 应用开始，穿过 client SDK 、 MCP Server 、下游服务，在 OpenTelemetry 后端里显示为一棵完整的 span tree 。

之前很多 SDK 已经在做了，只是 key name 各搞各的。现在统一了。

## Extensions 成年了

Extensions 在 `2025-11-25` 就有了，但没有正式流程。现在有了（ SEP-2133 ）：

•用反向域名 ID 标识

•通过 capabilities 里的 `extensions` map 协商

•住在各自的 `ext-*` 仓库里，有独立维护者

•版本和主规范独立演进

这个版本带了两个官方 Extension 。

**MCP Apps**（ SEP-1865 ）： Server 可以推送交互式 HTML UI ， Host 在沙箱 iframe 里渲染。 UI 和 Host 之间走的还是 JSON-RPC ，所有操作经过同一套审计和用户同意流程。

**Tasks 扩展**：从 `2025-11-25` 的实验性核心功能毕业为独立 Extension 。生命周期围绕无状态模型重新设计——Server 从 `tools/call` 返回一个 task handle ，客户端用 `tasks/get`、`tasks/update`、`tasks/cancel` 驱动。

注意：如果你之前对接了 `2025-11-25` 的实验性 Tasks API ，需要迁移。

## 授权加固：六个 SEP

OAuth 和 OIDC 相关的加固，说几个关键的：

•客户端必须验证 authorization response 上的 `iss` 参数（ SEP-2468 ），防 mix-up 攻击

•Dynamic Client Registration 时声明 `application_type`（ SEP-837 ），避免桌面/CLI 客户端被当成 web 应用注册然后 redirect URI 被拒

•注册凭据绑定到 issuer （ SEP-2352 ），资源在授权服务器间迁移时自动重新注册

这些不是那种"以后再说也行"的改动。 MCP 的部署模式是一个客户端连很多 Server ， mix-up 攻击面比一般 OAuth 场景大得多。

## 三个核心功能被 Deprecated 了

Roots 、 Sampling 、 Logging ，全标了 deprecated 。

| 功能 | 替代方案 |
| --- | --- |
| Roots | Tool 参数、 Resource URI 、 Server 配置 |
| Sampling | 直接对接 LLM provider API |
| Logging | stdio 用 stderr ，正式场景用 OpenTelemetry |

注意只是 deprecated ，不是 removed 。当前版本和一年内的后续版本都还能用。但别再新写了。

## 迁移时间线

Release Candidate 5 月 21 日锁定，最终规范 7 月 28 日发布。中间十周是给 SDK 维护者和客户端实现者验证用的——Tier 1 SDK 要在这窗口内出支持。

Breaking changes 是有的。但规范团队同时落地了正式的 deprecation policy （ SEP-2577 ）：每个功能有 Active → Deprecated → Removed 生命周期，从 deprecated 到可能被 removed 至少 12 个月。

他们说得很明确：这次 stateless rework 是那种需要 clean break 的基础性变更，以后不打算再来这种级别的了。

## 我的判断

这次改版方向是对的。 MCP 从一开始的设计就带着"本地 stdio 连接"的基因——有状态、单实例、不考虑扩展。当它开始被部署在远程 HTTP 上时，这个基因就变成了负担。

现在他们做了该做的事：认清 MCP 最终会跑在普通 HTTP 基础设施上，然后把协议层的设计对齐过来。

Tools schema 升级到完整 JSON Schema 2020-12 也是个好消息——支持 `oneOf`、`anyOf`、`allOf`、`$ref`，终于能表达复杂的输入输出了。

扔掉你的 session store ，检查一下你的 OAuth 实现，开始规划 Tasks API 迁移。 7 月 28 号见。
