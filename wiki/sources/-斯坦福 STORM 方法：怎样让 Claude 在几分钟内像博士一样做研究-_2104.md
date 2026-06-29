---
title: "斯坦福 STORM 方法：怎样让 Claude 在几分钟内像博士一样做研究"
type: source
created: 2026-06-27
updated: 2026-06-27
source_path: 印象笔记管理工具/斯坦福 STORM 方法：怎样让 Claude 在几分钟内像博士一样做研究.md
tags: [evernote, impression]
---
---
title: "斯坦福 STORM 方法：怎样让 Claude 在几分钟内像博士一样做研究"
source: evernote
type: note
export_date: 2026-06-23
guid: b2268b49-1d55-4789-81fa-17c06aa76ea3
---

# 斯坦福 STORM 方法：怎样让 Claude 在几分钟内像博士一样做研究

原文链接: [https://mp.weixin.qq.com/s?chksm=ec75f728db027e3e958a8a5f4e25566...](https://mp.weixin.qq.com/s?chksm=ec75f728db027e3e958a8a5f4e2556654278b60a93f74a1ddf76800013100894a68ce09dac9b&exptype=unsubscribed_card_recommend_article_u2i_mainprocess_coarse_sort_tlfeeds&ranksessionid=1782029952_1&req_id=1782029952718987&scene=169&mid=2247486276&sn=3dc846ddb3dd865c74ac9ec1b16fb1fc&idx=1&__biz=MzI5MzI2ODczOQ==&sessionid=1782029952&subscene=200&clicktime=1782030211&enterid=1782030211&flutter_pos=4&biz_enter_id=5&jumppath=WAWebViewController_1782030186543,WAWebViewController_1782030187041,20020_1782030199118,1104_1782030199809&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b28&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQFYpTur/mB8N38s5xeNYThxLTAQIE97dBBAEAAAAAADMRLAxIqMIAAAAOpnltbLcz9gKNyK89dVj0OA89PGSpXdf6RH7Zqo2Q6EK6ggSQ+g/p+TxgkuWjZetIKIo8FZUPno5tq2qAPf3mcrLLRvUTon2tYFtzWkgPb374msILAUwCDWOGUuPRW5wX0epH4XnH7/MPL/QSboVC491JC1E5MYEJ2ajWeVCJ6O6sVbQN9Qg7ip8mMRGjGv/xJdPTszRr+F2GmUnjN2M2QV/xmsjQcLWZfI2UR4mhjVDfe6ZIuTx7mAzi8hQ=&pass_ticket=I6S/Hs3GK/w1iorIW84e32vKGbm5xVV/h3lKDddZtkywiaD4qXbsPqQwZ704znT4&wx_header=3)

# 斯坦福 STORM 方法：怎样让 Claude 在几分钟内像博士一样做研究

Tom人工智能与安全笔记

大多数人用 Claude 的方式，其实和用搜索框差不多：提问、看答案、关标签页。这样做，等于把它最强的能力锁住了。

建议把这篇存起来。

斯坦福做过一个研究系统，叫 STORM。在同行评审测试里，它生成的文章组织度比第二名方法高出 25%。它是开源的。免费的。真正知道自己也能把同一套思路直接搬进 Claude 里跑的人，却几乎没有。

不需要软件。不需要 GitHub。不需要安装。只要复制粘贴。五分钟之后，你对一个主题的理解，可能会比那些花了几天时间四处读材料的人还更完整。

下面就是完整方法。

![](attachments/519870f29b8c1479.jpg)

## 第一阶段：STORM 到底是什么

STORM 的全称是 Synthesis of Topic Outlines through Retrieval and Multi perspective Question Asking（**通过检索和多视角提问来综合生成主题大纲**）。它由斯坦福 OVAL Lab 发布在 NAACL 2024 上。

你可以直接去 `storm.genie.stanford.edu` 体验在线版本。免费。不用注册。输入一个主题，然后看它实时写出一篇带引用来源的文章。

还有一个 12 分钟的演示视频：《STORM by Stanford on YouTube》。很值得至少看一遍。

完整代码在 `github.com/stanford-oval/storm`，MIT 许可证。如果你愿意，完全可以自己在本地电脑上跑起来。

但真正关键的地方在这里：你其实不需要上面任何东西。斯坦福方法本质上只是一种思考方式。你可以把同样的思考模式，直接放进 Claude 里，通过 4 个复制粘贴的提示词来跑。

这篇文章剩下的内容，讲的就是这件事。

![](attachments/f6b8fd3e33c0fc3a.jpg)

## 第二阶段：为什么“一条 prompt”永远不够

当你问 Claude “tell me about X” 时，你得到的通常是主流观点，是最常见的叙事方式，是表层答案。

你得不到的，是那个每天都在一线和 X 打交道的从业者；是那个觉得整个行业判断都错了的怀疑者；是那个专门追踪利益流向的经济观察者；是那个见过类似模式反复出现的历史研究者；是那个真的把论文读完了的学者。

这五种声音看到的，是五套不同的现实。这正是博士生会做的事情：他们不会只问一个问题，而是会问五种问题。

斯坦福这篇论文用数据证明了这一点：基于多视角构建出来的文章，在组织性上比普通方法高出 25%，在覆盖广度上高出 10%。这就是整个突破的核心。多视角提问能够抓住那些单次 prompt 研究根本看不见的盲点。

一个博士级别的研究任务，通常要花 40 到 60 小时的人类阅读时间。多数人拿不出这个时间。STORM 把它压缩了。下面这 4 个提示词，又把它继续压缩了一层。总共 5 分钟。

## 第三阶段：Prompt 1，多视角扫描

这是整个方法的核心。把下面这段提示词贴进 Claude，只需要把第一行里的主题换成你自己的。

```
I need to research [YOUR TOPIC].  
Simulate 5 different expert perspectives on this topic:  
1. THE PRACTITIONER: works with this daily.  
What do they know that academics miss?  
What practical realities are usually ignored?  
2. THE ACADEMIC: has studied this for years.  
What does the peer reviewed evidence actually say?  
Where does the evidence contradict popular belief?  
3. THE SKEPTIC: thinks the mainstream view is wrong.  
What is the strongest counterargument?  
What evidence do proponents conveniently ignore?  
4. THE ECONOMIST: follows the money.  
Who profits from the current narrative?  
What financial incentives shape the research?  
5. THE HISTORIAN: has seen similar patterns before.  
What historical parallels exist?  
What can we learn from how those played out?  
For each perspective give me:  
- Their core position in 2 sentences  
- The strongest evidence supporting their view  
- The one thing they would tell me that no other perspective would
```

你拿回来的，会是同一个主题的五种完全不同读法。实践者会看到学者忽略的现实；怀疑者会挑战实践者视为当然的东西；经济学视角会揭开学者常常不谈的激励机制；历史学视角则会提供经济视角看不到的长期模式。

这一步只花 60 秒，但它能抓住那些单个 prompt 永远发现不了的东西。

## 第四阶段：Prompt 2，矛盾地图

下一步，是让 Claude 去找出这五种声音彼此冲突的地方。真正的理解，通常就藏在这些冲突里。

```
Based on the 5 perspectives above, map the contradictions:  
1. Where do two or more perspectives directly contradict  
each other? List each conflict with the specific claims  
that clash.  
2. Which perspective has the strongest evidence?  
Which has the weakest? Why?  
3. What is the one question that, if answered, would  
resolve the biggest contradiction?  
4. What does EVERY perspective agree on?  
(This is likely true. Even opponents confirm it.)  
5. What topic did NONE of the perspectives address?  
(This is the blind spot in the whole field.  
Often the most valuable finding.)
```

你得到的，将是一张关于“专家们在哪些地方意见不合、为什么不合”的矛盾地图。大多数人会跳过这一步。但恰恰是这一步，区分了“表面理解”和“真正懂了”。

> 如果五个视角都同意某件事，那它大概率是真的。  
> 如果没有任何一个视角提到某个问题，那你很可能刚刚发现了整个领域的盲区。

![](attachments/80baa2726179abab.jpg)

## 第五阶段：Prompt 3，综合

现在，让 Claude 把前面的内容整合成一份研究简报。

```
Synthesize everything from the 5 perspectives and the  
contradiction map into a research briefing:  
1. THE ONE PARAGRAPH SUMMARY: explain this topic as if  
briefing a CEO who has 60 seconds and needs nuance,  
not just the headline.  
2. THE 5 KEY FINDINGS: most important things I now know,  
ranked by reliability. For each, note which perspectives  
support it and which challenge it.  
3. THE HIDDEN CONNECTION: one non obvious link between  
findings that only shows up when you look at all 5  
perspectives together.  
4. THE ACTIONABLE INSIGHT: based on all the evidence,  
what should someone in [YOUR ROLE] actually DO  
differently? Be specific.  
5. THE FRONTIER QUESTION: the one question that, if  
answered, would change everything about how we  
understand this topic.
```

你得到的，会是一份几乎没有任何单一专家能独立写出来的 briefing（**研究简报**）。它会同时纳入每个角度、明确指出冲突、给出可靠性排序，最后还会落到一个清晰的行动建议上。这本来是一个博士生可能要花 48 小时才能产出的东西，而你刚刚只用了大约 90 秒。

## 第六阶段：Prompt 4，同行评审

STORM 有一个已知弱点。斯坦福研究团队自己也明确指出过：这个系统不会主动自我批判。来源偏差和事实错配，会悄悄混进去。下面这段 prompt 的作用，就是让 Claude 给自己的成果打分和挑刺。

```
Now peer review your own research briefing:  
1. CONFIDENCE SCORES: rate each of the 5 key findings  
on a 1 to 10 scale for reliability. Explain each score.  
2. WEAKEST LINK: which claim are you least confident in?  
What specific info would you need to verify it?  
3. BIAS CHECK: which perspective might be overrepresented  
in your synthesis? Did one voice dominate?  
4. MISSING PERSPECTIVE: is there a 6th angle I should  
have included that would change the conclusions?  
5. OVERALL GRADE: if a Stanford professor reviewed this  
briefing, what grade would they give and why?  
What would they tell me to fix?
```

你得到的，将是一份对自己研究结果的诚实解读：哪些结论最强、哪些最弱、有哪些偏差、缺了什么视角。真正的同行评审通常要花几个月，而你刚刚在 60 秒里做完了一轮简化版。

![](attachments/f9c8ac726294fba3.jpg)

## 第七阶段：5 分钟工作流

第 1 分钟：跑 Prompt 1。你得到 5 种专家视角。

第 2 到第 3 分钟：跑 Prompt 2。你得到一张矛盾地图。

第 3 到第 4 分钟：跑 Prompt 3。你得到一份研究简报。

第 5 分钟：跑 Prompt 4。你知道哪些内容更可靠，哪些内容还需要怀疑。

总耗时：5 分钟。  
最终产出：一份多视角研究简报，包含矛盾分析、综合结论、明确行动建议，以及可靠性评分。

一个博士生手工完成这一切，大概要花 40 到 60 小时。不是因为他们慢，而是因为从 5 个角度阅读、梳理冲突、综合结论、自我批判，本来就是一个人脑需要几十小时才能认真做完的事。

![](attachments/7b1d54019e6ec98e.jpg)

## 第八阶段：从今天开始的 7 种用法

1. 1. 在写任何文章或报告之前，先跑这 4 个 prompt。你的内容会天然覆盖别人根本没想到的角度。
2. 2. 在做重大商业决策之前，先拿到 5 种视角。实践者会告诉你现实里什么真正有效；怀疑者会告诉你哪里最可能出错；经济学视角会告诉你谁在从中获利。
3. 3. 在面试之前，用这 5 个角度研究公司。实践者视角会让你掌握“圈内语言”；怀疑者视角会帮你准备尖锐问题。你走进房间时，会比在场大多数人准备得更充分。
4. 4. 在投资之前，快速搭出多头逻辑、空头逻辑、历史对照、激励结构和学术证据。矛盾地图会直接把真正的风险点暴露出来。
5. 5. 在学习一项新技能之前，用 5 个视角先把领域地图跑出来。实践者告诉你先学什么；学者告诉你理论基础；怀疑者告诉你什么被过度炒作。你可以直接跳过噪音。
6. 6. 在谈判之前，从 5 个视角研究对手。理解他们的激励、弱点和历史行为模式。你进场时就会拥有结构性优势。
7. 7. 在做任何演讲或展示之前，先对主题跑一遍 STORM。你的幻灯片会在观众提出质疑之前，先把反对意见回答掉。你的 Q&A 会显得异常轻松。

## Persona Block

你是那种会认真读东西的人。你会问难问题。你不想要那种只有 200 字、看起来很聪明、但实际上什么都没说的摘要。

你想真正理解一件事。而且要快。要有来源。最好像斯坦福研究生那样理解它。又不用真的付出六年学费。

这套方法，就是为这种人准备的。

如果你正是这种人，把这篇存起来。用这 4 个 prompt。你会立刻感受到差别。

![](attachments/9fe6eff4460fc03b.jpg)

## 那个不太舒服的事实

这里有一件没人真正大声说出来的事：

斯坦福团队在 2024 年就已经把这套方法发表出来了。论文经过同行评审。代码是开源的。在线工具免费可用。方法本身只需要 4 个 prompt。可真正去用的人，却少得惊人。

我们正处在一个大约 18 个月的窗口期。那些更早学会“正确使用 AI 做研究”的人，会显著胜过那些没学会的人。不是因为他们更聪明，而是因为他们在同时跑 5 个视角、做矛盾映射、做综合、再做一轮同行评审，而别人还停留在看 Google 第一条结果。

再过 18 个月，这类工作流大概率会被内建进几乎所有工具里。那时，这种优势就不再稀缺了。而今天，它仍然是一种摆在明面上、却很少有人真的用的秘密。

挑一个你现在最需要研究的主题。打开 Claude。贴上 Prompt 1。

五分钟之后，你知道的会比那些花了几天时间到处阅读的人还更多。

提示词已经在上面。斯坦福已经证明了这套方法。剩下的，就看你了。

希望这对你有用。Nav ❤️
