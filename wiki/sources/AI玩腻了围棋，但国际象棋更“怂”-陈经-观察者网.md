---
title: AI玩腻了围棋，但国际象棋更“怂”-陈经-观察者网
type: source
created: 2026-07-09
updated: 2026-07-09
source_path: 印象笔记管理工具/AI玩腻了围棋，但国际象棋更“怂”-陈经-观察者网.md
tags: [印象笔记]
---

# AI玩腻了围棋，但国际象棋更“怂”-陈经-观察者网

---

![](.evernote-content/EA44EBB7-59FC-4E7A-A2BF-451AD6B1D053/9A60E887-32C6-4A72-B898-B5F30163A911.png)
观察者App
点击下载

![](.evernote-content/EA44EBB7-59FC-4E7A-A2BF-451AD6B1D053/61B4D7B3-77B9-4FFE-A5B8-0768BE8894DA.png)

* [首页](http://m.guancha.cn/)
* [政治](http://m.guancha.cn/politics)

  [教育](http://m.guancha.cn/education)
  [法治](http://m.guancha.cn/FaZhi)
  [社会](http://m.guancha.cn/society)
* [国际](http://m.guancha.cn/internation)

  [北美](http://m.guancha.cn/america)
  [欧洲](http://m.guancha.cn/europe)
  [周边](http://m.guancha.cn/Neighbors)
  [亚非拉](http://m.guancha.cn/Third-World)
* [军事](http://m.guancha.cn/military-affairs)

  [科技](http://m.guancha.cn/Science)
  [工程](http://m.guancha.cn/Project)
* [财经](http://m.guancha.cn/economy)

  [区域](http://m.guancha.cn/local)
  [产业](http://m.guancha.cn/Industry)
  [生活](http://m.guancha.cn/life)
* [文化](http://m.guancha.cn/culture-history)

  [艺术](http://m.guancha.cn/art)
  [体育](http://m.guancha.cn/sports)
  [传媒](http://m.guancha.cn/Media)
  [历史](http://m.guancha.cn/history)

陈经：Deepmind这次搞定国际象棋，只用了四个小时
===========================

2017-12-12 07:59:43

【文/ 观察者网专栏作者 陈经】

2017年12月6号，Deepmind扔出了一篇论文《Mastering Chess and Shogi by Self-Play with a General Reinenforcement Learning Algorithm》，声称从AlphaGo Zero发展来的新程序AlphaZero又零基础自学，只用4个小时和2个小时就胜过了国际象棋和日本将棋的最强程序。加上之前在围棋上的进展，这其实等于是说，世界上所有知名棋类都可以用一个架构轻松碾压过去的高手，不管是人还是程序。

这篇文章正在被审核，按Deepmind过去的风格有可能还是投到《自然》去。但这回Deepmind不保密了，直接在arxiv.org公布了全文。前两篇围棋AI的文章由于投出来之后有人机大战，是需要保密。

![](.evernote-content/EA44EBB7-59FC-4E7A-A2BF-451AD6B1D053/2C096317-D3C8-44A4-9621-3E4D85198726.jpg)

这篇文章在围棋上，用训练34小时的AlphaZero和训练72小时的AlphaGo Zero相比，100盘60:40。这个结果并不令人吃惊，就是训练速度快了，说明新的方法有提升，其实网络架构训练方法和AlphaGo Zero的差不太多，是一些小改进。围棋界对这篇文章应该反应不大，新东西不多，早就被震惊好几次了。

AlphaZero在日本将棋上训练2小时就超过最强程序Elmo。日本将棋和中国象棋、国际象棋差不多，也是各兵种吃对方的王。但是最大的不同是吃掉对方的棋子可以变成本方的棋子，放回棋盘任意位置，这使得对局攻杀极为激烈，和局很少，变化比国际象棋要多不少。中国象棋的理论局面数量超过国际象棋，但由于大量局面类似，高手们一般认为实际变化复杂程度比国象要少。

由于日本将棋更为复杂（以及研究人员关注的少），直到2017年冠军程序Elmo才战胜了人类高手。这个Elmo应该实力还比较弱，所以最终被AlphaZero以90胜2和8负战胜了。AlphaZero还会输几局，但这是因为训练时间不长，已经能够说明问题就行了。

真正影响重大的是国际象棋。这次倒不是说AlphaZero怎么碾压了人，人类高手早就被国际象棋AI整得服气了。但是AlphaZero训练4小时就反超了，最终以28胜72和战胜了Stockfish（鳕鱼），其中先行战绩是25胜25和。这个Stockfish在国际象棋界可不是随便搞搞研发的程序，也不仅是2016年国象AI冠军这么简单，它对职业棋手和爱好者们就像是亲人朋友一样，天天在为棋界服务。在chessbomb等网站上，职业棋赛每一步Stockfish都在实时地给出各种变化，爱好者们看棋的方式和以前完全不一样了。高手们训练也非常依赖顶级AI给出的各种提示，有时就像终极答案一样。高手们通过亲身感受，对于Stockfish的实力非常认可。

由于国际象棋最优解极有可能是和棋，所以高手和爱好者一般认为，Stockfish和国际象棋上帝也差不了太多，反正就是和棋。以前两个顶级AI对打（通常是大战100盘），总有90%的是和棋。排名世界前五的美国特级大师中村光就说：就算是上帝先手和Stockfish下，也得75%是和棋。

现在AlphaZero忽然跑出来，先行能以50%的概率战胜Stockfish，这让一些国际象棋高手和爱好者们有些难以接受。我对围棋很熟，AlphaGo对围棋界的冲击可以说是天翻地覆无以伦比。现在轮到国际象棋界来感受新型AI的冲击了，看着一些国外爱好者对AlphaZero的讨论，各种置疑或者不接受，不由得一阵暗爽。

Stockfish和AlphaZero都是机器，不管谁强谁弱，和人都没啥关系，为什么国际象棋界的人要着急？这里有一些算法背景。

![](.evernote-content/EA44EBB7-59FC-4E7A-A2BF-451AD6B1D053/C3B46BF6-C2E1-443E-B625-9AB1AD868AD5.png)

（图片来源：chessbase）

上图对弈者为国际象棋排名前两位的卡尔森与卡鲁亚纳，围观者左为卡斯帕罗夫，右为哈萨比斯。哈萨比斯本人是国际象棋职业选手，青少年时排名仅次于天才少女小波尔加，他的“一个框架解决一切棋类问题”的思想这次实现了。

Stockfish是机器，但是里面的算法是人们一步步看着发展过来的，程序员写了很多代码，每年都在不断升级，还有国际象棋大师出主意。棋界和计算机学界一起努力，才达到了非常高的水平，那一行行代码都开源在那，还有规模极大的开局库、残局库放在那帮着简化搜索。这都是业界的心血，那些精巧的alpha-beta搜索、剪枝算法、高效实现，各种知识库，有多少人的聪明才智在里面。业界其实对以Stockfish为代表的国际象棋AI比较满意，开发出来的程序又帮助棋手们涨棋，促进了国际象棋界的繁荣，职业棋手数量和水平都大大增加。

各种AI们自己在那对战，Stockfish前几天就正在和Komodo大战。但棋迷和高手们主要还是对人类对局有兴趣。这个局面是不错的，AI们自己玩，玩出东西来帮助人涨棋以及评化棋局，人不和AI较劲。

但是现在AlphaZero等于是说，人类之前开发AI的所谓“心血”都是没意义的白忙活。弄好一个resnet神经网络结构，把国际象棋基本规则做好了，来5000个一代TPU对局生成样本，再来64个二代TPU训练，过4小时就行了。

人类大师1000多年发掘的象棋精妙知识不需要，算法大师构造的精妙剪枝搜索不需要，也不要任何开局库残局库。就这么一个结构，还同时可以搞定围棋、日本将棋、国际象棋，区别只是训练出来的神经网络系数不同。

这种机器暴力征服，围棋AI界的人还是比较服气和欣赏的，说算法优美简单。可能是因为以前开发围棋AI的人也没写出什么好的搜索算法，各种搜索代码写得心烦意乱，明知一堆缺陷也勉强推出来被人类高手低手嘲笑。

老办法搞不定围棋，机器暴力搞定了，是很好的事。但国际象棋不一样了，业界好不容易各种精巧的代码折腾，精心添加维护开局库残局库，感觉摸到国际象棋真理的边了，忽然一下被机器暴力4小时否定了，难道过去的事真的是没有意义的？

因此一些棋迷和高手质疑AlphaZero这个结果，对Stockfish更有感情，是可以理解的。一种质疑是，你AlphaZero背后财大气粗，机器厉害，是不是让Stockfish运行在弱机上，不公平啊？有棋迷就声称，我还能战胜初代stockfish呢，Deepmind到底怎么试的？为什么每步只让Stockfish思考一分钟？但是按论文的数据，测试的Stockfish有64个线程，每秒能搜索7000万个局面，这机器并不弱。

另一种质疑就专业一些，如中村光说，Stockfish并不是一个简单的程序，需要配上合适的开局库残局库。Deepmind是不是配错了开局库，让Stockfish没有发挥最佳实力？怪不得AlphaZero先行能25胜，Stockfish没有好的开局库吃这么大亏才输成这样的。这种质疑比较专业，因为国际象棋开局变化要比中盘、后期复杂得多，AI也不可能搜索清楚。

业界的解决办法是，搞一个庞大的开局库，通过实战对局或者测试中发现不对劲，就放到开局库里免得Stockfish掉到沟里去。而且不同配置的机器对应的开局库是不同的，强机能走的开局，弱机不一定抗得住。这个Deepmind论文里说得是有些不清楚。

特级大师考夫曼是帮助Komodo开发的专家，对AI很了解，他也有类似意见。考夫曼认为，现在说“AlphaZero这种暴力训练的引擎比基于min-max搜索的传统算法强”还为时过早。AlphaZero这么训练，相当于自带了最合适的开局库，公平的比试应该让Stockfish配上最合适的开局库。

![](.evernote-content/EA44EBB7-59FC-4E7A-A2BF-451AD6B1D053/852CA1AE-7BF3-4421-BD29-C4F62C3BB52F.jpg)

对国际象棋不熟的人可能会说，Stockfish这不是还不错么，AlphaZero等级分和它也差不多，而且好像高不上去了。等级分高不上去，主要是因为太多和棋弄的，等级分系统认为分差大获胜概率就得很高，老和就说明你两水平差不多。对人类高手确实如此，人类和stockfish下基本是输，等级分差距很大。但是在极高的水平上，就不能看等级分了，要看输棋。

有经验的高手们认为，国际象棋特别容易和棋，正常走就是和棋，大比例的就应该和棋，就算走得稍不精确也能和，容错犯围比较大。只有说走多了，才偶尔掉进坑里算不清楚输掉。

卡斯帕罗夫和卡尔波夫争霸时曾经连和26局，两人都快折腾死了，卡尔波夫虽然胜局2:0领先，但是已经下崩溃了。

现在Stockfish在后走的50局里输掉一半，不太正常，掉坑概率过高，感觉像是开局库吃大亏。下到中后盘，Stockfish那每秒7000万步的搜索不是开玩笑的，如果有和棋的路线，不太可能输。

一些国象高手们对Deepmind应用Stockfish细节的质疑，似乎也有道理。但不管怎么说，就算Stockfish真是因为没有好开局库输大了，它总得依赖好几个G的宠大开局库，而且还得不停更新维护达到高水平，这看上去不是正路。这等于是说，吃了亏，就把吃亏算不清的地方用开局库补足。

这看上去很像腾讯的围棋AI绝艺之前挣扎的开发阶段，老是出死活bug，就去人工修，修来修去似乎是出错概率小了，但总修不干净。棋下得也不太自然，解说人类对局的时候也经常给出不靠谱结论。后来腾讯参考AlphaGo Zero的新版本“符合预期”就很好了，行棋自然，不出死活Bug，对人类高手也是60连胜，还让二子胜了绝艺。

符合预期这个版本2017年12月9日10日参加了在日本举办的龙星杯世界围棋AI赛，预赛决赛两次战胜最强对手DeepZenGo夺冠。但是绝艺预赛中对一个弱程序Maru输了一局，终局已经大胜了，但因为是用中国规则开发的，对日本规则没有准备，对手不断Pass，绝艺却自填了很多目填输了。比赛中多个中韩程序都因为日本规则中招了，自填负、自填超时负、终局死机负，状况不断。

从开发思想看，其实很清楚。Stockfish等之前的“顶级”国际象棋AI，是用精确搜索的思想开发的，各种细节都做到极致，人工编写的局面估值函数极尽精巧，算法剪枝操作研究极深，代码量不小。如果搜索不行，就加开局库、残局库补足弱点。这是传统的人工代码开发的思想，其实搜索本身是暴力倾向的，开发目标就是尽可能多搜增强实力，标志性指标之一就是一秒能搜多少个局面。

而AlphaZero的开发思想特别简单。人简直是太轻松了，给出网络结构，实现下棋规则，搞出强化学习方法，配上足够的学习和训练的机器就行了。一切都是机器自己学出来的，人没有什么事。而且学完后下棋，一些棋迷评论说AlphaZero下得混然天成，非常自然，人容易理解，没有什么开局库的生搬硬套，一切都在神经网络系数里。Stockfish倒是下得像机器，有些招法不知道怎么蹦出来的，人理解不了。

AlphaZero下国际象棋的时候，每秒只要搜索8万个局面就够了，个个变化图都很有意义。这反过来说明Stockfish每秒7000万个局面，双方对局时一分钟一步，那几十亿的局面绝大多数都没啥意义浪费了，还有漏算。

![](.evernote-content/EA44EBB7-59FC-4E7A-A2BF-451AD6B1D053/E66B6E58-C779-4D4D-9C64-C1409BE7C994.png)

国际象棋AI超级决赛（TCEC Season 10 SuperFinal ），第97场Komodo执白负于Houdini

从算法意义来说，AlphaZero下得更像人。AlphaZero是用MCTS来搜索的，不是精确的，有概率随机因素，是随机选择一些高概率的分枝进行搜索，低概率的分枝根本不浪费算力去碰。之前人们评论说，这不象人，人不可能这么下棋。这主要指的是MCTS用在围棋上，有一个下完数子的rollout用来代替代码写不好的局面估值，这确实不象人。

但是AlphaGo Zero已经把rollout取消了，直接用深度神经网络来进行估值。这样AlphaZero下棋其实更像人的思路，找直觉最想下的点往下推，再找其它也看着靠谱的点也试试。只不过AlphaZero比起人来还是特别能算，一秒能算8万个局面（人类高手每步一般考虑10个局面）。但是与Stockfish相比，AlphaZero这还是人的思考方式，Stockfish等于在那一秒7000万个局面疯狂分枝扩展，各种不靠谱的分枝占据了大量算力，真正有效的搜索没有太多，借着机器的暴力才搞定了人。

这就是机器学习算法界之前争议的，博弈算法“MCTS+神经网络”是更先进的框架。之前Deepmind有人简单地把“MCTS+神经网络”用在国际象棋上，只是大师的水平，达不到顶级AI的水平。有不少人认为，也许“MCTS+神经网络”这个套路只是对围棋这种简单规则的管用。国际象棋规则复杂，MCTS不够“精确”，还是人类程序员精心编制的确定性算法更管用。这次Deepmind新论文应该给出结论了，“MCTS+神经网络”就是先进生产力的代表。

哈萨比斯评论说，AlphaZero下国际象棋的时候，最革命性的一点是，它没有棋子的概念。在AlphaZero看来，只有整体局势才是它关心的，这相当于国际象棋理论对“position”的重视。但无论是人类高手还是过于的顶级AI，再怎么也是以棋子实力评估为基础的，被吃了大子会心疼，在这个基础上再去进行“重视中央”之类的局面评估理论。

而AlphaZero却完全对棋子没有概念，只要它认为未来整体局势好，弃子根本不叫事。所以哈萨比斯说，从棋艺理论来说，AlphaZero既不是人的下法，也不是机器的下法，它是自己创新了一个下法。

这次Deepmind公布了AlphaZero对Stockfish的十局胜局棋谱，[可以这个链接中动态查看](https://en.chessbase.com/post/the-future-is-here-alphazero-learns-chess)。

![](.evernote-content/EA44EBB7-59FC-4E7A-A2BF-451AD6B1D053/943D6D35-331F-4A88-BE6B-32212DC19147.png)

从棋谱中看，AlphaZero很善于弃子。人类或者机器也弃子，但多半有明确目的，弃了子立刻能吃回或者做杀入局。但AlphaZero经常早早放弃子力，在多步以后才建立优势，这个能力是令人震惊的。

如第十局AlphaZero执白对Stockfish，到36步这个局势黑多兵，而且还多一个马，粗看上去应该是黑大优。但实际上白棋进入了必胜局势，黑为了救命，只能用车后换白的后，白方车对马优势很大可以把黑的兵扫光。而AlphaZero第18步就把马弃了，这么多步以后人们才明白它在干什么。

AlphaZero刚出来，国际象棋高手们还在接受中，但方向应该是明确的。机器学习代表了一大类问题的未来，人类精心设计的算法，不如机器暴力自学习。和之前的围棋相比，这次的国际象棋和日本将棋进一步打开了想象力。也许以后，机器就自己学会编程了，因为编程其实就是实现一些明确的目标。

本文系观察者网独家稿件，文章内容纯属作者个人观点，不代表平台观点，未经授权，不得转载，否则将追究法律责任。关注观察者网微信guanchacn，每日阅读趣味文章。

![](.evernote-content/EA44EBB7-59FC-4E7A-A2BF-451AD6B1D053/06BC64C1-9FEB-43F1-8F4F-75F9E81F4D58.png)

陈经

风云学会会员，《中国的官办经济》

分享到

* [微信](http://m.guancha.cn/chenjing/2017_12_12_438753.shtml)
* [新浪微博](http://m.guancha.cn/chenjing/2017_12_12_438753.shtml)
* [QQ](http://m.guancha.cn/chenjing/2017_12_12_438753.shtml)
* [QQ空间](http://m.guancha.cn/chenjing/2017_12_12_438753.shtml)
* [收藏](http://m.guancha.cn/chenjing/2017_12_12_438753.shtml)

来源：观察者网 | 责任编辑:武守哲

专题 > 人工智能

[![](.evernote-content/EA44EBB7-59FC-4E7A-A2BF-451AD6B1D053/2C8BAB93-6716-463B-A1C5-33E655FE60E1.jpg)](http://m.guancha.cn/RenGongZhiNeng)

* [AI玩腻了围棋，但国际象棋更“怂”](http://m.guancha.cn/RenGongZhiNeng)
* [我是阿尔法——人哪，你们准备好没有？](http://m.guancha.cn/RenGongZhiNeng)

网友推荐最新闻

* [![](.evernote-content/EA44EBB7-59FC-4E7A-A2BF-451AD6B1D053/4BDE9CA0-E669-4B30-A06A-68934CEE2820.jpg)
  小伙人民币拼出“110”狂甩眼神 被的哥搭救脱身传销](http://m.guancha.cn/society/2017_12_11_438597.shtml)
* [![](.evernote-content/EA44EBB7-59FC-4E7A-A2BF-451AD6B1D053/E0FAA56A-8362-4A56-B3D3-A6FE1578C6B8.jpg)
  袁立再怼《演员的诞生》：把人剪成一个精神病，非常邪恶](http://m.guancha.cn/Celebrity/2017_12_11_438645.shtml)
* [![](.evernote-content/EA44EBB7-59FC-4E7A-A2BF-451AD6B1D053/ADF4CC6D-C2D3-4BA5-97BD-DACB81954EBC.jpg)
  这些书被400万“美国豆瓣”网友选为年度最佳](http://m.guancha.cn/america/2017_12_11_438602.shtml)
* [![](.evernote-content/EA44EBB7-59FC-4E7A-A2BF-451AD6B1D053/794B6A9D-8065-41EB-8A36-BED00E668939.jpg)
  3名日本人飞机上抽烟喝酒致返航 日网民气炸了](http://m.guancha.cn/Neighbors/2017_12_11_438624.shtml)
* [![](.evernote-content/EA44EBB7-59FC-4E7A-A2BF-451AD6B1D053/251BD4FE-16F5-43FF-B4A8-8C6ACB277E21.jpg)
  时隔8年，《一起来看流星雨》也有低配版了](http://m.guancha.cn/Celebrity/2017_12_08_438381.shtml)
* [![](.evernote-content/EA44EBB7-59FC-4E7A-A2BF-451AD6B1D053/D883CC55-FDBC-40CC-8ED1-48D3A15B7576.jpg)
  保姆电梯内疯狂虐童，已被拘留](http://m.guancha.cn/society/2017_12_09_438453.shtml)
* [![](.evernote-content/EA44EBB7-59FC-4E7A-A2BF-451AD6B1D053/68EDB036-46DE-4034-8836-6CFB40A349DA.gif)
  她们终于迎来首场“女性演唱会” 许多人摘下头巾](http://m.guancha.cn/internation/2017_12_09_438456.shtml)
* [![](.evernote-content/EA44EBB7-59FC-4E7A-A2BF-451AD6B1D053/DD6084F9-459E-49B2-AD49-A44E06495755.jpg)
  吴京接受美媒专访：举个国旗我就成了“红色中国”，为什么？](http://m.guancha.cn/Celebrity/2017_12_09_438483.shtml)
* [![](.evernote-content/EA44EBB7-59FC-4E7A-A2BF-451AD6B1D053/C963D7E2-70DE-4347-A0AB-344A853B0A56.jpg)
  好久不见的袁立，一上台就是一场“大戏”](http://m.guancha.cn/Celebrity/2017_12_10_438558.shtml)
* [![](.evernote-content/EA44EBB7-59FC-4E7A-A2BF-451AD6B1D053/33E575B0-9BC8-48DF-A1F6-F3A60DD87BB5.jpg)
  刚刚，中国这个港口被全世界围观](http://m.guancha.cn/Industry/2017_12_10_438543.shtml)
* [![](.evernote-content/EA44EBB7-59FC-4E7A-A2BF-451AD6B1D053/4F2C1CBE-2B65-4DD9-ACDB-BC07D8E8D0D7.gif)
  这又是在模仿谁？](http://m.guancha.cn/global-news/2017_12_10_438553.shtml)
* [![](.evernote-content/EA44EBB7-59FC-4E7A-A2BF-451AD6B1D053/D9165069-F554-4D54-AA3C-BDE3EB4B02E9.jpg)
  澳“反华闹剧”演出新境界 总理还用上中文了](http://m.guancha.cn/global-news/2017_12_10_438524.shtml)
* [![](.evernote-content/EA44EBB7-59FC-4E7A-A2BF-451AD6B1D053/37661559-04A2-472E-80B5-F561A71508E6.gif)
  特朗普难忍自豪自制视频：承认耶路撒冷，只有我兑现了！](http://m.guancha.cn/america/2017_12_08_438382.shtml)
* [![](.evernote-content/EA44EBB7-59FC-4E7A-A2BF-451AD6B1D053/670916CE-CC59-47BE-9FA1-549DF40FE587.jpg)
  “那么庞大的制作，不能因为我两个字毁掉”](http://m.guancha.cn/Celebrity/2017_12_06_438052.shtml)
* [![](.evernote-content/EA44EBB7-59FC-4E7A-A2BF-451AD6B1D053/1A96C545-79A2-4E4D-A192-EF144A9657A6.jpg)
  投纸飞机前为什么哈气？多年的疑问终于得到了院士的解答](http://m.guancha.cn/life/2017_12_06_438060.shtml)

Copyright © 2014 观察者
沪ICP备10213822号 互联网信息许可证:3112014003

切换网页版

[下载观察者App](http://m.guancha.cn/chenjing/2017_12_12_438753.shtml)
![](.evernote-content/EA44EBB7-59FC-4E7A-A2BF-451AD6B1D053/9A60E887-32C6-4A72-B898-B5F30163A911.png)

![](.evernote-content/EA44EBB7-59FC-4E7A-A2BF-451AD6B1D053/4FA78328-44FA-499F-A0C9-D5A1E925809B.png)
![](.evernote-content/EA44EBB7-59FC-4E7A-A2BF-451AD6B1D053/44150B6D-F5D5-4C85-916D-1845C390A7F4.png)

关闭

---

[🌐 原始链接](http://m.guancha.cn/chenjing/2017_12_12_438753.shtml)

[📎 在印象笔记中打开](evernote:///view/207087/s1/efd5f69d-c3ec-4c8e-9457-acabd31b99c8/efd5f69d-c3ec-4c8e-9457-acabd31b99c8/)
