---
title: 刚刚 Claude Fable 5 炸裂发布！附一手实测，夯还是拉？
type: source
created: 2026-06-11
updated: 2026-06-11
source_path: 印象笔记管理工具/刚刚 Claude Fable 5 炸裂发布！真是太烧了。。附一手实测，夯还是拉？.html
tags: [anthropic, claude, fable-5, mythos-5, review, comparison]
---

**摘要**: 程序员鱼皮对 Claude Fable 5 的硬核实测。Fable 5 与 Mythos 5 为同一底层模型，仅安全护栏不同。三轮实测（全栈看板项目、重构 Claude Code 源码）显示 Fable 5 "零修改跑通"、PTY 终端真实验证，综合评分 8.3 分排名第一，但费用是 Opus 4.8 的 3 倍（$38.66 vs $13.38）。

## 核心观点

- Fable 5 和 Mythos 5 是同一底层模型，区别仅在安全护栏松紧
- 全栈项目实测：Fable 5 唯一零修改跑通，Opus 4.8 和 GPT-5.5 需修 bug
- 重构 Claude Code 源码：Fable 5 是唯一做了 PTY 终端交互测试并交付可用产品的
- 费用极贵：$38.66 (2146 万 token) vs Opus $13.38 vs GPT $4.61
- "AI 自己测试通过"和"用户实际能用"之间存在巨大鸿沟
- 分级释放（安全降级）模式可能成为行业趋势

## 关键细节

- **安全降级机制**：敏感请求降级到 Opus 4.8，约 <5% 会话触发
- **定价**：输入 $10/百万 token，输出 $50/百万 token（总成本 $60/百万）
- **SWE-bench Pro**: Fable 5 80.3% vs GPT-5.5 58.6% vs Opus 4.8 69.2%
- **FrontierCode**: Fable 5 29.3% vs Opus 4.8 13.4% vs GPT-5.5 5.7%
- **视觉能力**: Fable 5 29.8%（宝可梦火红纯视觉通关）
- **免费窗口期**: 6月22日前 Pro/Max/Team 套餐可免费使用
- **模型选择建议**: 大规模重构用 Fable 5，中小项目用 Opus 4.8 性价比更高

## 相关页面

- [[products/Claude-Fable-5|Claude Fable 5]]
- [[sources/Claude-Fable-5首日实测]]
