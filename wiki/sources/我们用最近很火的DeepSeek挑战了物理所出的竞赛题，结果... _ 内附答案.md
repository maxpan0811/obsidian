---
title: 我们用最近很火的DeepSeek挑战了物理所出的竞赛题，结果... _ 内附答案
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/我们用最近很火的DeepSeek挑战了物理所出的竞赛题，结果... _ 内附答案.md
tags: [evernote, impression, yinxiang]
---

# 我们用最近很火的DeepSeek挑战了物理所出的竞赛题，结果... | 内附答案

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzAwNTA5NTYxOA==&mid=265156...](https://mp.weixin.qq.com/s?__biz=MzAwNTA5NTYxOA==&mid=2651561722&idx=1&sn=e0fd406b475a425506c4329a1376ca7e&chksm=8153cd66496684b561c2c3f885ecaad590123aee31e5fe390efa18a376b47d47916f7eaecef4&mpshare=1&scene=1&srcid=0130llqMWe6Mn5kt3XzmSGuQ&sharer_shareinfo=5a5dc522526f5b2739947bba90f544c2&sharer_shareinfo_first=5a5dc522526f5b2739947bba90f544c2&from=groupmessage&isappinstalled=0&clicktime=1738281166&enterid=1738281166&ascene=1&devicetype=iOS18.2.1&version=1800382d&nettype=3G+&abtest_cookie=AAACAA==&lang=zh_CN&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQDi6sg5BnbhnmI3nraURjxxLsAQIE97dBBAEAAAAAAFhpJk6gkwwAAAAOpnltbLcz9gKNyK89dVj02HkiPnsrNFfRW2K5xQaJV+IRGrz7XPsRZX0p7mzOVwQbu/a5K/znONOkaW1Xr5pQhCTyiF4EXiAS457ctI/ZuWloFpcECqwHX2IZEJW/uBYvpkLtC0uWsZ6fUKa3U697eGVRxfp6srZtLc1GXxlZiBFyqjpeOdTTdTD5W61JT4eVzwxnfs+9WZk33A1Yu35BAvvp1XHuHqYsnrrFkDoepGeFL2bhpFeKQnGleDyJJHHpkPTTe+d9A7FcL53SD81Fp52CXoW9&pass_ticket=nmeIU8Jui8sRDNPSDr9+mfgalXEx7IHFy06vKqE/IQr0PVGzfdHJT+K9mo3c6RHY&wx_header=3)

原创 冬令营组委会  中科院物理所

近日，我国“深度求索”公司发布的具备深度思考和推理能力的开源大模型DeepSeek-R1受到了全世界的关注。在DeepSeek-R1之前，美国OpenAI公司的GPT-o1，Athropic公司的Claude，Google公司的Gemini，都号称具备了深度思考和推理能力。这些模型在专业人士和吃瓜网友的五花八门的测试中，表现的确是惊才绝艳。特别引起我们兴趣的，是Google的专用模型AlphaGeometry在公认高难度的国际奥林匹克数学竞赛中取得了28/42的成绩，获得银牌。学生时代我们也接触过奥数，深知能在此类国际奥赛中获银牌的选手，无一不是从小就体现出相当数学天赋，且一路努力训练的高手。能够达到这个水平的AI，称其为具备了强大的思考能力并不过分。自打那之后，我们就一直好奇，**这些强大的AI，它们的物理水平又如何？**~~是不是以后就不用招研究生和博士后了？~~

1月17日，[中科院物理所在江苏省溧阳市举办了“天目杯”理论物理竞赛](https://mp.weixin.qq.com/s?__biz=MzAwNTA5NTYxOA==&mid=2651560408&idx=1&sn=3a803ed546cb33da7adbff07e1947a56&scene=21#wechat_redirect)。我们命题组完成了这份试卷的出题工作。七道题除一道外，都不是从现成的题库或考题中改编节选的，我们三个对这套试卷比较满意，觉得它既不像传统考试题一样盯着个别知识点考，也不像高中竞赛题一样需要很多技巧和熟练度，而更像实际科研中碰到的具体技术问题。竞赛前的某天，我们和几个朋友一起吃饭，其中一位AI的重度用户知道了我们出了这份题，就问有没有测试过AI的表现？我们觉得这个建议很有意思，于是决定**在竞赛后，测试几个有代表性的大模型**。

所谓来得早不如来得巧。1月20日，当我们刚结束竞赛回到北京，正赶上**DeepSeek-R1**发布引爆了AI圈，它自然成了我们测试的首选模型。此外我们测试的模型还包括：OpenAI发布的**GPT-o1**，Anthropic发布的**Claude-sonnet**。下面是我们测试的方式：

1.整个测试由8段对话完成。

2.第一段对话的问题是“开场白”：交代需要完成的任务，问题的格式，提交答案的格式等。通过AI的回复人工确认其理解。

3.依次发送全部7道题目的题干，在收到回复后发送下一道题，中间无人工反馈意见。

4.每道题目的题干由文字描述和图片描述两部分组成（第三、五、七题无图）。

5.图片描述是纯文本方式，描述的文本全部生成自GPT-4o，经人工校对。

6.每个大模型所拿到的文字材料是完全相同的（见附件）。

上述过程后，对于每个大模型我们获得了7段tex文本，对应于7道问题的解答。以下是我们采取的阅卷方式：

1.人工调整tex文本至可以用Overleaf工具编译，收集编译出的PDF文件作为答卷。

2.将4个模型的7道问题的解答分别发送给7位阅卷人组成的阅卷组。

3.阅卷组与“天目杯”竞赛的阅卷组完全相同，且每位阅卷人负责的题目也相同。举例：阅卷人A负责所有人类和AI答卷中的第一题；阅卷人B负责所有人类和AI答卷中的第二题，等等。

4.阅卷组汇总所有题目得分。

结果如何呢？请看下表。

![](.evernote-content/CE956E52-E16D-4E97-A337-4357F08C2218/53F4C6DA-33F5-4F5D-99F2-E19B4D52C71D.png)

结果点评：

1.**DeepSeek-R1表现最好**。基础题（前三题分数拿满），第六题还得到了人类选手中未见到的满分，第七题得分较低似乎是因为未能理解题干中“证明”的含义，仅仅重述了待证明的结论，无法得分。查看其思考过程，是存在可以给过程分的步骤的，但最后的答案中这些步骤都没有体现。

![](.evernote-content/CE956E52-E16D-4E97-A337-4357F08C2218/B079C587-B56C-4AE0-AED5-B755AC60F7AB.png)

2.**GPT-o1总分与DeepSeek相差无几**。在基础题（二题、三题）中有计算错误导致的失分。相比于DeepSeek，o1的答卷更接近于人类的风格，因此以证明题为主最后一题得分稍高。

![](.evernote-content/CE956E52-E16D-4E97-A337-4357F08C2218/770C9D14-C0F7-4450-BBC7-AC2E1D7C74CC.png)

3.**Claude-sonnet可谓“马失前蹄”**，在前两题中连出昏招打了0分，但后续表现跟o1相当接近，连扣分点都是类似的。

![](.evernote-content/CE956E52-E16D-4E97-A337-4357F08C2218/327C023A-D5A3-44F1-BD3B-41644163D84E.png)

4.如果将AI的成绩与人类成绩相比较，则DeepSeek-R1可以进入前三名（获特优奖），但与人类的最高分125分仍有较大差距；GPT-o1进入前五名（获特优奖），Claude-sonnet前十名（获优秀奖）。

最后想聊几句阅卷的主观感想。首先是**AI的思路是真的好，基本上没有无法下手的题**，甚至很多时候一下子就能找到正确的思路。**但跟人类不同的是，它们在有正确的思路后，会在一些很简单的错误里面打转**。比如通过看R1的第七题思考过程，就发现它一早就知道要用简正坐标来做，能想到这一步的考生几乎100%求解出了正确的简正坐标（一个简单的矩阵对角化而已），**但是R1似乎是在反复的猜测和试错，到最后也没有得到简正坐标的表达式**。还有就是所有的AI似乎都不理解一个“严密”的证明究竟意味着怎样的要求，似乎认为能在形式上凑出答案，就算是证明了。AI如同人类，也会出现许多“偶然”错误。比如在正式的统一测试前，我们私下尝试过多次，很多时候Claude-sonnet可以正确解出第一题的答案，但正式测试的那次它就偏偏做错了。出于严谨，我们也许应该对同一道题测试多次然后取平均，但实在是有点麻烦……

![](.evernote-content/CE956E52-E16D-4E97-A337-4357F08C2218/B182148C-85D0-47DA-AF37-0DB7E5D33783.png)

除了上面AI的测试结果，这次我们还发布了本次试题的参考答案。我们当然是故意比试题迟几天发布答案的，想让大家先自己挑战一下。在每道题的解答后，我们还加入了一小段“编后”，有命题人对这道题的评价，以及一些引申的思考等。我们希望答案可以帮助不会做的同学学习，也能引发会做的同学进一步的思考。

附件中我们提供了：

1.所有向大模型发问的输入文本（txt），

2.每个大模型给出的原始答案文本（txt）和人工整理出的答卷（PDF），

3.命题组提供的标准答案。

最后感谢“字节跳动”的AI“豆包”对本文的修改～

春节快乐，学习进步，工作顺利！

[附件：AI答卷](https://mp.weixin.qq.com/s?__biz=MzAwNTA5NTYxOA==&mid=2651561722&idx=1&sn=e0fd406b475a425506c4329a1376ca7e&chksm=8153cd66496684b561c2c3f885ecaad590123aee31e5fe390efa18a376b47d47916f7eaecef4&mpshare=1&scene=1&srcid=0130llqMWe6Mn5kt3XzmSGuQ&sharer_shareinfo=5a5dc522526f5b2739947bba90f544c2&sharer_shareinfo_first=5a5dc522526f5b2739947bba90f544c2&from=groupmessage&isappinstalled=0&clicktime=1738281166&enterid=1738281166&ascene=1&devicetype=iOS18.2.1&version=1800382d&nettype=3G+&abtest_cookie=AAACAA==&lang=zh_CN&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQDi6sg5BnbhnmI3nraURjxxLsAQIE97dBBAEAAAAAAFhpJk6gkwwAAAAOpnltbLcz9gKNyK89dVj02HkiPnsrNFfRW2K5xQaJV+IRGrz7XPsRZX0p7mzOVwQbu/a5K/znONOkaW1Xr5pQhCTyiF4EXiAS457ctI/ZuWloFpcECqwHX2IZEJW/uBYvpkLtC0uWsZ6fUKa3U697eGVRxfp6srZtLc1GXxlZiBFyqjpeOdTTdTD5W61JT4eVzwxnfs+9WZk33A1Yu35BAvvp1XHuHqYsnrrFkDoepGeFL2bhpFeKQnGleDyJJHHpkPTTe+d9A7FcL53SD81Fp52CXoW9&pass_ticket=nmeIU8Jui8sRDNPSDr9+mfgalXEx7IHFy06vKqE/IQr0PVGzfdHJT+K9mo3c6RHY&wx_header=3)

[附件：AI提问](https://mp.weixin.qq.com/s?__biz=MzAwNTA5NTYxOA==&mid=2651561722&idx=1&sn=e0fd406b475a425506c4329a1376ca7e&chksm=8153cd66496684b561c2c3f885ecaad590123aee31e5fe390efa18a376b47d47916f7eaecef4&mpshare=1&scene=1&srcid=0130llqMWe6Mn5kt3XzmSGuQ&sharer_shareinfo=5a5dc522526f5b2739947bba90f544c2&sharer_shareinfo_first=5a5dc522526f5b2739947bba90f544c2&from=groupmessage&isappinstalled=0&clicktime=1738281166&enterid=1738281166&ascene=1&devicetype=iOS18.2.1&version=1800382d&nettype=3G+&abtest_cookie=AAACAA==&lang=zh_CN&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQDi6sg5BnbhnmI3nraURjxxLsAQIE97dBBAEAAAAAAFhpJk6gkwwAAAAOpnltbLcz9gKNyK89dVj02HkiPnsrNFfRW2K5xQaJV+IRGrz7XPsRZX0p7mzOVwQbu/a5K/znONOkaW1Xr5pQhCTyiF4EXiAS457ctI/ZuWloFpcECqwHX2IZEJW/uBYvpkLtC0uWsZ6fUKa3U697eGVRxfp6srZtLc1GXxlZiBFyqjpeOdTTdTD5W61JT4eVzwxnfs+9WZk33A1Yu35BAvvp1XHuHqYsnrrFkDoepGeFL2bhpFeKQnGleDyJJHHpkPTTe+d9A7FcL53SD81Fp52CXoW9&pass_ticket=nmeIU8Jui8sRDNPSDr9+mfgalXEx7IHFy06vKqE/IQr0PVGzfdHJT+K9mo3c6RHY&wx_header=3)

[附件：参考答案](https://mp.weixin.qq.com/s?__biz=MzAwNTA5NTYxOA==&mid=2651561722&idx=1&sn=e0fd406b475a425506c4329a1376ca7e&chksm=8153cd66496684b561c2c3f885ecaad590123aee31e5fe390efa18a376b47d47916f7eaecef4&mpshare=1&scene=1&srcid=0130llqMWe6Mn5kt3XzmSGuQ&sharer_shareinfo=5a5dc522526f5b2739947bba90f544c2&sharer_shareinfo_first=5a5dc522526f5b2739947bba90f544c2&from=groupmessage&isappinstalled=0&clicktime=1738281166&enterid=1738281166&ascene=1&devicetype=iOS18.2.1&version=1800382d&nettype=3G+&abtest_cookie=AAACAA==&lang=zh_CN&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQDi6sg5BnbhnmI3nraURjxxLsAQIE97dBBAEAAAAAAFhpJk6gkwwAAAAOpnltbLcz9gKNyK89dVj02HkiPnsrNFfRW2K5xQaJV+IRGrz7XPsRZX0p7mzOVwQbu/a5K/znONOkaW1Xr5pQhCTyiF4EXiAS457ctI/ZuWloFpcECqwHX2IZEJW/uBYvpkLtC0uWsZ6fUKa3U697eGVRxfp6srZtLc1GXxlZiBFyqjpeOdTTdTD5W61JT4eVzwxnfs+9WZk33A1Yu35BAvvp1XHuHqYsnrrFkDoepGeFL2bhpFeKQnGleDyJJHHpkPTTe+d9A7FcL53SD81Fp52CXoW9&pass_ticket=nmeIU8Jui8sRDNPSDr9+mfgalXEx7IHFy06vKqE/IQr0PVGzfdHJT+K9mo3c6RHY&wx_header=3)

**冬令营组委会**

**乙巳年正月初二**

**编辑：雪影**

---

扫码进入“科学与中国”小程序，可观看以院士科普视频为代表的优秀科普视频，第一时间获取中国科学院公众科学日、科学节等科普活动报名信息。

![](.evernote-content/CE956E52-E16D-4E97-A337-4357F08C2218/375628EB-C9D1-49BC-87F1-71C0DA826952.jpg)

---

---

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzAwNTA5NTYxOA==&mid=2651561722&idx=1&sn=e0fd406b475a425506c4329a1376ca7e&chksm=8153cd66496684b561c2c3f885ecaad590123aee31e5fe390efa18a376b47d47916f7eaecef4&mpshare=1&scene=1&srcid=0130llqMWe6Mn5kt3XzmSGuQ&sharer_shareinfo=5a5dc522526f5b2739947bba90f544c2&sharer_shareinfo_first=5a5dc522526f5b2739947bba90f544c2&from=groupmessage&isappinstalled=0&clicktime=1738281166&enterid=1738281166&ascene=1&devicetype=iOS18.2.1&version=1800382d&nettype=3G+&abtest_cookie=AAACAA==&lang=zh_CN&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQDi6sg5BnbhnmI3nraURjxxLsAQIE97dBBAEAAAAAAFhpJk6gkwwAAAAOpnltbLcz9gKNyK89dVj02HkiPnsrNFfRW2K5xQaJV+IRGrz7XPsRZX0p7mzOVwQbu/a5K/znONOkaW1Xr5pQhCTyiF4EXiAS457ctI/ZuWloFpcECqwHX2IZEJW/uBYvpkLtC0uWsZ6fUKa3U697eGVRxfp6srZtLc1GXxlZiBFyqjpeOdTTdTD5W61JT4eVzwxnfs+9WZk33A1Yu35BAvvp1XHuHqYsnrrFkDoepGeFL2bhpFeKQnGleDyJJHHpkPTTe+d9A7FcL53SD81Fp52CXoW9&pass_ticket=nmeIU8Jui8sRDNPSDr9+mfgalXEx7IHFy06vKqE/IQr0PVGzfdHJT+K9mo3c6RHY&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/dc7cc625-4996-46bc-90a9-2421c0f697f5/dc7cc625-4996-46bc-90a9-2421c0f697f5/)
