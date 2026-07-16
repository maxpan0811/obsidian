---
title: "图解 Monad"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/图解 Monad.md
tags: [印象笔记]
---

# 图解 Monad

# 图解 Monad --- 函数式编程有一个重要概念，叫做[Monad](https://en.wikipedia.org/wiki/Monad_%28functional_programming%

---

# 图解 Monad

---

函数式编程有一个重要概念，叫做[Monad](https://en.wikipedia.org/wiki/Monad_%28functional_programming%29)。

![](.evernote-content/5A151E86-D65B-4EC7-AB0C-1DB9BC466B16/9E282413-30FC-491F-A7CF-F8D3C3F829FE.jpg)

网上有很多解释（[这里](http://stackoverflow.com/questions/2704652/monad-in-plain-english-for-the-oop-programmer-with-no-fp-background)和[这里](http://stackoverflow.com/questions/44965/what-is-a-monad)），但都很抽象，不容易看懂。我尝试了好多次，还是不明白Monad到底是什么。

![](.evernote-content/5A151E86-D65B-4EC7-AB0C-1DB9BC466B16/EB201E56-2AB3-4990-9480-85A7425836AB.jpg)

昨天，我读到了[Aditya Bhargava](http://adit.io/posts/2013-04-17-functors,_applicatives,_and_monads_in_pictures.html)的文章，他画了很多图。我想了半天，终于恍然大悟。下面，我就用这些图来解释Monad。

1.

![](.evernote-content/5A151E86-D65B-4EC7-AB0C-1DB9BC466B16/C71297E5-AB93-430D-8E06-A3CF6418861C.png)

软件最基本的数据，就是各种值（value）。

2.

![](.evernote-content/5A151E86-D65B-4EC7-AB0C-1DB9BC466B16/5D1521DC-C0E5-48F1-99F0-CACDD4623503.png)

处理值的一系列操作，可以封装成函数。输入一个值，会得到另一个值。上图的"(+3)"就是一个函数，对输入的值加上3，再输出。

3.

![](.evernote-content/5A151E86-D65B-4EC7-AB0C-1DB9BC466B16/4C3F7DBC-3652-46E8-9F37-009618294DEA.png)

函数很像漏斗，上面进入一个值，下面出来一个值。

4.

![](.evernote-content/5A151E86-D65B-4EC7-AB0C-1DB9BC466B16/83125F53-8100-4C2E-B60B-20D735D06984.png)

函数可以连接起来使用，一个函数接着另一个函数。

5.

![](.evernote-content/5A151E86-D65B-4EC7-AB0C-1DB9BC466B16/9102175A-B3C8-4125-9F85-9D34C24106C6.png)

函数还可以依次处理数据集合的每个成员。

6.

![](.evernote-content/5A151E86-D65B-4EC7-AB0C-1DB9BC466B16/5F2F5368-3CFF-403F-9B7B-B82055DDCDA4.png)

说完了函数，再来看第二个概念：数据类型（type）。

数据类型就是对值的一种封装，不仅包括值本身，还包括相关的属性和方法。上图就是2的封装，从此2就不是一个单纯的值，而是一种数据类型的实例，只能在数据类型的场景（context）中使用。

7.

![](.evernote-content/5A151E86-D65B-4EC7-AB0C-1DB9BC466B16/6A7FC7C7-8402-400B-9132-EBDB7B84E1AC.png)

2变成数据类型以后，原来的函数就不能用了。因为"(+3)"这个函数是处理值的（简称"值函数"），而不是处理数据类型的。

8.

![](.evernote-content/5A151E86-D65B-4EC7-AB0C-1DB9BC466B16/9278FFBE-C216-4C8D-AE8F-7027AEB800D5.png)

我们需要重新定义一种运算。它接受"值函数"和数据类型的实例作为输入参数，使用"值函数"处理后，再输出数据类型的另一个实例。上图的fmap就代表了这种运算。

9.

![](.evernote-content/5A151E86-D65B-4EC7-AB0C-1DB9BC466B16/5B4D16D5-0AB4-45D5-BC59-DB12F9540DE6.png)

fmap的内部，实际上是这样：打开封装的数据类型，取出值，用值函数处理以后，再封装回数据类型。

10.

![](.evernote-content/5A151E86-D65B-4EC7-AB0C-1DB9BC466B16/DC08BBFE-8488-4493-9958-3257EDE41296.png)

一个有趣的问题来了。如果我们把函数也封装成数据类型，会怎样？

上图就是把函数"(+3)"封装成一种数据类型。

11.

![](.evernote-content/5A151E86-D65B-4EC7-AB0C-1DB9BC466B16/6C4C9215-D4C5-4512-AAFE-92B4C0420DE3.png)

这时，就需要再定义一种新的运算。它不是值与值的运算，也不是值与数据类型的运算，而是数据类型与数据类型的运算。

上图中，两个数据类型进行运算。首先，取出它们各自的值，一个是函数，一个是数值；然后，使用函数处理数值；最后，将函数的返回结果再封装进数据类型。

12.

![](.evernote-content/5A151E86-D65B-4EC7-AB0C-1DB9BC466B16/30BBF180-BD4C-4E44-A4AA-F2C8A08EA549.png)

函数可以返回值，当然也可以返回数据类型。

13.

![](.evernote-content/5A151E86-D65B-4EC7-AB0C-1DB9BC466B16/B7631AD4-E09B-47AD-B782-BC90E44F26DD.png)

我们需要的是这样一种函数：它的输入和输出都是数据类型。

14.

![](.evernote-content/5A151E86-D65B-4EC7-AB0C-1DB9BC466B16/1EECEA52-77BB-4695-BFC8-200CAAC1FD5B.png)

这样做的好处是什么？

因为数据类型是带有运算方法的，如果每一步返回的都是数据类型的实例，我们就可以把它们连接起来。

15.

![](.evernote-content/5A151E86-D65B-4EC7-AB0C-1DB9BC466B16/36DEBF69-DEB6-47D0-A098-167EDA9D9578.png)

来看一个实例，用户输入一个值10。

16.

![](.evernote-content/5A151E86-D65B-4EC7-AB0C-1DB9BC466B16/36A0A1B6-2902-4A74-9878-C55EA082FDEA.png)

getLine函数可以将它处理成一个STR类型的实例。

17.

![](.evernote-content/5A151E86-D65B-4EC7-AB0C-1DB9BC466B16/150BF52F-13E4-49A1-B237-2255ECE6D075.png)

readfile函数接受STR类型当作文件名，返回一个文件类型的实例。

18.

![](.evernote-content/5A151E86-D65B-4EC7-AB0C-1DB9BC466B16/507B347F-C7B2-45E2-B7C2-17CF43B00433.png)

putStrLn函数将文件内容输出。

19.

![](.evernote-content/5A151E86-D65B-4EC7-AB0C-1DB9BC466B16/8B4457AF-B8E8-47CE-BFBE-12404BE84C93.png)

所有这些运算连起来，就叫做Monad。

简单说，Monad就是一种设计模式，表示将一个运算过程，通过函数拆解成互相连接的多个步骤。你只要提供下一步运算所需的函数，整个运算就会自动进行下去。

（完）

### 文档信息

* 版权声明：自由转载-非商用-非衍生-保持署名（[创意共享3.0许可证](http://creativecommons.org/licenses/by-nc-nd/3.0/deed.zh)）
* 发表日期： 2015年7月16日
* 更多内容： [档案](http://www.ruanyifeng.com/blog/archives.html) » [理解计算机](http://www.ruanyifeng.com/blog/computer/)
* 购买文集：[![](.evernote-content/5A151E86-D65B-4EC7-AB0C-1DB9BC466B16/7F2C0A36-6FA7-4323-A006-DAF97654F3B3.png) 《如何变得有思想》](http://www.ruanyifeng.com/blog/2014/12/my-blog-book.html)
* 社交媒体：[![](.evernote-content/5A151E86-D65B-4EC7-AB0C-1DB9BC466B16/96E08701-18A7-419D-9A57-B6BF147A8764.png) twitter](https://twitter.com/ruanyf)，[![](.evernote-content/5A151E86-D65B-4EC7-AB0C-1DB9BC466B16/5AA65CF3-F560-4FC5-87ED-D2327A2535FF.png) weibo](http://weibo.com/ruanyf)
* Feed订阅： [![](.evernote-content/5A151E86-D65B-4EC7-AB0C-1DB9BC466B16/FE9A3F82-3EAD-4843-931A-6454EB4105F9.gif)](evernote-html-snippet:///feed.html)

---

[🌐 原始链接](http://www.ruanyifeng.com/blog/2015/07/monad.html)

[📎 在印象笔记中打开](evernote:///view/207087/s1/42700de9-bcd0-4c42-afe0-80cc5946fbdb/42700de9-bcd0-4c42-afe0-80cc5946fbdb/)