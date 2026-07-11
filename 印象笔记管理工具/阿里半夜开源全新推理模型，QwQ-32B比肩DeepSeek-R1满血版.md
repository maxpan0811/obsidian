# 阿里半夜开源全新推理模型，QwQ-32B比肩DeepSeek-R1满血版

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzA3MzI4MjgzMw==&mid=265095...](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&mid=2650958115&idx=1&sn=26927008dad5cd9fb55576ebf460e25e&chksm=85d07517b4616f329da29d5333de051ac2d18ec5604ca5596d59c9ffcd2792789b43d89aff32&scene=90&xtrack=1&sessionid=1741230165&subscene=93&clicktime=1741230171&enterid=1741230171&flutter_pos=1&biz_enter_id=4&ranksessionid=1741229564&ascene=56&devicetype=iOS18.3.1&version=18003835&nettype=WIFI&abtest_cookie=AAACAA==&lang=zh_CN&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ/5XR/Fm1bZ1KgWXDmi1cNBLMAQIE97dBBAEAAAAAACriIM2/TaYAAAAOpnltbLcz9gKNyK89dVj0x0YdfRc2u6DDd3R3KS1m/BpI9E38gEDHsob4XGGY1dpWHLK0pUikwonHBauOoMO/squQx7DdJ2uBFgAA5NTESP+bjMCzAxYxJc3ppbfsGm2GEc/yGSpXUoxM1pPlUIf1PeE2wKvz3IiIdieQka/xPXcPGmGy58sljgqkJrxxodO4vdNN8l1pO65ktSxe0kRCBFleSxBQ90egmtaAA5fmoLpPhJYatg==&pass_ticket=DHGKQYhRLXs4ttgZyjpzQF0ovFmTD9orMHuEYvIMTqIart2qPEYJHUuBkWfK2Y3j&wx_header=3)

机器之心

机器之心报道

**机器之心编辑部**

今天凌晨 3 点，阿里开源发布了新推理模型 QwQ-32B，其参数量为 320 亿，但性能足以比肩 6710 亿参数的 DeepSeek-R1 满血版。

![](.evernote-content/ACD3BF49-6A68-4CFE-9FB7-6B6B34BF478A/7C20764B-73EC-442F-9126-5CFACB31612B.png)

千问的推文表示：「这次，我们研究了扩展 RL 的方法，并基于我们的 Qwen2.5-32B 取得了一些令人印象深刻的成果。我们发现 RL 训练可以不断提高性能，尤其是在数学和编码任务上，并且我们观察到 RL 的持续扩展可以帮助中型模型实现与巨型 MoE 模型相媲美的性能。欢迎与我们的新模型聊天并向我们提供反馈！」

QwQ-32B 已在 Hugging Face 和 ModelScope 开源，采用了 Apache 2.0 开源协议。大家也可通过 Qwen Chat 直接进行体验！

* 博客：https://qwenlm.github.io/zh/blog/qwq-32b/
* Hugging Face：https://huggingface.co/Qwen/QwQ-32B
* ModelScope：https://modelscope.cn/models/Qwen/QwQ-32B
* 演示：https://huggingface.co/spaces/Qwen/QwQ-32B-Demo
* Qwen Chat：https://chat.qwen.ai/

本地部署工具 Ollama 也第一时间提供了支持：ollama run qwq

![](.evernote-content/ACD3BF49-6A68-4CFE-9FB7-6B6B34BF478A/910FE7DC-E70F-48C3-B0E1-A6EA22131056.png)

千问官方发布了题为「QwQ-32B: 领略强化学习之力」的官方中文博客介绍这一吸睛无数的进展。考虑到[强化学习之父 Richard Sutton 与导师 Andrew Barto 刚刚获得图灵奖](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&mid=2650958043&idx=1&sn=dc02ed349a811c96abf0270968621120&scene=21#wechat_redirect)，QwQ-32B 的发布可说是非常应景。

![](.evernote-content/ACD3BF49-6A68-4CFE-9FB7-6B6B34BF478A/E9FFC842-FA22-4B7A-ABCC-21E701E53F32.png)

博客中写到，大规模强化学习（RL）非常具有潜力，在提升模型性能方面可望超越传统的预训练和后训练方法。

近期的研究表明，强化学习可以显著提高模型的推理能力。例如，DeepSeek-R1 通过整合冷启动数据和多阶段训练，实现了最先进的性能，使其能够进行深度思考和复杂推理。

而千问团队则探索了大规模强化学习（RL）对大语言模型的智能的提升作用，推理模型 QwQ-32B 便由此而生。

这是一款拥有 320 亿参数的模型，其性能可媲美具备 6710 亿参数（其中 370 亿被激活）的 DeepSeek-R1。该团队表示：「这一成果突显了将强化学习应用于经过大规模预训练的强大基础模型的有效性。」

QwQ-32B 中还集成了与 Agent（智能体）相关的能力，使其能够在使用工具的同时进行批判性思考，并根据环境反馈调整推理过程。该团队表示：「我们希望我们的一点努力能够证明强大的基础模型叠加大规模强化学习也许是一条通往通用人工智能的可行之路。」

**模型效果**

QwQ-32B 在一系列基准测试中进行了评估，包括数学推理、编程和通用能力。以下结果展示了 QwQ-32B 与其他领先模型的性能对比，包括 DeepSeek-R1-Distilled-Qwen-32B、DeepSeek-R1-Distilled-Llama-70B、o1-mini 以及原始的 DeepSeek-R1。

![](.evernote-content/ACD3BF49-6A68-4CFE-9FB7-6B6B34BF478A/5E33D467-1DC6-49E8-B5AF-7EE9980A6542.png)

可以看到，QwQ-32B 的表现非常出色，在 LiveBench、IFEval 和 BFCL 基准上甚至略微超过了 DeepSeek-R1-671B。

**强化学习**

QwQ-32B 的大规模强化学习是在冷启动的基础上开展的。

在初始阶段，先特别针对数学和编程任务进行 RL 训练。与依赖传统的奖励模型（reward model）不同，千问团队通过校验生成答案的正确性来为数学问题提供反馈，并通过代码执行服务器评估生成的代码是否成功通过测试用例来提供代码的反馈。

随着训练轮次的推进，QwQ-32B 在这两个领域中的性能持续提升。

在第一阶段的 RL 过后，他们又增加了另一个针对通用能力的 RL。此阶段使用通用奖励模型和一些基于规则的验证器进行训练。结果发现，通过少量步骤的通用 RL，可以提升其他通用能力，同时在数学和编程任务上的性能没有显著下降。

**API**

如果你想通过 API 使用 QwQ-32B，可以参考以下代码示例：

![](.evernote-content/ACD3BF49-6A68-4CFE-9FB7-6B6B34BF478A/8B8DD15A-B573-471B-8A7C-FE217E99C150.png)

**未来工作**

千问团队还在博客中分享了未来计划，其中写到：「这是 Qwen 在大规模强化学习（RL）以增强推理能力方面的第一步。通过这一旅程，我们不仅见证了扩展 RL 的巨大潜力，还认识到预训练语言模型中尚未开发的可能性。在致力于开发下一代 Qwen 的过程中，我们相信将更强大的基础模型与依托规模化计算资源的 RL 相结合，将会使我们更接近实现人工通用智能（AGI）。此外，我们正在积极探索将智能体与 RL 集成，以实现长时推理，目标是通过推理时间扩展来释放更高的智能。」

**QwQ-32B 收获无数好评**

QwQ-32B 一发布就收获了无数好评，甚至我们的不少读者也在催促我们赶紧报道。

在前段时间的 DeepSeek 热潮中，大家都热衷于讨论满血版，因为蒸馏版性能受限。但是 671B 的满血版模型无法轻易部署，普通的端侧设备只能退而求其次。现在，Qwen 把模型大小打下来了，端侧有希望了吗？

![](.evernote-content/ACD3BF49-6A68-4CFE-9FB7-6B6B34BF478A/758F26B0-566A-40FF-A58D-3946AEB4B706.png)

有网友表示，手机上肯定还不行，但运行内存比较高的 Mac 或许可以一战。

![](.evernote-content/ACD3BF49-6A68-4CFE-9FB7-6B6B34BF478A/1D8B34E3-674D-4B79-A464-4CDD08B59C04.png)

还有人喊话阿里巴巴通义实验室科学家 Binyuan Hui 去做更小的模型。

![](.evernote-content/ACD3BF49-6A68-4CFE-9FB7-6B6B34BF478A/7FACF95C-6439-4883-A8A5-1ECD2A195D21.png)![](.evernote-content/ACD3BF49-6A68-4CFE-9FB7-6B6B34BF478A/4178B762-825D-4C80-A592-61B5DCD27CA9.png)

还有人晒出体验，表示运行很快：

![](.evernote-content/ACD3BF49-6A68-4CFE-9FB7-6B6B34BF478A/679F337D-41C9-4DA6-B8A7-56BEED14EE47.png)![](.evernote-content/ACD3BF49-6A68-4CFE-9FB7-6B6B34BF478A/1BCD84C3-0D1D-4C7E-92F3-C677F3A1C8F7.gif)

苹果机器学习研究者 Awni Hannun 也同样已经在 M4 Max 上成功运行了 QwQ-32B，看起来速度非常快。

![](.evernote-content/ACD3BF49-6A68-4CFE-9FB7-6B6B34BF478A/4EE0E344-379F-49D8-BA70-C05B350BFEED.gif)

在 Qwen 的官方聊天界面（Qwen Chat），我们已经能看到 QwQ-32B 的预览版模型。感兴趣的读者可以前去测试。

![](.evernote-content/ACD3BF49-6A68-4CFE-9FB7-6B6B34BF478A/483D1B83-7F91-4A3B-B4A5-451DFABAB89A.png)

测试链接：https://chat.qwen.ai/

© THE END

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&mid=2650958115&idx=1&sn=26927008dad5cd9fb55576ebf460e25e&chksm=85d07517b4616f329da29d5333de051ac2d18ec5604ca5596d59c9ffcd2792789b43d89aff32&scene=90&xtrack=1&sessionid=1741230165&subscene=93&clicktime=1741230171&enterid=1741230171&flutter_pos=1&biz_enter_id=4&ranksessionid=1741229564&ascene=56&devicetype=iOS18.3.1&version=18003835&nettype=WIFI&abtest_cookie=AAACAA==&lang=zh_CN&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ/5XR/Fm1bZ1KgWXDmi1cNBLMAQIE97dBBAEAAAAAACriIM2/TaYAAAAOpnltbLcz9gKNyK89dVj0x0YdfRc2u6DDd3R3KS1m/BpI9E38gEDHsob4XGGY1dpWHLK0pUikwonHBauOoMO/squQx7DdJ2uBFgAA5NTESP+bjMCzAxYxJc3ppbfsGm2GEc/yGSpXUoxM1pPlUIf1PeE2wKvz3IiIdieQka/xPXcPGmGy58sljgqkJrxxodO4vdNN8l1pO65ktSxe0kRCBFleSxBQ90egmtaAA5fmoLpPhJYatg==&pass_ticket=DHGKQYhRLXs4ttgZyjpzQF0ovFmTD9orMHuEYvIMTqIart2qPEYJHUuBkWfK2Y3j&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/2ccee6e4-19c5-4bfc-b007-308b4f08cf29/2ccee6e4-19c5-4bfc-b007-308b4f08cf29/)