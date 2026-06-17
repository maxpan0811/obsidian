---
title: 完整的671B MoE DeepSeek R1怎么塞进本地化部署？详尽教程大放送！
type: source
created: 2026-06-17
updated: 2026-06-17
source: 印象笔记管理工具
source_path: 印象笔记管理工具/完整的671B MoE DeepSeek R1怎么塞进本地化部署？详尽教程大放送！.html
tags: [AI技术, 教育]
---

# 完整的671B MoE DeepSeek R1怎么塞进本地化部署？详尽教程大放送！

原文链接: https://mp.weixin.qq.com/s?chksm=84e7920db3901b1b5ce5a502447f62b...

完整的671B MoE DeepSeek R1怎么塞进本地化部署？详尽教程大放送！  机器之心

AIxiv专栏是机器之心发布学术、技术内容的栏目。过去数年，机器之心AIxiv专栏接收报道了2000多篇内容，覆盖全球各大高校与企业的顶级实验室，有效促进了学术交流与传播。如果您有优秀的工作想要分享，欢迎投稿或者联系报道。投稿邮箱：liyazhou@jiqizhixin.com；zhaoyunfeng@jiqizhixin.com

本文的作者是李锡涵（Xihan Li）。他是伦敦大学学院（UCL）计算机系博士研究生，谷歌开发者专家，主要研究方向为学习优化，在 NeurIPS、ICLR、AAMAS、CIKM 等会议发表过学术论文，Circuit Transformer 作者，图书《简明的 TensorFlow 2》（https://tf.wiki）作者。

过年这几天，DeepSeek 算是彻底破圈了，火遍大江南北，火到人尽皆知。虽然网络版和 APP 版已经足够好用，但把模型部署到本地，才能真正实现独家定制，让&#xa0;DeepSeek&#xa0;R1 的深度思考「以你为主，为你所用」。

关于本地部署，大多数人使用的是蒸馏后的8B/32B/70B版本，本质是微调后的Llama或Qwen模型，并不能完全发挥出DeepSeek R1的实力。

然而，完整的671B MoE模型也可以通过针对性的量化技术压缩体积，从而大幅降低本地部署门槛，乃至在消费级硬件（如单台Mac Studio）上运行。

那么，如何用 ollama 在本地部署 DeepSeek R1 671B（完整未蒸馏版本）模型呢？一篇在海外热度很高的简明教程即将揭晓。

作者主页：https://snowkylin.github.io
原文地址：https://snowkylin.github.io/blogs/a-note-on-deepseek-r1.html

本地部署后，让&#xa0;DeepSeek R1 「数草莓」

原版 DeepSeek R1 671B 全量模型的文件体积高达 720GB，对于绝大部分人而言，这都大得太离谱了。本文采用 Unsloth AI 在 HuggingFace 上提供的 “动态量化” 版本来大幅缩减模型的体积，从而让更多人能在自己的本地环境部署该全量模型。

“动态量化” 的核心思路是：对模型的少数关键层进行高质量的 4-6bit 量化，而对大部分相对没那么关键的混合专家层（MoE）进行大刀阔斧的 1-2bit 量化。通过这种方法，DeepSeek R1 全量模型可压缩至最小 131GB（1.58-bit 量化），极大降低了本地部署门槛，甚至能在单台 Mac Studio 上运行！

根据我自己的工作站配置，我选择了以下两个模型进行测试：

DeepSeek-R1-UD-IQ1_M（671B，1.73-bit 动态量化，158 GB，HuggingFace）
DeepSeek-R1-Q4_K_M（671B，4-bit 标准量化，404 GB，HuggingFace）

Unsloth AI 提供了 4 种动态量化模型（1.58 至 2.51 比特，文件体积为 131GB 至 212GB），可根据自身硬件条件灵活选择。建议阅读官方说明了解各版本差异。

...Unsloth AI&#xa0;官方说明：htt
