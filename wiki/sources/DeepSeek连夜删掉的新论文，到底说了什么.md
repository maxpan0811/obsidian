---
title: DeepSeek连夜删掉的新论文，到底说了什么
type: source
created: 2026-06-17
updated: 2026-06-17
source: 印象笔记管理工具
source_path: 印象笔记管理工具/DeepSeek连夜删掉的新论文，到底说了什么.html
tags: [AI技术, 教育]
---

# DeepSeek连夜删掉的新论文，到底说了什么

原文链接: https://mp.weixin.qq.com/s?__biz=MjM5MjAyNDUyMA==&mid=265108...

...Original发现明日产品的 APPSO 
昨晚 DeepSeek 多模态研究员陈小康在 X 上发了一条推，并公布了DeepSeek 关于多模态技术的新论文《Thinking with Visual Primitives》，表示「Excited to release」。
今天一早，推文删了，GitHub 上的论文也撤了。
但 APPSO 在它消失之前把全文读完了。读完之后觉得，这篇论文被撤可能不是因为内容有问题。恰恰相反，它可能透露了太多了。前天我们刚实测完 DeepSeek 的识图模式，让它数手指，它思考了一通，自己吐槽「我真的是数晕了」，然后答错了。当时以为是灰测阶段的小问题。
这篇论文告诉我们，数手指数晕这件事，背后藏着一个 GPT、Claude、Gemini 集体没解好的技术瓶颈。而 DeepSeek 给出的解法，说出来几乎有点可笑的朴素：给 AI 装一根手指。
陈小康在那条推文里写道：「Traditional CoT stays in the linguistic space, but visual reasoning needs more. By using points and boxes as cognitive anchors, our model bridges the Reference Gap—mimicking the "point-to-reason" synergy humans use.」「传统的思维链停留在语言空间里，但视觉推理需要更多。通过使用点和框作为认知锚点，我们的模型弥合了「引用鸿沟」，模拟了人类「边指边想」的协同机制。」看得清和指得准，是两回事目前所有多模态大模型做图像推理，本质都是把看到的画面转化成文字，然后在文字空间里做思维链推理。GPT-5.4、Claude-Sonnet-4.6、Gemini-3-Flash，全是这个路子。过去两年，OpenAI、Google、Anthropic 的改进方向集中在一个问题：怎么让模型看得更清楚。高分辨率裁切、动态分块、把图片放大再塞进去。DeepSeek 管这个叫 Perception Gap，感知鸿沟。但这篇论文指出了另一个瓶颈：Reference Gap，引用鸿沟。模型看清了，但在推理过程中没法精确指向图中的某个东西。你可以这样理解：一张图里 25 个人密密麻麻站在一起，你用语言去描述「左边第三排穿蓝色球衣那个人旁边的那个」，描述本身就是模糊的。模型数着数着就丢了上下文，忘了刚才数到谁。人类怎么解决这个问题？够原始的：伸出手指，指一个数一个。284B 参数的模型，装上了一根手指DeepSeek 的方案：让模型在思考过程中直接输出图片上的坐标。想象一下，模型看到一张图里有很多人，它的思维链不再是「我看到左边有个穿蓝衣服的人」，而是「我看到这个人」然后附上一个框的坐标，把人圈出来。每数一个人就圈一个框，圈完之后数框的数量就行了。两种坐标格式：一种是框（bounding box），画个矩形把物体圈住，适合标定物体位置；一种是点（point），在图上戳一个位置，适合追踪路径和走迷宫。DeepSeek 管这两种东西叫「视觉原语」，最小的思维单元。关键变化在这里：以前模型输出坐标是作为最终答案（「目标在这里」），现在坐标嵌入了思考过程本身。坐标是草稿纸上的标记，不是答卷上的答案。把一张图压缩 7056 倍，然后还能数清楚里面
