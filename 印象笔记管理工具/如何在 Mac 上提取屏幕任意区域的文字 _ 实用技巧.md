# 如何在 Mac 上提取屏幕任意区域的文字 | 实用技巧

---

如何在 Mac 上提取屏幕任意区域的文字 | 实用技巧
===========================

| 本文为付费栏目文章，您已订阅，可阅读全文 |

更新：中文字符间的空格问题已解决。感谢读者 @cobb。

各位大概没少遇到过这种情况：明明看到一段文字，却很难或不能选中复制它。

原因很复杂，也许文字上有隐藏广告链接，也可能是网页本身有保护不准复制，或者我们遇上的根本就是一张图片 —— 这些问题，如果要一一击破其实很困难。但不妨换个思路，既然我们可以看到文字，那就有个统一的解决方案：**OCR（Optical Character Recognition），光学字符识别。**

Power+ 有过不少通过 OCR 来解决问题的文章，之前我们就多次处理过扫描版的 PDF，将其中的文字变成可识别的文字：

* 《[通过 OCRmyPDF 实现在扫描版 PDF 中检索文字](https://sspai.com/post/44045)》
* 《[5 个不为人知的 PDF 技巧](https://sspai.com/article/52237?series_id=70)》

这次，我们把目标转向更加日常的情形，实现随时随地的文字提取。为了照顾尽可能多的使用场景，我为 Mac 做了一套**完全免费的 OCR 自动化动作，可以在任何 App 中召唤出来，截取想要识别的屏幕区域，就能提取出文字。**

![](.evernote-content/35EAAFF3-6A24-413B-8D0E-CD74F72817AC/B128531D-537E-4900-90FC-9C2BDA6E4874.gif)

从网页图片中提取文字（文字颜色和背景区别不明显也可以提取）

动作使用
----

使用前要做好自动化动作和 OCR 引擎两部分准备，引擎的安装在下面小节会细说。

* [动作下载 Automator 版](https://cl.ly/4800f6a6c726) ，[GitHub 地址](https://github.com/BlackwinMin/Automator-gallery/tree/master/OCR%20Screencapture.workflow.zip)
* [动作下载 LaunchBar 版](https://cl.ly/c9e6a61d0e04) ，[GitHub 地址](https://github.com/BlackwinMin/LaunchBar-gallery/tree/master/OCR%20Screencapture.lbaction.zip)
* [动作下载 Alfred 版](https://cl.ly/10a57c89e583) ，[GitHub 地址](https://github.com/BlackwinMin/Alfred-gallery/tree/master/OCR%20Screencapture/OCR%20Screencapture.alfredworkflow)

用法一样，都是先召唤动作出来（Automator 版可以绑定快捷键或者从菜单栏启动，方法可参考 [我以前的文章](https://sspai.com/post/52151)），随后会弹出截屏选框，**选中需要提取文字的屏幕区域，即可把文字拷贝到剪贴板。**

![](.evernote-content/35EAAFF3-6A24-413B-8D0E-CD74F72817AC/A4E0E52E-8814-4578-8FEE-744C9B8C9E23.gif)

截图提取文字

整个脚本不涉及和自动化工具本身的交互（等于只是拿自动化工具给裸露的脚本套了件衣裳），所以不进行任何修改几乎就可以直接移植。我提供了 3 个版本的动作，需要自己修改或移植的读者可以在下载链接后的 GitHub 项目中获取源码。

### 安装 Tesseract

文字识别的动作用到了 Tesseract，这是一个 Google 赞助并维护的开源 OCR 引擎。默认情况下它只支持英文识别，当然也可以自己添加语言包，这点我们稍后就说。

下面涉及命令的操作都需要在终端（Terminal）中进行，复制代码到终端后回车运行即可。建议通过 HomeBrew 来管理 Tesseract 这类命令行工具，这样只需要在系统自带的终端里，用几条短命令就能实现安装、升级和卸载，不用再有其他多余工具和操作。已经有 HomeBrew 的读者可以跳过第一步。

1. 安装 HomeBrew，用于接下来安装 Tesseract：  

   ```
   /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
   ```
2. 安装 Tesseract：  

   ```
   brew install tesseract
   ```

装好 Tesseract 和我提供的动作之后，就可以进行基础的文字识别了（暂时还不能识别中文）。

![](.evernote-content/35EAAFF3-6A24-413B-8D0E-CD74F72817AC/F34EA862-B02B-40CA-A19D-29C1A8036505.gif)

默认情况下是识别英文

### 配置自定义语言包

日常使用中，中文识别必不可少。现在配置自定义语言包：

1. 为 Tesseract 设置环境变量（不然你的 Mac 认不出自己添加的语言包）：  

   ```
   export TESSDATA_PREFIX=/usr/local/Cellar/tesseract/4.0.0/share/tessdata
   ```
2. 为 Tesseract 添加中文语言包：前往官方 GitHub 仓库的中文语言包页面（[这里](https://github.com/tesseract-ocr/tessdata_best/blob/master/chi_sim.traineddata)），点击 Download 下载中文语言包 `chi_sim.traineddata`，并移到以下文件夹中（这里存放所有 Tesseract 的语言包文件）：  

   ```
   /usr/local/Cellar/tesseract/4.0.0/share/tessdata/
   ```

![](.evernote-content/35EAAFF3-6A24-413B-8D0E-CD74F72817AC/39A109AC-96BE-4370-A6D3-C107A6AD2430.png)

把语言包放到指定文件夹

需要其他语言的话，可以在 Tesseract 的 [支持列表](https://github.com/tesseract-ocr/tessdata_best) 里面找找，足有一百多种语言供选择。Tesseract 还有个比较厉害的特性，即可以自己进行机器学习训练、培养自己的语言包，让识别结果贴近自己的工作环境（尤其是一些专业性较强的科研、金融行业，日常用语往往不够用），不过这部分内容就不在本文讨论范围内了。

装好语言包后在终端里输入 `tesseract --list-langs` 检查一下，看到自己要用的语言就表示安装成功。下图中显示了 `chi_sim`，表示简体中文已经安装完毕。

![](.evernote-content/35EAAFF3-6A24-413B-8D0E-CD74F72817AC/20D708FA-9E3A-4F9F-8D3A-20971C0A9B1E.png)

检查语言包安装状况

原理解析
----

整个动作由两部分组成：先获取图片，再进行 OCR 字符识别。其中 OCR 部分比较简单，只需要一行命令就能搞定，我们先从它开始。

### OCR 命令

OCR 引擎的选择很多，有在线 API，有开源工具，也有 App 自带的套件 —— 比如 DEVONthink Pro Office 的 AABBYY 引擎。考虑泛用性，我选择了 [Tesseract](https://github.com/tesseract-ocr/tesseract) 这个开源工具。Power+ 1.0 的读者可能对 Tesseract 还有点印象，没错，@契丹神童 写过一篇《 [通过 OCRmyPDF 实现在扫描版 PDF 中检索文字](https://sspai.com/post/44045)》，其中介绍的扫描工具 OCRmyPDF 就是基于 Tesseract 的。

这回继续用 Tesseract，主要有两方面的考虑：

1. 它可以**离线**使用，即时获得结果，断网也不影响；
2. 它完全**免费**，想用多少次就用多少次（一般 API 有次数限制）。

目前 Tesseract 背后由 Google 提供支持，未来一段时间里还是可以安心使用的。

Tesseract 的安装我们已经讲过了，现在来看一下它的具体命令。进行文字识别的命令很简短，比如想把一张桌面上的图片进行处理，命令就是这样：

```
tesseract ~/Desktop/测试图片.png stdout -l chi_sim+eng
```

这段命令表示，调用 Tesseract 来处理测试图片，并把结果直接显示在命令行里面。其中 `chi_sim+eng` 意味着使用了中文和英文语言包，需要其他语言包的话也可以如法炮制，用加号 `+` 把几个包串在一起使用。

当然，也要承认 Tesseract 的准确度 —— 特别是中文方面 —— 不如商用 API，不过平时需要提取小段文字的频率更高，Tesseract 基本够用，实在有大段文本提取需求的读者，可以参考我以前写的《[OCR 识别文字](https://sspai.com/article/42643?series_id=9)》（Power+ 1.0），里面有百度 OCR API 的使用介绍。

### 获取图片

就获取屏幕上任意区域的内容来说，截图仍然是最简单的方法之一。配合 macOS 下的截图命令 `screencapture`，我们几乎在任何界面下都可以进行文字提取。

和 Tesseract 一样，`screencapture` 也是命令行里执行的，它们可以直接写在同一份脚本文件里面。来看一下组合好后的整段脚本（Shell 脚本）：

1. 绿色部分：指定路径，因为 Tesseract 是第三方工具，所以要指名道姓才能把它叫唤出来。
2. 蓝色部分：截图保存到本地，稍后会自动删除。
3. 粉色部分：调用 Tesseract 进行文字识别，并把识别结果拷贝到剪贴板。
4. 橙色部分：删除刚才生成的截图文件。

![](.evernote-content/35EAAFF3-6A24-413B-8D0E-CD74F72817AC/C6667256-6881-4DCA-A927-D415C503AEEF.png)

代码分解

把这段脚本放到 Automator、LaunchBar、Alfred 等等自动化工具里面，就能做到随时随地提取屏幕上的字符。

考虑通常的使用习惯，第 3 步默认同时使用英文和中文语言包，有其他语言需求的可以参照上一节方法进行修改。OCR 处理之后的 `pbcopy` 小命令很实用，可以直接把结果拷贝到剪贴板。

知识点一：Shell 脚本中的环境变量

喜欢折腾命令行的读者可能经常发现，分明在终端 Terminal 中运行无碍的命令，写成脚本放进自动化工具里就会报错。很大的可能性在于，没有指定环境变量，更具体点说，就是没指定门牌号 —— 具体用哪个 Shell。

所谓 Shell 就是一层壳儿，可以理解为一个交互界面，我们通过它给 macOS 系统下命令。由于历史原因，Mac 里留了各种各样的 Shell，上面命令第一行的 `bin` 也是其中之一，macOS 默认的则是 `bash`。各个 Shell 功能和语法都有不同，而想调用第三方命令行工具（比如各种 HomeBrew 安装的）的话，就要指定使用 `bin`。

像 `PATH=$PATH:/usr/local/bin/;` 这种使用率非常高的环境变量，建议放进剪贴板管理工具里面，写脚本时可以随时调出来粘上。

![](.evernote-content/35EAAFF3-6A24-413B-8D0E-CD74F72817AC/17A886D9-DD9F-4C8A-AAEF-DE97058D4BF1.png)

把常用环境变量收藏进剪贴板管理工具

知识点二：macOS 的拷贝命令

不少命令行工具功能都很强大，不过它们一般都会把结果呈现在命令行里，手动复制出来显然不方便。macOS 提供了一个很好用的 `pbcopy` 命令，配上管道符号 `|` 加在任何命令后面，就能把命令结果拷贝到剪贴板了。至于所谓管道符号，简单说就是把一个命令的结果交给另一条命令。「管道」这个名字很贴切。

这套截屏、处理、最后清理截图文件的方法，我在《[在 Mac 上随时随地以图搜图](https://sspai.com/article/52742?series_id=70)》一文中也尝试过，当时是为了搜索图片，这回则是进行文字识别，但利用临时文件作为中转站这一点是相通的。为了在不打扰用户的情况下删掉临图片，我用了 `rm` 命令 —— 还是那句话，这条命令平时不要随意使用，它会彻底清掉一个文件。

制作这套动作时，我也想过做一个处理整幅图片的版本，后来发现还是截图操作比较方便，偶尔遇到一个不想手打的长单词、看见一个拗口的老外名字，随手截下来就能获得本文，这样的操作更符合直觉。

小结
--

这套小巧的 OCR 动作就到此为止。以前觉得 OCR 很神奇，用得多了，慢慢感觉到它已经成为一种**基础性的功能**，在很多工作流里都可以充当一个零件。

少数派已经有不少作者把 OCR 融入了自己的工作流。@契丹神童 写过 [处理 PDF](https://sspai.com/post/44045)、@涔 E 写过  [扫描图片](https://sspai.com/post/43845)，我自己也给 Automator 做过  [OCR 动作](https://sspai.com/article/52237?series_id=70)。或许是为了可拓展性，我们不约而同都选择了 Tesseract。这回我再次介绍了这个诸多自动化动作的背后功臣，希望给愿意自己动手的读者更多启发。

---

[🌐 原始链接](https://sspai.com/post/53321)

[📎 在印象笔记中打开](evernote:///view/207087/s1/1752bde4-6941-4edb-8209-72c8b09d11bd/1752bde4-6941-4edb-8209-72c8b09d11bd/)