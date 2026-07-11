# 告别卡顿：真正让 MacBook Pro 顺如闪电的优化

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=Mzk0MzU5NzQ4Mw==&mid=224749...](https://mp.weixin.qq.com/s?__biz=Mzk0MzU5NzQ4Mw==&mid=2247493714&idx=1&sn=8e89d2d89541d2a8153de5af8a50cbb4&chksm=c28116003d0630f8b80b9ebee6b75407b58b7536d263a71d3ab1bf738fa8c87337053abcba6c&scene=90&xtrack=1&sessionid=1757723960&subscene=93&clicktime=1757728313&enterid=1757728313&flutter_pos=12&biz_enter_id=4&ranksessionid=1757727948&jumppath=20020_1757728041947,1104_1757728059704,20020_1757728263006,1104_1757728270429&jumppathdepth=4&ascene=56&devicetype=iOS18.6.2&version=18003f28&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQj5xM0unQUliIc2wEy5XuvxLVAQIE97dBBAEAAAAAAFZWMq+DFlsAAAAOpnltbLcz9gKNyK89dVj0HhopquUroXmdQ9wR4mQy2fVVnOMV1QU2cG1b57BXPpVbRzoME23ymo/iYHTl3UaxjMvXh4/fzNFnpOVjGw+afhcNDQE0saeREaEaoVSgEO2TQ3S8HdnjrjIECuNbyxf5MWObaWANcvGhOx2INjf65QIOl6uSUJ7ddAGzjr1css03Tb2qoj6udGHjZISh+lxMuEzNwFFQuPfJu502s1/G8AjEQbyps9/iuIQJnUlTtg==&pass_ticket=Mb8tZYGgr92J443qEGB5Q75Ud9tKRyz1VFasdRTDQBTdeDM3scKTUPW+PkAR2KHc&wx_header=3)

Original 点蓝色字关注👉 程序员echo

![](.evernote-content/AF26F9AA-B94A-4AD2-AE6E-AB2C45F145A8/0F3FA308-4A97-4797-AA99-54F49E14A224.png)

我每天都在 Mac 和 Windows 之间来回切换，一台用来处理客户的工作，一台用来做自己的项目，时间长了我就发现了一个苹果不会告诉你的小秘密，那就是 macOS 出厂的默认设置更多是为了好看，看起来很顺眼，但实际上会牺牲掉不少速度，让你平时操作起来感觉慢了不少。

![](.evernote-content/AF26F9AA-B94A-4AD2-AE6E-AB2C45F145A8/7218C67C-3AD6-49EE-9C32-B224B8C9799A.jpg)

对此。我简单整理了一份设置清单，把那些苹果不希望你随便去关掉的功能扒出来，同时告诉你关掉它们之后，你的学习、工作效率能立刻提升一大截。

设置一：关闭窗口动画（你从未意识到的 400 毫秒）
--------------------------

路径：**系统设置 > 辅助功能 > 显示 > 开启“减少动态效果”**

这个简单的操作就能为每次窗口切换节省约 400 毫秒。如果你每小时切换 30 次窗口，等于节省 12 秒。看似微不足道，但累积起来，就是一段“时间的魔法”。

我是在做屏幕录制时发现的。客户的 Mac 同型号、同配置，却感觉比我的快——区别就在于他很久以前为了辅助功能关闭了动画。

苹果的动画确实赏心悦目，但在真正的工作中，它们更像“隐形刹车”。每一次 Mission Control 切换、全屏切换、最小化动画，都在悄悄消耗你的效率。

关闭动画后，你会立即感受到变化：

* 桌面空间切换瞬间完成，不再滑动慢吞吞
* 应用打开不再有缩放特效
* Dock 图标不再无休止地跳动

最快的动画，就是没有动画。

设置二：关闭耗 GPU 的视觉效果
-----------------

路径：**系统设置 > 辅助功能 > 显示 > 开启“降低透明度”**

一方面，你的显卡就不会再去渲染每个窗口背后的模糊效果了，菜单栏也会变得不透明，Dock 的磨砂玻璃效果会消失，但显卡会轻松不少，温度也能降个大约 15%，用起来会觉得舒服很多，另一方面 macOS 原本是用这些透明效果来营造层次感，让界面看起来高大上，但其实有没有必要呢，真心说，没必要，因为每秒 60 帧的透明计算背后都是 WindowServer 在默默地帮你干活，CPU 就会被吃掉不少

我自己用 iStat Menus 测量过，发现 CPU 占用从 8% 降到了 3%，也就是说这些本来被浪费掉的处理能力你可以拿回来，好好用在真正重要的工作上，比如渲染、编程或视频剪辑

![](.evernote-content/AF26F9AA-B94A-4AD2-AE6E-AB2C45F145A8/302348F5-0750-4675-95E9-57BD90A6F2AC.jpg)

选择的时候也有标准，一是你在剪辑 4K 视频，就一定要把性能放第一，二是你在跑 Docker 容器，也会建议优先性能，作为创意工作者，把性能放前面会更明智

至于优缺点，一方面，优点就是界面响应会很快，CPU 占用降低，设备温度也会更低，另一方面缺点也有，就是看起来没那么“Mac 风格”，界面会显得扁平一些，少了原本的层次感，有些元素甚至会显得有点过时

设置三：阻止 Siri 背后偷偷分析你的操作
----------------------

路径：**系统设置 > Siri 与 Spotlight > Siri 建议与隐私 > 关闭所有应用的建议**

没错，你如果有把每个应用的建议全都关掉就行了，因为 Siri 会在后台默默分析你的一切输入——邮件、消息、日历、Safari 历史都会被它“学习”，这些机器学习模型会占用不少 RAM 和 CPU，时间长了，你会感觉 Mac 有点卡

![](.evernote-content/AF26F9AA-B94A-4AD2-AE6E-AB2C45F145A8/B72FC09A-7D79-4CBD-BBEA-F4ED026D8780.png)

我自己就遇到过这种情况，有时候在视频通话的时候 Mac 会频繁卡顿，我一看活动监视器，发现“Siri 建议”居然占了 2GB 内存，而这些建议我根本从来没点过

关掉 Siri 建议之后变化真的很明显，一方面通话就不再卡顿了，另一方面在 Final Cut 导出一个 20 分钟的视频项目时，时间也缩短了大概 3 分钟

当然，也有一些小缺点，但有办法解决，第一点是 Spotlight 不再有智能建议，这个可以用 Raycast 来替代，第二点是日历不会自动识别事件，这个就只能手动添加，第三点是 Safari 不再自动填表单，这个可以用密码管理器来补上

设置四：阻止 Spotlight 索引无用数据
-----------------------

路径：**系统设置 > Siri 与 Spotlight > 搜索结果**

取消索引：字体、邮件与信息、音乐、电影、演示文稿，只保留你真正会搜索的内容。Spotlight 停止索引数十 GB 你永远不会查找的数据。

![](.evernote-content/AF26F9AA-B94A-4AD2-AE6E-AB2C45F145A8/D696E98F-3DCE-4B8A-BDEF-35854B498908.jpg)

简单举个例子：在 Mac 开启全部索引，Spotlight 需要搜索 847,000 项，耗时 3 秒；优化后只索引 12,000 项，瞬间搜索完成。

Spotlight 会持续重建索引：新文件？索引它。修改文档？重新索引。下载附件？再索引。SSD 写入量增加约 30%。

开发者的 node\_modules 文件夹尤其夸张，我的就有 400,000 个文件，Spotlight 一直在浪费 CPU。

❌ 不适合人群：

* 依赖 Spotlight 搜索全部文件的人
* RAM 少于 16GB 的用户
* 每天必须使用 Siri 的用户

设置五：关闭热角和通知预览
-------------

路径：

* **系统设置 > 桌面与 Dock > 热角 → 全部设为无**
* **系统设置 > 通知 → 关闭所有通知预览**

误触消失。通知中心不再预渲染消息内容。鼠标移动也不会触发隐藏计算。

热角看似方便，但每个像素的移动都会被系统检测，后台执行数千次计算。我用 Instruments 测试过：当鼠标接近角落时，WindowServer CPU 会飙升。

通知预览更糟，每条消息生成缩略图、抓取应用数据、渲染内容。十条通知，就意味着十次后台运算。

⚠️ 注意： 这些设置可能会影响辅助功能和可访问性功能。视觉障碍用户需要动画来感知界面。解决方案：保留必要的动画，关闭多余的。

![](.evernote-content/AF26F9AA-B94A-4AD2-AE6E-AB2C45F145A8/0F3FA308-4A97-4797-AA99-54F49E14A224.png)

讲到这，你的 MacBook Pro 出厂的时候，其实是带着训练轮的，现在到了可以摘掉的时候了，一方面动画和透明效果虽然看起来好看，但实际上会让操作变慢，而不是带来奢华体验，另一方面 Siri 的各种建议会偷偷消耗掉大量资源，远远超过它能带给你的价值，第三方面 Spotlight 会去索引很多你根本不会查找的文件，还有热角，每秒都会去检测你鼠标的位置，累积起来也是消耗性能

用过这些设置之后你会发现变化很明显，一方面 Mac 看起来可能不再那么光滑，但另一方面工作效率会翻倍，你能瞬间看到所有操作的响应，也能更专心地投入到真正需要做的创作里，整体体验会轻快很多。不管是好的设备还是坏的设备，曾经、未来将是你的战斗伙伴，只有坚持到最后一刻，才能看到不一样的风景。😭又到了告别的时刻，本期的分享到这了，下期我们再见！！！🚀

![](.evernote-content/AF26F9AA-B94A-4AD2-AE6E-AB2C45F145A8/3C40CF1A-39F9-48C8-8F49-32153156CACF.gif)

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=Mzk0MzU5NzQ4Mw==&mid=2247493714&idx=1&sn=8e89d2d89541d2a8153de5af8a50cbb4&chksm=c28116003d0630f8b80b9ebee6b75407b58b7536d263a71d3ab1bf738fa8c87337053abcba6c&scene=90&xtrack=1&sessionid=1757723960&subscene=93&clicktime=1757728313&enterid=1757728313&flutter_pos=12&biz_enter_id=4&ranksessionid=1757727948&jumppath=20020_1757728041947,1104_1757728059704,20020_1757728263006,1104_1757728270429&jumppathdepth=4&ascene=56&devicetype=iOS18.6.2&version=18003f28&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQj5xM0unQUliIc2wEy5XuvxLVAQIE97dBBAEAAAAAAFZWMq+DFlsAAAAOpnltbLcz9gKNyK89dVj0HhopquUroXmdQ9wR4mQy2fVVnOMV1QU2cG1b57BXPpVbRzoME23ymo/iYHTl3UaxjMvXh4/fzNFnpOVjGw+afhcNDQE0saeREaEaoVSgEO2TQ3S8HdnjrjIECuNbyxf5MWObaWANcvGhOx2INjf65QIOl6uSUJ7ddAGzjr1css03Tb2qoj6udGHjZISh+lxMuEzNwFFQuPfJu502s1/G8AjEQbyps9/iuIQJnUlTtg==&pass_ticket=Mb8tZYGgr92J443qEGB5Q75Ud9tKRyz1VFasdRTDQBTdeDM3scKTUPW+PkAR2KHc&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/b82b203e-aa80-4be4-9994-2071e93b7705/b82b203e-aa80-4be4-9994-2071e93b7705/)