# 有人用来代替 Claude Code ，真香 。

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=Mzg3NzU0NzIxMA==&mid=224751...](https://mp.weixin.qq.com/s?__biz=Mzg3NzU0NzIxMA==&mid=2247512321&idx=1&sn=3ceff59b88e60822d34f0483a3161c42&chksm=ce8b3998c2bfab7644d5fd771aafb469e83d5c8532815fea27d6a726ab42b81f8ace074c57b0&scene=90&xtrack=1&req_id=1779522096563956&sessionid=1779522314&subscene=93&clicktime=1779522413&enterid=1779522413&flutter_pos=0&biz_enter_id=4&ranksessionid=1779522096&jumppath=1001_1779522201661,1102_1779522203641,1001_1779522211162,1104_1779522314992&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004931&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQUGk6jN3gmT3cvyZr2/tN+RLTAQIE97dBBAEAAAAAAANpMt7xfIcAAAAOpnltbLcz9gKNyK89dVj0Lbk1bf3PnEWxCS4itjUBRacDTcKiUqY8plr38ospnyPLxazkBBJB1qEjQ95c6gSsxscrcGNETcwD1uieGpVAgmbAA8ZfnuPpBCqnU5AHqNWvncDym2tFArcA+oM4mLhpHzRIwfrv7Qt3lxrVBmRfzn7rB1K0iAiGDZbpHtgO2mBJRzE3UtHPHXLS5YVvEFQMQ2ZtBWeAeRdOOEODIT/fVJLle2KAfkKQkGQBnS0=&pass_ticket=rVCKA0Ecb0m0B8lzvLpqbr0/FHv2xWW1+SNZJsYQprGu9QSKlAyyynehfbaiDl9h&wx_header=3)

有人用来代替 Claude Code ，真香 。
========================

Original开源日记开源日记

6200+ Star，这个项目太猛了。

![](.evernote-content/BE85D672-7EA3-4533-BF73-33651CE78D77/E7AF3692-D454-4C86-9E67-CBC219C771DE.png)

我看到社区里已经有人开始用来替换 Claude Code 了。

到底是什么神仙工具，敢挑战 Claude Code ?

它叫 oh-my-pi，**不用切 VS Code，待在终端里也能写代码、改代码、查 Bug，补全和提示照样有。**

![](.evernote-content/BE85D672-7EA3-4533-BF73-33651CE78D77/112006E1-3B0C-458B-B38E-77F109286B32.png)

有朋友会说 Claude Code 已经很牛X，为什么还要用 oh-my-pi ？

我总结出3点，供大家参考。

**01 能接入的模型种类更多。**

两个工具都要花 API 的钱，不过 oh-my-pi 能选的模型更多，成本上也更灵活。

看到这又有人要说了Claude Code也能接其它模型，是可以的，但要上点手段。

**02 使用它的开销相对来说会更小一些。**

oh-my-pi 的系统提示词只占 200 个 token，而 Claude Code，掏出来就是 10000 个 token。

同样是去完成写代码的任务，oh-my-pi 成本会更低。

**03 每一步怎么干的列的清清楚楚。**

我是一直在用 Claude Code的， 给我的使用感受，Claude Code 更像是一个黑箱，改了一段代码，你不知道它的整个操作过程。

而 oh-my-pi 不会跟你玩黑盒，它干了什么，你都看得见：调了哪个 API、改了哪些文件、花了多少钱，一清二楚。

它把 IDE 能力放进了终端。
---------------

**01 把 LSP 集到了终端里。**

以前像代码报错提示、跳转到定义、查找引用，还有重命名这些活儿，我基本都得切回 IDE 里面去操作。

现在不用了。

直接在终端里就可以全部搞定。

![](.evernote-content/BE85D672-7EA3-4533-BF73-33651CE78D77/DC1D4BCE-2545-4C8F-98CD-B62BD97019D7.jpg)

**02 具备代码调试能力。**

代码调试算得上是我日常工作中频率很高的一件事情。像 lldb、dlv，还有 debugpy 这一类调试器，都可以很顺畅地接进来。

不管是设断点、单步往下走，还是查看变量，AI 也能在旁边搭把手，陪你一起把整个调试流程往前推。

![](.evernote-content/BE85D672-7EA3-4533-BF73-33651CE78D77/E6D5EAF0-770B-4883-B867-88C01173FD15.jpg)

**03 能一直保留状态的 Python 环境。**

它内置了一套可以持续运行的 Python 执行环境，相当于是直接带了一个 IPython 内核。

你一边和 AI 对话，一边就能让它帮你跑 Python 代码，而且这个执行环境是会一直保留下来的。

上一轮定义的变量、导入过的库，不会凭空消失，下一轮可以直接接着往下用。

还有 Python 这边还能反过来去调用 AI 自身的那些工具。比方说读文件、搜索代码、拉起子任务之类的，全都能联动到一起。

也就是说，AI 不光能帮你写代码，它还能自己把一整套活儿从头到尾给串起来。

**04 同时处理多个任务。**

遇到大任务 。

它把任务都拆好后，就扔给不同子代理处理，各自在独立环境里干活，所有子代理做完后，把结果汇总起来。

做大项目和复杂重构时，这个就很实用。

![](.evernote-content/BE85D672-7EA3-4533-BF73-33651CE78D77/64FFCEA7-2A3C-410B-94C4-E3B04B99D83A.jpg)

**05 资源用的也更少了。**

它把 ripgrep、glob、shell 这些高频操作都放到了内部执行，不用再绕出去起进程。

这样做的好处是，终端更快，也更省资源。

**06 目前支持 40 多个提供商。**

不管你用哪路模型，基本都有得选。

OpenAI、Anthropic、Gemini 能接，本地的 Ollama、LM Studio 也支持，GLM-5、DeepSeek、Qwen 这些同样能跑。

![](.evernote-content/BE85D672-7EA3-4533-BF73-33651CE78D77/FCDE35EB-3550-4C38-B846-BF244B21C5FD.png)

**07 多模型路由。**

项目规划给 GLM-5，写代码交给 Qwen。

按我的经验，这样分着用，效果通常比一个模型全包更好。

**08 调用真实浏览器和 Electron 应用。**

这个能力在终端工具不多见。

oh-my-pi 终端可以直接调用真实浏览器和 Electron 应用。

![](.evernote-content/BE85D672-7EA3-4533-BF73-33651CE78D77/4048097E-135E-498E-B4E4-22BAB8E3E030.png)

默认开启隐身模式，网页正常渲染，看不出任何差异。

不光能操作浏览器，像 Slack 这种 Electron 应用也能驱动。

Slack 接进去之后，代理读消息就跟读网页差不多。

这个看家本领要单独拿出来说说。
---------------

我记得以前让 AI 改代码，经常碰到这种情况：它说把第 123 行改成什么，结果下一秒就报错——找不到这一行。

其实挺无语的。

有时候只是你中间插了几行代码，位置变了；或者复制的内容，跟原代码差了一个不容易发现的空格。

oh-my-pi 给了另外一种思路：

它给每一行代码，都配发了一张独属于自己的“身份证”。

这张“身份证”就叫哈希，是根据这行代码的具体内容计算出来的。

等到 AI 需要去修改代码的时候，它不会再跟你说**把第几行改成什么**，而是会告诉你**把哈希值是 xxx 的那行，改成什么**。

我给你打个比方。假如你有这样一行代码：

```
function add(a, b) {
```

oh-my-pi 就会为这行代码生成一个哈希值，类似这样 `x7y8z9w0`。

**传统方式**：

AI 会说，把第 1 行的 `function add` 改成 `function sum`。

问题就在于，你中间一改代码，原来的第 1 行可能早就对不上了。

**oh-my-pi 的做法**：

它不靠行号，而是直接认代码本身。

AI 会说，去改哈希值是 `x7y8z9w0` 的那一行。这样就算前面插了很多新代码，只要这行还在，它都能准确找到。

这样做的好处是不管中间插入再多代码。只要这行还在，它都能被精确地找到。

看似小小的优化，却能让你用起来更舒服。

想必有些人已经想上手了。
------------

Windows 和 macOS 都是一行命令都可以装上。

用 Windows 的朋友打开 PowerShell，复制执行。

```
irm https://omp.sh/install.ps1 | iex
```

macOS 和 Linux ，打开终端执行下面的命令。

```
curl -fsSL https://omp.sh/install | sh
```

装完以后很直接，终端里输入 pi，按提示把模型和 API key 配好，就能用了。

![](.evernote-content/BE85D672-7EA3-4533-BF73-33651CE78D77/6874A7A8-0E4F-40CC-926C-9C6B28B06051.png)

写在最后
----

读到这儿，又有朋友说了。

好家伙，又冒出一个新工具，光跟上节奏就已经让人头大了，哪里学得过来。

你就直接说 Claude Code 和 oh-my-pi 这俩，到底怎么选？

我的答案是：**两个都上手试试。**

Claude Code 用来做复杂重构和优化，oh-my-pi 就国产的模型，跑跑日常编码的活。

主打一个专业加省钱。

反正 oh-my-pi 是开源免费的，装上试试也不费电。

你说对吧？

项目基于 MIT 协议开放，感兴趣的同学可以去 GitHub 仓库看看源码和文档。

开源地址：https://github.com/can1357/oh-my-pi

既然都看到这儿了，顺手点个赞、在看、转发都行，也欢迎给我个星标⭐，好第一时间收到最新的文章，咱们下期见！

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=Mzg3NzU0NzIxMA==&mid=2247512321&idx=1&sn=3ceff59b88e60822d34f0483a3161c42&chksm=ce8b3998c2bfab7644d5fd771aafb469e83d5c8532815fea27d6a726ab42b81f8ace074c57b0&scene=90&xtrack=1&req_id=1779522096563956&sessionid=1779522314&subscene=93&clicktime=1779522413&enterid=1779522413&flutter_pos=0&biz_enter_id=4&ranksessionid=1779522096&jumppath=1001_1779522201661,1102_1779522203641,1001_1779522211162,1104_1779522314992&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004931&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQUGk6jN3gmT3cvyZr2/tN+RLTAQIE97dBBAEAAAAAAANpMt7xfIcAAAAOpnltbLcz9gKNyK89dVj0Lbk1bf3PnEWxCS4itjUBRacDTcKiUqY8plr38ospnyPLxazkBBJB1qEjQ95c6gSsxscrcGNETcwD1uieGpVAgmbAA8ZfnuPpBCqnU5AHqNWvncDym2tFArcA+oM4mLhpHzRIwfrv7Qt3lxrVBmRfzn7rB1K0iAiGDZbpHtgO2mBJRzE3UtHPHXLS5YVvEFQMQ2ZtBWeAeRdOOEODIT/fVJLle2KAfkKQkGQBnS0=&pass_ticket=rVCKA0Ecb0m0B8lzvLpqbr0/FHv2xWW1+SNZJsYQprGu9QSKlAyyynehfbaiDl9h&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/44746802-d338-430e-8d2f-1b74b582838b/44746802-d338-430e-8d2f-1b74b582838b/)