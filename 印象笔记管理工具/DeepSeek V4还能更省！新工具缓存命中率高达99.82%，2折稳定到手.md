# DeepSeek V4还能更省！新工具缓存命中率高达99.82%，2折稳定到手

---

来源：[打开原文](https://mp.weixin.qq.com/s/Fgw6dUiIBSfPBYlkwWOpWQ)

鱼羊 发自 凹非寺量子位 | 公众号 QbitAI
-------------------------

我悟了，DeepSeek V4系列发布1个月，价格屠夫的本色这才刚刚发力啊！

官方这边，打折促销期还没过，折上折价格已官宣落定为永久降价。

![](.evernote-content/46CA3FE7-22CF-4221-BC68-2E84967ADED4/620208E0-D55F-4D38-9307-18C96102F547.png)

就这样，开源社区仍不满足。您猜怎么着？缓存命中率直接给干到99.82%了！

![](.evernote-content/46CA3FE7-22CF-4221-BC68-2E84967ADED4/0C234C59-D847-4E36-9307-03215A05F2FE.png)

什么概念？就是原本4亿+token、61美元（合人民币414元）的账单，能直降至12美元（合人民币81元），2折轻松到手。

![](.evernote-content/46CA3FE7-22CF-4221-BC68-2E84967ADED4/09082874-CBB3-45AD-8AAA-670C9BCA131D.png)

老哥老姐们给这个名为Reasonix的项目点星都点疯了，状态be like：

![](.evernote-content/46CA3FE7-22CF-4221-BC68-2E84967ADED4/EC7B28FA-F0EC-455E-9874-555F7047948D.png)

具体来说，Reasonix是一款专为DeepSeek打造的终端coding harness，核心目的很简单，就是两个字：省钱——

长会话能把缓存命中保持在90%+，输入token成本降到1/5的那种。

![](.evernote-content/46CA3FE7-22CF-4221-BC68-2E84967ADED4/C14F0957-170C-4635-A749-1948CC94A16D.png)

DeepSeek原生编程Agent
-----------------

Reasonix的实现思路也不复杂，最核心的一点是：基于字节稳定prefix-cache设计的append-only运行循环。

就是说，Reasonix的工作流程是专门为了DeepSeek的缓存机制设计的：旧的上下文固定不动，新消息只往后追加，尽量保证每一轮请求的前半部分完全一样，从而提高缓存命中率，降低长会话成本。

具体架构可以拆分成3个部分来看。

![](.evernote-content/46CA3FE7-22CF-4221-BC68-2E84967ADED4/76255ECA-AEC7-4AD7-8115-F57F47FB4E67.png)

缓存优先循环（Cache-First Loop）
------------------------

自动前缀缓存（prefix-cache）仅在当前请求的精确字节前缀和先前请求匹配时才会激活，想要提高缓存命中率，需要解决的是大多数智能体循环会在每次交互时重新排序、重写或注入新的时间戳的问题。

Reasonix的解决方案是把上下文划分为三个区域：

![](.evernote-content/46CA3FE7-22CF-4221-BC68-2E84967ADED4/D45150F8-7F29-4F8C-995A-312DFB7900E5.png)

这样，前缀会被固定下来，在每个会话中仅计算一次；历史消息只追加不重写；而草稿区中的任何信息在归入日志前，均需通过Tool-Call Repair进行提炼。

工具调用修复（Tool-Call Repair）
------------------------

DeepSeek比较容易遇到的问题包括：

工具调用JSON在内部已经生成，但在最终消息里却消失不见；模型想调用工具，但参数写歪了，即JSON参数畸形；同一工具被反复调用且参数完全相同，即重复调用风暴；JSON被截断。

工具调用修复会通过4轮处理，让Reasonix在真正执行前，先尝试修复这些问题。

成本控制
----

首先，默认优先使用v4 flash，困难任务才会切pro。

![](.evernote-content/46CA3FE7-22CF-4221-BC68-2E84967ADED4/F8ACC042-8DC7-45F9-A833-03EEE0B5F445.png)

其次，轮次结束自动压缩上下文。

用户要是觉得下一次任务比较难，就输入/pro，这样下一轮对话模型就会切换为v4 pro。跑完这一轮后Reasonix自动切回便宜模型，无需用户手动更改。

最后，失败信号会触发自动升级：失败次数到达警戒线后，当前轮次的剩余部分就会切到v4 pro上运行。

Reasonix在安装使用方面也比较简单。

两步即可运行，无需全局安装：

进入项目目录；输入：npx reasonix code，启动TUI会话。

不习惯用终端的话，Reasonix还提供了桌面版。

以及再次再次高亮一下来自Reasonix官方的提醒：

Reasonix只为DeepSeek打造，每一个抽象层级都基于DeepSeek的Feature构建，完全不通用，也“不会发布通用功能”。

One More Thing
--------------

省钱的事情，大家伙当然喜闻乐见，毕竟也不是每个人都能像龙虾之父Peter那样无限狂烧公司token。

![](.evernote-content/46CA3FE7-22CF-4221-BC68-2E84967ADED4/850D2B9A-6923-46B5-B671-7F9E2C61CDBB.png)

于是关于Reasonix的讨论，是轻轻松松就盖了几百楼。

![](.evernote-content/46CA3FE7-22CF-4221-BC68-2E84967ADED4/68EFE146-3B92-481D-A7B9-873E95EC8121.png)

不少小伙伴已经摩拳擦掌跃跃欲试，但也有人提出疑问：

我们真的需要一个DeepSeek原生编程Agent吗？

有网友分享说，Ta写了一个微型桥接程序，在Codex中使用DeepSeek V4 Pro，同样实现了95%以上的高缓存命中。

并且Ta“没做任何特殊处理，只是将DeepSeek API的格式调整为Codex所需要的”。

![](.evernote-content/46CA3FE7-22CF-4221-BC68-2E84967ADED4/B5F0790F-F126-4F01-9EEA-8127A7509BF2.png)

anyway，harness和harness之间肯定是有区别的。就有网友分享说，在Claude Code里使用DeepSeek V4比在OpenCode上省钱。

甭管你用了哪一种方案，都欢迎在评论区分享分享心得体验。

大家省才是真的省（doge）。

项目地址：https://github.com/esengine/DeepSeek-Reasonix

参考链接：[1]https://github.com/esengine/DeepSeek-Reasonix/blob/main/docs/ARCHITECTURE.md#pillar-1--cache-first-loop[2]https://esengine.github.io/DeepSeek-Reasonix/index.html#agents

— 欢迎AI产品从业者共建 —

[📎 在印象笔记中打开](evernote:///view/207087/s1/e8dfe92f-8e95-4bca-88bb-e5a15ec6e4fa/e8dfe92f-8e95-4bca-88bb-e5a15ec6e4fa/)