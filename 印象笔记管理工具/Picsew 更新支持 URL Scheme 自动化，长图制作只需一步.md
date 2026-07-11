# Picsew 更新支持 URL Scheme 自动化，长图制作只需一步

---

[Picsew](https://itunes.apple.com/app/id1208145167?at=1001lsTF&ct=iOS_extension_share_1208145167&uo=4&at=10lJSw) 作为 iOS 上一款长截图制作与截图拼接软件，凭借其强大的功能以及低廉的价格获得了许多用户的青睐，在最近几个月更新加入「长截图插件」功能后，在最的近一次 2.71 更新中又加入了对 URL Scheme 的支持，通过对 X-Callback-URL 的应用，用户可以更加方便的对截图或图片进行拼接操作。

**拓展阅读：**[URL Schemes 使用详解](https://sspai.com/post/31500)

简化操作，从未止步
---------

对于一般长截图拼接应用来说，一张长截图的制作包括以下几个步骤：

* 对相应界面截图
* 打开拼图 App
* 选取刚刚的截图进行拼接
* 保存/分享对应长截图
* 删除原截图

虽然现在大多数长截图拼接应用都已经自带了「截图拼接完成后删除来源图片」的功能，但长截图的制作仍然需要打开应用并手动选取所选图片这几项操作。对于经常制作长截图的用户来说，这样的操作仍然比较繁琐繁琐。在最近几个月的更新中，Picsew 陆续加入了「[网页快照](https://sugarmo.github.io/picsew-help/zh-Hans/guide-web-snapshot)」和「[长截图插件](https://sugarmo.github.io/picsew-help/zh-Hans/guide-create-scrollshot)」两项功能，使得用户可以直接在 Safari浏览器浏览网页时制作网页长截图或直接在相册中直接选取截图进行拼接。而本次更新中对 URL Scheme 的加入，更是实现了对长图制作步骤简化的质的飞跃。

结合 Workflow 拼图操作
----------------

首先我们来看一下结合 Workflow，Picsew 可以实现怎样的自动拼图操作。在 Picsew 的 [x-callback-url](https://sugarmo.github.io/picsew-help/zh-Hans/x-callback-url) 文档中，已经自带了三个最常用的长截图制作工作流，我也根据我常用的操作制作了自己的拼图工作流。你也可以根据自己的习惯，结合 workflow, Launcher Center Pro 或其它支持 URL Scheme 的应用定制自己的拼图动作。

* [**制作长截图**](https://workflow.is/workflows/e9b64bc79d854bb0a9f9531d6cab5bdd)：这个工作流会让你选择最新截图的数量，调起 Picsew 来自动拼接，保存图片到相册，然回到 Workflow，查看结果，删除来源图片。

![](.evernote-content/CFEA82EE-F217-48F8-8739-7E4FAF1F02E6/256EE2AE-1AC9-4FE5-BC63-23749FB43376.gif)制作长截图

* [**最近长截图**](https://workflow.is/workflows/b3084df208c34b74877471bddad84576)：这个工作流会自动检测最近的截图，调起 Picsew 来自动拼接，并且根据你的选择加上设备外壳或者清理状态栏，保存图片到相册，删除来源图片，然回到 Workflow，查看结果。

![](.evernote-content/CFEA82EE-F217-48F8-8739-7E4FAF1F02E6/469E977D-B5FA-4FE2-AE51-872F6A7D5BC0.gif)最近长截图

* [**创建长截图**](https://workflow.is/workflows/a9c746a2306e400c914d274b5d0998bd)：这个工作流会根据你选择的截图，调起 Picsew 来自动拼接，并且根据你的选择加上设备外壳或者清理状态栏，保存图片到相册，然回到 Workflow，查看结果，删除来源图片。

![](.evernote-content/CFEA82EE-F217-48F8-8739-7E4FAF1F02E6/254219ED-40ED-4404-A5A4-19936D44BAAD.gif)创建长截图

* [**图片拼接**](https://workflow.is/workflows/b5aec761d90546b5857d684990140762)：这个工作流会让你选择需要拼接的图片，进行横向或纵向的图片拼接，保存图片到相册，回到Workflow，查看结果，并根据你的选择来决定是否删除来源图片。

![](.evernote-content/CFEA82EE-F217-48F8-8739-7E4FAF1F02E6/86350452-3114-4329-A671-56A809DF1A8F.gif)图片拼接

URL Scheme 指令
-------------

在 Picsew 的设置中，可以看到关于 URL Scheme 的相关帮助。基础方面，通过 `picsew://` 和 `picsew://recent` 可以直接打开或查看最近的截图，在 Picsew 的 [x-callback-url 文档](https://sugarmo.github.io/picsew-help/zh-Hans/x-callback-url)中，可以进一步看到详细的对 x-callback-url 的支持格式：

```
picsew://x-callback-url/[动作]?[动作参数]&[x-callback 参数]
```

功能方面，Picsew 拥有的三种拼图操作：截图拼接、图片竖向拼接以及图片横向拼接都可以通过 URL Scheme 来实现，对应的动作分别为：`/scroll`、`/vert` 和 `/hori`，除了三种不同动作的基础参数外，Picsew 还为其配备了水印、加壳、清理状态栏以及是否删除来源图片四项自定义可选操作。用户可以通过自己的习惯来定制属于自己的 URL Schemes。

![](.evernote-content/CFEA82EE-F217-48F8-8739-7E4FAF1F02E6/1D85694A-BEFA-477F-8F9A-1F674D29315A.png)URL Scheme 参数

例如，使用最近的长截图进行拼接，自动清理状态栏，加上白色设备外壳，把结果保存到设备相册并删除来源图片的 URL Schemes 为：

```
picsew://x-callback-url/scroll?in=recent&out=save&clean_status=yes&mockup=white&delete_source=yes
```

长截图制作、图片拼接、打码标注、水印添加……Picsew 完善的功能令长图的制作越来越简单，通过本次更新对 URL Scheme 的支持，拼图的操作进一步简化，使得 [Picsew](https://itunes.apple.com/app/id1208145167?at=1001lsTF&ct=iOS_extension_share_1208145167&uo=4&at=10lJSw) 在同类型软件中更加突出。如果你也厌烦了繁琐的拼图操作，一定不要错过这款长图制作软件。

> 下载 [少数派 iOS 客户端](http://sspai.com/s/nqQk)、关注 [少数派公众号](http://sspai.com/s/KEPQ)，了解更多有趣的应用 📱

---

[🌐 原始链接](http://sspai.com/post/43761)

[📎 在印象笔记中打开](evernote:///view/207087/s1/fb938c4c-c0d5-4d33-8fe1-6d9947b8040f/fb938c4c-c0d5-4d33-8fe1-6d9947b8040f/)