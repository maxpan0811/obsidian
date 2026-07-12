# 批量加水印、裁剪、压缩……一个 Retrobatch 就能搞定

---

如果只是批量压缩图片，那么 Mac 上有不少软件可以做到；如果还需要批量裁剪、调色、加边框、加滤镜呢？剩下的选择就屈指可数了。Lightroom Classic 的同步功能可以做到，但是其界面陈旧又繁琐；Picasa 支持一些常规批量操作，终究不够全面；而 [Retrobatch](https://flyingmeat.com/retrobatch/) 则以一种灵活优雅的方式实现图片批量操作。

Retrobatch 由用户自由创建 Workflow 来实现相应的功能，这些 Workflow 能取代大量的重复劳动，可以说是提高生产力的利器。Retrobatch 的一般操作是从左边栏拖动相应动作到工作区形成节点（Nodes），节点连接起来形成一个 Workflow，最后运行这个 Workflow 即可。

![](.evernote-content/6301D90C-8696-4AE4-8746-5C64DFC5AC58/AF99F04C-78DB-48A8-8AD2-92C61BDA0B73.jpg)Retrobatch 主界面

以批量给图片加边框为例
-----------

创建批量给图片加边框的工作流：批量导入图片 → 加边框 → 导出图片。

**1. 批量导入图片**：从左边栏把「Read Folder」拖到工作区，在右边栏选择图片文件夹（也可以直接从任意地方把图片文件夹拖入工作区）。

![](.evernote-content/6301D90C-8696-4AE4-8746-5C64DFC5AC58/74525DBA-96C4-49F0-BBE1-5E03AEFD607E.gif)

**2. 加边框**：从左边栏把「Add Border」拖到工作区，在右边栏设置边框颜色和尺寸。

![](.evernote-content/6301D90C-8696-4AE4-8746-5C64DFC5AC58/DC8EA8F9-4041-4751-9189-C54ECA7DC9BD.gif)

**3. 导出图片**：从左边栏把「Write Images」拖到工作区，会自动弹出窗口选择导出到哪个文件夹，右边栏可以设置文件名后缀。

![](.evernote-content/6301D90C-8696-4AE4-8746-5C64DFC5AC58/DBEB92A3-9C80-470C-8868-C566844E7ACA.gif)

**4. 运行 Workflow**：以上三个节点连接成 Workflow 后，点击上方的运行按钮，静待处理完成。

![](.evernote-content/6301D90C-8696-4AE4-8746-5C64DFC5AC58/DA1F9D45-0D55-43BC-B45D-183919A922CC.gif)

可以看到 Retrobatch 的主要操作就是 drag & drop, 它的大多数 Workflow 的逻辑都是相当简单的，而且可视化的界面简洁明了，非常容易上手。需要注意的是往工作区添加新的节点不能超过一个格子的间隔，否则就连接不上。

灵活的 Workflow 组合
---------------

既然这些动作节点是可以随意拖动连接的，那么就表明我们可以灵活地创建各种 Workflow。比如我们可以给上面那个批量加边框的 Workflow 添加一条支线，让它同时保存一份尺寸缩小 50% 的图片，如下图这样：

![](.evernote-content/6301D90C-8696-4AE4-8746-5C64DFC5AC58/BF776283-123A-456A-87E8-57B3B80E121F.jpg)

Retrobatch 就相当于提供了一套运行规则和基础设施，剩下的完全由用户自己去组合创造。它本身也提供了一些 Workflow 模版，比如转换格式、添加日期等，我们也可以把自己经常用到的 Workflow 保存为 .retrobatch 格式的文件，方便下次使用。

**Retrobatch** **能做到的常用批量操作包括**：调色、加边框、加滤镜、加水印、移除地址信息、裁剪、镜像、压缩… … 其实一个图片编辑器的基础功能 Retrobatch 已经覆盖的七七八八，当这些功能在 Workflow 里自由组合和运转时，Retrobatch 的强大之处就显现出来了。

目前 Retrobatch 还处于 beta 阶段，可以免费试用 14 天，购买完整版需要 $30。 如果你对 Retrobatch 感兴趣，可以到[官方网站](https://flyingmeat.com/retrobatch/)下载试用。

---

> 下载 [少数派 iOS 客户端](http://sspai.com/s/nqQk)、关注 [少数派公众号](http://sspai.com/s/KEPQ)，让智能设备更好用 💪

---

[🌐 原始链接](http://sspai.com/post/44531)

[📎 在印象笔记中打开](evernote:///view/207087/s1/361c741e-14f2-4e31-bc95-3a0fa27ba88d/361c741e-14f2-4e31-bc95-3a0fa27ba88d/)