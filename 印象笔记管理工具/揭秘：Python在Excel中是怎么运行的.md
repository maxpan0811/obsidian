# 揭秘：Python在Excel中是怎么运行的

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzA3NTMzMjMyOA==&mid=265093...](https://mp.weixin.qq.com/s?__biz=MzA3NTMzMjMyOA==&mid=2650939362&idx=1&sn=e2bf346312554fca15c091de3d71c808&chksm=850d9fa99e771acf68dc223c8da6d26d11b8a61cfb302491c22a52ba9e84066f4ed8e9cffcea&scene=90&xtrack=1&sessionid=1743321397&subscene=272&clicktime=1743327502&enterid=1743327502&flutter_pos=69&biz_enter_id=4&ranksessionid=1743324730&jumppath=20020_1743324729591,WAOpenWxMaterialListController_1743324858056,20020_1743324873833,1104_1743324874794&jumppathdepth=4&ascene=56&devicetype=iOS18.3.2&version=1800392b&nettype=3G+&abtest_cookie=AAACAA==&lang=zh_CN&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQvLwPLgOMk3Yxargb4L1O3hLYAQIE97dBBAEAAAAAAIyWJePPSgIAAAAOpnltbLcz9gKNyK89dVj0E5mJNmoE4fCtslVRJMpmWMYhN9S42CXpfRj+O5hPKEj+jDmkQdfEEQpqAMHvurmvr57Hs2Ar4DOxEAnSJ1+GtdUSKbTpqOqkRkAEzmbzcgQkX8cHIAqw+bOEo1pFxVHCltlRWYG+EOZ9sdj2KuxAZe6qr3FTJBRaN6Yem4Q3Fg9PN/5F5ec6sxfTNWwqmmhF1epNbT0Rq740tapbGpetPLhyr/xmtix6+Tryk8+eXQ10mg==&pass_ticket=AZRGGa184RKJ7urw0wZWVX9TQd5CBYAdzz+KpKA0bE4AkU7YgfIP/cr/z5SDdJky&wx_header=3)

原创fanjy完美Excel

学习Excel技术，关注微信公众号：

*excelperfect*

**标签：**Python与Excel

现在，Excel中已经集成了Python，意味着可以使用Python来实现更多更灵活强大的Excel解决方案了。

在工作表单元格中，像输入公式一样，输入：

=py

按Tab键，此时就创建了一个Python单元格，如下图1所示。

![](.evernote-content/557705CF-8D87-45C3-9231-BE4B4906F5ED/E709938F-38F0-4355-98E1-A077DD74E044.jpg)

图1

现在，就可以在该单元格或者公式栏中输入Python语句命令了。正如图1中所提示的，输入后直接按Enter键，会创建一个新行，继续输入Python命令；按Ctrl+Enter组合键，则会提交来运行已经输入的Python命令。

提交后，你会看到该单元格中会出现刷新图标或BUSY字样，等个几秒钟就会出现结果了，这是为什么呢？

这是因为集成在Excel中的Python托管在云中的Azure（即Microsoft的云数据库）中，需要联网才能工作。而Python代码是保存在工作表单元格中的，当提交或者更新了Python单元格时，它会与云端通信，在云端运行代码，并将结果返回给Python单元格。正是由于这种云端交互，Python单元格的计算时间可能会比普通单元格要长。

大多数Python代码是多行的，在Python单元格中输入代码时，按Enter键会插入一个新代码行用于输入代码；如果代码全部输入完了，那么按Ctrl+Enter组合键表明提交最终的代码。

下面，通过一个示例来展示Python代码在Excel中的运行。

在工作表单元格A1中，输入：

=py

按Tab键后，输入：

#生成虚拟数据

from faker import Faker

fake = Faker()

"初始化Faker"

如下图2所示。

![](.evernote-content/557705CF-8D87-45C3-9231-BE4B4906F5ED/FB55E7A9-ECAE-44FD-8AA6-8F7B6DDEEF70.jpg)

图2

输入完成后，按Ctrl+Enter键提交，结果如下图3所示。

![](.evernote-content/557705CF-8D87-45C3-9231-BE4B4906F5ED/601B0679-C9DF-4F55-B893-ED45DF11CA35.jpg)

图3

上述代码中：

#生成虚拟数据

与在专业Python编辑器中编写代码一样，如果前面带有#符号的行，表明该行是注释行，不是Python代码，只是用来描述代码的作用。

from faker import Faker

用于导入Faker包，这样就可以访问其功能。

fake = Faker()

将Faker赋给为名为fake的变量。这意味着，在这个工作表中所有其他Python单元格都可以使用变量fake来访问Faker包及其功能。在单元格A1中创建的任何变量都可以在整个工作表中被访问。

"初始化Faker"

在单元格A1中显示一条消息，什么都不做，只是一个文本描述。有时Python单元格不会显示任何内容，或者可能只会显示一个词。通过用引号中的文本结束代码，可以描述该单元格的功能，也有助于记录。

同样，在单元格A2中，输入：=py，按Tab键，输入Python代码：

#随机名字

fake.name()

按Ctrl+Enter键提交，结果如下图4所示。

![](.evernote-content/557705CF-8D87-45C3-9231-BE4B4906F5ED/4D287019-7A5B-40AB-83ED-CE8FC30FE22C.jpg)

图4

代码：

fake.name()

此代码显示了一个虚拟名字。注意，每次重新计算这个Python单元格时，这个名字都会改变。

要显示多个名字，可以使用Python循环语句。在单元格A4中，按上面同样的方法，输入Python代码：

#多个虚拟名字

fake\_names = [fake.name() for \_ in range(20)]

按Ctrl+Enter键，结果如下图5所示。

![](.evernote-content/557705CF-8D87-45C3-9231-BE4B4906F5ED/ED0F5F3B-2816-45A3-890A-AE1881AB2ABA.jpg)

图5

该代码中有一个循环，用来创建20个名字。其中的方括号定义一个列表，方括号内的代码是一个创建20个单独名字的循环。

然而，该代码并没有显示名字，如下图6所示，只是返回文本“列表”。要看到所有的名字，需要单击公式栏PY左侧的下拉图标，选择“Excel值”，如下图6所示。

![](.evernote-content/557705CF-8D87-45C3-9231-BE4B4906F5ED/DDD85D1E-34B3-48EB-9ACA-4C2ABC658596.jpg)

图6

这样就会看到所有随机生成的名字，如下图7所示。

![](.evernote-content/557705CF-8D87-45C3-9231-BE4B4906F5ED/F68EFB84-87B6-47AA-85E0-4EFC4764B6BE.jpg)

图7

同样，当这个Python单元格被重新计算时，这些名字也会发生改变。

在上图6中，我们看到点击下拉箭头后会有两个选项：“Python对象”和“Excel值”。注意，通常默认是“Python对象”。

此外，在Excel工作表界面右侧，还会出现“Python编辑器”窗格，如下图8所示，在其中可以看到所有单元格中的代码，可以编辑代码，也会显示代码错误消息。

![](.evernote-content/557705CF-8D87-45C3-9231-BE4B4906F5ED/DA1E6E92-53A2-4852-B4C6-DD92B5344ED5.jpg)

图8

注：本文学习整理自a4accounting.com.au，供有兴趣的朋友参考。

**欢迎在下面留言，完善本文内容，让更多的人学到更完美的知识。**

欢迎到知识星球：***完美******Excel******社群***，进行技术交流和提问，获取更多电子资料，并通过社群加入专门的微信讨论群，更方便交流。

![](.evernote-content/557705CF-8D87-45C3-9231-BE4B4906F5ED/908FCC8F-B965-49FF-A3C8-FEB54F7779A0.jpg)

素材来源官方媒体/网络新闻

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzA3NTMzMjMyOA==&mid=2650939362&idx=1&sn=e2bf346312554fca15c091de3d71c808&chksm=850d9fa99e771acf68dc223c8da6d26d11b8a61cfb302491c22a52ba9e84066f4ed8e9cffcea&scene=90&xtrack=1&sessionid=1743321397&subscene=272&clicktime=1743327502&enterid=1743327502&flutter_pos=69&biz_enter_id=4&ranksessionid=1743324730&jumppath=20020_1743324729591,WAOpenWxMaterialListController_1743324858056,20020_1743324873833,1104_1743324874794&jumppathdepth=4&ascene=56&devicetype=iOS18.3.2&version=1800392b&nettype=3G+&abtest_cookie=AAACAA==&lang=zh_CN&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQvLwPLgOMk3Yxargb4L1O3hLYAQIE97dBBAEAAAAAAIyWJePPSgIAAAAOpnltbLcz9gKNyK89dVj0E5mJNmoE4fCtslVRJMpmWMYhN9S42CXpfRj+O5hPKEj+jDmkQdfEEQpqAMHvurmvr57Hs2Ar4DOxEAnSJ1+GtdUSKbTpqOqkRkAEzmbzcgQkX8cHIAqw+bOEo1pFxVHCltlRWYG+EOZ9sdj2KuxAZe6qr3FTJBRaN6Yem4Q3Fg9PN/5F5ec6sxfTNWwqmmhF1epNbT0Rq740tapbGpetPLhyr/xmtix6+Tryk8+eXQ10mg==&pass_ticket=AZRGGa184RKJ7urw0wZWVX9TQd5CBYAdzz+KpKA0bE4AkU7YgfIP/cr/z5SDdJky&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/9db70616-a074-4e42-b009-d0390e0cb63d/9db70616-a074-4e42-b009-d0390e0cb63d/)