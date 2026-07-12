# 将你的 iOS 设备备份到外置磁盘 | 一日一技 · Mac - 少数派

---

前不久我更换了一次手机，并通过 iTunes 将旧设备的备份恢复到了新设备中。恢复完成后，我惊讶地发现几乎所有的东西都和之前在旧设备上看到的一模一样（注：需要特别指出的是，QQ 和微信的聊天记录也都恢复了回来），令我十分感动！

夸奖完毕，下面是猛烈的批评：和很多人一样，在过去的半年时间里，我（几乎）没有使用 iCloud 成功地备份过我的设备，以至于我又不得不老老实实地用回 iTunes 备份！时间一长，体量日渐庞大（两个设备，约 12G）的备份文件，开始侵占我那 128G 的内置磁盘，令人忧伤。

考虑到备份文件并不会经常被使用，所以即便是 iTunes 默认情况下只能备份到内置磁盘，手动将备份文件迁移到外置磁盘中也并不麻烦。但如果能够「一劳永逸」地将默认的备份路径修改为外置磁盘路径，那又何乐而不为呢？

方法一：通过 iMazing 修改备份路径
---------------------

1. 退出 iTunes（如果你已经打开了的话），并连接你的外置磁盘。

2. 前往 [iMazing](https://imazing.com/) 官网，下载并安装试用版本（就本文中所要实现的需求来说，试用即可，无需购买完整版本）。

3. 前往 iMazing 「偏好设置」-「备份」，修改「默认备份位置」为外置磁盘文件夹，在弹出的警告窗口中选择「继续」。

[![](.evernote-content/0F134A11-AF51-4F4D-9EE5-FE62DB39C745/D35F4EEB-43C3-4A2A-A8D2-584B8646401E.jpg)](http://cdn.sspai.com/attachment/thumbnail/2016/03/30/9b6863e183bdee8596fbb26abda6f16f4dec7_mw_800_wm_1_wmp_3.jpg)

* 如果你此前备份过你的设备的话，iMazing 将移动所有备份到指定的外置磁盘文件夹；

[![](.evernote-content/0F134A11-AF51-4F4D-9EE5-FE62DB39C745/FE4719AE-9CB9-4C86-A1F3-E12F7DB28CA8.jpg)](http://cdn.sspai.com/attachment/thumbnail/2016/03/30/b32eed9a9361a69e76019aba0a4c2dc54dec5_mw_800_wm_1_wmp_3.jpg)

* 如果没有的话，在接下来弹出的窗口中选择「忽略」即可。

完成后，我们会发现 iMazing 在外置磁盘中新建了一个名为 iOS backup 的文件夹。

4. 关闭 iMazing，打开 iTunes，并前往「偏好设置」-「设备」，勾选「防止 iPod、iPhone 和 iPad 自动同步」。

[![](.evernote-content/0F134A11-AF51-4F4D-9EE5-FE62DB39C745/DE3F612C-21CA-40BF-91E4-A8A807C1C523.jpg)](http://cdn.sspai.com/attachment/thumbnail/2016/03/30/46e201ad66be21144e1e4e0aa8d12d754dec6_mw_800_wm_1_wmp_3.jpg)

5. 连接你的设备，点击「立即备份」即可。此后，使用 iTunes 对设备进行的备份都将保存到外置磁盘中。

[![](.evernote-content/0F134A11-AF51-4F4D-9EE5-FE62DB39C745/3C2512F5-EF1C-44CB-823C-21BFCED0CD19.jpg)](http://cdn.sspai.com/attachment/thumbnail/2016/03/30/d88491e1434c1f2901162a0f978927754dec1_mw_800_wm_1_wmp_3.jpg)

方法二：手动修改备份路径
------------

如果你对方法一的实现原理不感兴趣的话，就无需看方法二了，因为接下来要讲的方法，操作起来要麻烦许多。不过，如果你希望「知其然，亦知其所以然」的话，不妨接着看。

### 迁移旧的备份文件

1. 退出 iTunes（如果你已经打开了的话），并连接你的外置磁盘。

2. 打开 Finder，依次点击「前往」-「前往文件夹」，在弹出窗口中输入如下路径（iTunes 的默认备份路径）：

`~/Library/Application Support/MobileSync/Backup`

[![](.evernote-content/0F134A11-AF51-4F4D-9EE5-FE62DB39C745/CAF97E56-D38D-4770-9AEB-83F7F5ED9519.jpg)](http://cdn.sspai.com/attachment/thumbnail/2016/03/30/5ae3fd432734c57d1b0d83741bc8d7a84dec3_mw_800_wm_1_wmp_3.jpg)

将 Backup 文件夹中的备份文件（如有）拷贝到外置磁盘中。完成后，即可删除 Backup 文件夹或将其重命名为其他名字，例如 Backup old（**一定要执行删除或重命名操作，这很重要！**）。

### 创建符号链接

为了让 iTunes 能够备份到外置磁盘，关键是在原备份文件夹和外置磁盘文件夹之间建立符号链接（Symbolic Link，也称软链接，类似于Windows 的快捷方式或 OS X 中的替身文件）。从而使得我们能够欺骗 iTunes，令其误以为是备份在内置磁盘。

为了方便说明，下文中以外置磁盘名称为 Mac，其中用于存储备份的文件夹名为 iOS Backups 为例进行说明。**你可以根据需求对名称进行调整，不过要记得在输入下文中的路径命令时也要进行对应调整。**

1. 打开 Finder，选中外置磁盘中的 iOS Backups 文件夹。

2. 打开「终端」，将前述 iOS Backups 文件夹拖入，得到路径为：

`/Volumes/Mac/iOS\ Backups`

[![](.evernote-content/0F134A11-AF51-4F4D-9EE5-FE62DB39C745/D471D4AC-A843-451D-BC75-F3CACD154E77.jpg)](http://cdn.sspai.com/attachment/thumbnail/2016/03/30/775d6ee710b24a6e5e2933de0c25156f4dec4_mw_800_wm_1_wmp_3.jpg)

3. 在文本工具中，复制、粘贴上述路径和 iTunes 默认备份路径，并将其组合为下面命令（注意其中的空格）：

`ln -s /Volumes/Mac/iOS\ Backups ~/Library/Application\ Support/MobileSync/Backup`

[![](.evernote-content/0F134A11-AF51-4F4D-9EE5-FE62DB39C745/3BA4E615-171E-42CA-B019-0F9F6A5CC6A2.jpg)](http://cdn.sspai.com/attachment/thumbnail/2016/03/30/334961e3b839518864b8347f6d434b894dec0_mw_800_wm_1_wmp_3.jpg)

4. 重启终端，执行上一步中的命令，回车确认。完成后，再次查看 iTunes 默认备份文件夹，发现一个带着小箭头的 Backup 文件，表明软链接建立完成。

[![](.evernote-content/0F134A11-AF51-4F4D-9EE5-FE62DB39C745/9A9CEB21-322E-4B05-9797-74E16B69572D.jpg)](http://cdn.sspai.com/attachment/thumbnail/2016/03/30/f278a0df66d5ddc3f2c8117e9f32f7b34dec2_mw_800_wm_1_wmp_3.jpg)

此后的步骤，和「方法一」中的第四、五步相同。

---

[🌐 原始链接](http://sspai.com/33524)

[📎 在印象笔记中打开](evernote:///view/207087/s1/769bb773-9398-4c85-a360-8da074d885f6/769bb773-9398-4c85-a360-8da074d885f6/)