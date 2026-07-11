# 发现 5 个宝藏级 GitHub 项目，做 AI 开发太香了！

---

来源：[打开原文](https://mp.weixin.qq.com/s/HkzRvaAcr_zY4bJepCld3w)

\* 戳上方蓝字“程序掘金”关注我

01 Outlines
-----------

这是 Python 生态里做 LLM 结构化生成（Structured Generation）的利器。

大语言模型的输出经常不可控，普通做法是生成完再用正则或解析器去修，脆弱又麻烦。Outlines 直接在 token 生成阶段就用有限状态机约束输出，保证结果一定符合你指定的 JSON Schema、Pydantic 模型或正则表达式——不需要重试、不需要后处理。

![](.evernote-content/2180F10C-D65C-4A54-9BE2-5C4E7AAF2414/F10FDEF0-842B-41E4-8A12-2F3717DE21FD.jpg)

它支持 OpenAI、Anthropic、vLLM、transformers、llama.cpp、Ollama 等主流后端，写法也很 Pythonic，比如 outlines.generate.json(model, MyPydanticModel) 就能拿到类型安全的对象。适合做 Agent 工具调用、数据抽取管道、API 响应封装等对输出格式严格要求的生产场景。

https://github.com/dottxt-ai/outlines

02 Spec Kit
-----------

GitHub 官方开源的 Spec-Driven Development（规格驱动开发）工具包，专治"随口跟 AI 说需求→代码乱写→反复返工"的痛点。

![](.evernote-content/2180F10C-D65C-4A54-9BE2-5C4E7AAF2414/98A25E97-51F9-491B-9DF9-386B11899983.jpg)

核心理念是先写清楚规格再让 AI 动手——用 /speckit.constitution 定项目原则，/speckit.specify 描述做什么（不谈技术栈），/speckit.plan 给出技术方案，/speckit.tasks 拆任务，/speckit.implement 让 AI 按计划实现，每步产物都是 Markdown 文档供后续追溯。

![](.evernote-content/2180F10C-D65C-4A54-9BE2-5C4E7AAF2414/9F21B812-0F8E-42F8-84EC-C7AFF52AA05B.jpg)

支持 Claude Code、GitHub Copilot、Cursor、Gemini CLI 等 30+ AI 编码助手，通过 specify init 一键注入 slash commands。如果你想告别纯 vibe coding、让 AI 辅助开发变得可预测可复盘，这个工作流非常值得试试。

https://github.com/github/spec-kit

03 Pinokio
----------

你是不是经常在GitHub上发现一些超酷的AI开源项目，但一看安装说明要输一堆命令行就开始头大？

![](.evernote-content/2180F10C-D65C-4A54-9BE2-5C4E7AAF2414/03A3837C-040A-4035-B6F4-8B27661056CF.jpg)

Pinokio就是为了拯救我们这些“命令行恐惧症”患者而生的。它是一个图形化的“AI应用浏览器”，让你能像安装手机App一样，一键安装并运行各种复杂的AI软件。它本质上是把复杂的安装脚本封装在了友好的界面之下。

![](.evernote-content/2180F10C-D65C-4A54-9BE2-5C4E7AAF2414/D145E947-1F28-46C3-93C7-5AB2E1FE2FCC.jpg)

Pinokio最有意思的设计是它的“脚本策略”：它通过一个像“应用商店”一样的“发现”页面来分发经过人工审核的安全脚本，保证了开箱即用的安全性。同时，它也保留了高度的灵活性，你可以自己编写脚本，让Pinokio去执行任何复杂的任务。

如果你想把本地各种AI模型、工具统一管理起来，又不想被环境配置、依赖冲突等问题劝退，Pinokio绝对值得一试。

https://github.com/pinokiocomputer/pinokio

04 EdgeGlow
-----------

Mac 专属的小工具（macOS 13+，Intel/Apple Silicon 通吃），解决一个很细微但恼人的问题：用 Claude Code 或 Hermes Agent 编程时，它在后台读文件、跑命令，你根本不知道是在忙还是在等。

![](.evernote-content/2180F10C-D65C-4A54-9BE2-5C4E7AAF2414/697EA41F-AB03-4ED9-AE0A-0A3019FCCE70.jpg)

EdgeGlow 在屏幕四边显示 iPhone Apple Intelligence 同款虹彩流光，AI 思考时光效流动，完成后淡出。

通过本地 HTTP Hook（127.0.0.1:9876）与 Agent 联动，设置界面能直接复制引导词让 Claude Code 自动配置 hooks。支持 5 种颜色主题、流动/呼吸双模式、多显示器适配，纯 Swift 写成仅 ~900KB，CPU 占用近乎为零。用 Claude Code 重度编码的同学装上会有种"终于看见 AI 在干嘛"的解脱感。

https://github.com/vector4wang/EdgeGlow

05 SiliconScope
---------------

Apple Silicon Mac（M1–M5，需 macOS 14+）上无需 sudo 的原生系统监视器，最大亮点是 Activity Monitor 看不到的东西它都有：ANE（Neural Engine）使用率估算、Media Engine 负载、内存带宽（对比芯片上限如 M1 Max 400GB/s）、GPU 降频标记、每核 E/P-core 温度、SoC 功耗细分等，跑本地 LLM 或媒体转码时特别有用。

![](.evernote-content/2180F10C-D65C-4A54-9BE2-5C4E7AAF2414/04C1817E-6F04-4117-83D4-3F2E73E20916.jpg)

提供漂亮的 SwiftUI 仪表盘和可固定的菜单栏项（CPU/GPU/内存/网络/SSD/传感器/电池），自带短时基准测试可记录模型的 tokens/sec 和 tokens/Wh。"Measure tok/s" 功能对挑本地模型跑什么硬件很有参考价值。

想替代 iStat Menus 或单纯想看 Apple Silicon 加速器的真实工况，这个开源方案很香。

https://github.com/kennss/SiliconScope

[📎 在印象笔记中打开](evernote:///view/207087/s1/8be452cb-9453-4ca6-92f7-caa7395b648d/8be452cb-9453-4ca6-92f7-caa7395b648d/)