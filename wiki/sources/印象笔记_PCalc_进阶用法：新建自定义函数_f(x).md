---
title: "PCalc 进阶用法：新建自定义函数 f(x)"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/PCalc 进阶用法：新建自定义函数 f(x).md
tags: [印象笔记]
---

# PCalc 进阶用法：新建自定义函数 f(x)

# PCalc 进阶用法：新建自定义函数 f(x) --- （为了避免翻译造成误解，文中部分词语仍以英文表达或中文旁备注英文。） 作为一个机械系「攻城狮」，经常需要查询螺纹的基础数据，比如最常用的螺纹

---

# PCalc 进阶用法：新建自定义函数 f(x)

---

（为了避免翻译造成误解，文中部分词语仍以英文表达或中文旁备注英文。）

作为一个机械系「攻城狮」，经常需要查询螺纹的基础数据，比如最常用的螺纹大径、中径和小径（如图，d 为外螺纹大径，d2 为中径，d3 为小径）。在电脑前，可以直接用 Excel 公式计算获得，但很多时候在生产现场就马上需要某种螺纹规格数据，随身带着袖珍版纸质标准既不方便也不效率。

![](.evernote-content/0D84EF4A-04AB-4336-AAA0-B3E2E6664C4A/02BBE142-B870-44EE-83C4-22FFD3170DDF.jpg)螺纹基本参数

上图中 d1、d2 可根据 d （已知数值参数，不要问为什么，这和本文无关 :P）和螺距 P（你就理解为另外一个已知数值参数）查询标准得出。

![](.evernote-content/0D84EF4A-04AB-4336-AAA0-B3E2E6664C4A/E15EBE9F-20E9-4BF6-AD67-B1A2D5CB9205.png)纸质标准数据

这很不效率，通过手机利用公式自动计算数据才是最佳方案， 随拿随用，用完放兜。

既然是计算数据，自然是用计算器喽。计算器 App 林林种种，能计算公式的也不少，但 PCalc 三点特性使其更适合用于工程领域。

1. 高开放性，所有按键可自定义，根据不同领域定制最合适的布局；
2. 高效率性，丰富的 URL Scheme 以及对 3D Touch 的支持。平时作为普通计算器使用，通过 3D Touch 快速切换到自定义布局进行工程计算；
3. 可编程性1 ，丰富的运算法则让你得心应手，编写出更强大的函数。

看下 PCalc 查询效果，数据和标准是一致的。

![](.evernote-content/0D84EF4A-04AB-4336-AAA0-B3E2E6664C4A/6AF3F3A9-4704-422F-8E46-CD1F2ECBA0D7.gif)PCalc 快速查询螺纹数据

如何新建自定义函数

新建函数必须通过 `f(x) 按键` 进入函数界面，编辑添加新函数类别（**New Category**），应用会自动建立 **New Function** 并附带一个**「Multiply X by 42**」。

![](.evernote-content/0D84EF4A-04AB-4336-AAA0-B3E2E6664C4A/34E57232-DDED-4909-8EEC-FD9E9AE3F566.png)PCalc 新建函数

「Multiply X by 42」就是一个乘法「**运算命令 Command**」，即 X 乘以 42。而 X 称为「**变量 Variable**」。

PCalc 之所以强大是因为它有着丰富的变量和完善的运算命令。

丰富的变量 Variable
--------------

![](.evernote-content/0D84EF4A-04AB-4336-AAA0-B3E2E6664C4A/F0DC943B-2120-4699-9972-F2F2A5815E3C.png)PCalc 所有函数变量

### 变量可以分为以下六类：

1. X、Y
   * 当前输入行的数值即为 X，比如输入「42」，X 的值就是42；
   * 在代数模式（algebraic mode）下，通过 xy 按键（Swap x and y）来分别输入 Y 和 X 值。
2. Memory 0 ~ 9
   * 当函数运算前需要输入多个基础数据时，这些数据可先存储在 Memory 中；

     ![](.evernote-content/0D84EF4A-04AB-4336-AAA0-B3E2E6664C4A/34688C52-3F58-4CDD-850B-C76CF2C4BFC9.jpg)Memory 相关命令按钮
   * Memory 0 ~ 9 可以通过 Memory 相关命令按钮操作，用 reg按键 进入「registers section」界面查看具体数值。

     ![](.evernote-content/0D84EF4A-04AB-4336-AAA0-B3E2E6664C4A/EB6452F5-B5FF-4C9F-ADF5-F810DB4ECBC8.png)「registers section」界面
3. RPN Stack 1 ~ 9
   * RPN 模式2 下堆栈位，功能类似 Memory。
4. Register 0 ~ 9，A ~ F
   * 功能同 Memory。但是，对于需要输入较多基础数据的函数，建议把 Memory 的值赋给 Register，并用 Register 替代 Memory 参与函数的运算。虽然不这么做对最终运算结果没有影响，但万一运算结果有误，你无法判断是数值输入错误还是函数运算过程不对；
   * Register 0 ~ 9，A ~ F 只能通过运算命令 Command 调用，无法在「registers section」界面查看；
   * PCalc 不会在函数运行后清除 Registers 被赋的值。
5. Tax Rate
   * 税率，可实时更新。只能通过运算命令 Command 调用，无法在「registers section」界面查看；
6. Clipboard
   * 提取剪贴板数据。

完善的运算命令 Command
---------------

通俗点讲，运算命令就是运算法则，加减乘除、平方、立方、对数、指数、三角函数等。以下列出所有 PCalc 支持的运算命令。

![](.evernote-content/0D84EF4A-04AB-4336-AAA0-B3E2E6664C4A/ABACEDA7-AAF9-4686-BEF0-50D2FA37919D.png)PCalc 函数运算命令 1

![](.evernote-content/0D84EF4A-04AB-4336-AAA0-B3E2E6664C4A/82DF3416-1089-4352-8995-8C62E989636A.png)PCalc 函数运算命令 2

### 运算命令按需要输入的参数数量分为四类：

1. 只有 command 本身，比如 `Switch to Decimal`；

![](.evernote-content/0D84EF4A-04AB-4336-AAA0-B3E2E6664C4A/E931BB4F-C546-4693-838D-C094599FFB3C.jpg)Switch to Decimal

2. command 及一个参数，比如 `Clear`；

![](.evernote-content/0D84EF4A-04AB-4336-AAA0-B3E2E6664C4A/91863758-F70B-45AF-BB77-5B4F6D259ABA.jpg)Clear

3. command 及两个参数，比如 `Set`；

![](.evernote-content/0D84EF4A-04AB-4336-AAA0-B3E2E6664C4A/B07AF5E4-1840-4D21-8637-0702D317A6CC.jpg)Set

4. command 及三个参数，比如 `Skip If Greate Than`。Skip 值是跳过该 if command 后面的 commands 数量。

![](.evernote-content/0D84EF4A-04AB-4336-AAA0-B3E2E6664C4A/55B36D90-2168-49A9-B757-475A36232A55.jpg)Skip If Greate Than

每个运算命令中，Register 一栏是目标参数，Value 是被运算参数，比如 Set X to 42，即把 42 赋值给 x，x=42。

函数运作模式
------

我们通过 App 自带的 Special Category 里面的解一元二次方程来了解函数运作模式.。

![](.evernote-content/0D84EF4A-04AB-4336-AAA0-B3E2E6664C4A/BBDCFBE9-E4FF-42A2-917F-F18D583F238B.png)一元二次方程

一元二次方程通用求根公式（中学知识，应该都知道吧）：

![](.evernote-content/0D84EF4A-04AB-4336-AAA0-B3E2E6664C4A/19103871-9140-4C37-89B4-7F6965D0338E.png)一元二次方程求根公式

函数步骤如下：

| Commands | 值 |
| --- | --- |
| Switch to Decimal | 切换到十进制 |
| Set R1 to X | R1 = X |
| Set R2 to Y | R2 = Y |
| Negate R2 | R2 = -Y |
| Set R3 to M0 | R3 = M0 = m *（m 值存储在 Momery 0 中）* |
| Set R4 to R2 | R4 = R2 = -Y |
| R4 to Power of 2 | R4 = Y^2 |
| Multiply R3 by R1 | R3 = R3 \* R1 = Xm |
| Multiply R3 by 4 | R3 = R3 \* 4 = 4Xm |
| Subtract R3 from R4 | R4 = R4 - R3 = Y^2 - 4Xm |
| R4 To Power of 0.5 | R4 = (Y^2 - 4Xm)^0.5 |
| Set X to R2 | X = R2 = -Y |
| Add R4 to X | X = X + R4 = -Y + (Y^2 - 4Xm)^0.5 |
| Divide X by 2 | X = X / 2 = (-Y + (Y^2 - 4Xm)^0.5) / 2 |
| Divide X by R1 | X = X / R1 = (-Y + (Y^2 - 4Xm)^0.5) / 2X **（根1）** |
| Set Y to R2 | Y = R2 = -Y |
| Subtract R4 from Y | Y = Y - R4 = -Y - (Y^2 - 4Xm)^0.5 |
| Divide Y by 2 | Y = Y / 2 = (-Y - (Y^2 - 4Xm)^0.5) / 2 |
| Divide Y by R1 | Y = Y / R1 = (-Y - (Y^2 - 4Xm)^0.5) / 2X **（根2）** |
| Set M0 to 0 | M0 = 0 |

我们来试着解下述一元二次方程。

![](.evernote-content/0D84EF4A-04AB-4336-AAA0-B3E2E6664C4A/AF67E01A-9A17-4004-AEBF-B44BC508B7A2.png)一元二次方程实例

使用自带的 「Retro 按键布局」且关闭「Multiple Memories」选项时，输入过程3 为：

`2`→`x~y`→`3`→`+/-`→`x~m`→`1`→`f(x)`→Special→Solve X\*x2+Y\*x+m=0   
此时根 1（也就是 X 值）直接显示在界面上，根 2（即 Y 值）需要通过 `reg 按键` 在「registers section」界面查看。

![](.evernote-content/0D84EF4A-04AB-4336-AAA0-B3E2E6664C4A/A4D425A8-54DB-4333-8C15-A2C19A225BFD.png)registers section」界面查看两根

如何更效率地编辑函数
----------

如果函数步骤不多，在 PCalc 中一个个拖动编辑 command 也还能忍受。当建立复杂函数时，其 command 数量会多得吓人，你不仅得有十足的耐心，更需要十分的小心，避免遗漏或弄错 command。

幸运的是，自定义函数可以以 **.pcalcfunctions 文件**形式通过系统 Share 传到电脑，然后用 **plist 编辑器**修改。

新建计算圆面积函数 π\*X^2 及其 plist 代码如下图。

![](.evernote-content/0D84EF4A-04AB-4336-AAA0-B3E2E6664C4A/A9DBFE7C-D8AA-4EB5-A2B9-D0B83A7CA82D.jpg)计算圆面积函数![](.evernote-content/0D84EF4A-04AB-4336-AAA0-B3E2E6664C4A/7B81BACC-67F4-4C2E-8DEF-FDB595F0EB4A.png)圆面积函数 plist 代码

**pwr x 2; mul x pi** 即运算步骤，command 需缩写。这里列出部分 command 对应的缩写形式4 。

```
1.set x 42      # Set X to 42  
2.clr x         # Clear X  
3.add x 42      # Add 42 to X  
4.sub x 42      # Subtract 42 from X  
5.mul x 42      # Multiply X by 42  
6.div x 42      # Divide X by 42  
7.neg x         # Negate X  
8.inv x         # Invert X  
9.pwr x 42      # Raise X to the power of 42  
10.roo x 42      # Raise X to the power of 1/42  
11.sin x         # Sine of X  
12.cos x         # Cosine of X  
13.tan x         # Tangent of X  
14.asn x         # Arcsine of X  
15.acs x         # Arccosine of X  
16.atn x         # Arctangent of X  
17.ln x          # Natural log of X  
18.log x         # Base 10 log of X  
19.exp x         # e to the power of X  
20.e10 x         # 10 to the power of X  
21.fac x         # Factorial of X  
22.rnd x         # Round X to nearest integer  
23.trn x         # Truncate X to nearest integer  
24.hyp x 42      # Hypotenuse of triangle with legs X and 42  
25.leg x 42      # Leg of triangle with hypotenuse and other leg of X and 42   
26.dec           # Decimal mode  
27.hex           # Hex mode  
28.oct           # Octal mode  
29.bin           # Binary mode  
30.deg           # Degrees mode  
31.rad           # Radians mode  
32.jmp 1         # Skip 1 step  
33.beq x 42 1    # Skip 1 step if X is equal to 42  
34.bne x 42 1    # Skip 1 step if X is not equal to 42  
35.bgt x 42 1    # Skip 1 step if X is greater than 42  
36.bge x 42 1    # Skip 1 step if X is greater than or equal to 42  
37.blt x 42 1    # Skip 1 step if X is less than 42  
38.ble x 42 1    # Skip 1 step if X is less than or equal to 42  
39.stp           # Stop
```

总结
--

正所谓「工欲善其事必先利其器」，如果你经常需要使用计算器，老牌 PCalc 绝对算得上是易用性和开放程度最高的一款（至少目前是）。通过设置每个按键大小、样式和功能，完全可以打造一个最顺手的计算器。同时，其强大的自建函数功能更会让你觉得物超所值，而且作者从 2012 年开始不断地更新添加新功能。

关于 PCalc 基础用法以及如何自定义按键布局，详见 [《PCalc 入门用法：自定义一个最顺手的计算器》](https://sspai.com/post/36853)。

了解更多关于 PCalc 的评测、用法和技巧，见 [此博客](http://www.leancrew.com/) 并搜索 PCalc （搜索需带梯子），博主是个工程师，从 PCalc 早期版本就在使用。

---

[🌐 原始链接](https://sspai.com/post/39613)

[📎 在印象笔记中打开](evernote:///view/207087/s1/ffcf7c1f-cc47-4330-9d96-964c37938710/ffcf7c1f-cc47-4330-9d96-964c37938710/)