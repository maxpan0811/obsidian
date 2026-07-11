# 为什么Dynamic Workflows自动工作流如此重要?

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzIzMzQyMzUzNw==&mid=224751...](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247517509&idx=1&sn=d11854fa45299c747af54ec7ea58342e&chksm=e9a7b7c5354eb00854f4fe2476fc105b540cb326c28a734a4dd9b80c0f4a9a2d586121d16403&scene=90&xtrack=1&req_id=1780222028292007&sessionid=1780219776&subscene=93&clicktime=1780222108&enterid=1780222108&flutter_pos=11&biz_enter_id=4&ranksessionid=1780222028&jumppath=20020_1780222003783,1104_1780222054233,30024_1780222068835,1104_1780222091138&jumppathdepth=4&forceh5=1&ascene=56&devicetype=iOS26.5&version=18004a24&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQne9xtbUU2r3v64IK8Y5gshLTAQIE97dBBAEAAAAAAKeXJBu0eqQAAAAOpnltbLcz9gKNyK89dVj0LaCGHc3ON8C5hleU6bMz0g4BwBp+xg6qPhlILE1TnKEfwdJ+XxgxdwSAViAsOaMiFi6xgeRgE8VUA5ThIGdR2LfwdIMqHJqdZEye/JJAaQpgHstDIqWgydh3S1FUoxxcX7Ng7x3B5Gwg/H/AkW31M9XrXpHgvENFv8M1NNdGebQqQgb7teXQRdRQO/G1pkuSlPMaTD8UbUALKJ9H+56TPrBf4G+hllwdDsGZW30=&pass_ticket=UyNOGzGVQKuGKzGSeiHolGi+XmIq/49fQQqepZUP/hqEb5jywkeaZ50ZnteHoU6z&wx_header=3)

为什么Dynamic Workflows自动工作流如此重要?
==============================

Original字节笔记本 字节笔记本

 

抛开抄袭不说，[状告Anthropic！开源团队爆Claude新功能 Dynamic Workflows 抄袭](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247517388&idx=1&sn=0b6c80afb5ec08e9e2c5a8cedef26751&scene=21#wechat_redirect)，为啥各家都把自己的功能拓展押注在这个自动工作流上？

以前我们说 Agent 编程，大多数时候说的是一个模型在Claude Code对话里边想边做。

它读代码、改文件、跑命令、看报错，然后继续下一步。

再后来有了 subagent，主 Agent 可以派几个小弟出去查资料、读文件、分析问题。[Claude Code Sub Agents的正确打开方式和案例演示](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247503891&idx=1&sn=c64af7e038d0c7b9ec8c5d7a2d032f9e&scene=21#wechat_redirect)

再后来有了 Agent Teams，多个 Claude Code 实例可以像一个小团队一样并行协作。[一个人就是一个公司！Claude Code 团队组织化模式高效使用](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247513409&idx=1&sn=c6a8228bacbc02d0725295e3815a2ddc&scene=21#wechat_redirect)

这些能力当然有用，但它们有一个共同的问题：**编排者还是 Claude 自己**。

也就是说，下一步派谁去做、做完以后怎么合并、发现问题以后怎么回滚、怎么交叉验证，还是靠 Claude 在当前上下文里临时判断。

任务小的时候没问题，一旦任务变大，中间结果越来越多，Claude 的上下文就开始被过程信息塞满。

它不是不会干，而是协调成本越来越高。

Dynamic Workflows 换了一个思路。

它不再让 Claude 在对话里一轮一轮地调度，而是让 Claude 先**把怎么调度写成一段 JavaScript 脚本**。

这个脚本里可以有循环、分支、并发、校验、汇总。写完之后，脚本交给本地运行时执行。只有在脚本执行到需要模型干活的地方，才临时拉起一个 subagent。

也就是说，把编排逻辑被代码化了。

以前 Claude 是现场临时指挥，看到一个结果，再决定下一步。

现在 Claude 更像是先画出施工图，然后让一群 Agent 按图施工。中间过程不再全部塞回主对话窗口，而是留在脚本变量里，最后只把汇总结果交回来。

这就是 Dynamic Workflows 和 subagent 最大的区别。

subagent 解决的多任务，Workflow 解决的是任务如何分配和协调。

以Claude Code官方的例子，Bun 作者 Jarred Sumner 用 Dynamic Workflows，把 Bun 运行时从 Zig 迁移到 Rust。结果是 11 天、约 75 万行 Rust 代码、99.8% 的原有测试通过。

![](.evernote-content/CC286189-3612-4164-91C6-E418930F042D/3BC990F0-F376-478E-8D93-18759D0ADD1F.jpg)

在这种跨语言迁移项目里面有大量文件、生命周期、内存所有权、编译错误、测试回归。单个 Agent 就算能力再强，也很难靠一轮对话把整个任务协调完。

Workflow 的做法更像流水线。

第一步，先让一批 Agent 分析 Zig 代码里的结构和生命周期。

第二步，把不同文件分发给不同 Agent 并行迁移。

第三步，再让 reviewer Agent 对迁移结果做交叉审查。

第四步，进入编译和测试的 fix loop：报错、修复、再跑，直到尽量收敛。

这就是它真正厉害的地方，Agent把复杂工程拆成了可执行流程。

每个节点可以是一个 Agent，但真正保证任务不跑偏的，是那段 Workflow 脚本。

这也解释了为什么它和 n8n、Dify、Coze 这类工作流工具既像又不像。

像，是因为它们本质上都是确定性流程 + 节点里调用 LLM。流程本身不是模型临场决定的，而是提前写好的。

不同的是，n8n 里的流程通常是人拖出来的图，Dynamic Workflows 里的流程是 Claude 当前任务现场写出来的一段代码。

让模型自己写工作流。

真正大任务难的地方，往往不是某一步怎么做，而是整套流程怎么组织。什么时候并行，什么时候汇总，什么时候交叉验证，什么时候进入循环，什么时候停止。

这些东西如果都靠模型在对话里临场想，就很容易随着上下文膨胀而失控。

但一旦它变成代码，就有了三个好处。

第一，可读。你可以看到 Claude 到底准备怎么安排这件事。

第二，可审。你可以在运行前检查它是不是要乱改文件、乱跑命令、乱烧 token。

第三，可复用。一个好的 Workflow 可以保存下来，变成项目里的长期能力。

这也是我觉得它比普通 subagent 更重要的原因。subagent 更像一次性的帮手，Workflow 更像一套沉淀下来的生产流程。

当然，它并不适用于所有的场景。

一两步就能搞定的小任务，完全没必要起 Workflow。让几十个 Agent 并行干活，token 成本一定更高，它适合的是那种范围大、步骤多、需要并行、需要验证、需要反复循环的大工程。

比如全仓库安全审计，从旧框架迁移到新框架，大规模 API 替换，找性能瓶颈，让多个 Agent 从不同角度审查一个方案，再派对抗性的 Agent 去推翻它。

过去我们总是在讨论谁写代码更强，谁修 bug 更稳，谁上下文更大。

接下来可能还要讨论另一个问题：谁更会组织一支 Agent 队伍。

单个模型再强，也还是一个大脑。真正的大工程，靠的从来不是一个人从头写到尾，而是一套流程、一套分工、一套检查机制。

是会先判断这件事该怎么拆，哪些部分并行做，哪些部分需要审查，哪些地方需要循环验证，然后自动生成一套可执行的工作流，让它生成一套稳定推进的系统。

之前我们也介绍过Goals，[Codex&Claude Code的 /goal 指令的高级进阶使用技巧](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247516287&idx=1&sn=b09eacc8e7f33cc93a927bc063a28fe7&scene=21#wechat_redirect)，Goals 更像是把目标钉住，让模型持续朝那个方向推进。

Dynamic Workflows 则是把过程写下来，让代码保证流程不跑偏。

这也解释了这几家为什么会把这种自动工作流作为关键性的功能组件。

不过目前这个功能只能是订阅用户来使用的，对于非订阅，或者想结合Deepseek这类开源模型来使用的用户，我们可以使用Pi[OpenClaw的心脏 Pi Agent从入门到精通](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247513895&idx=1&sn=89218ec19ccd086cff9df100b3cd02e4&scene=21#wechat_redirect)的插件来体验Dynamic Workflows。

安装步骤如下。

pi install npm:pi-dynamic-workflows

安装后，在 Pi 里执行：

/reload

这样就启用了，不用自己写代码，直接对 Pi 说：

运行一个工作流，分析当前项目结构，并总结主要模块。

或者：

运行一个工作流，从架构、安全、性能、可维护性几个角度审查这个项目，最后给我一份改进建议。

Pi 会自动生成工作流脚本，然后调用多个子 Agent 分头处理。

以一个分析陌生代码库呢例子：

运行一个工作流，扫描这个仓库，告诉我入口文件、核心模块、配置文件和整体运行逻辑。

做代码审查：

运行一个工作流，从架构、安全、性能、可维护性四个角度 review 当前项目。

重构前分析：

运行一个工作流，找出这个项目里最值得优先重构的文件、重复逻辑和潜在风险。

做资料研究：

运行一个工作流，分别从技术实现、使用场景、优缺点和替代方案几个角度研究这个主题，最后汇总。

它会显示类似这样的进度：

◆ 工作流：inspect\_project
  ✓ 扫描
  ✓ 分析
  ✓ 汇总

如果不想继续跑，可以按 `Esc` 取消。

普通 Pi 是一个 Agent 从头做到尾，`pi-dynamic-workflows` 是让 Pi 先写一张任务拆解图，再派多个子 Agent 并行干活，最后把结果汇总回来。

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247517509&idx=1&sn=d11854fa45299c747af54ec7ea58342e&chksm=e9a7b7c5354eb00854f4fe2476fc105b540cb326c28a734a4dd9b80c0f4a9a2d586121d16403&scene=90&xtrack=1&req_id=1780222028292007&sessionid=1780219776&subscene=93&clicktime=1780222108&enterid=1780222108&flutter_pos=11&biz_enter_id=4&ranksessionid=1780222028&jumppath=20020_1780222003783,1104_1780222054233,30024_1780222068835,1104_1780222091138&jumppathdepth=4&forceh5=1&ascene=56&devicetype=iOS26.5&version=18004a24&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQne9xtbUU2r3v64IK8Y5gshLTAQIE97dBBAEAAAAAAKeXJBu0eqQAAAAOpnltbLcz9gKNyK89dVj0LaCGHc3ON8C5hleU6bMz0g4BwBp+xg6qPhlILE1TnKEfwdJ+XxgxdwSAViAsOaMiFi6xgeRgE8VUA5ThIGdR2LfwdIMqHJqdZEye/JJAaQpgHstDIqWgydh3S1FUoxxcX7Ng7x3B5Gwg/H/AkW31M9XrXpHgvENFv8M1NNdGebQqQgb7teXQRdRQO/G1pkuSlPMaTD8UbUALKJ9H+56TPrBf4G+hllwdDsGZW30=&pass_ticket=UyNOGzGVQKuGKzGSeiHolGi+XmIq/49fQQqepZUP/hqEb5jywkeaZ50ZnteHoU6z&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/d8a6e599-06cb-4529-a3e4-3ec0fd0ba6a0/d8a6e599-06cb-4529-a3e4-3ec0fd0ba6a0/)