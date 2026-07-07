---
title: 1亿Token，花谁的钱？五大国内模型价格清单+选型指南
type: source
created: 2026-06-14
updated: 2026-06-14
source_path: 印象笔记管理工具/1亿Token，花谁的钱？五大国内模型价格清单+选型指南.md
tags: [印象笔记, 其他]
updated: 2026-06-27
---

---
title: "1亿Token，花谁的钱？五大国内模型价格清单+选型指南"
source: evernote
type: note
export_date: 2026-06-26
guid: 51623a31-25c8-4e8b-ae11-cc2a85f66ce3
---

# 1亿Token，花谁的钱？五大国内模型价格清单+选型指南

来源：[打开原文](https://mp.weixin.qq.com/s/dBNQ3hYfbOjfuLRH1cvKqQ)

用量大了之后，API 费用是笔正经账。

最近把 DeepSeek、智谱、MiniMax、Kimi、小米五家主流国产模型的 API 价格摸了一遍，核心问题就一个：用 DeepSeek 按量计费，还是买小米的 Token Plan？

结论先说：

没有一家国内厂商有"固定月费 + 71亿Tokens"的套餐——这个模式目前只有 MiniMax Ultra版有（469元/月）。国内的话，DeepSeek V4-Flash 是按量计费里性价比最高的。

下面直接上数字。

各家模型特点：选谁要看场景

数据来源：OpenRouter 月度调用量排行榜 openrouter.ai/rankings?view=month[1]（2026年5月），以及各厂商官方发布。

OpenRouter 月度调用量排行（2026年5月）

| 排行 | 模型 | 月调用量 | 备注 |
| --- | --- | --- | --- |
| 🥇 1 | DeepSeek V4 Flash | 7.99T tokens | 2026年4月24日上线，首月即登顶 |
| 🥈 2 | 腾讯混元 Hy3 Preview | 7T tokens | 国产闭源 |
| 🥉 3 | Claude Sonnet 4.6 | 6.65T tokens | 编程工作流首选 |
| 4 | Claude Opus 4.7 | 6.07T tokens | 复杂推理旗舰 |
| 5 | Gemini 3 Flash Preview | 4.57T tokens | 多模态+长上下文 |
| 6 | Kimi K2.6 | 5.45T tokens | 国产开源，Agent 长程任务主力 |
| 7 | DeepSeek V3.2 | 4.06T tokens | 角色扮演/批量任务 |
| 8 | DeepSeek V4-Pro | 3.4T tokens | 编程性价比首选 |
| 9 | MiniMax M2.7 | 2.95T tokens | 国产开源，编程性价比 |
| 10 | MiniMax M2.5 | — | 编程价值 pick |

说明：排行数据来自 OpenRouter 全球第三方调用统计，2026年5月。国产模型已占据月调用量前10中的5席。

DeepSeek V4 —— 极致性价比

一句话：V4-Flash ¥1/M 输入、¥2/M 输出，SWE-bench 80.6%，重度代码用量首选，直接走官方 API。

GLM-5.1（智谱）—— 中文场景首选

一句话：中文理解最准，SWE-bench Pro 全球前三。中文业务代码首选，API 比 DeepSeek 贵但省心。

Kimi K2.6 —— 开源可微调

一句话：开源可本地部署，超长上下文，中文长文本处理强。灵活定制，但纯编程性价比不如 DeepSeek V4-Pro。

MiniMax M3 —— 多模态 + Agent 全能

一句话：多模态最强（语音/视频/音乐），Agent 编排国产第一。Token Plan 用量透明，多工具并发首选。

小米 MiMo —— 轻量场景最低价

一句话：V2.5 输入 ¥1/M，简单任务够用。编程能力不如 DeepSeek V4。

阿里 Qwen3.6 —— 企业生态优先

一句话：开源生态最活跃，阿里云存量用户首选。企业集成最稳，单独比价优势不明显。

先说一个重要前提：Token Plan 不是每家都有

| 厂商 | 是否有 Token/Coding Plan | 备注 |
| --- | --- | --- |
| DeepSeek | ❌ 没有 | 只有按量计费 |
| MiniMax（国内版） | ✅ 有 Token Plan | ¥49/¥119/¥469 三档，仅限编程工具 |
| Kimi（月之暗面） | ✅ 有 Code Plan（¥49起） | 按 prompt 次数，API 只能按量充值 |
| 小米（MiMo） | ✅ 有 Token Plan | 4档套餐，人民币计价，仅限编程工具 |
| 智谱（ChatGLM） | ✅ 有 Coding Plan | ¥49/¥149/¥469 三档，限编程工具 |

注意：MiniMax、小米、智谱的 Token/Coding Plan 都只能在各自的编程工具（OpenClaw、Claude Code、MiniMax Code 等）里用，不能当普通 API 调用。Kimi Code Plan 是按 prompt 次数计量，不是 token 总量。

各厂商旗舰模型 API 价格（人民币/百万Tokens）

⚠️ 以下数据均来自各厂商官方文档（2026年6月），实际价格以官网为准。  
Kimi K2.6 因官方文档未渲染出价格，标注为"待确认"。

DeepSeek

| 模型 | 上下文 | 输入（未命中缓存） | 输出 | 缓存命中 |
| --- | --- | --- | --- | --- |
| V4-Flash | 1M | ¥1 | ¥2 | ¥0.02 |
| V4-Pro | 1M | ¥3 | ¥6 | ¥0.025 |

来源：api-docs.deepseek.com[2]

MiniMax

| 模型 | 上下文 | 输入 | 输出 | 缓存读 |
| --- | --- | --- | --- | --- |
| M3（≤512K） | 1M | ¥4.2 | ¥8.4 | ¥0.84 |
| M3（512K~1M） | 1M | ¥33.6 | ¥8.4 | — |
| M2.7 | 256K | ¥2.1 | ¥8.4 | ¥0.42 |
| M2.7-highspeed | 256K | ¥4.2 | ¥16.8 | ¥0.42 |

来源：platform.minimaxi.com[3]

小米（MiMo）

| 模型 | 上下文 | 缓存命中 | 输入（未命中） | 输出 |
| --- | --- | --- | --- | --- |
| V2.5-Pro | 256K | ¥0.025 | ¥3.00 | ¥6.00 |
| V2.5 | 256K | ¥0.02 | ¥1.00 | ¥2.00 |

来源：platform.xiaomimimo.com[4]  
注：V2.5 系列价格于 2026.5.27 正式生效；V2-Pro/V2-Omni 已于 2026.6.1 自动转入 V2.5 系列。

智谱（ChatGLM）

| 模型 | 上下文 | 输入 | 输出 |
| --- | --- | --- | --- |
| GLM-4-Plus | 128K | ¥5 | ¥5 |
| GLM-4-Air | 128K | ¥0.5 | ¥0.5 |
| GLM-4-FlashX | 128K | ¥0.1 | ¥0.1 |
| GLM-4-Long | 128K | ¥1 | ¥0.5 |

来源：bigmodel.cn/pricing[5]  
注：GLM-5.1、GLM-5、GLM-5-Turbo、GLM-4.7 均为"限时免费"阶段，非正式商业定价。

Kimi（月之暗面）

| 模型 | 上下文 | 缓存命中 | 输入（未命中） | 输出 |
| --- | --- | --- | --- | --- |
| K2.6 | 256K | ¥1.10 | ¥6.50 | ¥27.00 |

来源：platform.kimi.com/docs/pricing/chat-k26[6]（价格参考第三方整理，以官方公示为准）

100M Tokens 实际花多少钱？

以输入:输出 = 1:1 的常规场景计算（已确认价格的模型）：

| 厂商 | 模型 | 100M 总花费 | 备注 |
| --- | --- | --- | --- |
| 智谱 | GLM-4-FlashX | ¥20 | 便宜到离谱 |
| 智谱 | GLM-4-Air | ¥100 | — |
| DeepSeek | V4-Flash | ¥300 | 性价比之王 |
| 小米 | V2.5 | ¥300 | 和 DeepSeek 持平 |
| 小米 | V2.5 Pro | ¥900 | — |
| DeepSeek | V4-Pro | ¥900 | — |
| MiniMax | M2.7 | ¥1050 | — |
| MiniMax | M3 | ¥1260 | — |
| Kimi | K2.6 | ¥1,675 | ⚠️ 输出价格极高（¥27/M），建议实际按需评估 |

数字差距是十倍以上，不是十%。

六家订阅方案对比：小米 vs MiniMax vs Kimi vs 智谱 vs 火山 vs 百炼

⚠️ 订阅方案数据来自各厂商官方文档（2026年6月）。价格以官网最新公示为准。

火山方舟 Coding Plan（字节跳动）

| 套餐 | 月付 | 首月特惠 | 支持模型 |
| --- | --- | --- | --- |
| Lite | ¥40 | ¥8.91 | Doubao-Seed-Code / DeepSeek-V3.2 / GLM-4.7 / Kimi-K2-Thinking 等6款 |
| Pro | ¥200 | ¥44.91 | 同上，更高用量额度 |

亮点：多模型聚合 + Auto 模式自动匹配最优模型，支持 Cursor / Claude Code / Cline 等主流编程工具。  
来源：volcengine.com/activity/codingplan[7] 及 developer.volcengine.com[8]

阿里云百炼 Coding Plan

| 套餐 | 月付 | 支持模型 | 用量限制 |
| --- | --- | --- | --- |
| Pro | ¥200 | qwen3.6-plus / kimi-k2.5 / glm-5 / MiniMax-M2.5 等9款 | 每5小时6,000次 / 每周45,000次 / 每月90,000次 |

亮点：综合模型最多，qwen + GLM + Kimi + MiniMax 四家主流模型全覆盖。  
⚠️ Coding Plan Pro 不支持退订；额度按"模型调用次数"扣减（简单任务约5-10次/问，复杂10-30+次/问）。  
来源：help.aliyun.com/zh/model-studio/coding-plan[9]

MiniMax Token Plan

MiniMax Token Plan（人民币）

| 套餐 | 月付 | 年付（立省2月） | M3用量估算 | 并发Agent数 | 其他权益 |
| --- | --- | --- | --- | --- | --- |
| Plus | ¥49 | ¥490/年 | 约6亿+ Tokens | 3-4个 | 图/视/音/乐共享同一额度 |
| Max | ¥119 | ¥1,190/年 | 约18亿+ Tokens | 4-5个 | 含视频生成3条/日 |
| Ultra | ¥469 | ¥4,690/年 | 约71亿+ Tokens | 6-7个 | 含视频生成5条/日 |

来源：platform.minimaxi.com/subscribe/token-plan[10] （月付）及 platform.minimaxi.com/subscribe/token-plan[11] （年付）

小米 Token Plan（人民币）

| 套餐 | 月费 | Credits 额度 | 折算V2.5用量 | 折算V2.5-Pro用量 |
| --- | --- | --- | --- | --- |
| Lite | ¥39 | 待确认 | — | — |
| Standard | ¥99 | 待确认 | — | — |
| Pro | ¥329 | 待确认 | — | — |
| Max | ¥659 | 待确认 | — | — |

⚠️ 小米于2026年5月27日调整API按量计费价格并更新Token Plan计费体系，套餐价格未变但可用Credits额度增加。具体额度请以官方页面为准。  
来源：platform.xiaomimimo.com/docs/zh-CN/price/pay-as-you-go[4] 及 platform.xiaomimimo.com/price[12]

智谱 GLM Coding Plan（人民币）

| 套餐 | 月付 | 季付（9折） | 年付（7折） | 5小时配额 | 周配额 | 可用模型 |
| --- | --- | --- | --- | --- | --- | --- |
| Lite | ¥49 | ¥132 | ¥411 | ~80 prompts | ~400 prompts | GLM-4.7 / GLM-4.6 |
| Pro | ¥149 | ¥402 | ¥1,251 | ~400 prompts | ~2,000 prompts | GLM-5 / GLM-4.7 / GLM-4.6 全部 |
| Max | ¥469 | ¥1,266 | ¥3,939 | ~1,600 prompts | ~8,000 prompts | GLM-5 / GLM-4.7 / GLM-4.6 全部，含优先保障 |

⚠️ 智谱2026年已有多轮价格调整，套餐价格及模型可能发生变化，请以 bigmodel.cn/pricing[5] 及 bigmodel.cn/glm-coding[13] 官方页面为准。  
每次 prompt 约触发 15-20 次模型调用；GLM-5 消耗 3 倍额度（仅 Pro/Max 可用）。  
MCP 工具：Lite 100次/月，Pro 1,000次/月，Max 4,000次/月。

Kimi Code Plan（人民币）

| 套餐 | 月付 | 年付 | 5小时配额 | 核心权益 |
| --- | --- | --- | --- | --- |
| Andante | ¥49 | ¥468（月均¥39） | ~300-1,200 次调用 | K2.5 旗舰模型，AI建站/文档/PPT权益 |
| Moderato | ¥99 | ¥948（月均¥79） | 更大配额 | 多设备登录，支持 Claude Code / Roo Code |
| Allegretto | ¥199 | — | 更高配额 | 更高并发 |
| Allegro | ¥699 | — | 最高配额 | 最高并发 |

⚠️ Kimi 官方定价页面 platform.kimi.com/docs/pricing/chat-k26[6] 价格渲染异常，请以 Kimi 官网实际公示为准。上述价格参考第三方整理，准确性待确认。

| 套餐 | 月费 | M3用量估算 | 并发Agent数 | 其他权益 |
| --- | --- | --- | --- | --- |
| Plus | ¥49/月 | 约6亿+ Tokens | 3-4个 | 图/视/音/乐共享同一额度 |
| Max | ¥119/月 | 约18亿+ Tokens | 4-5个 | 含视频生成3条/日 |
| Ultra | ¥469/月 | 约71亿+ Tokens | 6-7个 | 含视频生成5条/日 |

具体换算：Ultra 套餐 ¥469/月 ≈ 71亿+ Tokens。按量计费同样 71亿 Tokens 用 M3 需要约 ¥76万——订阅便宜 1600 倍。

小米 Token Plan（人民币）

小米是目前国内厂商里另一个有 Token Plan 的，分为4档：

| 套餐 | 月费 | Credits 额度 | V2.5折算Tokens | V2.5-Pro折算Tokens |
| --- | --- | --- | --- | --- |
| Lite | ¥39 | 41亿 Credits | ≈4100万 Tokens | ≈1367万 Tokens |
| Standard | ¥99 | 110亿 Credits | ≈1.1亿 Tokens | ≈3667万 Tokens |
| Pro | ¥329 | 380亿 Credits | ≈3.8亿 Tokens | ≈1.27亿 Tokens |
| Max | ¥659 | 820亿 Credits | ≈8.2亿 Tokens | ≈2.73亿 Tokens |

消耗比（输入未命中缓存）：

• • V2.5：100 Credits / Token

• • V2.5-Pro：300 Credits / Token

一个具体例子：Standard 套餐 ¥99/月，110亿 Credits，全部用 V2.5 模型，约等于 1.1亿 Tokens。按量计费同样 1.1亿 Tokens 需要 ¥11000——订阅便宜了 100 倍。

但有限制：小米 Token Plan 只能在 OpenClaw、OpenCode、Claude Code 等编程工具里用，不能当普通 API 调用。

智谱 GLM Coding Plan（人民币）

| 套餐 | 月费 | 季付 | 年付 | 核心权益 |
| --- | --- | --- | --- | --- |
| Lite | ¥49/月 | ¥44.1/季 | ¥411/年 | 3x Claude Pro 用量额度 |
| Pro | ¥149/月 | ¥134.1/季 | ¥1251/年 | 5x Lite，1000次MCP/月 |
| Max | ¥469/月 | ¥422.1/季 | ¥3939/年 | 20x Lite，4000次MCP/月 |

所有套餐支持 GLM-5.1、GLM-4.7 等模型，覆盖 20+ 编程工具。

Kimi Code Plan（人民币）

Kimi 有编程订阅套餐，但不是按 token 总量的模式，是按 prompt 次数：

| 套餐 | 月费 | 核心权益 |
| --- | --- | --- |
| Andante | ¥49/月 | K2.5 模型，AI建站/文档/PPT权益 |
| Moderato | ¥99/月 | 更大配额，支持 Claude Code / Roo Code |
| Allegretto | ¥199/月 | 更高配额 |
| Allegro | ¥699/月 | 最高配额 |

注意：Kimi Code Plan 按 prompt 次数计量（每 prompt 约触发 15-20 次模型调用），不是 token 总量的概念。换算成实际 token 消耗取决于每次 prompt 的长度。Kimi API 本身没有 Token Plan，只能按量充值。

怎么选？

用量大、图省心 → MiniMax / 火山方舟 / 百炼的 Token/Coding Plan

这三个平台都是订阅制，用量透明、不用算余额。火山方舟支持豆包+DeepSeek+GLM+Kimi 多模型切换 + Auto 模式；百炼支持 qwen+GLM+Kimi+MiniMax 共9款。MiniMax Token Plan 是最早做国内订阅的，用量估算最透明。

挑模型、追求效果 → 直接选官方服务

⚠️ 一个重要提醒：即使是同一个开源模型（如 DeepSeek-V4-Pro），在百炼/火山这类聚合平台上的表现可能和官方有差距——尤其是工具调用（Tool Calling）场景，有用户反馈百炼的效果明显弱于官方直连。如果你的场景高度依赖 Agent 工具调用，强烈建议直接用官方 API。

简单任务、预算敏感 → DeepSeek V4-Flash（¥1/M 输入）

重度用量选按量计费性价比最高，简单任务随便选别纠结。

中文业务代码 → GLM-5.1（智谱）

中文理解最准，SWE-bench Pro 全球前三。

一句话结论：用的多上订阅（MiniMax/火山/百炼），挑模型走官方。

数据来源（2026年6月）

| 厂商 | 来源 |
| --- | --- |
| DeepSeek | api-docs.deepspark.cn/zh-cn/quick\_start/pricing[2] |
| 智谱 | bigmodel.cn/pricing[5] |
| 小米 MiMo | platform.xiaomimimo.com/docs/zh-CN/price/pay-as-you-go[4] |
| Kimi | platform.kimi.com/docs/pricing/chat-k26[6] |
| MiniMax | platform.minimaxi.com/subscribe/token-plan[3] |
| 火山方舟 | volcengine.com/activity/codingplan[7] |
| 百炼 | help.aliyun.com/zh/model-studio/coding-plan[9] |
| OpenRouter 月排行 | openrouter.ai/rankings?view=month[1] |

引用链接

[1] openrouter.ai/rankings?view=month: https://openrouter.ai/rankings?view=month  
[2] api-docs.deepseek.com: https://api-docs.deepseek.com/zh-cn/quick\_start/pricing  
[3] platform.minimaxi.com: https://platform.minimaxi.com/subscribe/token-plan?tab=api-enterprise  
[4] platform.xiaomimimo.com: https://platform.xiaomimimo.com/docs/zh-CN/price/pay-as-you-go  
[5] bigmodel.cn/pricing: https://bigmodel.cn/pricing  
[6] platform.kimi.com/docs/pricing/chat-k26: https://platform.kimi.com/docs/pricing/chat-k26  
[7] volcengine.com/activity/codingplan: https://www.volcengine.com/activity/codingplan  
[8] developer.volcengine.com: https://developer.volcengine.com/articles/7595502342175195187  
[9] help.aliyun.com/zh/model-studio/coding-plan: https://help.aliyun.com/zh/model-studio/coding-plan  
[10] platform.minimaxi.com/subscribe/token-plan: https://platform.minimaxi.com/subscribe/token-plan?tab=individual\_\_monthly  
[11] platform.minimaxi.com/subscribe/token-plan: https://platform.minimaxi.com/subscribe/token-plan?tab=individual\_\_yearly  
[12] platform.xiaomimimo.com/price: https://platform.xiaomimimo.com/price  
[13] bigmodel.cn/glm-coding: https://bigmodel.cn/glm-coding
