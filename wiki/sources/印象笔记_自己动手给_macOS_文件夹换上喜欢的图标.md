---
title: "自己动手给 macOS 文件夹换上喜欢的图标"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/自己动手给 macOS 文件夹换上喜欢的图标.md
tags: [印象笔记]
---

# 自己动手给 macOS 文件夹换上喜欢的图标

# 自己动手给 macOS 文件夹换上喜欢的图标 --- 受到 FolderMarker Emoji 这款 App 的启发，我开始尝试用 Emoji 为 macOS 文件夹提供更为直观的视觉指引方案。

---

# 自己动手给 macOS 文件夹换上喜欢的图标

---

受到 FolderMarker Emoji 这款 App 的启发，我开始尝试用 Emoji 为 macOS 文件夹提供更为直观的视觉指引方案。然而遗憾的是 FolderMarker Emoji 的效果并不符合我的审美，显而易见的问题是，Emoji 与蓝色文件夹之间的比例总是让人感觉与原生的效果有差异，简单而言就是太大了，使得整体观感很突兀。

![](.evernote-content/242DD13E-87B3-45B4-8B00-B1D9FAD8115C/F7B7E7CA-CAB4-4558-BFC3-657096E35A87.png)真的很大 ![](.evernote-content/242DD13E-87B3-45B4-8B00-B1D9FAD8115C/E9749DDE-3860-4AEC-8957-220DC0AC7854.png)系统自带图案的文件夹就优雅很多

于是，我尝试自己动手，自定义文件夹图标，使其在视觉上更符合系统文件夹。

---

用 Emoji 标记文件夹图标
---------------

需要用到的工具有：

* Adobe Photoshop 或 Affinity Photos、Pixelmator 等图片编辑 App
* macOS「预览」App

首先，需要找到合适的 Emoji 素材，[emojipedia](https://emojipedia.org) 这个网站是 Emoji 届的维基百科，上面可以找到 Apple、Google、Microsoft 等各个平台的 Emoji。找到自己需要的 Emoji，点击进入详情页，以 Apple 为例，保存选中的 Emoji，这样会得到一个 160×160 的 PNG 文件，这个分辨率对于文件夹来说已经足够了。

![](.evernote-content/242DD13E-87B3-45B4-8B00-B1D9FAD8115C/DF7032DC-8115-4D5B-A451-2724558C9A45.png)全平台的 Emoji

除了 Emoji 之外，还需要准备一个空白的文件夹图标（即默认的图标），可以通过下面的方法获得：

1. 新建一个文件夹，选中后 `⌘ + I`，在详情页选中左上角的文件夹图标后 `⌘ + C` 复制；
2. 打开 预览 App，`⌘ + N` 从剪切板新建文件，得到 ICNS 文件预览；
3. 选中左栏第一个图标，将其导出为 PNG 文件，后期将其白色背景去除即得到 1024×1024 分辨率的空白文件夹图标。

![](.evernote-content/242DD13E-87B3-45B4-8B00-B1D9FAD8115C/C698D5DC-7CE3-475B-B155-70FCB99C3913.png)详情页选中左上角的文件夹图标并复制 ![](.evernote-content/242DD13E-87B3-45B4-8B00-B1D9FAD8115C/BA7E4269-7914-4D62-9BE5-60F258742437.png)选中左栏第一个图标，将其导出为 PNG 文件![](.evernote-content/242DD13E-87B3-45B4-8B00-B1D9FAD8115C/68BCDB41-1A67-4A4A-A1A9-C0A70D4234D0.png)后期将白色背景去除即得到空白文件夹图标

接下来，将 Emoji 素材和空白文件夹图标导入 Photoshop。经过实践，发现将素材的尺寸控制在 **7.76 cm × 7.76 cm** 的矩形内最为接近系统文件夹的样式，当然也可以根据自己的需要进行调整，原则是保证结果能带来原生的观感。

![](.evernote-content/242DD13E-87B3-45B4-8B00-B1D9FAD8115C/DC2D5C83-71FC-40DC-A90A-D3A9463CB26A.png)将素材尺寸控制在7.76 cm × 7.76 cm 的矩形内为佳

然后只需靠基础的 Photoshop 技能，将素材编辑好，导出为 PNG 格式的文件。最后，再次用 预览 App 打开导出的 PNG 文件，`⌘ + A` 选中全部，`⌘ + C` 复制，回到需要替换图标的文件夹打开详情页，按照上面介绍过的方法选中左上角的文件夹，`⌘ + V` 粘贴即可。

![](.evernote-content/242DD13E-87B3-45B4-8B00-B1D9FAD8115C/5DF83844-3C98-48AF-96BA-0586CE93CA5D.png)![](.evernote-content/242DD13E-87B3-45B4-8B00-B1D9FAD8115C/8687FED8-CD90-4CB3-B69F-6165E9F4C11F.png)效果对比

仿原生样式标记文件夹
----------

实际上，我们可以参考许多第三方 App 的做法，用同样的思路来模仿原生文件夹的样式，只需将 Emoji 素材换成特定的图标素材即可。

![](.evernote-content/242DD13E-87B3-45B4-8B00-B1D9FAD8115C/BB66F097-973B-4B4E-B5D6-690AF0924871.png)第三方 App

以 **GitBook** 文件夹为例，首先从 Google Image 或者其他图标资源库（推荐 [Iconfont](http://www.iconfont.cn/home/index?spm=a313x.7781069.1998910419.2)）找到 GitBook 的图标，将其直接和空白文件夹素材一起导入 Photoshop。通过图层样式，添加**内阴影**、**颜色叠加**和**渐变叠加**，具体参数可以根据情况进行调整，目的是使得最终效果与原生基本一致。

![](.evernote-content/242DD13E-87B3-45B4-8B00-B1D9FAD8115C/D5FA9C4C-DC41-4956-BBE4-DB9C70112C15.png)通过图层样式对素材进行调整![](.evernote-content/242DD13E-87B3-45B4-8B00-B1D9FAD8115C/6A415D41-0980-425B-9059-DC9817BDF60B.png)最终效果 ![](.evernote-content/242DD13E-87B3-45B4-8B00-B1D9FAD8115C/D197D4F8-E5BB-40B9-BEBA-92914D59F071.png)在 Finder 中的效果

结尾
--

如果想要删掉自定义的图标，同样进入详情页，选中左上角的文件夹图标后 `⌘ + X` 或 `delete` 即可。

大家估计觉得，跟 FolderMarker Emoji 比起来这种方法太麻烦了吧…然而其实我们真正需要自定义的文件夹也就是最重要的几个，普通的文件夹我并不建议用这种方法一个一个进行标记，一来是要耗费更多时间，二来 macOS 本来就是淡化文件夹的操作系统，使用 LanchBar 等工具会更有效率。

另，FolderMarker Emoji 同厂的 FolderMarker 售价 ¥30，支持用文字、图片、Emoji、图标等自定义文件夹，能迅速实现前文的效果，也是一个 NOT BAD 的选择。

![](.evernote-content/242DD13E-87B3-45B4-8B00-B1D9FAD8115C/AAB8FB71-C8D6-4654-8148-22343A4B49A6.png)给你一个五彩斑斓的文件夹

---

[🌐 原始链接](https://sspai.com/post/41380)

[📎 在印象笔记中打开](evernote:///view/207087/s1/463afff9-f1e0-407b-915e-255d7b07f7b0/463afff9-f1e0-407b-915e-255d7b07f7b0/)