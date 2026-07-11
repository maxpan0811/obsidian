# 比泡澡水还烫！英伟达用45°C「热水」给AI芯片洗澡,数据中心用水量干到接近于零

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzkwMjY4MzAzMQ==&mid=224749...](https://mp.weixin.qq.com/s?__biz=MzkwMjY4MzAzMQ==&mid=2247493511&idx=1&sn=010b878b4e68e08ef9ad3b68847ee43b&chksm=c1cfd188d0ed2c041366b42af5d168abc76ee78d0bda459fd168c6eff058588a379f4723d288&scene=90&xtrack=1&req_id=1783417286150446&sessionid=1783415889&subscene=93&clicktime=1783417449&enterid=1783417449&flutter_pos=14&biz_enter_id=4&ranksessionid=1783417286&jumppath=20020_1783417424382,1104_1783417425105,20020_1783417433527,1104_1783417440680&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b35&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQcBeBrC978Gvn11wLf+wSCBLTAQIE97dBBAEAAAAAALuqMFbdly0AAAAOpnltbLcz9gKNyK89dVj0tkaT+kU04uBrbdOYWK7UmsoekeV7g3AfQy2MVOBot0PRnidj3Y5oQ24EwyuysAwgnlOJ+tSo92pJ+GUPYuArTGFvqktxwsUiN19Csroxf8Tb07GDKNmdkXhfpfBEkKK/9MIBHaMHaLKYu/8mpViiMeEmQB0KHotxaIRORmSS22yxXsEZrFzV4433+sijatshJB4C9n79vIDx9JIIOIs66HBZgR5SnCLOzSv1qRI=&pass_ticket=CXGBzXq1ep6KdG+seEbH2KVJekYvWxg7L3zyE+kvZrA5+g2U6vqkhDxL7Jj/FQoc&wx_header=3)

Original井底之硅虚拟灵枢

泡浴缸的水温,一般在38到40°C,泡上15分钟人就受不了了。

现在,英伟达把这个数字往上抬了整整5度。**45°C,113华氏度**——这是英伟达最新一代AI服务器里,冷却液进水口的温度。

更反直觉的是:水温越高,芯片反而冷却得越好。这套系统一上线,数据中心里"几乎所有的用水",都被英伟达宣布清零了。

一条推文,把整个AI圈的水资源焦虑点着了
--------------------

6月23日,推特大V unusual\_whales 转述了这条消息:

"Nvidia, $NVDA, has announced a warm-water cooling system that it says can dramatically reduce the amount of water a data center uses, eliminating 'pretty much all water usage' inside the data center."

「英伟达（$NVDA）宣布了一套温水冷却系统,据称可大幅降低数据中心用水量,基本上消除数据中心内部的"所有用水"。」

![](.evernote-content/681E5406-C470-436E-B960-0EED49E0205A/44CDB994-7528-486C-8743-9AB06C821168.jpg)

▲ unusual\_whales 发布的这条推文,62.3万次查看,6300+点赞,把英伟达的说法推到了整个市场面前。

这条帖子挂出来没多久,评论区就热闹了起来。有人兴奋:又一个卡AI发展的枷锁被拆掉了。也有人皱眉:"pretty much"这个措辞,到底留了多大的口子?

**在过去几年里,"AI耗水"一直悬在数据中心头顶,像一片挥之不去的乌云。**每建一座新的AI工厂,附近社区就要担心自己的水龙头会不会变细。得克萨斯、亚利桑那,已经有超过75个数据中心项目因为用水争议被推迟。现在英伟达说,这个问题"基本解决"了。

真的这么简单吗?

官方原话:一套"泡热水澡"式的冷却系统
-------------------

把时间往回拨一天。6月22日,英伟达官方账号发了一条视频推文,详细摆出了数据:

"By moving to 45°C liquid cooling, AI factories in favorable climates can use dry coolers instead of conventional cooling-tower-based systems, cutting facility cooling water use from roughly 2.6M gallons per MW per year to near zero."

「通过转向45°C液冷,AI工厂在适宜气候下可使用干式冷却器替代传统冷却塔系统,将设施冷却用水从每年每兆瓦约260万加仑降至接近零。」

![](.evernote-content/681E5406-C470-436E-B960-0EED49E0205A/7484C82D-8852-44C3-9249-9190B01C3B14.jpg)![](.evernote-content/681E5406-C470-436E-B960-0EED49E0205A/F7A075C6-667F-4C41-B874-7155116F9BCD.jpg)

▲ 英伟达官方视频帖,3375万次查看,3万点赞,画面里是布满银色管道的液冷机房——每一根管子里流的都是45°C的"热水"。

**260万加仑,降到接近零。**这是一整年、一兆瓦算力的冷却用水量,几乎被砍去了全部。

而这套系统的名字,写在英伟达官方博客的标题里,几乎是在挑衅传统认知:

"Hotter Than a Hot Tub: The 45°C Breakthrough to Cool AI's Biggest Machines"

「比热水浴缸还烫:45°C突破,冷却AI最大的机器。」

负责英伟达数据中心冷却与基础设施的总监 Ali Heydari 在博客里撂下一句更狠的话:

"The NVIDIA DSX reference design for AI factories has zero water consumption — we have eliminated massive amounts of power usage and pretty much all water usage."

「英伟达DSX的AI工厂参考设计,用水量为零——我们消除了巨量的电力消耗,和几乎所有的用水。」

![](.evernote-content/681E5406-C470-436E-B960-0EED49E0205A/7E69CBA6-D4F5-46D6-B57E-ACBE88F209F7.jpg)

▲ 英伟达官方博客首页截图,发布于2026年6月21日,作者Josh Parker——他正是英伟达的首席可持续发展官。

这套说法没有夸大。Rubin这一代AI基础设施,是全球第一个实现"100%液冷"的系统:每一颗芯片、每一个网络组件,全部靠液体带走热量,服务器里连一个风扇都没有。

为什么"更热的水"反而冷却效果更好?
------------------

这里有个反直觉的点,得先掰开揉碎讲清楚。

**传统数据中心的冷却逻辑,是"越冷越好"。**服务器发热,靠冷空气吹散热片带走热量;热空气积多了,再靠"冷却塔"喷水蒸发降温——蒸发要消耗巨量的水。为了把水温压得足够低,还得配上耗电惊人的制冷机(chiller)。冷却这一项,能占掉数据中心总电耗的40%。

液冷的思路完全不同。液体的导热能力比空气强得多,贴着芯片表面的金属冷板走一圈,热量传递效率就高出一大截。

**关键问题来了:进水温度为什么能设到45°C这么高?**

答案在于温差。芯片工作时表面温度远超45°C,液体只要比芯片"凉",就能把热量吸走。吸完热之后,液体被送到室外的干式冷却器(dry cooler)——就是一大片散热盘管,靠风扇或者自然风把热量甩进大气里。

**这时候,进水温度越高,盘管和室外空气之间的温差就越大,散热反而越轻松。**很多气候条件下,单靠室外空气就能把循环液体重新降温,压根不需要开动制冷机。

整套系统是**闭环**的:管道里的液体是75%水加25%丙二醇的混合液,类似汽车防冻液,只在系统建成时灌注一次,之后循环使用,几乎不产生新的用水消耗。丙二醇的作用是防冻、防腐蚀,还能让整个系统的热容更稳定。

液体从芯片带走热量后,出口温度大约55°C。这套系统还带来一个意外的好处:**服务器彻底取消了风扇**,机房环境噪音大幅下降——传统风冷机房动辄超过85分贝,得戴耳罩才能待得住。

数字有多狠?一座50兆瓦工厂,一年省下400万美元
-------------------------

把这套技术换算成真金白银,冲击力更明显。

* 传统冷却塔基线:每兆瓦每年耗水约**260万加仑**。
* 换成45°C液冷+干冷器:适宜气候下,用水量降到**接近零**。
* 一座50兆瓦规模的数据中心,每年在冷却相关的能源和水成本上,能省下**超过400万美元**。
* 服务器机架的体积密度也在同步提升——过去要占6个机架单位(6U)的系统,现在压缩到2U的空间就能装下。

行业里还有一个粗略的经验值:**冷却液设定温度每提高1°C,整体电耗大约能降低4%**。液冷不只是省水,连电费都一起省了。

![](.evernote-content/681E5406-C470-436E-B960-0EED49E0205A/BDC87839-1963-4CF4-936D-2A4EB77A20C5.jpg)

▲ Tom's Hardware报道配图,实拍冷却液流经服务器的画面。文章开篇就点出:"数据中心正在从冰库变成蒸笼。"

Tom's Hardware这篇报道里提到,英伟达这套液冷方案有迹可循——Blackwell那一代已经把进水温度推高到了40°C左右,Rubin只是在这个基础上,再往前迈了一步,顺便把"全液冷"标准化,写进了名为DSX的AI工厂参考设计里。

![](.evernote-content/681E5406-C470-436E-B960-0EED49E0205A/655D24C2-F5A2-47A1-B40B-2B69EAEA92FA.jpg)

▲ 一块液冷Blackwell计算托盘的内部特写。金色的散热冷板紧贴着芯片,深色的管道像血管一样缠绕在电路板之间——这就是"服务器里没有风扇"的真实模样。

但是,英伟达没告诉你的那部分
--------------

事情要是这么简单,这条推特下面就不会吵起来了。

**质疑声几乎是伴随着兴奋一起冒出来的。**TechCrunch的记者Tim De Chant专门写了一篇文章反驳英伟达的说法,标题就是当头一棒:

"Nvidia wants to cut data center water use, but that's not the same as fixing AI's water problem."

「英伟达想削减数据中心用水,但这不等于解决了AI的水资源问题。」

![](.evernote-content/681E5406-C470-436E-B960-0EED49E0205A/29210C32-2A3A-4824-9BD1-A097F60EAF1A.jpg)

▲ TechCrunch这篇报道发布于2026年6月22日,配图是一座正在冒烟的化石燃料电厂——用意很明显。

文章里揪出了英伟达首席可持续发展官Josh Parker此前对Axios说过的话:

"The water consumption challenge for data centers is largely solved."

「数据中心的用水挑战,已经基本解决了。」

TechCrunch的反驳逻辑站得住脚:**英伟达算的是"设施内部"的冷却用水,却没算发电环节的用水。**只要AI数据中心的电力还有一半来自化石燃料电厂——而现实是,越来越多科技公司正在这么做——那么省下来的水,只是把消耗从数据中心的围墙内,转移到了几十公里外的发电厂旁边。天然气电厂每发一度电,大约消耗1.17升水;燃煤电厂的耗水量更高。

换句话说,**英伟达定义的"水问题",可能只覆盖了AI真实水足迹的四分之一到三分之一。**芯片制造本身需要的超纯水,也完全没被计算进去。

社区里的怀疑者还揪住了英伟达那句话里的一个限定词——"favorable climates"(适宜气候)。有网友扒出了原文里的但书:

"The catch... is 'favorable climates'. ... ambient atmospheric temperature... below 30°C."

「关键就在于那句'适宜气候'……室外气温得低于30°C。」

也就是说,这套系统在北欧、在温带地区效果拔群;可放到亚利桑那州凤凰城那种夏天动辄40°C+的地方,一年里仍然有大约1%的时间需要开动传统制冷机来兜底。

还有更犀利的技术流吐槽:

"They already made that announcement at nvidia GTC. To truly eliminate water usage they would need to move to 2 phase cooling."

「他们在GTC大会上已经宣布过一次了。真要彻底消灭用水,还得上两相冷却。」

有人翻出斯坦福大学的例子——这所学校用第四代区域供冷系统,靠空气源热泵加废热回收,十年前就做到了零水损耗校园供冷,而且用的是太阳能供电。这背后的意思不难体会:这项技术并非横空出世,英伟达做的是把它推向了AI基础设施的量产级别。

也有人给出了更冷静的数字:目前液冷方案在数据中心行业的实际落地率,估算只有大约19%。**技术已经摆在那儿了,真正铺开还要好几年。**

移除了水的枷锁,下一道墙是什么?
----------------

争议归争议,这套系统留下的一个彩蛋,可能比省水本身更有意思。

液体带走热量后,出口温度还有55°C——这一块低品位的热量,完全可以再利用。欧洲已经有项目把数据中心排出的热量接进了区域供暖管网,给附近的居民楼供暖。**数据中心从一个纯粹"抽水抽电"的邻避设施,变成了一个能反哺社区的"电网资产"。**

这也是英伟达在博客里特意提到"heat reuse and dispersal to local communities"(废热回收与向本地社区散热)的原因——从纯消耗者到热能生产者,这个身份转变,可能比省下多少加仑水更值得留意。

**回头看整件事,水资源焦虑被移除的过程,像是在剥洋葱。**每解决一层限制——先是空间、后是噪音,现在轮到水——AI建厂的故事就往前推进一截,直到下一层限制露出来。这一次露出来的是电力和气候依赖:国际能源署预测,到2030年,数据中心新增的电力需求里,仍然会有相当一部分靠化石燃料填补。

英伟达没有说谎,只是选择性地讲述了故事最漂亮的那一段。数据中心院墙以内的水龙头,或许真的快要拧紧了。院墙以外,发电厂冷却塔上方蒸腾的水汽,还没人认领。

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzkwMjY4MzAzMQ==&mid=2247493511&idx=1&sn=010b878b4e68e08ef9ad3b68847ee43b&chksm=c1cfd188d0ed2c041366b42af5d168abc76ee78d0bda459fd168c6eff058588a379f4723d288&scene=90&xtrack=1&req_id=1783417286150446&sessionid=1783415889&subscene=93&clicktime=1783417449&enterid=1783417449&flutter_pos=14&biz_enter_id=4&ranksessionid=1783417286&jumppath=20020_1783417424382,1104_1783417425105,20020_1783417433527,1104_1783417440680&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b35&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQcBeBrC978Gvn11wLf+wSCBLTAQIE97dBBAEAAAAAALuqMFbdly0AAAAOpnltbLcz9gKNyK89dVj0tkaT+kU04uBrbdOYWK7UmsoekeV7g3AfQy2MVOBot0PRnidj3Y5oQ24EwyuysAwgnlOJ+tSo92pJ+GUPYuArTGFvqktxwsUiN19Csroxf8Tb07GDKNmdkXhfpfBEkKK/9MIBHaMHaLKYu/8mpViiMeEmQB0KHotxaIRORmSS22yxXsEZrFzV4433+sijatshJB4C9n79vIDx9JIIOIs66HBZgR5SnCLOzSv1qRI=&pass_ticket=CXGBzXq1ep6KdG+seEbH2KVJekYvWxg7L3zyE+kvZrA5+g2U6vqkhDxL7Jj/FQoc&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/5c1784fa-9c0e-408b-b9cd-10690514104b/5c1784fa-9c0e-408b-b9cd-10690514104b/)