# 圣塔菲学者：AI 大语言模型真的理解人类语言吗？

---

智能摘要

作者认为，进一步拓展人工智能与自然科学的交叉研究，有望拓展多学科的审视角度，总结不同方法的优势边界，应对交叉认知理念的融合挑战。尽管AI系统在许多具体任务中表现出似乎智能的行为，但直到最近，人工智能研究界依然普遍认为机器无法像人类那样理解它们所处理的数据。正如不同的物种适应于不同的环境一样，我们的智能系统也将更好地适应于不同的问题。将继续青睐大规模的统计模型，如LLMs，而那些依赖有限知识和强大因果机制的问题将更青睐人类智能。

原文约 9884  字  | 图片 3 张 | 建议阅读 20 分钟 | [评价反馈](https://static.app.yinxiang.com/embedded-web/clipper/#/Evaluating?d=2023-04-21&nu=eba3ea89-8c34-4dde-88c8-281e589f5b4f&fr=myyxbj&ud=328ef&v=2&sig=424E8E2607C3C9FF113859D213F4A6E7)

圣塔菲学者：AI 大语言模型真的理解人类语言吗？
========================

原创 Mitchella等  集智俱乐部

收录于合集#复杂科学前沿2023179个

![](.evernote-content/4A010F02-AA50-481B-AC29-EFEF2C6A99CA/3057D326-C4A6-4107-B082-41921175C51B.jpg)

导语

**********尽管大语言模型表现出近似人类的理解能力，但 AI 系统真的可以像人类一样理解语言吗？机器理解的模式必须和人类理解相同吗？近日，圣塔菲研究所前所长克拉考尔和研究员梅拉尼·米歇尔在 PNAS 发表文章，探讨大型预训练语言模型（LLMs）是否能够以类似人类的方式理解语言及其所编码的物理和社会情境。**********

**********本文分别讨论赞成和反对的观点，并进一步探讨了更广泛的智能科学的关键问题。作者认为，进一步拓展人工智能与自然科学的交叉研究，有望拓展多学科的审视角度，总结不同方法的优势边界，应对交叉认知理念的融合挑战。**********

**************************关键词：人工智能，**大语言模型，心智模型****************************

![](.evernote-content/4A010F02-AA50-481B-AC29-EFEF2C6A99CA/37A8B77D-457B-4DB5-A72A-30509D1C9475.png)

Melanie Mitchella, David C. Krakauera | 作者

范思雨、张骥**| 译者**

梁金**| 编辑**

> 文章题目：
>
> The debate over understanding in AI’s large language models
>
> 文章地址：
>
> https://www.pnas.org/doi/10.1073/pnas.2215907120

什么是“理解”？这个问题长期以来一直吸引着哲学家、认知科学家和教育家们的关注。对“理解”的经典研究几乎都是以人类和其他动物为参照。然而，随着大规模人工智能系统，特别是大型语言模型的崛起，AI社区中出现了热烈的讨论：机器现在是否可以理解自然语言，从而理解语言所描述的物理和社会情境。

这场讨论不仅仅局限在自然科学的范畴；机器理解我们世界的程度和方式决定了我们在多大程度上能够相信AI与人类交互任务中的稳健和透明行为能力，包括AI驾驶汽车、AI诊断疾病、AI照顾老年人、AI教育儿童等等。同时，当前的讨论展现了一个智能系统进行“理解”的关键问题：如何判别统计相关性和因果机制？

尽管AI系统在许多具体任务中表现出似乎智能的行为，但直到最近，人工智能研究界依然普遍认为机器无法像人类那样理解它们所处理的数据。例如：人脸识别软件不理解面部是身体的一部分、面部表情在社交互动中的作用、"面对"不愉快的情境意味着什么，或者做鬼脸的方式方法。同样，语音转文字和机器翻译程序不理解它们处理的语言，自动驾驶系统也不理解驾驶员和行人在规避事故时的微表情和肢体语言。因此，这些AI系统常常被认为是脆弱的，缺乏“理解”的关键证据是，它们不可预测错误、泛化能力缺乏鲁棒性[1]。

### **大语言模型真的理解语言吗？**

然而，过去几年情况发生了转变，一种新型的AI系统在研究界广受欢迎并产生了影响，改变了一些人对机器理解语言的前景和看法。这些系统被称为大型语言模型（LLMs）、大型预训练模型或基础模型[2]，它们是具有数十亿到数万亿参数（权重）的深度神经网络，被“预训练”于数TB的巨大自然语言语料库上，包括大量网络快照、在线图书和其他内容。在训练期间，这些网络的任务是预测输入句子中的隐藏部分，这种方法被称为“自监督学习”。最终的网络是其训练数据中的单词和短语之间相关性的复杂统计模型。

这些模型可以用来生成自然语言，进行特定语言任务的微调[3]，或进一步训练以更好地匹配“用户意图”[4]。例如，OpenAI的著名GPT-3[5]、更近期的ChatGPT[6]和Google的PaLM[7]这样的LLMs能够产生惊人的类人文本和对话；此外，尽管这些模型并没有以推理为目的开展训练，一些研究认为它们具有类人的推理能力[8]。LLMs 如何完成这些壮举对于普通人和科学家来说都是个谜。这些网络内部的运作方式大都不透明，即使是构建它们的研究人员对于如此巨大规模的系统也只有些许直观感受。神经科学家 Terrence Sejnowski 这样描述LLM的出现：“奇点降临，似天外来客，忽纷沓而来，语四国方言。我们唯一清楚的是，LLMs 不是人类……它们的某些行为看起来是智能的，但如果不是人类的智能，又是什么呢？”[9]

尽管最先进的LLMs很令人印象深刻，它们仍然容易出现不像人类的脆弱性和错误。然而，这样的网络缺陷在其参数数量和训练数据集规模扩大时显著改进[10]，因而一些研究者认为LLMs（或者其多模态版本）将在足够大的网络和训练数据集下实现人类级别的智能和理解能力，出现了一个AI新口号：“规模就是一切”[11, 12]。

上述主张是AI学界在LLMs讨论中的一个流派。一部分人认为这些网络真正理解了语言，并且能够以一种普遍的方式进行推理（虽然“尚未”达到人类水平）。例如，谷歌的LaMDA系统通过预先训练文本，再微调对话的方式构造了一个谈吐流畅的对话系统[13]，某AI研究者甚至认为这样的系统“对大量概念具备真实理解能力”[14]，甚至“朝着有意识的方向迈进”[15]。另一位机器语言专家将LLMs视为通向一般人类水平AI的试金石：“一些乐观研究者认为，我们见证了具有一定普遍智能程度的知识注入系统诞生”[16]。另一些人士认为，LLMs很可能捕捉到了意义的重要方面，而且其工作方式近似于人类认知的一个引人注目的解释，即意义来源于概念角色。”[17]。反对者被挂上“AI否认主义”标签[18]。

另一方面，有人认为尽管像GPT-3或LaMDA这样的大型预训练模型的输出很流利，但仍然不能具备理解能力，因为它们没有世界的经验或思维模式；LLMs的文本预测训练只是学会了语言的形式，而不是意义[19-21]。最近一篇文章认为：“即使从现在开始一直训练到宇宙热寂，单凭语言训练的系统永远也不会逼近人类智能，而且这些系统注定只能拥有肤浅的理解，永远无法逼近我们在思考上的全面性”[22]。还有学者认为，把“智能”、“智能体”和“理解”等概念套用在LLMs身上是不对的，因为LLMs更类似于图书馆或百科全书，是在打包人类的知识存储库，而不是智能体[23]。例如，人类知道“挠痒痒”会让我们笑，是因为我们有身体。LLMs可以使用“挠痒痒”这个词，但它显然从未有过这种感觉。理解挠痒痒不是两个词之间的映射，而是词和感觉之间的映射。

那些持“LLMs无法真正理解”立场的人认为，我们惊讶的不是LLMs流畅程度本身，而是流畅程度随模型规模的增长超乎直觉这件事情。任何将理解或意识归因于LLMs的人都是“伊莱扎效应（Eliza effect）”的受害者[24]。“伊莱扎效应”是指我们人类倾向于将理解和代理能力归因于具有即使是微弱的人类语言或行为迹象的机器，得名于Joseph Weizenbaum在1960年代开发的聊天机器人“Eliza”，尽管非常简单，仍然欺骗了人们相信它理解了他们[25]。

2022年对自然语言处理领域活跃学者的一项调查亦佐证了这场讨论的观点分歧。其中一项调查内容是询问受访者是否同意以下关于LLMs是否在原则上理解语言的说法：“一些仅在文本上训练的生成模型（即语言模型），在给定足够的数据和计算资源的情况下，可以在某些非平凡意义上理解自然语言。”480人的答案几乎一半（51％）对一半（49％）[26]。

支持者佐证当前LLMs具备理解能力的重要依据是模型能力表现：既包括对模型根据提示词生成文本的主观质量判断（尽管这种判断可能容易受到Eliza效应的影响），亦包括在用于评估语言理解和推理能力的基准数据集客观评价。例如，评估LLMs的两个常用基准数据集是通用语言理解评估（GLUE）[27]及其后继者SuperGLUE[28]，它们包括大规模的数据集和任务，如“文本蕴含”（给定两个句子，第二个句子的意思是否可以从第一个句子推断出来？），“情景含义”（在两个不同的句子中，给定的词语是否有相同的意义?）和逻辑回答等。OpenAI的GPT-3（具有1750亿个参数）在这些任务上表现出人意料之外的好[5]，而Google的PaLM（具有5400亿个参数）在这些任务上表现得更好[7]，能够达到甚至超越人类在相同任务上的表现。

### **机器理解必须重现人类理解吗？**

这些结果对LLMs的理解有何启示？从“泛化语言理解”，“自然语言推理”，“阅读理解”和“常识推理”等术语的选择不难看出，上述基准数据集的测试暗含机器必须重现人类理解方式的前提假设。但这是“理解”必须的吗？并非一定如此。以“论证推理理解任务”基准评估为例[29]，在每个任务示例中，都会给出一个自然语言的“论据”，以及两个陈述句；任务是确定哪个陈述句与论据一致，如下例所示：

论点：罪犯应该有投票权。一个在17岁时偷了一辆车的人不应该被终身剥夺成为完整公民的权利。

推断A：盗窃汽车是一项重罪。

推断B：盗窃汽车不是一项重罪。

BERT在这项基准任务中获得了近似人类的表现[31]。或许我们能够由此得出结论，即BERT可以像人类一样理解自然语言。但一个研究小组发现，在推断语句中出现的某些线索词（例如“not”）能够辅助模型预测出正确答案。当研究人员变换数据集来避免这些线索词出现时，BERT的表现性能变得和随机猜测无异。这是一个明显的依靠捷径学习（shortcut learning）的例子——一个在机器学习中经常被提及的现象，即学习系统通过分析数据集中的伪相关性，而不是通过类人理解（humanlike understanding），来获得在特定基准任务上的良好表现[32-35]。

通常情况下，这种相关性对于执行相同任务的人类来说表现得并不明显。虽然捷径学习现象在评估语言理解和其他人工智能模型的任务中已经被发现，但仍可能存在很多未被发现的“捷径”存在。像谷歌的LaMDA和PaLM这种拥有千亿参数规模、在近万亿的文本数据上进行训练的预训练语言模型，拥有强大的编码数据相关性的能力。因此，用于评估人类理解能力的基准任务或许对这类模型评估来说并不适用[36-38]。对于大规模LLMs（以及LLMs可能的衍生模型）来说，通过复杂的统计相关性计算能够让模型绕开类人理解能力，获得近乎完美的模型表现。

虽然“类人理解”一词没有严格的定义，但它本质上并不是基于当下LLMs所学习的这类庞大的统计模型；相反，它基于概念——外部类别、情况和事件的内部心智模型，以及人类自身的内部状态和“自我”的内部心智模型。对于人类来说，理解语言（以及其他非语言信息）依赖于对语言（或其他信息）表达之外的概念的掌握，并非局限于理解语言符号的统计属性。事实上，在认知科学领域的过往研究历史中，一直强调对概念本质的理解以及理解力是如何从条理清晰、层次分明且包含潜在因果关系的概念中产生的。这种理解力模型帮助人类对过往知识和经验进行抽象化以做出稳健的预测、概括和类比；或是进行组合推理、反事实推理；或是积极干预现实世界以检验假设；又或是向他人阐述自己所理解的内容。

毫无疑问，尽管有些规模越来越大的LLMs零星地表现出近似人类的理解能力，但当前的人工智能系统并不具备这些能力，包括最前沿的LLMs。有人认为，这种理解能力能够赋予人类纯统计模型无法获得的能力。尽管大模型展现出了非凡的形式语言能力（formal linguistic competence）——即产生语法流利、类人语言的能力，它仍然缺乏基于概念理解的类人功能语言能力（humanlike functional language abilities）——即在现实世界中正确理解和使用语言的能力。有趣的是，物理学研究中也有类似的现象，即数学技法的成功运用和这种功能理解能力之间的矛盾。例如，一直以来关于量子力学的一个争议是，它提供了一种有效的计算方法，而没有提供概念性理解。

关于概念的本质理解一直以来是学界争论的主题之一。对于概念在多大程度上是领域特定的和先天的，而不是更通用的和习得的[55-60]，或者概念在多大程度上是基于具象隐喻的，并通过动态的、基于情境的模拟在大脑中呈现[64]，又或者概念在何种条件下是由语言[65–67]、社会学习[68–70]和文化支撑的[71–73]，研究人员在这些方面存在分歧。

尽管存在以上争论，概念——就像前文所述的那样以因果心智模型的形式存在——一直以来被认为是人类认知能力的理解单元。毫无疑问，纵观人类理解能力的发展轨迹，不论是个人理解还是集体理解，都可以抽象为对世界进行高度压缩的、基于因果关系的模型，类似于从托勒密的行星公转理论到开普勒的椭圆轨道理论，再到牛顿根据引力对行星运动的简明和因果关系的解释。与机器不同的是，人类似乎在科学研究以及日常生活中都有追求这种理解形式的强烈内驱力。我们可以将这种动力描述为需要很少的数据，极简的模型，明确的因果依赖性和强大的机械直觉。

关于LLMs理解能力的争论主要集中以下几个方面：

1）这些模型系统的理解能力是否仅仅为一种类别错误？（即，将语言符号之间的联系混淆为符号与物理、社会或心智体验之间的联系）。简而言之，这些模型系统永远无法获得类人的理解能力吗？

或者，相反地，2）这些模型系统（或者它们近期的衍生模型）真的会在缺乏现实世界经验的情况下，创造出对人类理解来说至关重要的大量的基于概念的心智模型吗？如果是的话，增大模型规模是否会创造出更好的概念？

或者，3）如果这些模型系统无法创造这样的概念，那么它们难以想象的庞大的统计相关性系统是否能产生与人类理解功能相当的能力呢？又或者，这是否意味着人类无法达到的新形式的高阶逻辑能力成为可能？从这一角度上看，将这种相关性称为“伪相关性”或质疑“捷径学习”现象是否仍然合适？将模型系统的行为视为一系列新兴的、非人类的理解活动，而不是“没有理解能力”，是否行得通？这些问题已不再局限于抽象的哲学探讨，而是涉及到人工智能系统在人类日常生活中扮演的越来越重要的角色所带来的能力、稳健性、安全性和伦理方面的非常现实的担忧。

虽然各派研究者对于“LLMs理解能力”的争论都有自身的见解，但目前用于获得理解洞察力的基于认知科学的方法不足以回答关于LLMs的这类问题。事实上，一些研究人员已经将心理测试应用于LLMs，这些测试最初是用来评估人类理解和推理机制的。发现LLMs在某些情况下确实在心理理论测试[14, 75]中表现出类似人类的反应，以及在推理评估中表现出类似人类的能力和偏好 [76–78]。虽然这种测试被认为是评估人类通用能力的替代性测试，但对人工智能模型系统来说可能并非如此。

### **一种新兴的理解能力**

正如前文所提到的，LLMs有一种难以解释的能力，可以在训练数据和输入中学习信息符号之间的相关性，并且可以使用这种相关性来解决问题。相比之下，人类似乎应用了反映他们现实世界经验的被压缩的概念。当把为人类设计的心理测试应用于LLMs时，其解释结果往往依赖于对人类认知的假设，而这些假设对于模型来说可能根本不正确。为了取得进展，科学家们需要设计新的基准任务和研究方法，以深入了解不同类型的智能和理解机制，包括我们已经创造的“异类的、类似思维实体”（exotic, mind-like entities）[79] 的新形式，或许我们正在踏上通往挖掘“理解”本质的正确道路上[80, 81]。

随着关于LLMs理解能力的讨论声音越来越多，以及更多有能力的模型系统的出现，这一切似乎都在强调未来有必要加强对于智能科学的研究，以便对人类和机器的更广泛理解概念进行理解。正如神经科学家Terrence Sejnowski 所指出的，“专家们对LLMs智能的分歧表明，我们基于自然智能的传统观念是不够充分的。[9]”如果LLMs和其他模型成功地利用了强大的统计相关性，也许也可以被认为是一种新兴的“理解”能力，一种能够实现非凡的、超人的预测能力。比如DeepMind的AlphaZero和AlphaFold模型系统 [82, 83]，它们似乎分别为国际象棋和蛋白质结构预测领域带来了一种来自“外星”的直觉形式[84, 85]。

因此可以这样说，近年来在人工智能领域出现了具有新兴理解模式的机器，这或许是一个更大的相关概念动物园（zoo of related concepts）中的新物种。随着我们在追求智能本质的过程中所取得的研究进展，这些新兴的理解模式将不断涌现。正如不同的物种适应于不同的环境一样，我们的智能系统也将更好地适应于不同的问题。依赖大量的历史的编码知识（encoded knowledge）的问题（强调模型性能表现）将继续青睐大规模的统计模型，如LLMs，而那些依赖有限知识和强大因果机制的问题将更青睐人类智能。未来的挑战是开发出新的研究方法，以详细揭示不同智能形式的理解机制，辨别它们的优势和局限性，并学习如何整合这些不同的认知模式。

参考文献

[1]M. Mitchell, Artiﬁcial intelligence hits the barrier of meaning. Information 10, 51 (2019).

[2]R. Bommasani et al., On the opportunities and risks of foundation models. arXiv [Preprint] (2021). http://arxiv.org/abs/2108.07258(Accessed 7 March 2023).

[3]B. Min et al., Recent advances in natural language processing via large pre-trained language models: A survey. arXiv [Preprint] (2021). http://arxiv.org/abs/2111.01243(Accessed 7 March 2023).

[4]L. Ouyang et al., Training language models to follow instructions with human feedback. arXiv [Preprint] (2022). http://arxiv.org/abs/2203.02155(Accessed 7 March 2023).

[5]T. Brown et al., Language models are few-shot learners. Adv. Neural Inf. Process. Syst. 33, 1877-1901 (2020).

[6]J.Schulman et al., ChatGPT: Optimizing language models for dialogue. UpToDate (2022). https://openai.com/blog/chatgpt. Accessed 7 March 2023.

[7]A. Chowdhery et al., PaLM: Scaling language modeling with Pathways. arXiv [Preprint] (2022). http://arxiv.org/abs/2204.02311(Accessed 7 March 2023).

[8]J. Wei et al., Chain of thought prompting elicits reasoning in large language models (2022). http://arxiv.org/abs/2201.11903(Accessed 7 March 2023).

[9]T. Sejnowski, Large language models and the reverse Turing test. arXiv [Preprint] (2022). http://arxiv.org/abs/2207.14382(Accessed 7 March 2023).

[10]J. Wei et al., Emergent abilities of large language models. arXiv [Preprint] (2022). http://arxiv.org/abs/2206.07682(Accessed 7 March 2023).

[11]N. de Freitas, 14 May 2022. https://twitter.com/NandoDF/status/1525397036325019649. Accessed 7 March 2023.

[12]A. Dimakis, 16 May 2022. https://twitter.com/AlexGDimakis/status/1526388274348150784. Accessed 7 March 2023.

[13]R. Thoppilan et al., LaMDA: Language models for dialog applications. arXiv [Preprint] (2022). http://arxiv.org/abs/2201.08239(Accessed 7 March 2023).

[14]B. A. y Arcas, Do large language models understand us? UpToDate (2021). http://tinyurl.com/38t23n73. Accessed 7 March 2023.

[15]B. A. y Arcas, Artiﬁcial neural networks are making strides towards consciousness. UpToDate (2022). http://tinyurl.com/ymhk37uu. Accessed 7 March 2023.

[16]C. D. Manning, Human language understanding and reasoning. Daedalus 151, 127– 138 (2022).

[17]S. T. Piantasodi, F. Hill, Meaning without reference in large language models. arXiv [Preprint] (2022). http://arxiv.org/abs/2208.02957(Accessed 7 March 2023).

[18]B. A. y Arcas, Can machines learn how to behave? UpToDate (2022). http://tinyurl.com/mr4cb3dw(Accessed 7 March 2023).

[19]E. M. Bender, A. Koller, Climbing towards NLU: On meaning, form, and understanding in the age of data" in Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics (2020), pp. 5185–5198.

[20]E. M. Bender, T. Gebru, A. McMillan-Major, S. Shmitchell, On the dangers of stochastic parrots: Can language models be too big? in Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency (2021), pp. 610–623.

[21]G. Marcus, Nonsense on stilts. Substack, 12 June 2022. https://garymarcus.substack.com/p/nonsense-on-stilts.

[22]J. Browning, Y. LeCun, AI and the limits of language. UpToDate (2022)https://www.noemamag.com/ai-and-the-limits-of-language. Accessed 7 March 2023.

[23]A. Gopnik, What AI still doesn’t know how to do. UpToDate (2022).https://www.wsj.com/articles/what-ai-still-doesnt-know-how-to-do-11657891316. Accessed 7 March 2023.

[24]D. R. Hofstadter, Fluid Concepts and Creative Analogies: Computer Models of the Fundamental Mechanisms of Thought (Basic Books, Inc., New York, NY, 1995).

[25]J. Weizenbaum, Computer Power and Human Reason: From Judgment to Calculation (WH Freeman & Co, 1976).

[26]J. Michael et al., What do NLP researchers believe? Results of the NLP community metasurvey. arXiv [Preprint] (2022).http://arxiv.org/abs/2208.12852(Accessed 7 March 2023).

[27]A. Wang et al.,"GLUE: A multi-task benchmark and analysis platform for natural language understanding"in Proceedings of the 2018 EMNLP Workshop BlackboxNLP: Analyzing and Interpreting Neural Networks for NLP (Association for Computational Linguistics, 2018), pp. 353-355.

[28]A. Wang et al., SuperGLUE: A stickier benchmark for general-purpose language understanding systems. Adv. Neural Inf. Process. Syst. 32, 3266–3280 (2019).

[29]I. Habernal, H. Wachsmuth, I. Gurevych, B. Stein, "The argument reasoning comprehension task: Identfication and reconstruction of implicit warrants" in Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (2018), pp. 1930–1940.

[30]J. Devlin, M.-W. Chang, K. Lee, K. Toutanova, "BERT: Pre-training of deep bidirectional transformers for language understanding" in Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (2019), pp. 4171–4186.

[31]T. Niven, H.-Y. Kao, Probing neural network comprehension of natural language arguments" in Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics (2019), pp. 4658–4664.

[32]R. Geirhos et al., Shortcut learning in deep neural networks. Nat. Mach. Intell. 2, 665–673 (2020).

[33]S. Gururangan et al., "Annotation artifacts in natural language inference data" in Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (2018), pp. 107–112.

[34]S. Lapuschkin et al., Unmasking Clever Hans predictors and assessing what machines really learn. Nat. Commun. 10, 1–8 (2019).

[35]R T. McCoy, E. Pavlick, T. Linzen, "Right for the wrong reasons: Diagnosing syntactic heuristics in natural language inference" in Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics (2019), pp. 3428–3448.

[36]S. R. Choudhury, A. Rogers, I. Augenstein, Machine reading, fast and slow: When do models 'understand’language? arXiv [Preprint] (2022). http://arxiv.org/abs/2209.07430(Accessed 7 March 2023).

[37]M. Gardner et al., "Competency problems: On finding and removing artifacts in language data" in Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing (2021).

[38]T. Linzen, How can we accelerate progress towards human-like linguistic generalization? in Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics (2020), pp. 5210–5217.

[39]C. Baumberger, C. Beisbart, G. Brun, "What is understanding? An overview of recent debates in epistemology and philosophy of science" in Explaining Understanding: New Perspectives from Epistemology and Philosophy ofScience (Routledge, 2017), pp. 1–34.

[40]J. L. Kvanvig, "Knowledge, understanding, and reasons for belief" in The Oxford Handbook of Reasons and Normativity (Oxford University Press, 2018), pp. 685–705.

[41]M. B. Goldwater, D. Gentner, On the acquisition of abstract knowledge: Structural alignment and explication in learning causal system categories. Cognition 137, 137–153 (2015).

[42]A. Gopnik, “Causal models and cognitive development”in Probabilistic and Causal Inference: The Works ofJudea Pearl, H. Geffner, R. Dechter, J. Y. Halpern, Eds. (Association for Computing Machinery, 2022), pp. 593–604.

[43]D. R. Hofstadter, E. Sander, Surfaces and Essences: Analogy as the Fuel and Fire of Thinking. Basic Books (2013).

[44]F. C. Keil, Explanation and understanding. Ann. Rev. Psychol. 57, 227 (2006).

[45]M. Lake, T. D. Ullman, J. B. Tenenbaum, S. J. Gershman, Building machines that learn and think like people. Behav. Brain Sci. 40 (2017).

[46]S. A. Sloman, D. Lagnado, Causality in thought. Ann. Rev. Psychol. 66, 223–247 (2015).

[47]P. Smolensky, R. McCoy, R. Fernandez, M. Goldrick, J. Gao, Neurocompositional computing: From the central paradox of cognition to a new generation of AI systems. AI Mag. 43, 308–322 (2022).

[48]H. W. De Regt, Discussion note: Making sense of understanding. Philos. Sci. 71, 98–109 (2004).

[49]D. George, M. Lázaro-Gredilla, J. S. Guntupalli, From CAPTCHA to commonsense: How brain can teach us about artiﬁcial intelligence. Front. Comput. Neurosci. 14, 554097 (2020).

[50]B. M. Lake, G. L. Murphy, Word meaning in minds and machines. Psychol. Rev. (2021).

[51]J. Pearl, Theoretical impediments to machine learning with seven sparks from the causal revolution. arXiv [Preprint] (2018).http://arxiv.org/abs/1801.04016(Accessed 7 March 2023).

[52]M. Strevens, No understanding without explanation. Stud. Hist. Philos. Sci. A. 44, 510–515 (2013).

[53]K. Mahowald et al., Dissociating language and thought in large language models: a cognitive perspective. arXiv [Preprint] (2023).http://arxiv.org/abs/2301.06627(Accessed 7 March 2023).

[54]D. C. Krakauer, At the limits of thought. UpToDate (2020).https://aeon.co/essays/will-brains-or-algorithms-rule-the-kingdom-of-science. Accessed 7 March 2023.

[55]S. Carey, “On the origin of causal understanding”in Causal Cognition: A Multidisciplinary Debate, D. Sperber, D. Premack, A. J. Premack, Eds. (Clarendon Press/Oxford University Press, 1995), pp. 268–308.

[56]N. D. Goodman, T. D. Ullman, J. B. Tenenbaum, Learning a theory of causality. Psychol. Rev. 118, 110 (2011).

[57]A. Gopnik, A uniﬁed account of abstract structure and conceptual change: Probabilistic models and early learning mechanisms. Behav. Brain Sci. 34, 129 (2011).

[58]J. M. Mandler, How to build a baby: II. Conceptual primitives. Psychol. Rev. 99, 587 (1992).

[59]E. S. Spelke, K. D. Kinzler, Core knowledge. Dev. Sci. 10, 89–96 (2007).

[60]H. M. Wellman, S. A. Gelman, Cognitive development: Foundational theories of core domains. Ann. Rev. Psychol. 43, 337–375 (1992).

[61]R. W. Gibbs, Metaphor Wars (Cambridge University Press, 2017).

[62]G. Lakoff, M. Johnson, The metaphorical structure of the human conceptual system. Cogn. Sci. 4, 195–208 (1980).

[63]G. L. Murphy, On metaphoric representation. Cognition 60, 173–204 (1996).

[64]L. W. Barsalou et al., Grounded cognition. Ann. Rev. Psychol. 59, 617–645 (2008).

[65]J. G. De Villiers, P. A. de Villiers, The role of language in theory of mind development. Topics Lang. Disorders 34, 313–328 (2014).

[66]G. Dove, More than a scaffold: Language is a neuroenhancement. Cogn. Neuropsychol. 37, 288–311 (2020).

[67]G. Lupyan, B. Bergen, How language programs the mind. Topics Cogn. Sci. 8, 408–424 (2016).

[68]N. Akhtar, M. Tomasello, “The social nature of words and word learning”in Becoming a Word Learner: A Debate on Lexical Acquisition (Oxford University Press, 2000), pp. 115– 135.

[69]S. R. Waxman, S. A. Gelman, Early word-learning entails reference, not merely associations. Trends Cogn. Sci. 13, 258–263 (2009).

[70]S. A. Gelman, Learning from others: Children’s construction of concepts. Ann. Rev. Psychol. 60, 115– 140 (2009).

[71]A. Bender, S. Beller, D. L. Medin, “Causal cognition and culture”in The Oxford Handbook of Causal Reasoning (Oxford University Press, 2017), pp. 717–738.

[72]M. W. Morris, T. Menon, D. R. Ames,”Culturally conferred conceptions of agency: A key to social perception of persons, groups, and other actors”in Personality and Social Psychology Review (Psychology Press, 2003), pp. 169–182.

[73]A. Norenzayan, R. E. Nisbett, Culture and causal cognition. Curr. Direc. Psychol. Sci. 9, 132– 135 (2000).

[74]A. Gopnik, H. M. Wellman, “The theory theory”in Domain Speciﬁcity in Cognition and Culture (1994), pp. 257–293.

[75]S. Trott, C. Jones, T. Chang, J. Michaelov, B. Bergen, Do large language models know what humans know? arXiv [Preprint] (2022). http://arxiv.org/abs/2209.01515(Accessed 7 March 2023).

[76]M. Binz, E. Schulz, Using cognitive psychology to understand GPT-3. arXiv [Preprint] (2022). http://arxiv.org/abs/2206.14576(Accessed 7 March 2023).

[77]I. Dasgupta et al., Language models show human-like content effects on reasoning. arXiv [Preprint] (2022). http://arxiv.org/abs/2207.07051(Accessed 7 March 2023).

[78]A. Laverghetta, A. Nighojkar, J. Mirzakhalov, J. Licato, “Predicting human psychometric properties using computational language models”in Annual Meeting of the Psychometric Society (Springer, 2022), pp. 151–169.

[79]M. Shanahan, Talking about large language models. arXiv [Preprint] (2022). http://arxiv.org/abs/2212.03551(Accessed 7 March 2023).

[80]B. Z. Li, M. Nye, J. Andreas, “Implicit representations of meaning in neural language models” in Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (2021), pp. 1813–1827.

[81]C. Olsson et al., In-context learning and induction heads. arXiv [Preprint] (2022). http://arxiv.org/abs/2209.11895(Accessed 7 March 2023).

[82]J. Jumper et al., Highly accurate protein structure prediction with AlphaFold. Nature 596, 583–589 (2021).

[83]D. Silver et al., Mastering chess and shogi by self-play with a general reinforcement learning algorithm. arXiv [Preprint] (2017).http://arxiv.org/abs/1712.01815(Accessed 7 March 2023).

[84]D. T. Jones, J. M. Thornton, The impact of AlphaFold2 one year on. Nat. Methods 19, 15–20 (2022).

[85]M. Sadler, N. Regan, Game changer: AlphaZero’s Groundbreaking Chess Strategies and the Promise ofAI. Alkmaar (New in Chess, 2019).

（参考文献可上下滑动查看）

“后ChatGPT”读书会启动

2022年11月30日，一个现象级应用程序诞生于互联网，这就是OpenAI开发的ChatGPT。从问答到写程序，从提取摘要到论文写作，ChatGPT展现出了多样化的通用智能。于是，微软、谷歌、百度、阿里、讯飞，互联网大佬们纷纷摩拳擦掌准备入场……但是，请先冷静一下…… 现在 all in 大语言模型是否真的合适？要知道，ChatGPT的背后其实就是深度学习+大数据+大模型，而这些要素早在5年前的AlphaGo时期就已经开始火热了。5年前没有抓住机遇，现在又凭什么可以搭上大语言模型这趟列车呢？

集智俱乐部特别组织[“后 ChatGPT”读书会](http://mp.weixin.qq.com/s?__biz=MzIzMjQyNzQ5MA==&mid=2247656500&idx=1&sn=ef9d94a43068525c3b8aa155d8cd9cdc&chksm=e8993eb9dfeeb7af86c86834c2952d4a130be87bfd162a33907c5da6edb6cdd87cc1e4f9b69e&scene=21#wechat_redirect)，由北师大教授、集智俱乐部创始人张江老师联合肖达、李嫣然、崔鹏、侯月源、钟翰廷、卢燚等多位老师共同发起，旨在系统性地梳理ChatGPT技术，并发现其弱点与短板。本系列读书会线上进行，2023年3月3日开始，每周五晚，欢迎报名交流。

[![](.evernote-content/4A010F02-AA50-481B-AC29-EFEF2C6A99CA/21C880C6-E678-4BE9-8A50-3776D8BB144D.jpg)](http://mp.weixin.qq.com/s?__biz=MzIzMjQyNzQ5MA==&mid=2247656500&idx=1&sn=ef9d94a43068525c3b8aa155d8cd9cdc&chksm=e8993eb9dfeeb7af86c86834c2952d4a130be87bfd162a33907c5da6edb6cdd87cc1e4f9b69e&scene=21#wechat_redirect)

详情请见：

[“后 ChatGPT”读书会启动：从通用人工智能到意识机器](http://mp.weixin.qq.com/s?__biz=MzIzMjQyNzQ5MA==&mid=2247656500&idx=1&sn=ef9d94a43068525c3b8aa155d8cd9cdc&chksm=e8993eb9dfeeb7af86c86834c2952d4a130be87bfd162a33907c5da6edb6cdd87cc1e4f9b69e&scene=21#wechat_redirect)

****推荐阅读****

1. ********[人类语言能力的自然演化：乔姆斯基对阵达尔文|《达尔文的危险思想》](http://mp.weixin.qq.com/s?__biz=MzIzMjQyNzQ5MA==&mid=2247662122&idx=1&sn=eba702939d8def0bc4d5c66f5eb69427&chksm=e89920a7dfeea9b19f64f0737996e75d5c42791a5444d7d9886d9f9569a653670d5c7f55e746&scene=21#wechat_redirect)********

2. [AI何以涌现：复杂适应系统视角的ChatGPT和大语言模型](http://mp.weixin.qq.com/s?__biz=MzIzMjQyNzQ5MA==&mid=2247659365&idx=1&sn=d90cd2b209b6da9eefeb32b7e450e4ba&chksm=e89935e8dfeebcfe7f8fdfd9d1192a54004a95c48c8e94d37d17b3718dad647ec3862a6e58ea&scene=21#wechat_redirect)

3. [“意识机器”初探：如何让大语言模型具备自我意识？](http://mp.weixin.qq.com/s?__biz=MzIzMjQyNzQ5MA==&mid=2247662766&idx=1&sn=071ac5bd9a139e720ede6024ae6fd0c4&chksm=e8992623dfeeaf3517778ddeb5702b44a3fbdfbc8d5eadb28871ad0c96cc9ca3483a9539fff9&scene=21#wechat_redirect)

**4.******[Science前沿：大语言模型涌现演化信息，加速蛋白质结构预测](http://mp.weixin.qq.com/s?__biz=MzIzMjQyNzQ5MA==&mid=2247661929&idx=1&sn=de9f5d1f70ca63fbad3e8ce68ee14a87&chksm=e89923e4dfeeaaf2b8cbe1bbb230bdf997e360fe63d0c42f9523d0bb2c395c5f1dedbf232402&scene=21#wechat_redirect)****

****5. [《张江·复杂科学前沿27讲》完整上线！](http://mp.weixin.qq.com/s?__biz=MzIzMjQyNzQ5MA==&mid=2247576923&idx=2&sn=57f0d320812c01ff6f5ea97c09fc9623&chksm=e896f7d6dfe17ec038e8d238dae313119fca8c62aabd4730896bc99398db981dd5d9d3e0b927&scene=21#wechat_redirect)****

******6. **[成为集智VIP，解锁全站课程／读书会](http://mp.weixin.qq.com/s?__biz=MzIzMjQyNzQ5MA==&mid=2247617062&idx=1&sn=e963acb6885ea3b26d32e91c12eae076&chksm=e89650abdfe1d9bddf82c71e612a15bc4393d0a61cde39d325b01b3099247145c98b492c37b8&scene=21#wechat_redirect)********

****7.**********[加入集智，一起复杂！](https://mp.weixin.qq.com/s?__biz=MzIzMjQyNzQ5MA==&mid=2247659079&idx=2&sn=bb67a4c87c48119faa8134c2f2b5a27d&scene=21#wechat_redirect)******

**点击“阅读原文”，报名读书会**

---

[🌐 原始链接](http://mp.weixin.qq.com/s?__biz=MzIzMjQyNzQ5MA==&mid=2247662833&idx=1&sn=01542cf4303b84fb21746e5e2a230dc2&chksm=e899267cdfeeaf6aa5505dea35f86b3fbbbb06d06b279b4ea40b5af4b2e28e1f0bbc4240b994&mpshare=1&scene=24&srcid=0421Jj24jtHomNHvLO9VE1qQ&sharer_sharetime=1682029303152&sharer_shareid=ee47b9411760e9070f0b59d8d8655fa1#rd)

[📎 在印象笔记中打开](evernote:///view/207087/s1/79f5dcc9-ea30-40a1-b9b0-2c8b89f898c1/79f5dcc9-ea30-40a1-b9b0-2c8b89f898c1/)