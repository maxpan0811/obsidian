# 国货之光DeepSeek永久2.5 折！以及我的DeepSeek+使用工具链

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzIzMzQyMzUzNw==&mid=224751...](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247516934&idx=1&sn=88b86ec76b8e955f430728b2b69beae7&chksm=e9aa851005f7e46807146d05d3d351390bdefb141924ad29b09915d6f38a9b0c4b86a179b9e3&scene=90&xtrack=1&req_id=1779538779944202&sessionid=1779537340&subscene=93&clicktime=1779539037&enterid=1779539037&flutter_pos=8&biz_enter_id=4&ranksessionid=1779538780&jumppath=20020_1779538881233,1104_1779539019721,20020_1779539022596,1104_1779539033440&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004932&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQHnYiEiuWUwlfMRPkNwB8jBLTAQIE97dBBAEAAAAAAKnvBmcQ888AAAAOpnltbLcz9gKNyK89dVj0OPPbGVsuLw3mTtPCwok74rmq34QTLuwo5bZKvn7uGY0L/UGTqAz8WOMcPBJmxrZgDH14urYKMUEeY3rKXibaYT8aPXmHPsLYe2LMJX81QbTM4ZDY7dUhW3IVoli6xKZRsRDYBuVSCNiFOE7ZzrLIlUctgKAxiJ4nxKFUFmRQrRMJ9CquQ+KMbhF8pa1zjp0NOV6Fpk0hrC5A2/8x4MUv9Ql1cPtFO9I4UsL+d2k=&pass_ticket=IHh9STt690gzyhGbdYBctZU88WaSrExBHzAnzPtxyCOTqJEacvhtBe4AK6dBCZHc&wx_header=3)

国货之光DeepSeek永久2.5 折！以及我的DeepSeek+使用工具链
======================================

Original字节笔记本 字节笔记本

国货之光DeepSeek官宣DeepSeek-V4-Pro  2.5 折优惠不再截止，永久有效！

![](.evernote-content/5369F11E-4B3F-4C7D-ABF3-2FC0D80DF96D/0B245CEF-9A72-42A3-8B0C-B0AD8B489CB7.png)

调整后缓存命中输入 0.025 元 / 百万 token，未命中输入 3 元，输出 6 元。

什么概念呢？

一次有完整工具调用的长程编码任务，DeepSeek V4 Pro 的成本大约是 Claude Sonnet 4.6 的 1/20、Gemini 3.5 Flash 的 1/31。

但降价本身不是重点。

重点是DeepSeek 已经进了大部分主流 agent 工具的接入列表，你现在可以把它嵌进整个工作流的不同层。

这篇文章分享我目前的DeepSeek+的工具链分工，以及每个工具里 DeepSeek 怎么接、为什么接在这里，充分享受国产之光的便宜价格和强大的模型能力。

工具链的分工逻辑
--------

脱离场景讲模型能力，都是在耍流氓。

比如重构老旧项目的架构，和把这 30 个文件改一遍的批量执行任务，对 harness 的要求完全不同。

前者需要稳定的判断和低错误率，后者需要高 context 利用率和低成本。把所有任务都堆在同一个工具里，要么过贵，要么不够用。

所以我的分法是：

Claude Code + Codex，主力判断层。

OpenCode + DeepSeek，长程执行层。

Hermes + DeepSeek，多通道自主 Agent 层。

pi-goal + DeepSeek，超长程目标层。

Warp+ DeepSeek，终端统一接入层。

分工清楚了，下面逐个讲配置。

---

一、Claude Code 接 DeepSeek
------------------------

接入Claude Code之后，DeepSeek特别适合长程批量执行任务，用于token 消耗大、但对判断质量要求没那么极致的场景。

如果你也使用这两个工具，建议主力判断项目规划核心逻辑可以跑Claude Code原生或者Codex。

至于说其他的，杀猪焉用牛刀了。

日常项目中的大部分任务，并非每一个都需要用到最顶级、最昂贵的模型。写文档、做单元测试，搞部署，迁移重构，Deepseek其实足以应对80%以上的场景。

以Claude Code为例子的配置使用。

**安装：**

npm install -g @anthropic-ai/claude-code
claude --version  # 验证安装

配置环境变量，写入 `.zshrc` 或 `.bashrc`：

export ANTHROPIC\_BASE\_URL=https://api.deepseek.com/anthropic
export ANTHROPIC\_AUTH\_TOKEN=<你的 DeepSeek API Key>
export ANTHROPIC\_MODEL=deepseek-v4-pro[1m]
export ANTHROPIC\_DEFAULT\_OPUS\_MODEL=deepseek-v4-pro[1m]
export ANTHROPIC\_DEFAULT\_SONNET\_MODEL=deepseek-v4-pro[1m]
export ANTHROPIC\_DEFAULT\_HAIKU\_MODEL=deepseek-v4-flash
export CLAUDE\_CODE\_SUBAGENT\_MODEL=deepseek-v4-flash
export CLAUDE\_CODE\_EFFORT\_LEVEL=max

这样的配置分工让主模型走 V4-Pro，1M的上下文，subagent 和辅助性轻量调用走 V4-Flash 省成本。

`ANTHROPIC_DEFAULT_HAIKU_MODEL` 对应的是 Claude Code 内部各种不需要强推理的快速调用，建议是Flash。

另外提一嘴，不太建议新手朋友直接使用CC Switch这类桌面端配置工具，非常容易污染系统的环境配置，我远程给几个朋友调试的时就会发现他们的各种环境都这种第三方工具被改得乱七八糟。

可以每次就直接将这种export内容复制粘贴写入到当前的会话当中，

一是可以精准地修改控制管理变量，很轻松地实现了在不同窗口使用不同的模型修改同一项目。

第二个是干净，用完即走，不会去修改和覆盖操作系统或者Claude Code的原生配置，造成环境变量的冲突。

毕竟调用链条越简单，那么中间出错概率就越少，有问题也更容易排查。

---

二、OpenCode 接 DeepSeek
---------------------

Claude Code 相当于高级架构师，适合关键决策和复杂推理，OpenCode + DeepSeek 是耐造的执行工程师，适合长时间、低成本、重复性的项目落地。

Claude Code够极客，但也因为太极客，很多东西需要自己再配置、再写规则、再配命令、再装插件。

OpenCode +DeepSeek的组合开箱即用，到手就已经是一个已经搭好的便宜又高效的工程执行环境，适合于做长程任务的执行者。

**安装和配置如下：**

opencode

![](.evernote-content/5369F11E-4B3F-4C7D-ABF3-2FC0D80DF96D/69A18418-B40D-416A-865E-1F56001C39D0.png)

进入之后：

1. 1. 输入框输入 `/connect`
2. 2. 输入 `deepseek`，选择供应商
3. 3. 填入 DeepSeek API Key
4. 4. 选择模型：`DeepSeek-V4-Pro`

不需要手动改配置文件，四步完成。

OpenCode我最常用的习惯就是先用Shift+Tab切换到`Plan Executor` 让 agent 把要做什么说清楚，确认之后再动手。

![](.evernote-content/5369F11E-4B3F-4C7D-ABF3-2FC0D80DF96D/BF9372EA-2D04-4A78-98CF-A0C29BED03C0.png)

这样 codebase 里有旧文件、混乱命名、失败测试、跨文件依赖，先规划再执行能在 agent 开始改动之前帮你发现弱逻辑。

---

三、Hermes 接 DeepSeek
-------------------

Hermes之前我们都有非常详细的介绍[马斯克Grok再掏家底！Hermes 秒变全能战士](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247516716&idx=1&sn=2dbbedb0f3f87db6bfab6d204af360c2&scene=21#wechat_redirect)

OpenCode 和 Claude Code 都是编码工具，没有通道接入和跨会话记忆的概念。

Hermes覆盖了这类日常应用场景，在非编程类的记住上下文、能在飞书里接消息、能自己学会新技能。

接入后，DeepSeek在这里负责推理，Hermes 负责框架调度。

**安装：**

curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash

**配置方式一：交互式向导（推荐）**

hermes model

![](.evernote-content/5369F11E-4B3F-4C7D-ABF3-2FC0D80DF96D/3238054B-0189-4C71-A239-6EC683507A33.png)

向导会依次提示：

1. 1. 选择供应商 → 选 `deepseek`
2. 2. 输入 API Key → 粘贴你的 DeepSeek API Key
3. 3. 选择模型 → `deepseek-v4-pro` 或 `deepseek-v4-flash`
4. 4. 确认保存 → 写入 `~/.hermes/config.yaml`

目前我只用flash，够便宜速度够快，天然的Hermes搭子。

四、pi-goal + DeepSeek
--------------------

OpenCode 和 Claude Code 的单次任务有 context 上限和轮次限制，跑不了真正的几十步才能完成的任务，即便后来出了goal，说实话也不太好用。

pi-goal就是专业来做goal长程任务的，它的 prompt cache工作模式和Deepseek非常的合拍。

实测一次完整任务下来，cache hit rate 能到 97% 以上，实际看到的 token 量很大，但只有不到 3% 按正价计费。

DeepSeek 目前cache read 单价是 0.025 元 / 百万 token，几乎可以忽略不计。

安装

curl -fsSL https://pi.dev/install.sh | sh
pi install npm:@mariozechner/pi-goal

先拿到 API Key，填进 ~/.pi/agent/models.json：

{
  "providers": {
    "deepseek": {
      "baseUrl": "https://api.deepseek.com",
      "api": "openai-completions",
      "apiKey": "DEEPSEEK\_API\_KEY",
      "models": [
        {
          "id": "deepseek-chat",
          "name": "DeepSeek V3",
          "contextWindow": 64000
        },
        {
          "id": "deepseek-reasoner",
          "name": "DeepSeek R1",
          "contextWindow": 64000,
          "reasoning": true
        }
      ]
    }
  }
}

具体的使用

/goal --tokens 200k 你的目标描述，写到能逐项 checklist 的颗粒度

goal的高级应用和写法可以看这里[Codex&Claude Code的 /goal 指令的高级进阶使用技巧](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247516287&idx=1&sn=b09eacc8e7f33cc93a927bc063a28fe7&payreadticket=HIeScNUb7TzJV6uneo8yIKer44gxPzD9dDS_cjEISrSaSB_jdz8qQ9a2gkTBKZWMJWWbyyo&scene=21#wechat_redirect)

五、Warp + DeepSeek
-----------------

Warp的官方正式版开通了自定义接口的接入，10 人以内团队免费。

接入Deepseek之后，相当于就拥有了目前市面上最好的命令行Agent工具，不用另外再掏一份20刀的订阅费用。

配置路径，自定义 Inference Endpoint打开 Warp，进入 `Settings → AI → Custom inference endpoint`，填入：

![](.evernote-content/5369F11E-4B3F-4C7D-ABF3-2FC0D80DF96D/F4FC6BCC-0AA2-4C90-B422-0D03508006FD.png)

* • Base URL：`https://api.deepseek.com/v1`
* • API Key：你的 DeepSeek API Key
* • Model：`deepseek-v4-pro`

![](.evernote-content/5369F11E-4B3F-4C7D-ABF3-2FC0D80DF96D/37D60053-E973-4C3A-822F-0703E507A2AB.png)

保存之后 Warp Agent 的所有请求都路由到 DeepSeek，不再在另外充值Warp会员。

![](.evernote-content/5369F11E-4B3F-4C7D-ABF3-2FC0D80DF96D/EC602533-A0C4-4301-BEEA-A72914C2AB7D.png)

另外，Warp 同时是 Claude Code、OpenCode、Codex 这些 CLI agent 的良好宿主。

它支持侧边栏快速切换，也支持 Rich Input Editor 支持在终端里直接给 agent 发多行 prompt、附上文件路径，比普通终端好用不少。

Deepseek降价之后，我又充了100多块钱，这个月算下来，也就花了140多元，相比较国产另外几家所谓的Coding Plan订阅套餐反而要便宜划算很多，目前Deepseek唯一的缺陷就是缺内置的多模态功能，如果加上，真的是无敌般的存在。

更多AI编程的高级使用技巧，以及Claude Code/Codex/Hermes系列请关注字节笔记本星球的每日推送，特别优惠码如下：

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247516934&idx=1&sn=88b86ec76b8e955f430728b2b69beae7&chksm=e9aa851005f7e46807146d05d3d351390bdefb141924ad29b09915d6f38a9b0c4b86a179b9e3&scene=90&xtrack=1&req_id=1779538779944202&sessionid=1779537340&subscene=93&clicktime=1779539037&enterid=1779539037&flutter_pos=8&biz_enter_id=4&ranksessionid=1779538780&jumppath=20020_1779538881233,1104_1779539019721,20020_1779539022596,1104_1779539033440&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004932&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQHnYiEiuWUwlfMRPkNwB8jBLTAQIE97dBBAEAAAAAAKnvBmcQ888AAAAOpnltbLcz9gKNyK89dVj0OPPbGVsuLw3mTtPCwok74rmq34QTLuwo5bZKvn7uGY0L/UGTqAz8WOMcPBJmxrZgDH14urYKMUEeY3rKXibaYT8aPXmHPsLYe2LMJX81QbTM4ZDY7dUhW3IVoli6xKZRsRDYBuVSCNiFOE7ZzrLIlUctgKAxiJ4nxKFUFmRQrRMJ9CquQ+KMbhF8pa1zjp0NOV6Fpk0hrC5A2/8x4MUv9Ql1cPtFO9I4UsL+d2k=&pass_ticket=IHh9STt690gzyhGbdYBctZU88WaSrExBHzAnzPtxyCOTqJEacvhtBe4AK6dBCZHc&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/22be716c-3e43-4e67-93f5-2d7c5deed461/22be716c-3e43-4e67-93f5-2d7c5deed461/)