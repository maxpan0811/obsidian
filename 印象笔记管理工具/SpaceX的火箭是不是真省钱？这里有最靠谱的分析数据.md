# SpaceX的火箭是不是真省钱？这里有最靠谱的分析数据

---

SpaceX的火箭是不是真省钱？这里有最靠谱的分析数据
===========================

小火箭
2017-04-01

小火箭出品

本文作者：邢强博士

北京时间公元2017年3月31日清晨6点27分（美国东部时间3月30日傍晚6:27），SpaceX公司的一枚猎鹰9号火箭将一枚卢森堡SES SA公司的商业通信卫星送入太空轨道。

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1340534973/0&src=read&t=0&w=320&h=213&q=6&rspimgflag=0&imgflag=15&filesize=198722&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

这次发射，使得SpaceX公司再一次给人类太空探索技术史竖立了一块里程碑：有史以来，第一次使用一枚回收利用的火箭成功发射卫星。

鉴于3月31日当天，已经有不少媒体、业内工程师和业余爱好者对此事进行了报道，同时也对事件本身做了或多或少地点评，小火箭觉得压力小了不少。

本文，小火箭将抛开新闻事件本身，而是从猎鹰9号火箭的技术细节和成本相关的估算方面进行分析，从而尽量避免对国外文献的翻译，而是试着给出咱们自己进行计算和分析的结果。

本文，小火箭邢强博士将要和大家共同探讨以下几个问题：

猎鹰9号火箭的一级回收是如何实现的？

为什么非得要研究海上移动平台的回收？

作为秉承快速迭代理念的公司，这次发射有哪些值得留意的小细节？

回收后的火箭再次使用的时候，在发射流程上是否有不同？

历史上对于航天飞行器的回收，有过怎样的尝试？

这次发射的是怎样的一颗卫星？

小火箭给出的猎鹰9号火箭的成本核算。

**实现**

要想让火箭实现发射后的可回收软着陆，至少要攻克两个技术要点：一是可在较大范围调节推力大小的火箭发动机技术，二是再入段多约束制导控制技术。

在小火箭2015年12月31日与2016年04月12日的公号文章《猎鹰9号：SpaceX公司的成名之作》中，已经给出了猎鹰9号火箭的总体设计特点的阐述。

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1340534974/0&src=read&t=0&w=320&h=233&q=6&rspimgflag=0&imgflag=15&filesize=155834&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

默林采用燃气发生器循环，使用RP-1煤油和液氧作为推进剂。该发动机是美国在进入21世纪后，从头开始研制的少有的火箭发动机之一（其实能够排的上号的就两个，第一要数洛克达因RS-68液氢液氧发动机，第二就是默林1D发动机了）。

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1340534975/0&src=read&t=0&w=320&h=393&q=6&rspimgflag=0&imgflag=15&filesize=98392&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

默林发动机使用了早期在阿波罗计划里的登陆舱发动机上所使用的喉栓式喷嘴。推进剂通过一个涡轮泵输出，进入燃烧室。

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1340534977/0&src=read&t=0&w=320&h=213&q=6&rspimgflag=0&imgflag=15&filesize=59306&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

同时，涡轮泵也提供高压液体驱动液压控制器，之后进入低压燃料入口。这样排除了对独立的液压动力系统的依赖，这意味着很少会出现由于液压耗尽而失去对推力方向控制的情况。涡轮泵另外的用处是提供侧向推力来控制火箭自旋。

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1340534978/0&src=read&t=0&w=320&h=240&q=6&rspimgflag=0&imgflag=15&filesize=13147&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

猎鹰9号火箭一二级分离示意图

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1340535245/0&src=read&t=0&w=320&h=182&q=6&rspimgflag=0&imgflag=15&filesize=48872&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

猎鹰9号火箭的第一级在与第二级分离后，用3台发动机完成了程序转弯的过程。在太空中利用姿态控制火箭使箭体旋转180度，令第一级的9台主发动机朝向地面，进行“Boostback Burn”减速。

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1340535246/0&src=read&t=0&w=320&h=180&q=6&rspimgflag=0&imgflag=15&filesize=170529&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

当第一级再入大气后，进行“Entry Burn”减速，并逐渐调整箭体姿态。在火箭接近地面时，第一级火箭顶部的四个栅格翼展开，对箭体姿态进行稳定。主发动机再次点火，利用略低于火箭重量的推力使火箭进一步减速。火箭第一级利用带有终端角度、速度和位置约束的制导律接近地面着陆场并实施软着陆，实现火箭第一级的回收。

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1340535247/0&src=read&t=0&w=320&h=198&q=6&rspimgflag=0&imgflag=15&filesize=91952&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

从下往上看猎鹰9火箭第一级。注意其9台发动机的喷管和4片栅格翼。

栅格翼用在如此巨大的火箭上尚无可以借鉴的模型。小火箭需要对栅格翼的气动流场和其受力情况进行建模和仿真计算。

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1340535248/0&src=read&t=0&w=320&h=253&q=6&rspimgflag=0&imgflag=15&filesize=90369&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

以下为小火箭专门对猎鹰9号火箭栅格翼（舵）的相关计算结果：

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1284242187/0&src=read&t=0&w=320&h=248&q=6&rspimgflag=0&imgflag=15&filesize=193195&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1340526670/0&src=read&t=0&w=320&h=226&q=6&rspimgflag=0&imgflag=15&filesize=57907&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1340526671/0&src=read&t=0&w=320&h=247&q=6&rspimgflag=0&imgflag=15&filesize=130404&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

用更密一些的流线来表现气流的流场，虽然用的时间更久，但是能够出结果，还是值得的。

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1340526672/0&src=read&t=0&w=320&h=229&q=6&rspimgflag=0&imgflag=15&filesize=153598&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

栅格翼表面压力分布情况

值得注意的是，3月31号清晨成功发射并回收的，创造人类航天史的一个里程碑的那枚火箭的栅格翼是最后一款使用铝合金的产品。今后的栅格翼将统一升级为钛合金材料，以便更好地应对有可能会沉浸在一级火箭发动机尾焰和尾烟中的情况。

小火箭对猎鹰9火箭进行了建模，并采用多约束制导律复现了猎鹰9火箭的第一级回收弹道。制导算法详见小火箭在2012年发表在美国航空航天学会的论文：

Xing, Qiang, and Wan. C. Chen. "Segmented optimal guidance with constraints on terminal angle of attack and impact angle." 50th AIAA Aerospace Sciences Meeting, AIAA. Vol. 257. 2012.

如果有更好的算法，也可以将制导律或者仿真弹道发给小火箭一起讨论。

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1156701414/0&src=read&t=0&w=320&h=224&q=6&rspimgflag=0&imgflag=15&filesize=113445&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

猎鹰9号火箭第一级回收仿真。仿真参数：默林1D发动机，海平面比冲：282秒；真空比冲311秒；第一级发动机上升段工作时间：180秒。

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1156701415/0&src=read&t=0&w=320&h=328&q=6&rspimgflag=0&imgflag=15&filesize=48044&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1340527019/0&src=read&t=0&w=320&h=213&q=6&rspimgflag=0&imgflag=15&filesize=31293&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1340527021/0&src=read&t=0&w=320&h=213&q=6&rspimgflag=0&imgflag=15&filesize=46195&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

猎鹰9号火箭发射与回收的火箭轨迹摄影

**海上**

如今，Space X公司共回收了8枚火箭，其中，3枚降落在地面，5枚落在海中的浮动平台上。

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1340527022/0&src=read&t=0&w=320&h=199&q=6&rspimgflag=0&imgflag=15&filesize=724240&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

既然能够实现在陆地上的回收，那么为什么要专门研究在海面平台上的回收呢？要知道，海上平台在海狼中是难以保证其倾斜角度和位置都是理想状态来等待着猎鹰9号火箭的到来的。海上回收的难度和不可预测性要比陆上回收高得多。

实际上，这主要是由火箭的运载能力与可回收性能之间的权衡造成的。可回收火箭需要比一次性使用的火箭携带更多的燃料，以便在再入大气层的时候，借助自身推力来抵抗地球引力的召唤，降低自身的速度，同时也需要借助火箭发动机的推力和栅格翼的空气动力来稳定箭体姿态。

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1340527023/0&src=read&t=0&w=320&h=177&q=6&rspimgflag=0&imgflag=15&filesize=29377&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

多携带的燃料占用的火箭重量侵蚀了火箭携带其他载荷的能力。因此，可回收火箭几乎不可避免地要比一次性使用火箭少携带一些载荷。（当猎鹰9号火箭发射的载荷重量实在太大时，火箭会在任务规划时放弃回收，以便挖掘出火箭自身的运载潜力。）

按现有条件计算，猎鹰9号火箭的可回收型号在陆地上回收的话要损失40%左右的运载能力。而如果将回收地点改在海上，则仅损失16%的运载能力。

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1340527025/0&src=read&t=0&w=320&h=168&q=6&rspimgflag=0&imgflag=15&filesize=72123&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

为什么会有这样的区别呢？因为陆上回收，要求火箭飞到指定着陆场附近，对火箭再入之后的横程提出了要求，相当于多走了很长一段路。而海上回收的话，可以将回收平台拖到一级火箭落区，来个守株待兔，反正火箭不做任何控制，也会按照飞行力学和牛顿先生的法则落到指定海域附近。这样，一级火箭的发动机的任务便可集中在减速和稳定姿态方面，不用再飞很长的冤枉路了。

关于落区和落点的事情，小火箭觉得没有什么会比拿一枚导弹的弹道来演示更合适的了。

下面，小火箭用WGS-84大地模型、考虑地球转动、采用美国标准大气COESA，将发射地点选在了美国德克萨斯州某地，打了一枚红石导弹。

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1340539485/0&src=read&t=0&w=320&h=255&q=6&rspimgflag=0&imgflag=15&filesize=75978&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1340540169/0&src=read&t=0&w=320&h=222&q=6&rspimgflag=0&imgflag=15&filesize=29771&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

放大一些看，基本上是个亚轨道的样子。（注意稠密大气段的弹道）

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1340541768/0&src=read&t=0&w=320&h=221&q=6&rspimgflag=0&imgflag=15&filesize=43455&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

基本上红石导弹的弹道打出来就是这个样子的了。

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1340541882/0&src=read&t=0&w=320&h=309&q=6&rspimgflag=0&imgflag=15&filesize=22153&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

摸了一下早期型号的红石导弹的射程，导弹确实命中了目标。保守估计，红石导弹早期型号的有效射程至少有318.282千米。经常提到红石导弹320千米有效射程的说法，经仿真验证，是较为符合的。

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1340543627/0&src=read&t=0&w=320&h=230&q=6&rspimgflag=0&imgflag=15&filesize=106088&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

弹道最高点为93.721千米处，出现在发射后第207秒。

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1340528572/0&src=read&t=0&w=320&h=309&q=6&rspimgflag=0&imgflag=15&filesize=25090&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

同时，小火箭打了速度曲线。红石导弹在上升段还是比较猛的，不到40秒的时候就超声速了，不到60秒的时候Mach 2、1分多钟Mach 3。

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1340528573/0&src=read&t=0&w=320&h=384&q=6&rspimgflag=0&imgflag=15&filesize=62086&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

SpaceX官方给出的第一级火箭回收过程示意图，黄色实线为上升段弹道，绿色实线为下降段弹道。

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1340528575/0&src=read&t=0&w=320&h=266&q=6&rspimgflag=0&imgflag=15&filesize=60733&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1340528576/0&src=read&t=0&w=320&h=240&q=6&rspimgflag=0&imgflag=15&filesize=225960&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

细心的你可能已经注意到了，小火箭对红石导弹的计算与猎鹰9号火箭海上回收的发射点与落点之间的距离都是300公里左右。嗯，情况类似，原因仅仅是小火箭不算算导弹就手痒痒。

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1340528577/0&src=read&t=0&w=320&h=213&q=6&rspimgflag=0&imgflag=15&filesize=138694&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

有关这个海上浮动平台的名字，还是值得说一说的。她叫做Of Course I Still Love You （当然，我依然爱你）。

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1340528793/0&src=read&t=0&w=320&h=222&q=6&rspimgflag=0&imgflag=15&filesize=153493&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

这个名字的出现在当年SpaceX公司多次尝试在海上回收遇挫时出现，不禁让很多人认为，这是对火箭本身的鼓励。虽然炸了平台，但是，依然爱你。

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1340528795/0&src=read&t=0&w=312&h=505&q=6&rspimgflag=0&imgflag=15&filesize=35694&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

实际上，这个名字是向苏格兰的科幻小说作家伊恩·班克斯致敬。

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1340528796/0&src=read&t=0&w=320&h=180&q=6&rspimgflag=0&imgflag=15&filesize=32181&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1340528798/0&src=read&t=0&w=320&h=179&q=6&rspimgflag=0&imgflag=15&filesize=90547&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

在大西洋上迎接猎鹰9号火箭的平台，长91.1米，宽52.05米，采用4台300马力的发动机来维持在大洋中的稳定。

**细节**

猎鹰9号火箭的这次成功发射，创造了可回收火箭回收后的首次可回收发射的历史。（感觉有点绕啊）不过，即使是这样的发射，按照快速迭代的设计理念，我们依然能够看到一些细节上的改进。

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1340528799/0&src=read&t=0&w=320&h=320&q=6&rspimgflag=0&imgflag=15&filesize=413912&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

比如，之前猎鹰9号火箭成功地在海上回收之后，会有“敢死队”工程师冒着火箭和甲板的余温炙烤和火箭在海浪中倾覆的危险，给火箭绑上固定线缆。

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1340529505/0&src=read&t=0&w=320&h=256&q=6&rspimgflag=0&imgflag=15&filesize=183739&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

而之后，传说中的回收机器人就该上阵了。虽然她没有像之前传闻中提到了有拖拽火箭、摆平火箭甚至是再次加注的能力，但是她有个很实在的功能：能够尽快抓住猎鹰9号火箭一级的大空壳子，而不再需要让人类工程师去冒风险。这一个细节的变化还是蛮赞的。

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1340529506/0&src=read&t=0&w=320&h=213&q=6&rspimgflag=0&imgflag=15&filesize=325905&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

猎鹰9号火箭的一级尾部，有一个用于吊运的孔。对于液体燃料火箭这种“皮薄馅大”的飞行器来说，弹体大部分地方是不能乱踩乱抓的，需要按照规程来对其吊装部位进行操作。这个规定还是要遵守的，弄不好会出大事情，详见小火箭的公号文章《一柄扳手引发的美国核导弹大爆炸》。

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1340529507/0&src=read&t=0&w=320&h=208&q=6&rspimgflag=0&imgflag=15&filesize=112951&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

再离近一些，可以看得更清楚一些。海上浮动平台的机器人就是抓住上图中间部位的那个孔来防止火箭在海浪中倾倒的。

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1340529508/0&src=read&t=0&w=320&h=213&q=6&rspimgflag=0&imgflag=15&filesize=213418&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

另外一个细节，是关于这枚火箭本身的。

看过直播的做火箭的兄弟姐妹们，或许也注意到了，这枚火箭的倒计时的一些动作和之前不同。

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1340529509/0&src=read&t=0&w=320&h=334&q=6&rspimgflag=0&imgflag=15&filesize=46822&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1340537424/0&src=read&t=0&w=320&h=311&q=6&rspimgflag=0&imgflag=15&filesize=55509&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

之前，这枚火箭在发射THAICOM 8卫星的时候，是这样的：

发射前38分钟：开始倒计时准备；

发射前35分钟：加注煤油和液氧确认；

发射前10分钟：发动机准备；

发射前1分30秒：发射指挥确认发射任务。

而同样一枚火箭，在发射SES-10卫星时，倒计时是这样的：

发射前78分钟：开始倒计时准备；

发射前70分钟：加注煤油确认；

发射前45分钟：加注液氧确认；

发射前7分钟：发动机准备；

发射前1分30秒：发射指挥确认发射任务。

由此可见，同一枚猎鹰9号火箭，在回收之后准备再次使用时，其倒计时准备时间明显变长，而加注时序和加注确认时刻发生了变化，发动机准备的时刻也相应延后。这是个值得注意的细节。小火箭会努力跟进进行相关分析。

**历史**

1969年5月20日，一枚土星5号火箭（出厂编号506）顶着阿波罗11号飞船，缓缓地向39A发射场行进。之后的事情，很多人都比较熟悉了：1969年7月16日，这枚火箭，从39A起飞，完成了人类首次登月任务。“这是我个人的一小步，却是全人类的一大步”这句话通过电视直播，向全世界传递了这个事实，让公众共同分享了人类登月的喜悦。

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1159513455/0&src=read&t=0&w=320&h=410&q=6&rspimgflag=0&imgflag=15&filesize=53990&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

其实，39A发射场与阿波罗飞船和土星5号火箭的缘分，从更早的时候就结下了。1967年11月9日，搭载阿波罗4号无人飞船的第一枚土星5号火箭在39A成功发射。这是土星5号火箭第一次向世界展示自己，同时也是39A第一次正式运营。

可以说，39号发射场与人类首次登月计划是相伴而生的。

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1159513625/0&src=read&t=0&w=320&h=270&q=6&rspimgflag=0&imgflag=15&filesize=38316&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

公元1981年4月12日，哥伦比亚号航天飞机首次发射升空，执行STS-1任务（也就是人类历史上，航天飞机的第一次正式任务）。在这次54.5小时的任务中，哥伦比亚号航天飞机环绕地球36圈。同时，这次任务创造了刚出厂的航天飞行器在没有进行过无人飞行试验的前提下，第一次发射就执行载人飞行任务的美国航天发射纪录。这个纪录保持到了今天，今后有可能会被SLS火箭打破。当然，哥伦比亚的发射也是在39A。

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1340537427/0&src=read&t=0&w=320&h=478&q=6&rspimgflag=0&imgflag=15&filesize=248841&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

航天飞机的出现使人类实现了对部分航天运载工具的重复使用。

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1159513814/0&src=read&t=0&w=320&h=221&q=6&rspimgflag=0&imgflag=15&filesize=12319&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

但是，处于对成本和可靠性的大量争议的考虑，2011年，航天飞机正式退役，结束了一个时代。

不过，人类对可回收的航天器的追求实际上可以往前追溯到上世纪60年代初。（详见小火箭2016年03月17日的公号文章《飞到天上去摘星：空中回收卫星的那些事》）

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/345870466/0&src=read&t=0&w=320&h=234&q=6&rspimgflag=0&imgflag=15&filesize=24136&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1340531980/0&src=read&t=0&w=320&h=253&q=6&rspimgflag=0&imgflag=15&filesize=121362&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

1960年8月19日，位于阿拉斯加南部的科迪亚克基地向卫星发出指令，启动了返回程序。“发现者14号”的发动机点火，将卫星推入-60°的大角度再入走廊。返回舱中一台重18.1千克的计算机发出一系列控制指令。离地面不到100千米了，返回舱的抖动越来越剧烈。计算机令滚转发动机启动。两股冷气高速喷出，使返回舱快速旋转起来。在陀螺效应的帮助下，返回舱的姿态得到了稳定。返回舱像一颗灼热的流星，划过太平洋上空，向着夏威夷飞奔而来！大气越来越稠密，反推火箭点火，返回舱减速成功，此时的速度为400米/秒。计算机令滚转发动机朝返回舱转动的反方向喷射，止住了返回舱的旋转。随后，导引伞弹出，返回舱在1.5万米的高空点亮了炫目的频闪灯。位于阿拉斯加和夏威夷的两个测控中心几乎同时收到了这样的信息：“火工品启动，即将展开主降落伞进入万米以下的空域！”剩下的工作，就要交给回收团队了。

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/345870475/0&src=read&t=0&w=320&h=397&q=6&rspimgflag=0&imgflag=15&filesize=21261&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

驾驶C-119的米切尔早早地就盯上了返回舱。C-119的尾舱门向下打开，四名回收人员两人一组，分列在敞开的舱门两旁。每个小组都抓着一根直径0.5英寸（12.7毫米）的尼龙绳。这种绳子是为回收任务特殊研制的，由多股超高强度尼龙旋拧制成。尼龙绳的一端固定在卷扬机上，另一端则拴着带有四个分叉的铜质抓钩。

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1340531982/0&src=read&t=0&w=320&h=248&q=6&rspimgflag=0&imgflag=15&filesize=19859&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

回收小组将尼龙绳伸出舱门外。靠近舱门的两个回收人员，一只脚踩在机舱内，另一只脚踏在伸出机舱的尾舱门上，各自伸出一根11米长的杆子。飞机向下方伸出两根长杆挑着拴有钩子的尼龙绳，像极了伸出利爪准备捕鱼的海鸟。为使铜钩挂住返回舱上方的降落伞，米切尔轻轻推杆，让C-119轻轻地向下俯冲（下降速度约488米/分钟），缓缓地向降落伞上方靠近。尼龙绳向后延展，与机身呈30°到45°的夹角。

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1340531983/0&src=read&t=0&w=320&h=316&q=6&rspimgflag=0&imgflag=15&filesize=24674&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/345870477/0&src=read&t=0&w=320&h=228&q=6&rspimgflag=0&imgflag=15&filesize=16798&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1340537742/0&src=read&t=0&w=320&h=257&q=6&rspimgflag=0&imgflag=15&filesize=33101&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

钩到了！铜钩抓住降落伞，借助尼龙绳的拉力，使伞扭曲折叠成长条状，让其阻力系数迅速降低。这对减轻尼龙绳和飞机的负担非常有利。卷扬机启动，开始往舱里拽降落伞。返回舱被降落伞的伞绳吊着，迎着气流左右摆动，像一条不肯束手就擒的大鱼。

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1340537743/0&src=read&t=0&w=320&h=248&q=6&rspimgflag=0&imgflag=15&filesize=35353&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1340537744/0&src=read&t=0&w=320&h=216&q=6&rspimgflag=0&imgflag=15&filesize=15899&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

回收人员拿出伞兵刀，相互留意着。随时准备在尼龙绳缠住人的时候迅速割断绳子。此时飞机已降到3000米以下。为防止晃动的返回舱和飘摆的降落伞击中飞机尾翼，飞行员轻轻拉杆，让飞机缓缓爬升，将返回舱甩到尾舱门的后下方。卷扬机持续运转，直到机舱里的欢呼声盖过了呼呼的风声。C-119成功捕获了“发现者14号”的返回舱，实现了对卫星返回舱的第一次空中回收。

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/345870470/0&src=read&t=0&w=320&h=379&q=6&rspimgflag=0&imgflag=15&filesize=44259&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1340539486/0&src=read&t=0&w=320&h=356&q=6&rspimgflag=0&imgflag=15&filesize=47761&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1340539487/0&src=read&t=0&w=320&h=259&q=6&rspimgflag=0&imgflag=15&filesize=16276&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

1961年9月14日，6593中队开始尝试用C-130执行回收返回舱的任务。

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1340539488/0&src=read&t=0&w=320&h=179&q=6&rspimgflag=0&imgflag=15&filesize=3935792&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

1960年8月19日，人类实现了对卫星的第一次回收，而从星回收到箭回收，人类足足等了50多年。实际上，从SpaceX成立的时候，他们说出的要研制可回收火箭的想法到现在的成功实现，也已经过去了15年。

**卫星**

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1340539490/0&src=read&t=0&w=320&h=240&q=6&rspimgflag=0&imgflag=15&filesize=81013&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1340546048/0&src=read&t=0&w=320&h=429&q=6&rspimgflag=0&imgflag=15&filesize=44891&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

2017年3月31日，猎鹰9号火箭发射的是一颗卢森堡通信卫星。

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1340540170/0&src=read&t=0&w=320&h=238&q=6&rspimgflag=0&imgflag=15&filesize=20335&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1340540171/0&src=read&t=0&w=320&h=238&q=6&rspimgflag=0&imgflag=15&filesize=26446&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1340540172/0&src=read&t=0&w=320&h=238&q=6&rspimgflag=0&imgflag=15&filesize=20308&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1340540173/0&src=read&t=0&w=320&h=238&q=6&rspimgflag=0&imgflag=15&filesize=29580&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

这颗卫星重5.28171吨，会定点在西经67°的地球同步轨道上。而猎鹰9号火箭需要将她送入近地点218.01公里，远地点35410.02公里，倾角为26.21°的同步转移轨道上。

这是SpaceX第3次在卡纳维拉尔角的航天圣地L39A发射火箭，也是其第3次为SES发射卫星。而算起来，这已经是猎鹰9号火箭的第32次发射了。干得漂亮。

**成本**

有人认为猎鹰9号火箭的发射成本和发射报价会在可回收技术成熟之后降到如今的1%；而有人则认为出于可靠性和大量检修的原因，可回收火箭或许会像航天飞机那样，虽技术上可行但并未实现真正的经济效益。到底哪一方说得更有道理一些呢？

即使是等到2017年3月31日的SpaceX公司的新闻发布会上，也没能给出火箭可重复使用后，今后的报价会怎样。要等结果么？

今天，小火箭就较一下真，给算一下相关的成本问题吧！大家一起探讨。

首先来说，有关可靠性的问题，猎鹰9号火箭的设计理念与通常一次性使用的火箭是不同的。

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1340546870/0&src=read&t=0&w=320&h=224&q=6&rspimgflag=0&imgflag=15&filesize=84324&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

猎鹰9-1.1型的发动机特写。这么多发动机，同时保证他们的可靠性可不是一件容易的事情。实际上，SpaceX给出了他们自己的解决方案：动力冗余。在火箭飞行的过程中，这9台发动机当中任何1台因故障关机，都不会影响猎鹰9火箭完成发射任务的能力。当火箭飞行了90秒的时间后，坏掉2台发动机都没问题。

然后，小火箭就说一下本文的重点内容，成本核算了。

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1340547592/0&src=read&t=0&w=320&h=235&q=6&rspimgflag=0&imgflag=15&filesize=75262&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

目前，可回收火箭使用的燃料为液氧和RP-1航空煤油。取近几年和可预见的短期价格的平均值，液氧的价格折算为人民币，约为1256元/立方米，或者按重量算的话，在1090元至1200元每吨之间。煤油的价格则在7000元/吨左右。（按极限条件，哪怕按8000元/吨来说也行）。

而偏二甲肼每吨的价格在8万元左右，四氧化二氮的价格也近2万元/吨。

总体来说，按运载能力和弹道反推的话，采用液氧煤油作为燃料的火箭的燃料成本约为采用常温有毒燃料火箭成本的1/30。而如果拿煤油和液氢来比的话，那更会是1/100的量级了。（液氢的成本会是煤油的100倍？为什么会这样？详见小火箭的公号文章《液态氢，一匹桀骜不驯的野马》）

而实际上，咱们甚至不用过于纠结于燃料的具体单价。因为燃料成本在火箭发射总成本中的占比实在是太小了。（火箭燃料在重量上虽然占火箭的90%以上，但成本基本上不到火箭发射总成本的1%，而SpaceX曾经在核算的时候，给出了0.4%的占比。）

也就是说，咱们去超市买了些吃的苹果，花了将近100元，然后在收银台买了一个4角钱的塑料袋。火箭燃料成本占发射成本的比例就相当于这个塑料袋与整袋苹果的比例。

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1340551839/0&src=read&t=0&w=320&h=479&q=6&rspimgflag=0&imgflag=15&filesize=154942&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

当然，有的火箭的发射成本的计算和发射流程的管理比较特殊，这也就造成了天价的发射费用。比如大力神4号运载火箭。在1999年的单次发射报价为4.32亿美元！

本文还是讲报价正常的情况吧。

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1340551426/0&src=read&t=0&w=320&h=487&q=6&rspimgflag=0&imgflag=15&filesize=41475&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

在这里，咱们假设SpaceX公司把单次火箭发射的利润锁定为10%（这个应该足够保守了吧。）

然后小火箭说一说我是怎样计算猎鹰9号可重复使用后，成本会怎样降吧。

按照小火箭的工程经验和历史数据，基本上火箭本身的成本占发射总报价的70%。另外的20%要给测控的弟兄们。而对于一枚二级火箭来说，如果大家接受小火箭之前的设计和计算的话，会按照4.35:1的比例来分配二级运载火箭第一级和第二级的成本。（具体为什么这样算，争取以后单独写一个成本核算系列来解释。）

好，本着SpaceX每次发射都保守挣10%的原则，按照其多次发射报价的平均值反推，猎鹰9号火箭（已经把保险相关费用算进去了）：

第一级的成本应该为3534.2万美元，

第二级的成本应为812.4万美元。

按现代航天发射和卡纳维拉尔角场地租用的费用推算，单次发射的指挥、测控的成本为：1242万美元。

利润，咱们按报价的10%来保守计算，取621万美元。

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1340554997/0&src=read&t=0&w=320&h=212&q=6&rspimgflag=0&imgflag=15&filesize=109671&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

好了，那么问题来了，每次回收后的检测、维护保养可都是要有费用的。暂且将其设为X万美元。

问：假如SpaceX公司要实现重复使用2次火箭，可将第2次发射的报价降低20%（打八折）的话，每次回收后的检测、维护保养费用应该控制在多少钱以内？

小火箭在这里和大家一起计算一下：

第一次发射，全新的火箭，第一级的成本为3534.2万美元，第二级的成本为812.4万美元，给测控的弟兄们1242万美元，利润为621万美元。

报价就是6209.6万美元。

第二次发射，成功回收了第一级，第一级的成本要和第一次发射的摊平，为3534.2万美元的一半（注意，这里不能按0计算，而是要用类似折旧的算法了），也就是1767.1万美元。第二级得新造一个，也就是还是812.4万美元，给测控的弟兄们还得有1242万美元。加上X万美元的检测维修第一级火箭的费用，第二次发射的总成本为（3821.5+X）万美元。

锁定10%利润的话，报价为（3821.5+X）/0.9万美元。

那么，用（3821.5+X）/0.9=80%\*6209.6，就可以求出：

X=649.4万美元。

也就是说，按照小火箭的估算，如果猎鹰9号可回收火箭只能回收第一级，而且只重复用了1次的话，只要回收后的维护保养费用控制在649.4万美元以内，第二次发射的报价就能打八折。

而我们不妨认为SpaceX公司对回收后的第一级火箭进行检测和维修的总费用为295万美元。这是基于现有技术条件下的比较乐观的估计。

由此可见，火箭回收以后，第2次发射打8折是完全可以实现的。

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1340541769/0&src=read&t=0&w=320&h=213&q=6&rspimgflag=0&imgflag=15&filesize=95643&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

或许有同学问了，既然检修的成本也知道了，那么咱们干脆计算一下猎鹰9号火箭多次发射的报价会呈现怎样的趋势吧！

好的，小火箭满足你。

第1次发射，全新的火箭。第一级的成本为3534.2万美元，第二级的成本为812.4万美元，给测控的弟兄们1242万美元，利润为621万美元。

第1次发射报价：6209.6万美元。

第2次发射，检修费用295万美元，第一级成本为1767.1万美元，第二级的成本为812.4万美元，给测控1242万美元。成本为4116.5万美元，利润为457.4万美元（成本的九分之一）。

第2次发射报价：4573.9万美元。（是首次报价的73.3%）

第3次发射，检修费用295万美元，第一级成本为1178.1万美元，第二级的成本为812.4万美元，给测控1242万美元。成本为3527.5万美元，利润为391.9万美元（成本的九分之一）。

第3次发射报价：3919.4万美元。（是首次报价的63.1%）

基本上，第2次就7折了，第3次6折，那么，第4次会是5折（半价）么？咱们继续算算看：

第4次发射，检修费用295万美元，第一级成本为883.6万美元，第二级的成本为812.4万美元，给测控1242万美元。成本为3233.0万美元，利润为359.2万美元（成本的九分之一）。

第4次发射报价：3592.2万美元。（是首次报价的57.8%）

嗯，还算不上半价。咱们接着发射。

第5次发射，检修费用295万美元，第一级成本为706.8万美元，第二级的成本为812.4万美元，给测控1242万美元。成本为3056.2万美元，利润为339.6万美元（成本的九分之一）。

第5次发射报价：3395.8万美元。（是首次报价的54.7%）

嗯，第5次发射依然难以称得上是半价。接着来。

第6次发射，检修费用295万美元，第一级成本为589.0万美元，第二级的成本为812.4万美元，给测控1242万美元。成本为2938.4万美元，利润为326.5万美元（成本的九分之一）。

第6次发射报价：3265.9万美元。（是首次报价的52.6%）

6次发射了，依然没能降到半价。

第7次发射，检修费用295万美元，第一级成本为504.9万美元，第二级的成本为812.4万美元，给测控1242万美元。成本为2854.3万美元，利润为317.1万美元（成本的九分之一）。

第7次发射报价：3171.4万美元。（是首次报价的51.1%）

第8次发射，检修费用295万美元，第一级成本为441.8万美元，第二级的成本为812.4万美元，给测控1242万美元。成本为2791.2万美元，利润为310.1万美元（成本的九分之一）。

第8次发射报价：3101.3万美元。（是首次报价的49.9%）

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1340541770/0&src=read&t=0&w=320&h=213&q=6&rspimgflag=0&imgflag=15&filesize=130334&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

哈！第8次发射，终于能够将单次发射的报价打半价了！但是，还别着急离开，继续算下去，看看会怎样。

第9次发射，检修费用295万美元，第一级成本为392.7万美元，第二级的成本为812.4万美元，给测控1242万美元。成本为2742.1万美元，利润为304.7万美元（成本的九分之一）。

第9次发射报价：3046.8万美元。（是首次报价的49.1%）

第10次发射，检修费用295万美元，第一级成本为353.4万美元，第二级的成本为812.4万美元，给测控1242万美元。成本为2702.8万美元，利润为300.3万美元（成本的九分之一）。

第10次发射报价：3003.1万美元。（是首次报价的48.4%）

第11次发射，检修费用295万美元，第一级成本为321.3万美元，第二级的成本为812.4万美元，给测控1242万美元。成本为2670.7万美元，利润为296.7万美元（成本的九分之一）。

第11次发射报价：2967.4万美元。（是首次报价的47.8%）

第12次发射，检修费用295万美元，第一级成本为294.5万美元，第二级的成本为812.4万美元，给测控1242万美元。成本为2643.9万美元，利润为293.8万美元（成本的九分之一）。

第12次发射报价：2937.8万美元。（是首次报价的47.3%）

第13次发射，检修费用295万美元，第一级成本为271.9万美元，第二级的成本为812.4万美元，给测控1242万美元。成本为2621.3万美元，利润为291.3万美元（成本的九分之一）。

第13次发射报价：2912.5万美元。（是首次报价的46.9%）

第14次发射，检修费用295万美元，第一级成本为252.4万美元，第二级的成本为812.4万美元，给测控1242万美元。成本为2601.8万美元，利润为289.1万美元（成本的九分之一）。

第14次发射报价：2890.9万美元。（是首次报价的46.5%）

报价这样就是实在降不下去了。

其根本原因在于：对于第一级火箭的维护保养成本已经高于第一级火箭的残余价值，早该将这枚火箭送入博物馆了。

按照这样计算，再考虑折旧和可靠性的风险，实际上，这枚猎鹰9号可回收火箭在第10次发射之后就应该早早退役了。（维护保养的费用已经和第一级火箭的残余价值比较接近了。）

小火箭计算后的结论就是：

如果SpaceX公司能够把对第一级火箭的检测维修成本控制在295万美元以内的话，同一枚火箭的第8次发射的报价将会是一次性火箭的一半。如果平均每一枚火箭能够发射3次的话，报价可以变为原报价的63.1%。

**未来**

未来，或者不远的将来，我们大概会看到SpaceX公司做点其他什么同样具有里程碑意义的事情呢？

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1340541771/0&src=read&t=0&w=320&h=212&q=6&rspimgflag=0&imgflag=15&filesize=80157&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

他们会尝试回收第二级火箭。感兴趣的同学可以计算一下，第二级火箭能够回收利用之后，会对发射报价有怎样的影响。

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1340541772/0&src=read&t=0&w=320&h=409&q=6&rspimgflag=0&imgflag=15&filesize=44793&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

猎鹰9系列火箭采用了芯级通用的设计理念。每个芯级都由9台默林1D发动机提供动力。将来的猎鹰9重型火箭在发射的时候，会由27台发动机来产生推力，其推力大小相当于15架波音747客机推力的总和。注意图中左下角等比例放置的一个小人儿。

如果重型猎鹰的助推器也能回收的话，可回收部分的成本占比就会涨到75%，更加有利于摊平发射成本。

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_match/0/1340542117/0&src=read&t=0&w=320&h=213&q=6&rspimgflag=0&imgflag=15&filesize=33085&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

不过，最近发布会上提到的火箭可以重复使用100次，将来重复使用1000次的说法有些太艺术了。实际上，从成本和可靠性的角度来分析，目前技术水平下，顶多发射15次就已经很不错了，单纯追求次数并不一定是最优化的。

火箭的介绍和分析以及小火箭对猎鹰9号可重复使用火箭的成本核算完成。

感谢大家对小火箭的支持！

**版权声明：**

**本文已由邢强博士独家授权小火箭刊发，禁止非授权转载，欢迎朋友圈转发。**

微信号：小火箭

微信ID：ixiaohuojian

**欢迎 加入 小火箭 ，进入航空航天大家庭！**

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_ls/0/1340558298_640480/0&src=read&t=0&w=320&h=240&q=6&rspimgflag=0&imgflag=15&filesize=88176&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

猎鹰9号火箭栅格翼流场计算 by：邢强

![](http://cdn.read.html5.qq.com/image?imageUrl=http://inews.gtimg.com/newsapp_ls/0/1340559283_640480/0&src=read&t=0&w=320&h=240&q=6&rspimgflag=0&imgflag=15&filesize=66611&referUrl=http://view.inews.qq.com/a/20170401A004MJ00)

猎鹰9号火箭实现人类历史上首次回收后的火箭成功发射后再成功回收的全过程。

本文来自腾讯新闻客户端自媒体，不代表腾讯新闻的观点和立场

阅读原文

---

[🌐 原始链接](https://zixun.html5.qq.com/coolread/article?ch=001837&tabId=0&tagId=MttTagSource&docId=3937446167&showAttach=0&url=http%3A%2F%2Fview%2Einews%2Eqq%2Ecom%2Fa%2F20170401A004MJ00&dataSrc=76&showDate=1&sc_id=VICivBB)

[📎 在印象笔记中打开](evernote:///view/207087/s1/9d7a8686-2c2a-4414-88c8-a82e28f7405d/9d7a8686-2c2a-4414-88c8-a82e28f7405d/)