# 谷歌的NotebookLM彻底解决了我的信息焦虑症。

---

原文链接: [https://mp.weixin.qq.com/s?chksm=c2b84246f5cfcb50725f24cfe4b6558...](https://mp.weixin.qq.com/s?chksm=c2b84246f5cfcb50725f24cfe4b65581300af9c3272b17182918b30beb001daa2c42113b8f50&exptype=unsubscribed_card_recommend_article_u2i_mainprocess_coarse_sort_tlfeeds&ranksessionid=1736949243_2&scene=169&mid=2247484588&sn=2c7097ec1eb4c3113db0e2f89047e033&idx=1&__biz=MzkzNDcxMjE5Nw==&sessionid=1736948515&subscene=200&clicktime=1736951057&enterid=1736951057&flutter_pos=22&biz_enter_id=5&ascene=56&devicetype=iOS18.2.1&version=1800372c&nettype=3G+&abtest_cookie=AAACAA==&lang=zh_CN&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ1L2a5u/q1PzfExL6AeohGRLYAQIE97dBBAEAAAAAAI9MDWM1JNoAAAAOpnltbLcz9gKNyK89dVj0QLvcJOcTs1xcGI3iuTCyp+RvWjpN1CsUcZHp/HLfbDumcaVvK9mRIhiG61o3zjs0wX8gYiJSKSLEpdLWRgdGwaSvwhW/aGqZjB+UJ5+ln07iIppa0Q/DE2H1QpzCcmHvDalhoMB7GK9ys3hc5HcjdEDVLPUsZgvsxivY8cBMAP7qcAw0VsBGgiNvaSUEdg6BSuBq6QqbUr344LJTeQxKbCjiDUTw6qTJDBni7GlsKqteAg==&pass_ticket=oBX7l/f4lqtwSIZ5WtleUxwWGig9uqtQtRy4niQ8kni75FWolatvaeoW4h/wQV0W&wx_header=3)

原创问问AI指北问问AI指北

我感觉自己会很容易陷入信息焦虑。

尤其是近两年AI大爆发，每天一睁眼，铺天盖地的AI论文和技术文章还躺在清单里面等待着去消化。

虽然，看到新技术和新产品的时候是兴奋的，但是实在扛不住AI进化的太快了，靠自己一篇一篇去理解，经常会信息过载。

经常会想，有没有一款产品，可以替代我去看，去读，然后把核心信息淬炼后直接告诉我，像个知识保姆，materials in，knowledges out。

市面上有很多这种初期形态的产品，你可以上传一篇pdf然后针对pdf进行提问，比如通义做的阅读助手，获取信息的效率确实提高了。

![](.evernote-content/DC2F8DAA-0680-442C-B958-F18A4A5448C7/F5D3DB94-3FCF-4286-A7B2-C028E60155A5.png)

但这还不够，本质上还是要耗费我的精力间接去看啊，去和AI提问。可尼玛，这不是个悖论吗，我都没读过这篇文章，怎么高质量地提问？

现在提示词都TM成玄学了，对很多普通人来说，阅读真不是件容易的事，还要和AI聊天，对AI提问真的挺难的。

咱就是说，能不能直接一点，别让我提问，别让我和AI聊天，简单粗暴地告诉我这篇文章讲啥了？最好能像朋友聊天一样告诉我，并且还要通俗易懂，另外我不想看文字，我只想听你讲给我听。

这种需求很正常吧，一点也不过分，AI不是很厉害吗？可目前国内市场上一片空白，没有一款产品能够解决这个痛点。

直到让我看到了谷歌的一款产品，名叫NotebookLM，如获至宝，太接近我想象的知识保姆形态了。

网址：https://notebooklm.google

![](.evernote-content/DC2F8DAA-0680-442C-B958-F18A4A5448C7/9F86C199-0096-4E4B-BF6D-771BCCD8916F.png)

去年9月，OpenAI创始大神Andrej Karpathy就安利过这款产品，我那会儿没太注意，因为你懂得，AI的信息太多了。。。

![](.evernote-content/DC2F8DAA-0680-442C-B958-F18A4A5448C7/DC4ADCDF-A7BC-44E4-B509-45C07C44808C.jpg)

最近，我才认真研究起来，真的，做的真好，不愧是谷歌出品。

NotebookLM是怎么做的呢？

它只需要用户上传一个文件、复制一个文章链接或者粘贴一段文字，接着，NotebookLM会转换成对话播客，关键是，播客里面有两个AI，用像极了真人的语音和口吻，围绕文件内容进行讨论，你啥也不用干，只需要在旁边听他们巴拉巴拉讲就行了，知识不知不觉就溜进了你的脑袋。

![](.evernote-content/DC2F8DAA-0680-442C-B958-F18A4A5448C7/56395D14-B0F5-4205-B5FB-CEA3345F810B.png)

有朋友会问，啥叫播客？播客确实在中国比较小众，emmm……喜马拉雅听过吧？没有的话，收音机总听过（读高中那会儿没智能手机，我经常用收音机听中国之声）。

大概就是这种类比，强行理解一下，播客它是一种电台节目，是因为iPod诞生后才有的一种音频内容，美国人很喜欢听这种玩意。

人，对信息的灌输天然是抗拒的，实在没办法才要去主动学习。如果把互联网上的信息按人的接受程度从易到难排个序，那一定是：视频 > 音频 > 文字，谁都愿意刷抖音，愿意听故事，远大于直接看文字。

NotebookLM做的就是把文字升了一维，转换成了音频，注意，并不是简单地用Text-To-Speech的技术读出来，而是，先进行知识萃取后，让两个像极了真人的AI声音，通过两人一问一答的方式，把信息给讨论出来。

是不是还很抽象？我给大家演示一下。

我上传一份巴菲特去年在股东大会上的讲话文稿给NotebookLM。

![](.evernote-content/DC2F8DAA-0680-442C-B958-F18A4A5448C7/B6FCF862-609C-4639-9ECF-8799F7CE9751.png)

NotebookLM中间部分可以对你上传的pdf提问，这个就不说了，烂大街了。。。右边有个生成按钮，点一下，等待个几分钟到十几分钟（看文件大小），一份10分59秒的播客就生成好了。

![](.evernote-content/DC2F8DAA-0680-442C-B958-F18A4A5448C7/03D24E66-AD7E-4EB5-ADF4-3B762B9A59CB.png)

给大家听一下生成好的播客，有点遗憾，播客目前还不支持中文，是纯英文的，毕竟是国外的产品，不过对pdf提问是支持中文的。

播客中一男一女的语气和发音听起来和真人没太大区别，有抑扬顿挫，有气口切换，聊着聊着还会笑出声，太真实了。

光听英文音频不太直观，所以我下载了音频，上传到通义听悟翻译成中文，看看AI在聊些什么。我们本意是为了听的，后面支持中文了就没这一步了哈哈，别开倒车又回去看文字了。

![](.evernote-content/DC2F8DAA-0680-442C-B958-F18A4A5448C7/B741082F-B9D9-427D-BFDC-9D7D67CE7B00.png)

播客的开头，AI自然地引出了主题。

NotebookLM以主持人和专家的对话形式，一问一答，帮你通俗易懂地解读文章。

男声说：好的，系好安全带，因为今天我们正在深入伯克希尔哈撒韦股东大会。你想要它，我们得到了它。抄本的摘录直接来自中文原文。

接着，女声说：是的，我们正在谈论沃伦·巴菲特，查理·芒格，整个伯克希尔哈撒韦团队。

果然是很西式的表达，翻译成中文之后一点也不地道。

![](.evernote-content/DC2F8DAA-0680-442C-B958-F18A4A5448C7/D3746652-C9AD-4C16-92B3-7D330277FCA8.png)

NotebookLM把材料提炼的非常精准，没有直接照搬原文，而是重新编排了文字，并且按照人的思维习惯，改写了观点的表达方式，做到结构清晰，引人入胜，让听众能形成自己的结论。

完整听下来之后，可以说，NotebookLM在听觉体验上自然流畅，具备非常强的服务听众意识，完全达到了人类播客的水准。

![](.evernote-content/DC2F8DAA-0680-442C-B958-F18A4A5448C7/2BB7566C-DBAB-43BD-A311-7FD4C7FF1FC1.png)

要注意，NotebookLM并不会搜索新的信息，只是基于我们上传的资料加工处理，所以，它足够个性化，会根据每个人自己的素材生成不同的播客，从而做到千人千面。

更牛的是，最近NotebookLM还上线了一个新功能：**加入（Join）**讨论。

![](.evernote-content/DC2F8DAA-0680-442C-B958-F18A4A5448C7/1F3D9C67-1D39-4DC5-835D-FE1E3EDA01DA.png)

这像极了在现实世界开会的时候，别人在讨论，我作为旁观者随时可以插话提问那种感觉了，赛博开会具象化了，我也可以成为播客一员了。

点击加入按钮，说出你的疑问和看法（目前也只能用英语提问），等个一秒钟左右，播客中的AI主播就会回答你的问题了。

比如，我问了一个问题：

**can you talk about the attitude of Warren Buffet about AI?**

这个互动的自然感，还是很惊人的。不仅是在语音上，也体现在内容上，两位AI主播非常准确而且全面的理解了问题。

原文巴菲特是这么说的：

![](.evernote-content/DC2F8DAA-0680-442C-B958-F18A4A5448C7/2F4375B7-037C-42E4-AAEE-1C2BA40502CD.png)

两位AI主播对我的问题回答的也非常到位，和原文的意思保持一致：

![](.evernote-content/DC2F8DAA-0680-442C-B958-F18A4A5448C7/6860A7C7-6E95-4144-8EA6-7001A2DDF064.png)

这两主播是真的挺强的。

首先他两得先理解我的问题，其次还得去原文找相关的文字段落，然后提炼出信息，最后再用拟人化的口吻和语气来回答我的问题，回答完问题还得接着断掉的地方继续播客。

整个过程用时也不过1秒钟左右，产品体验做到了极致。

唯一的硬伤是还不支持中文。。。

我感觉这东西要是能有国产替代，绝对会火，可是目前国内没有一家跟进了类似的产品。

为啥我这么笃定？

因为一个基本逻辑，人都需要老师教，需要旁人指点，这是受教育很重要的一个过程。

靠自己阅读还真的不一定能看懂，知识被老师口语化的表达出来，反而能迅速让我们的大脑接受，这也是为什么我们在学校有教科书了还需要老师传道受业解惑的原因。

我经常在得到APP上听罗振宇罗胖拆解一本书，厚厚的一本书如果自己看太花时间，得到提供的服务就是在十几分钟甚至几分钟内，把一本书拆解清楚，省略掉绝大部分废话，把核心知识灌输给你。

得到APP上很多书还是要花钱的，可NotebookLM是免费的，我们可以随时把没时间看的文章扔给它，在吃饭、走路、挤地铁、开车的时候播放给我们听，利用好碎片化的时间来消化知识。

吾生有涯而知无涯，这个知识爆炸的时代，帮助人们又好又快消化知识的工具，和知识本身一样重要。

以上，就是对谷歌NotebookLM的使用体验。

我们，下次再见啦。

— **完** —

**点这里👇关注我，记得标星哦～**

---

[🌐 原始链接](https://mp.weixin.qq.com/s?chksm=c2b84246f5cfcb50725f24cfe4b65581300af9c3272b17182918b30beb001daa2c42113b8f50&exptype=unsubscribed_card_recommend_article_u2i_mainprocess_coarse_sort_tlfeeds&ranksessionid=1736949243_2&scene=169&mid=2247484588&sn=2c7097ec1eb4c3113db0e2f89047e033&idx=1&__biz=MzkzNDcxMjE5Nw==&sessionid=1736948515&subscene=200&clicktime=1736951057&enterid=1736951057&flutter_pos=22&biz_enter_id=5&ascene=56&devicetype=iOS18.2.1&version=1800372c&nettype=3G+&abtest_cookie=AAACAA==&lang=zh_CN&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ1L2a5u/q1PzfExL6AeohGRLYAQIE97dBBAEAAAAAAI9MDWM1JNoAAAAOpnltbLcz9gKNyK89dVj0QLvcJOcTs1xcGI3iuTCyp+RvWjpN1CsUcZHp/HLfbDumcaVvK9mRIhiG61o3zjs0wX8gYiJSKSLEpdLWRgdGwaSvwhW/aGqZjB+UJ5+ln07iIppa0Q/DE2H1QpzCcmHvDalhoMB7GK9ys3hc5HcjdEDVLPUsZgvsxivY8cBMAP7qcAw0VsBGgiNvaSUEdg6BSuBq6QqbUr344LJTeQxKbCjiDUTw6qTJDBni7GlsKqteAg==&pass_ticket=oBX7l/f4lqtwSIZ5WtleUxwWGig9uqtQtRy4niQ8kni75FWolatvaeoW4h/wQV0W&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/1a86b678-18fb-4cd1-b9f0-bc76e01f1da8/1a86b678-18fb-4cd1-b9f0-bc76e01f1da8/)