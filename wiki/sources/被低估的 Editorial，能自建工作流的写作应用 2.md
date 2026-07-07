---
title: 被低估的 Editorial，能自建工作流的写作应用 2
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/被低估的 Editorial，能自建工作流的写作应用 2.md
tags: [evernote, impression, yinxiang]
---

# 被低估的 Editorial，能自建工作流的写作应用

---

当今 iOS 端 Markdown 写作软件基本由 Ulysses、Bear、Drafts 等明星软件把持，有的功能纯粹，有的界面优雅，但要说到功能强大、扩展强就要数今天的主角 Editorial 了，这是一款被严重低估的软件。当深度使用过后，不禁感叹，这货真是一款写作软件么？

Editorial 的中文意思是「编辑、社论」，通用于 iPhone 与 iPad，iPad 屏幕大，体验更佳。开发者是个德国人，当前优惠期间 30 元。

Editorial 的主要功能与 Ulysses、Bear、Drafts 没什么不同，主打 Markdown 语法写作。它其貌不扬，但杀气十足——支持深度自定义文档处理工作流，Drafts 也支持工作流，但 Drafts 工作流支持的 JavaScript 语言太局限。Editorial 的工作流与 Workflow for iOS 软件类似，将各种 Action（动作）串联起来，特快直达，让我们处理文档更得心应手。

![](.evernote-content/2A7845FC-5A03-458C-A3D6-14E3E6E1FC01/2483F1CD-6950-414D-AAC9-E4E9611D430D.jpg)基础界面：1. 本地文件夹；2. Dropbox 同步文件夹；3. 最近文件列表；4. 新建文档；5. 最近文件列表清理与立即同步；6. 软件设置

写作模式
----

Editorial 支持三种写作模式，Markdown、Plain Text（纯文本）、TaskPaper（任务清单）。后两种我基本没用过，使用更多的是 Markdown 模式。

相信少数派的读者基本都是老司机了，Markdown 语法就不详细科普。

简单的来说，Markdown 是一种简单易掌握的纯文本标记语言，经过解释器解释后生成漂亮的排版。

文章大纲
----

当我们准备写一篇文章前，为了文章结构清晰通常会先构思大纲，然后围绕各级大纲丰满文字。

Editorial 支持以各级标题为大纲的导航及折叠。写作界面点击屏幕上中位置的文档名称可以预览当前文章大纲结构，点击大纲可以直接跳转到该大纲段落。

![](.evernote-content/2A7845FC-5A03-458C-A3D6-14E3E6E1FC01/34D95752-923A-4E6F-B178-9DE54FA1CFF9.jpg)大纲界面

当你在写作时，可以很方便的把上文折叠，保持屏幕清明，专心写作，折叠后会在标题后显示该段单词统计。当有段落折叠时，点击左上角小三角可以快速全部展开。**单词计数功能对于中文然并卵，字符计数更实用。**

如果你在设置中启用了 **Arrange Paragraphs**，还可以使用段落编排，你可以按住任何一级大纲右侧的操作柄随心所欲拖拽移动该级大纲下所有字符到任何位置，你也可以拖拽移动任何一个段落到其它位置或其它大纲下。

![](.evernote-content/2A7845FC-5A03-458C-A3D6-14E3E6E1FC01/AAF5D776-F273-47B8-90D4-7F7DD6ACA6BF.jpg)段落编排

快捷键盘
----

Editorial 有 Markdown 语法常用标记符号的快捷键盘，输入状态会自动弹出，长按快捷键会提供更多同类型的标记符号以供选择，快捷键盘上左右滑动可以快速移动光标。

![](.evernote-content/2A7845FC-5A03-458C-A3D6-14E3E6E1FC01/2F6F70F6-CDCF-4C3D-BD5A-AC1EE9B79285.jpg)快捷键盘

点击快捷键盘最右边 ⚡ 符号快捷键可弹出片段插入，片段插入支持变量，软件已预置常见变量，年、月、日、小时、分、秒、当前文档名称、扩展名、语法模式等，并且可以自定义缩写命令。比如插入当前系统剪贴板内容，你可以直接在编辑区域输入 `ppp` 快捷插入，如果你输入的缩写有对应变量时左下角会提示，插入后缩写字符会自动清除。

![](.evernote-content/2A7845FC-5A03-458C-A3D6-14E3E6E1FC01/E11ECC42-948B-47D2-B149-4BFBEAA2597F.jpg)插入变量

你也可以自定义你常用的一个词语或一段句子快捷插入，对于经常需要重复输入某些内容非常有帮助，也可以选择变量 + 自定义文本的组合。

文章预览与发布
-------

文章预览功能中规中矩，唯一的亮点是 Editorial 的预览方便、很方便、非常方便，编辑界面左滑屏幕直接预览，右滑返回编辑界面。对于软件的某项功能，不需要高大上的黑科技，不需要绚丽的动画，只要能直击痛点就是完美。

Editorial 同样支持自定义预览模板，然并卵，仅本地预览有效，除非你能修改你文章发布点的渲染模板。

Editorial 预置同步服务仅支持 Dropbox，没毛病，我并不觉得国内使用难得住中国人。Dropbox 同步可以自定义同步文件夹路径，当你的文档有修改时软件会自动同步到云端。

如 Dropbox 不能满足你，需要发布到自定义的云储存或博客服务，比如 WordPress 等，接下来要讲的工作流功能可以满足你的一切需求。

工作流
---

苹果系工作流概念是老古董了，macOS 的 Automator 已发展多年依然不温不火，一直掌握在少数人手里，真正使苹果系工作流普及大众的是近两年大 🔥 的 Workflow for iOS。

Editorial 的工作流与其类似，当你看过他的 Action 后会发现与 Workflow for iOS 惊人的相似，没有谁抄袭谁，记忆中 Editorial 发布得更早，我臆断都有参考 Automator。

![](.evernote-content/2A7845FC-5A03-458C-A3D6-14E3E6E1FC01/1D2DE17B-BC6C-4607-90F5-4D659FD62D2E.jpg)工作流列表

在编辑界面点击右上角 🔧 按钮显示本地已有工作流，单击工作流直接运行，工作流同样支持自定义缩写命令，文档中输入缩写命令可直接运行。

![](.evernote-content/2A7845FC-5A03-458C-A3D6-14E3E6E1FC01/65F26408-6FA8-4F9B-A05D-239FEAB889C2.jpg)Action库

Editorial 预置有 65 个各种功能的 Action，能满足绝大部分使用场景。由于 65 个 Action 截图拼合后太大，所以这里放出 **[Action 库大图链接](http://ooaiyqbvu.bkt.clouddn.com/1495730512_action_lib_all.jpg "Action 库大图链接")**，有兴趣的可以看看。

### Editorial 的 Action 长什么样

为了让大家对 Editorial 的工作流有更直观的认知，在大家都熟悉的 Workflow for iOS 内选取几个使用频率较高且两者共有的 Action 进行简单的对比。

#### 定义变量

![](.evernote-content/2A7845FC-5A03-458C-A3D6-14E3E6E1FC01/FAAF3C58-8076-4067-BC32-B9884635E7AC.jpg)定义变量：1. Workflow for iOS 定义变量；2. Editorial 定义变量；3. Editorial Action 设置界面；4. Editorial 自定义样式 Action

两者区别在于 Editorial 的定义变量支持直接定义文本为变量，不像 Workflow for iOS 需要先在文本 Action 里输入文本然后再接定义变量。

另外 Editorial 的所有 Action 都支持自定义颜色及标题，并且可以将设置好数据及样式的 Action 保存，方便其它工作流调用。

#### 循环块

![](.evernote-content/2A7845FC-5A03-458C-A3D6-14E3E6E1FC01/3B20E12A-6FB2-4158-89B3-21DD5ABF9FE3.jpg)循环块

上图可以看出，Editorial 的预置循环块主要偏向于文本处理，可以直接使用正则表达式匹配循环源或设置反向循环。

#### 选择菜单

![](.evernote-content/2A7845FC-5A03-458C-A3D6-14E3E6E1FC01/44E08CC2-71F1-4487-94F7-800E1C6157A1.jpg)选择菜单

大同小异，两者都支持单选和多选，在多选时 Workflow for iOS 则支持默认全选状态，Editorial 则支持搜索。

#### 条件判断

![](.evernote-content/2A7845FC-5A03-458C-A3D6-14E3E6E1FC01/D98FB8B4-5F8D-4164-A64C-AB34328D0EB7.jpg)条件判断块

两者判断条件略有不同，Workflow for iOS 有大于小于，Editorial 有正则表达式匹配。

#### 正则表达式

![](.evernote-content/2A7845FC-5A03-458C-A3D6-14E3E6E1FC01/49A5AD2A-AB85-4AF7-BC9F-B09B114C6E0D.jpg)正则表达式

两者正则表达式块基本相同，Editorial 则有更细致的设置。

看完上面的简单对比，应该对 Editorial 的工作流有个基本的认识，总体上来说 Editorial 的内置 Action 偏向于文本处理，Workflow for iOS 的内置 Action 则更全面，但两者在自动化的实现原理是一样的。

### 大杀器

「Run Python Script」和「Custon Action」是 Editorial 的两个预置 Action，是 Editorial 工作流的大杀器，有了它们的武装使得 Editorial 一切可及。

#### Run Python Script

运行 Python 脚本。关于 Python 语言，有编程基础的基本都会，没有编程基础的基本都听说过。

引用维基百科内容：

> Python（英国发音：/ˈpaɪθən/ 美国发音：/ˈpaɪθɑːn/），是一种面向对象、直译式的电脑程序语言。它包含了一组功能完备的标准库，能够轻松完成很多常见的任务。它的语法简单，与其它大多数程序设计语言使用大括号不一样，它使用缩进来定义语句块。
>
> Python 的设计哲学是「优雅」、「明确」、「简单」。Python 开发者的哲学是「用一种方法，最好是只有一种方法来做一件事」，也因此它和拥有明显个人风格的其他语言很不一样。在设计 Python 语言时，如果面临多种选择，Python 开发者一般会拒绝花俏的语法，而选择明确没有或者很少有歧义的语法。这些准则被称为「Python 格言」。在Python解释器内运行 import this 可以获得完整的列表。

引用大牛 Bruce Eckel 的话：

> 原文：Life is short, you need Python。
>
> 译文：人生苦短，我用 Python。

引用我的胡言乱语：

> 作为新时代的男人，至少要会一种随便什么乐器，至少要会一门随便什么编程语言。

人生苦短，所以乐器我选择**口哨**，编程语言我选择 **Python**。

零编程基础，我花了一星期入门，一个月后还是入门，我想永远是入门了。我不去想高大上的机器学习、大数据，我要的仅仅是能给我带来方便，比如写个小爬虫爬下小姐姐们的图片视频什么的也是极美的。

Editorial 内置的为 Python 2.7，预置全部标准库及部分流行第三方库，比如 BS4 爬虫、PIL 等。

为了与 iOS 更好的联动，开发者还开发了 iOS 专门库，可以操作系统剪贴板、联系人、定位、通知、相册等。

![](.evernote-content/2A7845FC-5A03-458C-A3D6-14E3E6E1FC01/D3F9FAF7-C6BA-4CC3-B6DE-99AD6B62ADF2.jpg)预置库

遗憾的是并不支持导入第三方库，没毛病，够用了，至少我目前还没遇到因缺库而无法实现我要的功能，毕竟他是写作软件。有此需求的可以移步开发者另一作品 **Pythonista**（iOS 上最棒的 Python IDE 软件）。

有意思的是，Editorial 还预置有 UI 模块，支持函数方法调用及图形可视化编辑生成，如果你喜欢折腾可以为你的程序制作出漂亮的操作界面。

![](.evernote-content/2A7845FC-5A03-458C-A3D6-14E3E6E1FC01/CA61AF77-2432-4CBB-8F46-58B671847731.jpg)UI 模块

说了那么多，有人要问，有了 Python 能干什么？我都吹成这样了！你想干什么就干什么。

#### Custom Action

熟悉 Workflow for iOS 的都知道，90%的使用场景我们都要用到 Get Contents of URL 这个 Action，Editorial 是没有预置该 Action 的，用 Python 代码很容易实现，嫌麻烦每次要敲那几行代码怎么办？有了 Custom Action 我们可以自己做一个。

我们先来看看 Workflow for iOS 的 Get Contents of URL 与 Editorial 的 Custom Action 都是什么样子，然后照葫芦画瓢。

![](.evernote-content/2A7845FC-5A03-458C-A3D6-14E3E6E1FC01/7A7E10BE-DED8-4913-9B2C-5B5A952C30EA.jpg)Get Contents of URL

Editorial 的 Custom Action 的设置界面有标题、描述、窗体颜色、预置参数项编辑、Python 脚本编辑、保存为预置选项。

要制作一个 Action 的核心是参数项编辑与脚本编辑，分两步进行。

* Step 1：设置参数项

![](.evernote-content/2A7845FC-5A03-458C-A3D6-14E3E6E1FC01/D9544D3E-81E6-4B12-8011-B2139BCCFF03.jpg)自定义 Action 参数设置

长按 Custom Action 窗体打开设置界面进入参数编辑界面。参数项支持添加 6 种类型（如图），先单击左侧 - 号删除默认的 Info，然后单击右上角 + 号添加参数项。

![](.evernote-content/2A7845FC-5A03-458C-A3D6-14E3E6E1FC01/E9B1A82E-D80D-461D-AB00-A53DF5E9BBDA.jpg)添加参数

有时请求头及请求主体的参数有多项，所以参数输入框选择多行文本框便于添加多项请求参数。对于多种请求方法的选择采用选择菜单来完成，菜单选项的内容也要添加多项，每行为一项，添加完后保存。

* Step 2：添加脚本

![](.evernote-content/2A7845FC-5A03-458C-A3D6-14E3E6E1FC01/CE6224C1-2EEF-432B-B74B-C16C50D1F49F.jpg)脚本编辑  
回到 Action 设置进入脚本编辑界面，并添加下列伪代码。

```
    #coding: utf-8
    import workflow, requests, dialogs

    def parameter(get_value):
            pars = {}
            par = get_value.split('
')
            for x in par:
                    x = x.split(':')
                    key = x[0]
                    value = x[1]
                    pars[key] = value
            return pars

    def file():
            pars = {}
            x = get_set['File'].encode('utf8')
            x = x.split(':')
            key = x[0]
            value = vars()[x[1]]
            pars[key] = value
            return pars

    get_set = workflow.get_parameters()

    if not get_set['URL']:
            dialogs.hud_alert('未指定网址','error',1)
            exit()
    else:
            url = get_set['URL'].encode('utf8')

    method_select = str(get_set['Method'])
    method_list = {'0':'get','1':'post','2':'put','3':'patch','4':'delete'}
    method = method_list[method_select]

    if not get_set['Headers']:
            headers = None
    else:
            headers = parameter(get_set['Headers'].encode('utf8'))

    if not get_set['JSON&Form']:
            data = None
    else:
            data = parameter(get_set['JSON&Form'].encode('utf8'))

    if not get_set['File']:
            files = None
    else:
            files = file()

    res = requests.request(method,url,headers=headers,data=data,files=files)
    workflow.set_output(res.content)
```

添加完成后关闭脚本编辑界面会自动保存脚本，最后在 Action 设置界面单击保存为预置。

至此，一个简单的 Get Contents of URL 就完成了。

![](.evernote-content/2A7845FC-5A03-458C-A3D6-14E3E6E1FC01/05867624-B179-4BAE-8693-33557B83DCF9.jpg)Editorial Get Contents of URL

上图为成品，为了演示功能，我另外添加了一个开关，这个开关可以根据个人需求自定义功能。

在 Workflow for iOS 上制作有多项功能的工作流时会有一个痛点，就是功能的切换，一般会用两种办法解决，添加选择菜单或文本框输入选择然后判断，很 low 不是吗，如果有一个自定义开关多好，Editorial 很好解决了这个痛点。

下面我们来测试一下这个自制 Action 的功能。为了方便显示结果，在 Get Contents of URL 下面接一个 Console Output，该 Action 可以在 Python 控制台显示上一步输出结果。

先来试试 GET 方式请求百度，在 URL 框输入百度网址，单击右上角三角按钮运行。

![](.evernote-content/2A7845FC-5A03-458C-A3D6-14E3E6E1FC01/D3B75C49-F75C-488D-9FF2-D18132C2EB2F.jpg)GET 请求测试

可以从上图看到请求成功，并返回百度首页的 HTML 源码。

再试试 POST 方式带参数请求，这里调用一个专用测试网络请求的 API（`http://httpbin.org/post`）来测试，该 API 会将接收到的请求数据以 JSON 返回。如有多组参数时，每行为一组参数，参数的 `Key` 与 `Value` 用半角冒号 `:` 连接（可根据个人喜好自定义）。

![](.evernote-content/2A7845FC-5A03-458C-A3D6-14E3E6E1FC01/85798696-FE7B-4DD7-8EF0-E69DC04B157F.jpg)POST 请求测试

上图可以看出请求成功，填入参数正确返回，`origin` 那里显示的是发起请求的 IP。

经过测试，功能基本满足要求，这个 Action 仅为演示功能，如需要功能完全，还需进一步完善，比如加入返回数据类型判断及处理。

### 工作流实例

在写博客时，往往需要配图使你的博文更生动，手动操作步骤如下：打开手机相册 - 选择图片 - 上传到图床 - 获取图片外链 - 输入 Markdown 插入图片语法文字 - 粘贴图片外链地址。当使用工作流后，你仅需选择图片这一步，其他工作都交由工作流自动完成，优雅而高效。

我在给别人介绍 Editorial 工作流时总是喜欢以**七牛图床**为例，因为这是我学习 Python 的初动力，也是我人生的第一个 Python 程序，程序简单，但直击痛点。

![](.evernote-content/2A7845FC-5A03-458C-A3D6-14E3E6E1FC01/A450C270-8DE3-4AFA-8D86-CC4CDEB71D83.jpg)七牛图床

七牛图床工作流由 2 个 Action 组成，一个 Custom Action，一个是 Run Python Script，其中任一个 Action 单独都可以实现图床功能，但为了清晰易读所以分解为两步。

该工作流上传后文件名默认设置为上传时的时间戳，时间戳为全数字，不便于识别管理，所以加入一个**自定义文件名后缀**的开关，如果打开，上传到服务器后的文件名为 `时间戳_自定义后缀.jpg`。

上传成功后默认处理为在当前文档的光标处以 Markdown 语法插入图片外链地址，如果打开**复制图片外链至系统剪贴板**开关后，上传成功后会同时将图片外链添加到系统剪贴板。

（注册七牛免费空间：[七牛官网](https://www.qiniu.com "七牛官网")）

#### 为什么选择七牛？

首先七牛算是国内老牌云服务商了，开放易用。七牛提供 API 接口全，所有操作都可由 API 完成，七牛有图片云处理，比如图片瘦身、自动添加水印、防盗链、自定义缩放、裁剪等，简单自用，非常适合做图床。

比如我们引用图片外链是 `http://domain.bkt.clouddn.com/filename.jpg`，当设置图片处理样式后，只需要在后面添加 `?imageMogr2/thumbnail/!50p/blur/1x0/quality/100` 引用的图片就会自动等比缩放 50%。

还可以直接修改参数改变引用样式，比如改为 `http://domain.bkt.clouddn.com/filename.jpg?imageMogr2/thumbnail/!80p/blur/1x0/quality/100` 就是自动等比缩放 80%。

七牛免费配额如下图，作为个人图床完全够用。

![](.evernote-content/2A7845FC-5A03-458C-A3D6-14E3E6E1FC01/77DBA3AF-6FBD-4C7E-B208-92AA23D1942F.png)七牛免费配额

#### 设置七牛参数

注册七牛后首次使用需在对象存储里创建空间，可以创建多个空间。

需记下创建空间时定义的空间名称、选择的存储区域、创建完空间系统分配的空间测试域名、个人面板密匙管理中的 AK 密匙与 SK 密匙这 5 项，然后将这5项设置数据分别输入工作流的设置面板就可以运行了。

#### 运行演示

![](.evernote-content/2A7845FC-5A03-458C-A3D6-14E3E6E1FC01/E67E3E45-5E33-4496-8610-6E3FE64D0C89.gif)运行动图

七牛服务器速度不错，基本秒传。（**[七牛图床下载](http://www.editorial-workflows.com/workflow/5772888024023040/zY0qH69fsfA "七牛图床下载")**）

### Workflow Directory

[Workflow Directory](http://www.editorial-workflows.com/ "Workflow Directory") 是 Editorial 官方的工作流分享站点，用户可以分享自己的或下载他人的工作流。如果是你自己发布的工作流，在工作流内容更新后可以直接更新推送到云端，无需重新生成共享地址，这点很棒，不像 Workflow for iOS 更新需重新上传后生成新地址共享给别人。

![](.evernote-content/2A7845FC-5A03-458C-A3D6-14E3E6E1FC01/25FF6997-7FCA-455E-9CC6-380F727341E5.jpg)Workflow Directory

![](.evernote-content/2A7845FC-5A03-458C-A3D6-14E3E6E1FC01/DFB42843-2F39-43F1-873E-D2E2FFD0B562.jpg)下载Workflow

可以直接在 Editorial 程序内置浏览器或 Safari 打开别人分享的工作流地址，或在分享站点直接搜索到你想要的工作流，进入工作流页面点「Install Workflow」后会有警告提示，再点击「I understand，install the workflow！」就可以直接安装到本地。

URL Scheme
----------

作为一个 iOS 系的效率软件，支持 URL Scheme 是基础。Editorial 支持完整的 URL Scheme 方案，可传递参数运行工作流，并支持 x-callback-url 标准，可以与其他软件进行联动，比如Workflow for iOS 就内置调用 Editorial 工作流的 Action。

```
    editorial://<action>/<filename>?root=<dropbox|local>&selection=<from-to>&command=<command name>&input=<command input>

    editorial://?command=MyCommand

    editorial://back

    editorial-http://

    editorial-https://
```

结束语
---

全文用 Editorial 编写完成。

我曾私信开发者问，Editorial 本身作为一款写作软件工作流就已经这么强大了，为何不加以优化生成另外一款工作流效率软件，肯定会大杀四方，但开发者回信说「从没有想过」。

Workflow for iOS 一度火热，几近成为业界标杆，被苹果收购后基本处于停更状态，官方申明以后不会添加新功能，目前仍然有部分 Bug 未修复，当运行较复杂的工作流时显得力不从心，但仍不失为一款非常棒的软件。

同样的应用场景下，Editorial 不失为另一种选择，在 Workflow for iOS 现有功能无法满足需求时，我会用 Editorial 的工作流来替代，也可以选择两者互补使用。

---

[🌐 原始链接](https://sspai.com/post/39411)

[📎 在印象笔记中打开](evernote:///view/207087/s1/3031640c-580d-43b7-a3bc-6f0b85fdef0b/3031640c-580d-43b7-a3bc-6f0b85fdef0b/)
