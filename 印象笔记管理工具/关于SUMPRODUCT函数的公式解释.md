# 关于SUMPRODUCT函数的公式解释

---

关于SUMPRODUCT函数的公式解释
-------------------

*2016-05-23**罗国发*[Excel之家ExcelHome](http://mp.weixin.qq.com/s?__biz=MjM5NTcxODg0MA==&mid=400878215&idx=1&sn=58a437314fa9fb90192877b82ac8b185&mpshare=1&scene=1&srcid=032341X1AvPvC4YJdnMimcCP##)

![](.evernote-content/8567D6FB-C28D-4842-865F-55F1AE368B84/7C8D21FA-723C-4338-AADE-A53B6A2549B4.jpg)

本文是图书《别怕，Excel函数其实很简单》II随书问题参考答案，如需了解更多函数公式的用法，请关注图书正文。

问题

你知道在公式

=SUMPRODUCT((A2:A11=E2)+0,(B2:B11=F2)+0,C2:C11)

中，SUMPRODUCT函数的第1参数和第2参数的“+0”有什么用吗？为什么没有“+0”公式不能完成统计？

参考答案

这是一个多条件求和的公式。

想知道公式中的“+0”有什么用，让我们先来看看SUMPRODUCT函数对参数的要求。

SUMPRODUCT函数用于求多组数值的乘积之和。这就要求各参数中包含的是数值类型的数据，如果参数中包含的数据不是数值类型，在计算时，SUMPRODUCT函数会把该数据当成数值0处理。

记住这个规则后，让我们先来看看去掉“+0”的公式是什么样：

=SUMPRODUCT(A2:A11=E2,B2:B11=F2,C2:C11)

很显然，SUMPRODUCT函数的第1、2参数都是执行比较运算的表达式，而比较运算返回的结果只能是逻辑值TRUE或FALSE。

也就是说，SUMPRODUCT函数的第1、2参数都是由逻辑值TRUE或FALSE组成的数组，如图 1所示。

![](.evernote-content/8567D6FB-C28D-4842-865F-55F1AE368B84/A70AE284-88CA-4CE2-AE65-0A47EFD48D30.png)

图 1     SUMPRODUCT函数的各参数

因为第1、2参数中的逻辑值在计算时会被当成0值处理，和第3参数中的各个数值相乘后的结果也就是0，所以导致最终的统计结果为0，如图 2所示。

![](.evernote-content/8567D6FB-C28D-4842-865F-55F1AE368B84/D3AC7E0B-20FE-4925-8B3B-E94ED565CB53.jpg)

图 2     SUMPRODUCT函数错误的统计结果

公式中“+0”的作用就是将这些逻辑值转为数值，不让SUMPRODUCT将它们全部当成数值0。

因为逻辑值TRUE和FALSE可以直接参与算术运算，在运算时TRUE会被当成数值1，FALSE会被当成数值0。

让SUMPRODUCT函数第1、2参数中的逻辑值加上一个不会改变其对应数值大小的0值，就可以实现逻辑值转数值的目的。在转为数值的第1、2参数中，只有相同位置的两个数值都为TRUE，和第3参数相同位置的数值相乘后才不会得到0，SUMPRODUCT函数就是通过这样的思路来解决条件求和的问题。如图 3所示。

![](.evernote-content/8567D6FB-C28D-4842-865F-55F1AE368B84/53F98FCD-2C5A-4878-B85B-246AF1AB7F73.png)

图 3     SUMPRODUCT函数的计算结果

当然，你也可以使用其他方法代替“+0”来完成这个转换数据类型的问题。你还知道什么好方法？记得和我们大家分享。

![](.evernote-content/8567D6FB-C28D-4842-865F-55F1AE368B84/C8DB3378-1BE9-4AB6-A5DA-C241249AC6B0.png)

最佳的Excel微信公众号

如果希望获得更多关于Excel方面的优秀教程，请关注ExcelHome的官方微信，每天都能免费收到最优秀、最适用的Excel实用教程。

![](.evernote-content/8567D6FB-C28D-4842-865F-55F1AE368B84/28655815-CC98-4EA0-AF7B-BE6D7D30505A.jpg)

公众号：iexcelhome

长按识别左图的二维码，即可关注最受欢迎的Excel微信公众号。

1、如果在学习本书的过程中遇到问题，可以点击页面下方的“**阅读原文**“，到ExcelHome论坛与大家交流；

2、如果需要联系作者，解答学习过程中遇到的疑问，可以直接回复“**叶枫在线**”获得作者的联系方式。

[阅读原文](http://mp.weixin.qq.com/s?__biz=MjM5NTcxODg0MA==&mid=400878215&idx=1&sn=58a437314fa9fb90192877b82ac8b185&mpshare=1&scene=1&srcid=032341X1AvPvC4YJdnMimcCP##)

---

[🌐 原始链接](http://mp.weixin.qq.com/s?__biz=MjM5NTcxODg0MA==&mid=400878215&idx=1&sn=58a437314fa9fb90192877b82ac8b185&mpshare=1&scene=1&srcid=032341X1AvPvC4YJdnMimcCP#rd)

[📎 在印象笔记中打开](evernote:///view/207087/s1/ec8cce56-6cf1-422c-83c4-88823f72878c/ec8cce56-6cf1-422c-83c4-88823f72878c/)