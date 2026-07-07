---
title: 使用deepseek本地部署，搭建自己的私人知识库，但是效果并不理想 2
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/使用deepseek本地部署，搭建自己的私人知识库，但是效果并不理想 2.md
tags: [evernote, impression, yinxiang]
---

# 使用deepseek本地部署，搭建自己的私人知识库，但是效果并不理想

---

原文链接: [https://mp.weixin.qq.com/s?chksm=e9e8dda9de9f54bfc087352f0b178cd...](https://mp.weixin.qq.com/s?chksm=e9e8dda9de9f54bfc087352f0b178cd4700cd15ae505412e5eb077f6c25a84a0f3e138e20dd7&exptype=unsubscribed_card_recommend_article_u2i_mainprocess_coarse_sort_tlfeeds&ranksessionid=1738657625_4&scene=169&mid=2247485375&sn=e8474beb3430d14abcfbde4b07936132&idx=1&__biz=MzI1MjA1NTQxNw==&sessionid=1738654840&subscene=200&clicktime=1738659756&enterid=1738659756&flutter_pos=67&biz_enter_id=5&ascene=56&devicetype=iOS18.3&version=1800382d&nettype=WIFI&abtest_cookie=AAACAA==&lang=zh_CN&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQjf1ZSORvDth82yprA2EmxBLWAQIE97dBBAEAAAAAADJkODFm/K0AAAAOpnltbLcz9gKNyK89dVj0ZPpXxW+Iy3RlKF268GOj79NGqtRNc9UA8awoyJawmevryNRUtNskjAqrNjwVFwJgRi0Q4oW7U5zzCcElXb38bVLlzZGuXJCx/RzOpP8Se7omlyFD9Lh4jSylMRUvhJFSICSnKoi1pfJ2Z+qch5Xde03zU0WSqtx6SuNhocIWTrgESXPTQtzwksbH35S/pTgV9JumvQVTsP5DyFmbTC5PueaPWx/lqZZ3ChiBDcvXJP0=&pass_ticket=EDFXF15Fdb5gkAOwuHOCK4e8Cr6XsZ5DS/ND7xfa3g3rff73wrIJhZKkPrzZ3Gs3&wx_header=3)

原创 杨泽业  站长在线

使用deepseek本地部署，搭建自己的私人知识库教程

有人问：deepseek本来就可以在线使用，或者下载APP使用，为什么还要自己搭建呢？

回答这个问题，很简单，目前deepseek是免费，不代表以后是免费的，重要的是deepseek使用人数过多，或者受到攻击的时候，可能不能在线使用，而部署在自己的电脑上面，就可以不受网络的影响。但是，最重要的是搭建私人知识库，即内部知识库。不管是个人，还是公司，还是医院、学校等有一些知识、资料是不对外公开的，所以搭建私密数据库，还是有必要的。

如果想在线使用的，可以打开网页https://chat.deepseek.com/ 在线使用，也可以到手机应用市场搜索deepseek 下载手机APP使用。

下面是想自己折腾一下，搭建自己的私人知识库的教程。

先到官方网站下载开源软件。

到官方网站https://ollama.com/ 点击download进行下载。

![](.evernote-content/87D040D3-5012-4E61-ADC8-56EEE0864C02/8DE845C9-7D6B-4464-9B06-344BCB21E1EC.png)

我们这里选择下载的版本是Windows版本，如图：

![](.evernote-content/87D040D3-5012-4E61-ADC8-56EEE0864C02/986BCDFD-1A9E-4742-BC47-D9063885B8AB.png)

下载以后，右键，【管理员身份运行】进行安装。

![](.evernote-content/87D040D3-5012-4E61-ADC8-56EEE0864C02/42AE3F96-9B43-4FB6-8A8D-D8CBCFEA124B.png)![](.evernote-content/87D040D3-5012-4E61-ADC8-56EEE0864C02/2CD28BFB-2177-4E9D-A423-378053072E6A.png)

系统自动安装在C盘无法修改，等待安装完成。

![](.evernote-content/87D040D3-5012-4E61-ADC8-56EEE0864C02/D7DC9711-8B6F-4050-BFC2-31E9EEBB1BFE.png)

安装完成以后，电脑桌面是没有图标的，开始菜单里面有，不过有没有都不影响，因为启动也不是通过图标启动的。

查看安装成功了没有使用的方法是：

按住win+R键，调出运行程序，我们在输入框里面输入cmd，点击确定。

![](.evernote-content/87D040D3-5012-4E61-ADC8-56EEE0864C02/457C8C4F-BC2F-481D-BD01-0FFA987CAC37.png)

在新的窗口中，输入ollama -v 回车，显示：ollama version is 0.5.7 就说明安装成功了。

接下来就是下载模型了

我们到ollama.com首页，点击models，点击第一个deepseek-r1

![](.evernote-content/87D040D3-5012-4E61-ADC8-56EEE0864C02/2923BA5E-19FF-40FB-B6AE-53FB2623DD79.png)

在deepseek-r1中有好几个模型，如下图：

![](.evernote-content/87D040D3-5012-4E61-ADC8-56EEE0864C02/BD3512D8-39FE-4D1B-BD1E-688CAF0632F6.png)

在这里我们根据自己的电脑配置，选择自己的模型，因为默认安装在C盘，所以我这里选择第一个1.5b约占用空间1.1GB，7b模型是4.7GB，8b模型是4.9GB，14b模型是9.0GB，32b是20GB，70b是43GB，671b是404GB，大家根据自己的C盘空间做出选择，原则上数据越大，回答的问题就越全面。但是下载的时间也就越久，既然是自己私人知识库，就选第一个了。

我们选择第一个1.5b的数据右侧，点击复制以后，内容是ollama run deepseek-r1:1.5b，我们在窗口里面进行粘贴，然后点击回车，如图：

![](.evernote-content/87D040D3-5012-4E61-ADC8-56EEE0864C02/D8DBA160-6059-4AAA-AF01-81EE87E374A5.png)

开始的时候后面的速度显示一秒在20M，后面几M，到了截图的时候就是400多KB了，后面就更慢了，我们耐心等待安装完毕。

安装完成以后，就会显示success，就表示安装成功了。

![](.evernote-content/87D040D3-5012-4E61-ADC8-56EEE0864C02/BCB45044-EF92-463E-98B5-99F465C26303.png)

如上图所示，我在还对话框里面，输入了你是谁，系统回答的是：

您好！我是由中国的深度求索（DeepSeek）公司开发的智能助手DeepSeek-R1。如您有任何任何问题，我会尽我所能为您提供帮助。

当然，我们本地部署的目的不是进行对话，而是喂资料给大模型，搭建自己知识库。

说到这里，我们再安装一个交互界面的软件，可以把资料投喂给大模型，当然类似的有很多，本人使用的是AnythingLLM。

到网站anythingllm.com下载软件，如图：

![](.evernote-content/87D040D3-5012-4E61-ADC8-56EEE0864C02/78D1A970-ECAC-482E-A0FF-B34490F15914.png)![](.evernote-content/87D040D3-5012-4E61-ADC8-56EEE0864C02/8501DB6A-F585-4DB7-88F9-BADD975E043B.png)

下载以后，右键管理员身份运行，进行安装，如图：

![](.evernote-content/87D040D3-5012-4E61-ADC8-56EEE0864C02/B99ECC49-18B4-4EFE-9DA4-440F8E08E667.png)

接下来安装的时候，可以调整安装位置，比如我安装在D:\Program Files\AnythingLLM，如图所示：

![](.evernote-content/87D040D3-5012-4E61-ADC8-56EEE0864C02/6090F003-D9D8-4878-8832-994931DF3E54.png)

点击安装以后，直接等待安装完成即可。不过根据我自己的实际安装，速度也是很慢了，他会下载各种模型与之匹配的文件。

![](.evernote-content/87D040D3-5012-4E61-ADC8-56EEE0864C02/D12C5777-11DD-4E44-97D9-1ABD2C9CA897.png)

还好我的教程是图文教程，不是录屏的视频教程，要不然录制视频都要好几个小时，到时候再来剪切视频。图文教程截图以后就慢慢等待安装完成了。

安装好了AnythingLLM以后，桌面就有一个AnythingLLM的快捷方式的图标，我们点击启动软件。得到这样的一个界面，我们点击Get started 开始配置软件。

![](.evernote-content/87D040D3-5012-4E61-ADC8-56EEE0864C02/D271E74E-2DE1-4451-85F7-B446E7212499.png)

在弹出的设置中，我们选择我们要使用的大模型Ollama，然后选择我们模型参数，我这里是1.5b的，然后点击右侧的下一步，如下图所示：

![](.evernote-content/87D040D3-5012-4E61-ADC8-56EEE0864C02/352CED08-2290-4ECC-A983-C45A3D7E45AD.png)

接下来的，不用管，直接下一步，如图所示：

![](.evernote-content/87D040D3-5012-4E61-ADC8-56EEE0864C02/3626C9C1-D97E-4505-86FD-4F1D3E932B72.png)

接下来，需要你提供一个邮箱，这一步我们可以直接跳过，如图：

![](.evernote-content/87D040D3-5012-4E61-ADC8-56EEE0864C02/FDDD67F3-168F-439C-9204-8628E1589459.png)

接下来，命名一个工作区，比如叫做法律知识库、中医知识库、或者细分的唐诗宋词库等，自己命名一个该类型的知识库即可。然后进行下一步，如图所示：

![](.evernote-content/87D040D3-5012-4E61-ADC8-56EEE0864C02/3E77879A-422C-4130-BDE4-E79B3B94AFA9.png)

这个工作区的名称你是可以新建多个知识库的，开始我新建一个法律的，以后还可以新建一个中医的，会计的，文案的等等。每个人都可以根据自己的实际需求，做自己的独有的知识库。

这就是每一个个体或者说是小公司，小团体有机会0成本或者说低成本搭建自己的独有的知识库解决方案了。

接下来的画面是，软件的初始界面，是一些基本的使用说明，如下图：

![](.evernote-content/87D040D3-5012-4E61-ADC8-56EEE0864C02/D716FF6B-A754-4139-86D3-0BEB195158D3.png)

上面的初始界面，我们可以通读一下就不用管他了，重点是下面的内容：

我们先点击左侧的法律知识库这个工作区，右侧有一个上传和设置的图标，我们先点击设置图标，如图所示：

![](.evernote-content/87D040D3-5012-4E61-ADC8-56EEE0864C02/54B0DD25-FA6F-440F-A2BE-98D814927078.png)

这里着重讲一下，每一个知识库都能独立设置使用哪一个大模型，没有独立设置的话，就是系统默认的那一个，这里我们指定Ollama。

在聊天提示默认是英文的一些提示，我们改成与你工作区相对应的提示词，如：本教程写的就是：你是一位专业的法律人士，请根据知识库的内容，使用中文回复。

设置好以后记得点击下面的按钮进行保存哦！如下图所示：

![](.evernote-content/87D040D3-5012-4E61-ADC8-56EEE0864C02/B0789456-9E4F-477C-BDA1-7BB830FEDA83.png)

保存了设置以后，我们就来添加文档给大模型了。

点击法律知识库右侧的上传按钮，如下图所示：

![](.evernote-content/87D040D3-5012-4E61-ADC8-56EEE0864C02/4A4C85F2-3949-40A5-957D-2CDDDC16D2F8.png)

点击上传文档图标，选择你要上传的各种文档，得到下面的界面：

![](.evernote-content/87D040D3-5012-4E61-ADC8-56EEE0864C02/3FADF92A-8DC6-409E-A9B1-5E1E34284338.png)

上传以后，点击移动到工作区的按钮（上图上方长的红色框），得到下面图片，注意点击保存，

![](.evernote-content/87D040D3-5012-4E61-ADC8-56EEE0864C02/50E0B087-B92C-4F9B-878F-A87E079341B5.png)

上面的按钮保存以后是这样的：

![](.evernote-content/87D040D3-5012-4E61-ADC8-56EEE0864C02/C64B6027-BED0-411C-96FE-5AB4DC9708D8.png)

这时候，我们没有使用图钉按钮，没有把他钉起来的时候，也是不会读取其中的文档的，比如下面进行测试：

点击左侧的法律知识库，在右边的对话输入框里面输入：杨泽业法律工作室成立时间是什么时候，结果如下：

![](.evernote-content/87D040D3-5012-4E61-ADC8-56EEE0864C02/8DCB5E02-B097-48D8-A68D-A6B8A8A04945.png)

他的回答是：

根据目前的了解，杨泽业法律工作室成立于2010年左右。然而，具体成立的时间可能因企业而异，建议查阅企业的官方网站或相关的法律、会计资料以获取准确信息。

这样的回答完全不是我们想要的答案，我在上传的文档中有一个文档是【杨泽业法律工作室简介.pdf】，内容截图如下：

![](.evernote-content/87D040D3-5012-4E61-ADC8-56EEE0864C02/B8B4A0D5-6A9D-4B00-88F7-4D5C797254C7.png)

现在我们返回文档上传页面，即点击上传文档的按钮，把我们上传到工作区的文档，点击图钉按钮，把文档钉起来，就能识别文档的内容了，截图如下：

![](.evernote-content/87D040D3-5012-4E61-ADC8-56EEE0864C02/90E10EDD-E638-49B7-A87B-5A5E42F33E69.png)

上图中，最后两个文件，我没有钉起来，看起来就是白色的，钉起来以后就是黑色的了。现在我们新建一个对话框，看看会不会识别文档中的内容了：

![](.evernote-content/87D040D3-5012-4E61-ADC8-56EEE0864C02/FAD73525-545B-4B54-AB0B-2656868826A9.png)

实际上回答的还是不对，我提醒他看看文档：

![](.evernote-content/87D040D3-5012-4E61-ADC8-56EEE0864C02/7AA8126F-831C-46E7-B724-2FA03FECBF9F.png)

所以说，本地部署就算是成功了，效果也是不理想的，所以还没有折腾的就不用折腾了，当然想折腾的，就下载大一点的模型参数试试。

群里面有人说：

知识库是人工智能rag(检索增强生成)的领域，如果要做智能很多东西要优化，第一大模型本身足够强，1.5b只能作为简单示例，它还要考虑嵌入模型，重排序模型，向量数据库，文本分割等等，要实际应用还要学好多东西，所以要不然还是不要折腾了，各大自媒体都在教部署本地的，实际上不理想，没有必要了。

教程没有问题，但是效果不理想，有部署好的，比较理想的，大家可以相互交流。

---

[🌐 原始链接](https://mp.weixin.qq.com/s?chksm=e9e8dda9de9f54bfc087352f0b178cd4700cd15ae505412e5eb077f6c25a84a0f3e138e20dd7&exptype=unsubscribed_card_recommend_article_u2i_mainprocess_coarse_sort_tlfeeds&ranksessionid=1738657625_4&scene=169&mid=2247485375&sn=e8474beb3430d14abcfbde4b07936132&idx=1&__biz=MzI1MjA1NTQxNw==&sessionid=1738654840&subscene=200&clicktime=1738659756&enterid=1738659756&flutter_pos=67&biz_enter_id=5&ascene=56&devicetype=iOS18.3&version=1800382d&nettype=WIFI&abtest_cookie=AAACAA==&lang=zh_CN&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQjf1ZSORvDth82yprA2EmxBLWAQIE97dBBAEAAAAAADJkODFm/K0AAAAOpnltbLcz9gKNyK89dVj0ZPpXxW+Iy3RlKF268GOj79NGqtRNc9UA8awoyJawmevryNRUtNskjAqrNjwVFwJgRi0Q4oW7U5zzCcElXb38bVLlzZGuXJCx/RzOpP8Se7omlyFD9Lh4jSylMRUvhJFSICSnKoi1pfJ2Z+qch5Xde03zU0WSqtx6SuNhocIWTrgESXPTQtzwksbH35S/pTgV9JumvQVTsP5DyFmbTC5PueaPWx/lqZZ3ChiBDcvXJP0=&pass_ticket=EDFXF15Fdb5gkAOwuHOCK4e8Cr6XsZ5DS/ND7xfa3g3rff73wrIJhZKkPrzZ3Gs3&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/55718272-9929-4672-8d54-7d2a33328f06/55718272-9929-4672-8d54-7d2a33328f06/)
