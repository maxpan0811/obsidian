---
name: Claude Fable 5
type: product
category: ai-model
company: Anthropic
tags: [anthropic, claude, fable-5, ai-model]
created: 2026-06-11
updated: 2026-06-11
---

# Claude Fable 5

Anthropic 最新发布的旗舰模型，定位「Mythos 神话级」新段位。

## 主要特征

- **FC Diamond**: 成功率从 Opus 4.8 的 ~14% 飙升至 30%+，翻倍增长
- **代码能力**: 百万行级代码重构、自动追踪所有调用方
- **创意能力**: 一句提示复刻 Photoshop、构建完整游戏、3D 世界
- **多模态对抗**: MC 建站、网页生成等任务全面超越 GPT-5.5
- **成本高昂**: 高强度操作可快速消耗 30% 额度

## 评测数据

| 指标 | Fable 5 | Opus 4.8 | GPT-5.5 |
|------|:-------:|:--------:|:--------:|
| SWE-bench Pro | **80.3%** | 69.2% | 58.6% |
| FrontierCode | **29.3%** | 13.4% | 5.7% |
| 视觉 (GDPpdf) | **29.8%** | 22.5% | 24.9% |
| FC Diamond | **30%+** | ~14% | — |
| 全栈项目实测 | 零修改跑通 | 需修 Bug | 需修 Bug |
| 实测费用 | $38.66 | $13.38 | $4.61 |

## 定价

- 输入: $10 / 百万 token
- 输出: $50 / 百万 token
- 总计: $60 / 百万 token（DeepSeek V4 的 50 倍）
- 免费窗口期: 发布日至 6 月 22 日

## 安全机制

Fable 5 与 Mythos 5 为同一底层模型。Fable 5 加安全分类器，敏感请求降级到 Opus 4.8（<5% 会话触发）；Mythos 5 为完全解限版，仅限审核机构使用。

## 相关来源

- [[sources/Claude-Fable-5首日实测]]
- [[sources/程序员鱼皮-Claude-Fable-5实测]]
