# 首个中文Stable Diffusion模型开源，IDEA研究院封神榜团队开启中文AI艺术时代

---

智能摘要

AIGC模型——太乙，让中文世界得以拥有具备中国文化内核的AIGC模型，未来更好地助力中国AIGC文化产业数字化转型的创新发展。模型进行开发，但由于中英文之间存在文化差异，这种模型遇到中文独特的叙事和表达时，很难给出正确匹配的图片内容。Stable-Diffusion-v1-4的生成模型部分，在亿级别的高质量数据上微调语言编码器，调整学习率等超参数，训练语言模型中文部分的表征。Stable-Diffusion-v1-4的生成模型部分，增强中文引导图片生成的能力，目前训练中的一个checkpoint已取得不错的效果并进行了开源。

原文约 2191  字  | 图片 18 张 | 建议阅读 5 分钟 | [评价反馈](https://static.app.yinxiang.com/embedded-web/clipper/#/Evaluating?d=2022-11-10&nu=37a9860d-c000-4e7c-8e1d-09dcf3cbb030&fr=myyxbj&ud=328ef&v=2&sig=F67559C36DFA4C1A682D55A330D4DC7D)

首个中文Stable Diffusion模型开源，IDEA研究院封神榜团队开启中文AI艺术时代
===============================================

IDEA数字经济研究院

近日，IDEA研究院认知计算与自然语言研究中心（简称IDEA研究院CCNL）开源了首个中文版本Stable Diffusion AIGC模型——太乙，让中文世界得以拥有具备中国文化内核的AIGC模型，未来更好地助力中国AIGC文化产业数字化转型的创新发展。

今天晚上7点，IDEA研究院CCNL团队还将线上直播，揭秘太乙Stable Diffusion模型背后的关键技术。欢迎对AIGC及太乙感兴趣的小伙伴观看交流~

（以下文章来自于机器之心）

生成内容一直被视为 AI 领域中最具有挑战性的能力，最近大火的 AI 绘画背后，是 Stable Diffusion 模型的开源，催生了众多 AI 绘画的应用，得益于 Stability AI 的开源精神，这一创变推动了整个以英文为主的下游文生图生态的蓬勃发展。

然而在国内，目前大部分团队主要是基于翻译 API + 英文 Stable Diffusion 模型进行开发，但由于中英文之间存在文化差异，这种模型遇到中文独特的叙事和表达时，很难给出正确匹配的图片内容。IDEA 研究院CCNL开源了第一个中文版本的 Stable Diffusion 模型“太乙 Stable Diffusion”，让中文的世界真正拥有具备中国文化内核的 AIGC 模型。

1. 太乙Stable Diffusion 纯中文版本：https://huggingface.co/IDEA-CCNL/Taiyi-Stable-Diffusion-1B-Chinese-v0.1

2. 太乙 Stable Diffusion 中英双语版本：https://huggingface.co/IDEA-CCNL/Taiyi-Stable-Diffusion-1B-Chinese-EN-v0.1

中文运笔，意境浮现

![](.evernote-content/F7AA207F-44BC-416C-B02C-5899A954C0BE/15F834A7-251E-4D42-9B35-D49BF8AF06EE.png)

君不见黄河之水天上来 ，唯美，油画

![](.evernote-content/F7AA207F-44BC-416C-B02C-5899A954C0BE/021DED4F-87D1-4889-8292-0D6E48D81224.png)

滔滔江水，连绵不绝，唯美，插画

![](.evernote-content/F7AA207F-44BC-416C-B02C-5899A954C0BE/D080C6D7-7444-444F-BDBA-0A457951E2CA.png)

飞流直下三千尺 ，唯美，插画

![](.evernote-content/F7AA207F-44BC-416C-B02C-5899A954C0BE/061D26CC-2869-44AA-9F91-EB090E3EA4BE.png)

长城，清晨，朦胧，唯美，插画

![](.evernote-content/F7AA207F-44BC-416C-B02C-5899A954C0BE/6BE93197-F32E-4887-946A-E2CFCC9218E2.png)

梦回江南，中国古代小镇，唯美，插画

![](.evernote-content/F7AA207F-44BC-416C-B02C-5899A954C0BE/98EF8D5E-CBF7-4399-9C8C-53E9B6A2672B.png)

云南苗家古寨，原始森林，鸟语花香，唯美，插画

![](.evernote-content/F7AA207F-44BC-416C-B02C-5899A954C0BE/4D51CAAC-AD4A-4CAC-8542-BA0656BD29F1.png)

中国的未来城市，科幻插画

中文 vs 英文的图片生成

![](.evernote-content/F7AA207F-44BC-416C-B02C-5899A954C0BE/387CBAD5-A6D7-4724-8252-CF6B2881CCD3.png)

![](.evernote-content/F7AA207F-44BC-416C-B02C-5899A954C0BE/26F36C8E-CEF1-48B6-85F6-1B18EAE3B9F1.png)

![](.evernote-content/F7AA207F-44BC-416C-B02C-5899A954C0BE/C9E4E43F-C6F9-4188-9164-07F8E01975B2.png)

![](.evernote-content/F7AA207F-44BC-416C-B02C-5899A954C0BE/44EB80B3-4936-43D8-861B-83EB68C08CE2.png)

中文指导的特定风格生成

![](.evernote-content/F7AA207F-44BC-416C-B02C-5899A954C0BE/0E832210-E385-4456-9E2A-B5C916C5AAB5.png)

小桥流水人家，水彩

（Taiyi-Stable-Diffusion-1B-Chinese-EN-v0.1）

![](.evernote-content/F7AA207F-44BC-416C-B02C-5899A954C0BE/7B04B7A0-F0AC-471A-8B44-50F6B4144CB8.png)

小桥流水人家，Van Gogh style

（Taiyi-Stable-Diffusion-1B-Chinese-EN-v0.1）

太乙系列文本生成图像模型技术揭秘

第一个开源中文 CLIP 模型

2022 年 7 月，IDEA研究院CCNL开源了第一个中文 CLIP 模型，目前已经有 4 个版本。

1. Taiyi-CLIP-Roberta-102M-Chinese：https://huggingface.co/IDEA-CCNL/Taiyi-CLIP-Roberta-102M-Chinese

2. Taiyi-CLIP-Roberta-large-326M-Chinese：https://huggingface.co/IDEA-CCNL/Taiyi-CLIP-Roberta-large-326M-Chinese

3. Taiyi-CLIP-RoBERTa-102M-ViT-L-Chinese：https://huggingface.co/IDEA-CCNL/Taiyi-CLIP-RoBERTa-102M-ViT-L-Chinese

4. Taiyi-CLIP-RoBERTa-326M-ViT-H-Chinese：https://huggingface.co/IDEA-CCNL/Taiyi-CLIP-RoBERTa-326M-ViT-H-Chinese

以 Taiyi-CLIP-Roberta-large-326M-Chinese 为例，IDEA研究院CCNL用中文语言模型替换了开源的英文 CLIP 中语言编码器，在训练过程中冻结了视觉编码器并且只微调这个中文语言模型，在 1 亿级别的中文数据上训练了 24 个 epoch，一共过了约 30 亿中文图文数据，得到了这个包含图片信息的中文表征语言模型，为后续训练中文 Diffusion 相关的模型奠定了重要的基础。

第一个开源中文 Disco Diffusion 模型

2022 年 10 月，IDEA研究院CCNL开源了第一个中文 Disco Diffusion 模型 Taiyi-Diffusion-532M-Nature-Chinese，该模型由 Katherine Crowson's 的无条件扩散模型在自然风景图上微调而来。结合 Taiyi-CLIP-Roberta-large-326M-Chinese 可以实现中文生成各种风格的风景图片。

![](.evernote-content/F7AA207F-44BC-416C-B02C-5899A954C0BE/50F2A358-DAED-420A-A2EE-E7ED8B34B73C.png)

东临碣石，以观沧海，水何澹澹，山岛竦峙

第一个开源中文 Stable Diffusion 模型

2022 年 11 月，IDEA研究院CCNL开源了第一个中文 Stable Diffusion 的模型和中英双语 Stable Diffusion 模型。

太乙 Stable Diffusion 纯中文版本（Taiyi-Stable-Diffusion-1B-Chinese-v0.1）

该模型利用已经开源的太乙 CLIP 模型 (Taiyi-CLIP-RoBERTa-102M-ViT-L-Chinese) 替换了英文 Stable-Diffusion-v1-4 中的语言编码器，因为太乙 CLIP 模型已经具备了很强的中文图文概念，所以直接冻结英文 Stable Diffusion 的生成模型部分，在亿级别的高质量数据上微调语言编码器，调整学习率等超参数，将太乙 CLIP 模型理解的中文图文概念与 Stable Diffusion 生成能力对齐。

太乙 Stable Diffusion 中英双语版本（Taiyi-Stable-Diffusion-1B-Chinese-EN-v0.1）

不同于太乙 Stable Diffusion 纯中文版本，这个模型希望在支持中文的情况下，同时能保留 Stable-Diffusion-v1-4 的英文生成能力。由于Stable-Diffusion-v1-4 原有语言模型不具备太乙 CLIP 模型强大的中文图文概念，IDEA研究院CCNL希望在它的基础上增加了中文数据训练，这里采取了两阶段的训练。第一阶段也是冻住 Stable-Diffusion-v1-4 的生成模型部分，在亿级别的高质量数据上微调语言编码器，调整学习率等超参数，训练语言模型中文部分的表征。第二阶段放开 Stable-Diffusion-v1-4 的生成模型部分，增强中文引导图片生成的能力，目前训练中的一个 checkpoint 已取得不错的效果并进行了开源。

使用方法

如果需要进行古诗场景、中文概念生成，建议尝试中文版本 Taiyi-Stable-Diffusion-1B-Chinese-v0.1。如果需要一些通用场景和概念的生成，尤其是有中文混合英文需要，建议尝试中英双语版本 Taiyi-Stable-Diffusion-1B-Chinese-EN-v0.1。

![](.evernote-content/F7AA207F-44BC-416C-B02C-5899A954C0BE/2D11DB8E-0D71-45DA-9372-D81B159EE6ED.png)

中文版本

![](.evernote-content/F7AA207F-44BC-416C-B02C-5899A954C0BE/F19C2AEE-71B9-4DC6-B043-99208E9CAB8D.png)

中英双语版本

太乙：中文 Stable Diffusion 的未来

目前在庞大的中国市场中，有将近 10 亿的文化产业正在被 AIGC 冲击并快速创新发展，也有更多的新机遇在裂变中产生。

由于此前的 AIGC 模型还无法和特殊的中国文化背景相结合，致力于成为中文认知智能的基础设施的 IDEA 研究院CCNL，希望通过推出太乙模型，助力加快在 AIGC 全球市场化中中国的文化产业数字化转型的创新发展，促进各个相关行业的升级。而太乙所在的封神榜预训练模型开源体系，已经开源 80 个模型，覆盖 AIGC、自然语言理解、受控文本生成等多个领域，成为中文最大的预训练模型开源体系。基于封神榜模型的 GTS 模型生产平台，自动生产的 1 亿参数模型，击败众多百亿千亿参数模型，进入 FewCLUE 榜单前三名，机器自动化生成模型的能力达到了算法专家水平，AI 生产 AI 的时代正在到来。

IDEA研究院CCNL认为，在 AIGC 中，人的作用是更为重要的，生成式 AI 应悄无声息地融入大众生活中并更好地帮助人类拓展想象力边界。所以，与 AI 互动生产的内容，是帮助 AIGC 走向下一个生产力阶段的关键。除了基础模型和基础算法的研究之外，团队还在研究更精准的文本生成和基于中文文本的交互式图片编辑。以太乙为核心的 AIGC 模型会持续更新和升级，敬请期待。

欢迎对太乙感兴趣的小伙伴们

与我们联系交流

一起共建中文 AIGC 的新世界

（可添加封神榜团队交流微信：fengshenbang-lm）

封神榜相关链接

1.封神榜总论文（中英双语）：                    https://arxiv.org/abs/2209.02970

2.封神榜主页：

https://github.com/IDEA-CCNL/Fengshenbang-LM

3.huggingface 地址：

https://huggingface.co/IDEA-CCNL

4.封神榜 doc：

https://fengshenbang-doc.readthedocs.io/zh/latest/

关于 IDEA研究院CCNL

IDEA研究院认知计算与自然语言研究中心（Cognitive Computing and Natural Language, CCNL）致力于推动预训练大模型为代表的新一代认知与自然语言基础前沿技术的进一步发展，力图解决大模型实际落地过程中的全部技术问题，构建对话机器人、知识抽取、知识体系等自然语言领域的新的技术架构，打造认知人工智能的新技术范式。

扫描下方二维码，加入IDEA研究院CCNL。

![](.evernote-content/F7AA207F-44BC-416C-B02C-5899A954C0BE/476CD6B5-EA6C-4250-839E-59A1A60743B5.png)

![](.evernote-content/F7AA207F-44BC-416C-B02C-5899A954C0BE/D53685CC-E359-4636-AE6C-80CE2BDB3786.jpg)

---

[🌐 原始链接](http://mp.weixin.qq.com/s?__biz=MzU0MjA0OTYxNA==&mid=2247492269&idx=1&sn=1cd53d1dbdcb63e1c3474e8541f4b705&chksm=fb22368ccc55bf9ac044141e0a066f8a985e03381226e1a380fcfd80c2ffececd07cc3549c38&mpshare=1&scene=1&srcid=11108nIqBH9bwZlL8TqHQwYE&sharer_sharetime=1668076494470&sharer_shareid=ee47b9411760e9070f0b59d8d8655fa1#rd)

[📎 在印象笔记中打开](evernote:///view/207087/s1/dde63fec-bc77-4456-ad2c-67c7e629c879/dde63fec-bc77-4456-ad2c-67c7e629c879/)