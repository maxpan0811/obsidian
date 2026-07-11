# OpenCode，把 DeepSeek V4 Flash 免费了

---

原文链接: <https://mp.weixin.qq.com/s/zFXVLABDcYxKC-HCA9ZuUQ>

原创Dr.Joyi像素与咖啡时光

最近大家对厂商免费送模型这件事热情很高。前三篇文章聊的都是 GLM-5.2，美团送、阿里送、达子也送，三篇全上了公众号热门。GLM-5.2 确实是目前开源模型的顶流，这一点没什么争议。

但今天想跟大家聊另一个国内的优秀开源模型，**DeepSeek V4 Flash**。

如果说 GLM-5.2 是开源编程模型里的重型坦克，那 DeepSeek V4 Flash 就是轻骑兵。它不追求在所有基准测试上拿第一，它追求的是速度和效率的极致平衡。同样一个编程任务，Pro 模型可能要想三秒给你一个精雕细琢的答案，Flash 一秒就甩出来一个够用的结果。对于日常写代码改 bug 的场景，**够用就是最好用**。

说实话 DeepSeek V4 Flash 是我日常用得最多的编程模型之一。很多人选 Flash 而不是 Pro，原因很简单，Pro 太贵了。Flash 速度快、推理效率高，日常写代码干活完全够用。但即便是 Flash，按 DeepSeek 官方 API 的价格长期高频调用，一个月下来账单也不是个小数字。后台留言里好几个人问的都是同一件事，「Flash 有没有免费渠道」。

还真有。而且我从今年 5 月份就开始用了，到现在快两个月，活动还在继续。既然这系列大家喜欢看，索性把我知道的信息都给大家分享出来。

**OpenCode**，一个开源的 AI 编程代理工具，从 5 月 11 号开始在它的 Zen 模型网关上提供 DeepSeek V4 Flash 的免费使用。官方正式宣布的，不是什么野路子渠道。不需要信用卡，不需要 DeepSeek 的 API Key，支持 20 万 token 上下文。模型 ID 是 deepseek-v4-flash-free。

先说清楚一个容易混淆的点

这是 OpenCode Zen 模型网关提供的免费层，不是 DeepSeek 官方 API 本身免费。你去 DeepSeek 官方那边调 V4 Flash 还是正常计费的。OpenCode 相当于自己掏钱买了 DeepSeek 的推理算力，然后免费开放给社区用。

为什么它愿意做这个亏本买卖？官方的说法是「收集反馈改进模型体验」，但我觉得更现实的原因是拉新。用免费 Flash 把人吸引到 OpenCode 的生态里，然后让你看到 Go 套餐里那一堆好东西。

PART 01

先说 OpenCode 是什么东西

开源版 Claude Code，17.8 万星

![](.evernote-content/DC4A63D3-70A3-4D8E-B62E-6C9F6E35A66F/F5ED7A6D-2EDF-4AA1-BA0F-987856EDC012.png)

OpenCode 是目前全球最火的开源 AI 编程代理，GitHub 上 **17.8 万颗星**，750 万月活开发者。你可以把它理解成一个开源版的 Claude Code。终端里运行，支持 75 个以上的模型供应商，Anthropic、OpenAI、Google、DeepSeek、本地 Ollama 模型全都能接。MIT 协议完全开源，你可以审计它的每一行代码。

跟 Claude Code 最大的区别是，Claude Code 只能用 Anthropic 自己的模型，钱只能花在 Claude 身上，但架不住开源社区的大神们，使得我们现在在Claude Code 也可以使用上第三方模型。OpenCode 不挑，你想用谁家的模型就接谁家的 Key。你甚至可以用 Ollama 在本地跑一个开源模型，整个过程完全离线，代码不出你的电脑。

它有两个内置的工作模式，Build 和 Plan，按 Tab 键切换。Build 是默认模式，AI 可以读写文件、执行命令、修改代码。Plan 是只读模式，AI 只做分析和规划，不动你的文件。先 Plan 理清思路，再切 Build 动手干活。这个工作流我觉得比 Claude Code 设计得更合理。

一个很多人不知道的杀手级特性：LSP 集成

就是语言服务器协议，它能把 TypeScript、Python、Rust、Go 这些语言的实时编译诊断信息喂给 AI 模型。模型改完代码之后能立刻看到编译器报不报错，根本不用你手动跑一遍 build 去验证。这个反馈循环让 AI 写出来的代码质量明显更高，有测试数据显示 OpenCode 在相同模型上比 Claude Code 平均多生成 21 个测试用例。其他主流编程代理里，目前做到这一点的很少。

PART 02

免费模型怎么用

零配置、零 API Key、零信用卡

安装很简单。macOS 和 Linux 一行命令就可以安装，Windows 也行。不想用终端的人可以直接下载桌面版安装包。装完在项目目录里输入 opencode 就启动了。

第一次启动它会问你要连接哪个模型供应商。选 OpenCode Zen，DeepSeek V4 Flash Free 自动就在模型列表里了。**零配置、零 API Key、零信用卡，打开就能用**。这个体验跟前面几篇文章里的工具完全不同。CatPaw 和 QoderWork 虽然也是开箱即用，但它们是图形界面的产品。OpenCode 是终端工具，面向的就是开发者。一个开发者打开终端，一行命令安装，选个免费模型，直接开始干活，这才是最自然的工作方式。

![](.evernote-content/DC4A63D3-70A3-4D8E-B62E-6C9F6E35A66F/AF216EE1-EE21-4E27-85FE-76193E6997C0.png)

启动后底部状态栏显示当前模型是「DeepSeek V4 Flash Free OpenCode Zen」，后面跟着「max」标记表示最大上下文模式。按 Ctrl+P 弹出模型选择器。

![](.evernote-content/DC4A63D3-70A3-4D8E-B62E-6C9F6E35A66F/9DCAD2DD-000F-4920-8694-7392431DE91C.png)

免费模型有两个。DeepSeek V4 Flash Free 和 Big Pickle。Big Pickle 是 OpenCode 自己做的一个模型，定位不太清楚，我没深度测试过不敢评价。**DeepSeek V4 Flash Free 才是重点**，它就是 DeepSeek 官方的 V4 Flash 模型，只不过通过 OpenCode Zen 的推理网关提供免费调用。你用它跟直接用 DeepSeek API 调 Flash 在能力上没有区别，区别只在于速度和稳定性。

我测试了一下，问它「你是什么模型」。它先走了一个 755 毫秒的思考过程，然后老老实实回答 deepseek-v4-flash-free，模型 ID 是 opencode/deepseek-v4-flash-free。整个响应 7.5 秒。

![](.evernote-content/DC4A63D3-70A3-4D8E-B62E-6C9F6E35A66F/401E0690-1A08-4BB4-9046-F8CB1A7065D2.png)

坦率的讲，7.5 秒不算快。DeepSeek 官方 API 直连 Flash 一般两三秒出结果，这个免费版本慢了一倍多。但免费嘛，比没有强。而且这是我工作日下午测的，晚上和周末跑的时候体感明显快不少。

PART 03

免费到底能免到什么程度

官方故意模糊，社区实测宽松

说到这里你肯定想问，这个「免费」到底能免到什么程度。

我翻了一下 OpenCode Zen 的官方说明，关于这个免费模型的规则只有一句话，大意是「DeepSeek V4 Flash Free 在 OpenCode 上限时提供，团队借这个阶段收集反馈来改进模型」。就这一句，没有提到任何具体的 Token 数量、请求次数或者每日上限。

**官方故意模糊处理了额度这件事。**

但从我个人的使用情况来看，5 月初活动开始到现在快两个月，日常在上面跑小型编程任务，我确实没有触发过任何限额提示。社区里也有人做过压力测试，开三个 OpenCode 实例同时跑 DeepSeek V4 Flash 一个小时，月度限额才消耗了 1%。说明这个免费层的天花板其实设得相当宽松，轻度到中度使用基本摸不到。

不过 Reddit 和 GitHub 上也有人遇到过限制。有人在 GitHub 提了个 issue 标题就叫「Free Model limit」，说某天使用 DeepSeek V4 Flash Free 时突然触发了额度限制的提示。也有人在 Reddit 反馈遇到大量排队或者请求失败的情况。所以「免费无限」这件事并不是铁板钉钉的，只是从目前大多数用户的反馈来看还没摸到上限。

这个活动从始至终都被定性为「limited time」，限时的，没有明确结束日期。这意味着活动随时可能结束。你可以把它当作一个低成本试错的窗口期来用，但不建议把核心生产流程完全绑在上面。万一哪天活动下线了，你得有备选方案。好消息是，如果你习惯了 OpenCode 的工作流，切到 Go 套餐只要 10 美元一个月，或者接自己的 DeepSeek API Key 也行，迁移成本几乎为零。

PART 04

10 美元的中国模型全家桶

Go 套餐里一个西方闭源模型都没有

再聊一个我觉得很有意思的东西。OpenCode 的付费套餐。

![](.evernote-content/DC4A63D3-70A3-4D8E-B62E-6C9F6E35A66F/F1088780-516A-41F2-A527-ABECBB155185.png)

它有一个叫 Go 的订阅计划，首月 5 美元，之后每月 10 美元。你猜这 10 美元能用什么模型？

![](.evernote-content/DC4A63D3-70A3-4D8E-B62E-6C9F6E35A66F/E4E89396-ABEA-46C0-AC4A-34005C795930.png)

GLM-5.2、GLM-5.1、Kimi K2.7 Code、Kimi K2.6、MiMo-V2.5-Pro、MiMo-V2.5、Qwen3.7 Max、Qwen3.7 Plus、Qwen3.6 Plus、MiniMax M2.7、MiniMax M3、DeepSeek V4 Pro、DeepSeek V4 Flash。

**全是中国的开源模型。没有 Claude，没有 GPT，没有 Gemini，没有 Grok。**

其实你仔细看这个名单就很有意思。GLM-5.2 是智谱的，DeepSeek V4 是深度求索的，Kimi K2.7 是月之暗面的，Qwen3.7 是阿里的，MiMo 是小米的，MiniMax 是稀宇科技的。**六家中国 AI 公司的模型，凑成了一个面向全球开发者的 10 美元付费套餐**。对比一下隔壁，Cursor Pro 每月 20 美元只给你用 Claude 和 GPT 两家的模型，Claude Code 的 Max 订阅 100 美元一个月只能用 Anthropic 一家。OpenCode Go 10 美元随便切十几个顶级开源模型，这个性价比是碾压级的。你今天用 GLM-5.2 写后端，明天用 DeepSeek V4 Pro 调逻辑，后天切 Kimi K2.7 Code 做代码审查，随便换不加价。

![](.evernote-content/DC4A63D3-70A3-4D8E-B62E-6C9F6E35A66F/29E158AA-6E02-4EAF-B42F-A9A11F4DF02B.png)

Go 套餐里的模型按每 5 小时请求数限制。GLM-5.2 每 5 小时 880 次，Qwen3.7 Max 950 次，DeepSeek V4 Pro 3450 次，DeepSeek V4 Flash 31650 次。这个资源分配逻辑很聪明，Flash 模型的请求上限是 Pro 的将近十倍，明确引导你日常任务多用 Flash，只在关键时刻切 Pro。跟我之前在阿里 QoderWork 那篇里说的一样，杀鸡不用牛刀。而且 10 美元一个月是什么概念呢，一杯星巴克的钱，你就能同时用上 GLM-5.2、DeepSeek V4、Kimi、Qwen 这些在各种排行榜上打架的顶级开源模型。反正我觉得，如果你每天都在用 AI 写代码，这 10 美元花得比任何一杯咖啡都值。

PART 05

写完这四篇，我自己也挺感慨的

免费是获客手段，但窗口期是真的

回过头来看整个系列四篇文章，其实写着写着我自己也挺感慨的。

美团 CatPaw 把 GLM-5.2 免费塞进了自己的 IDE。阿里 QoderWork 把 GLM-5.2 免费塞进了桌面办公搭子。英伟达把 GLM-5.2 挂在 API 平台上免费给开发者用。OpenCode 选了 DeepSeek V4 Flash 作为免费引流模型，然后把 GLM-5.2 和 DeepSeek V4 Pro 这些更重的模型放在 10 美元的 Go 套餐里。

四家的选择不同，但底层逻辑完全一致。用免费模型把人吸引进来，让你养成使用习惯，再用产品生态和付费层把你留住。**免费是获客手段，不是慈善**。但对于我们用户来说，这个阶段就是最好的薅羊毛窗口。

你想想看，一个全球 750 万开发者用的开源编程工具，它的付费套餐里一个西方闭源模型都没有。全是 GLM、DeepSeek、Kimi、Qwen、MiMo、MiniMax。这不是偶然，这是市场选择的结果。这些中国开源模型在编程场景下的性价比太高了，高到一个面向全球开发者的商业产品，宁愿只用它们也不愿付 Claude 和 GPT 的溢价。

一个非中国公司做的面向全球开发者的开源编程工具，付费模型名单里全是中国模型。这件事放在三年前你敢想吗。

2023 年大家茶余饭后聊的还是中国大模型到底能不能追上 GPT-4。2024 年 DeepSeek V3 横空出世，中国开源模型第一次让人觉得「真的能打了」。到了 2025 年底 DeepSeek R1 推理模型发布，彻底把「中国模型只会抄」的偏见打碎。然后是 2026 年上半年，GLM-5.2 开源即巅峰，Code Arena 排行榜全球开源第一。DeepSeek V4 全系列登场，Flash 版本把速度和成本做到了极致。这两个模型加上 Kimi、Qwen、MiMo、MiniMax，组成了一支完整的中国开源模型军团。全球的 AI 工具厂商不管大小，都在争着把这些模型集成进自己的产品里。不是出于什么情怀，纯粹就是因为性价比碾压。

**不是谁在推动它们。是所有人都已经在用它们了。**

1946 年联合国投票选择工作语言。英语成了六种官方语言之一，不是因为英国或者美国推动了什么决议，而是因为全世界已经有太多文件、合同、技术文档和学术论文是用英语写的。当一种语言变成了事实上的标准，你就不需要再去「推广」它了。它已经在那里了。

中国的开源模型正在走同一条路。不是靠谁的推广计划，而是靠每一个开发者在终端里按下回车键时做出的选择。**当够多的人选择了你，你就不需要再被选择了**。

写在最后

活动还在进行中，想试的趁早。

这个活动截至我发稿时仍然在进行中，感兴趣的直接去 opencode.ai 下载安装。限时的，没有明确结束日期，想试的话趁现在还在就赶早。反正装完打开选个免费模型就能直接用，两分钟的事。

---

[🌐 原始链接](https://mp.weixin.qq.com/s/zFXVLABDcYxKC-HCA9ZuUQ)

[📎 在印象笔记中打开](evernote:///view/207087/s1/73d1d80e-6469-48b1-9564-9908c0101ba1/73d1d80e-6469-48b1-9564-9908c0101ba1/)