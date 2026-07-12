# 转发：必须采取措施: Dropbox 与 iCloud 的兼容性问题

---

发自网易邮箱大师

--------- 转发的邮件 ---------

发件人： 
[Dropbox](mailto:no-reply@dropboxmail.com)

发送日期： 
2017年09月22日 00:41

收件人： 
[maxpan0811@hotmail.com](mailto:maxpan0811@hotmail.com)

主题： 
必须采取措施：Dropbox 与 iCloud 的兼容性问题

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  | | --- | --- | --- | |  | | | |  | | |  |  |  | | --- | --- | --- | |  | | | |  | 尊敬的潘渤：您好！  我们与您联系，是因为检测到您的 Dropbox 中有一个或多个 .iCloud 占位文件。如果不采取措施，这些占位文件可能会导致数据丢失，因为最近发布的 macOS Sierra 改变了 Dropbox 在某些情况下同步文件的方式。  要确保您的所有文件都安全无忧，请执行以下操作：   * **在 Dropbox 上搜索 .iCloud 文件。**使用 dropbox.com 上的搜索栏，输入 .iCloud 以查看 Dropbox 中有哪些文件受影响。找出这些文件后，您需要从 iCloud 恢复实际版本（按照[这里的 Apple 说明操作](https://support.apple.com/en-us/HT201104)）。 * **更新到最新版本的 Dropbox 桌面客户端（11.4.22 版）**。为确保 Dropbox 继续正常同步，请[下载最新版本](https://www.dropbox.com/l/AAArud-VSXTB8-19lx6mQYwxznFqvi6i3IQ/downloading)的桌面客户端。 * **管理警告通知。**如果您从由 iCloud 同步的文件夹中移动文件至 Dropbox，可能会看到 iCloud 的警告通知。您可以[按这些步骤](https://www.dropbox.com/l/AADlOcfnmFwHUQtyT_kpZrvZMBLX8iEBxgs/help/9269)选择不接收这些通知。   **为什么会出现这种情况？**  .iCloud 文件类型是由 iCloud 创建的一种“占位文件”。作为 Apple 全新发布的优化存储功能的一部分，iCloud 会在尝试释放 Mac 设备磁盘空间时创建这种文件。占位文件所占用的磁盘空间极少，因为它们不含构成真实文件的各项信息。您可将占位文件视为真实文件的映射 — 占位文件存在于您的设备上，而占位文件所代表的真实文件存在于 iCloud 服务器上。  不幸的是，将 .iCloud 文件移入 Dropbox 可能导致一些严重的问题。当您移动文件时，iCloud 会认为您要从 iCloud 删除文件，因此会删除 iCloud 服务器上的真实文件。在一些情况下，iCloud 仅会将占位文件移入 Dropbox，因而 Dropbox 会同步相应的占位文件，而不是您的真实文件。在这种情况下，Dropbox 和 iCloud 上都没有真实文件。  如果您将 Dropbox 移至由 iCloud 同步的位置（如“文稿”或“桌面”），或者如果您的这些位置存在指向 Dropbox 的[符号链接](https://www.dropbox.com/l/AABIodUbqELVNVqkcgpR8or8c_Z-o1n-1Hs/help/9269)，也可能出现上述状况。  如需详细了解 macOS Sierra 上的 Dropbox 和 iCloud，请访问我们的[帮助中心](https://www.dropbox.com/l/AABqkjnb1IKm9CDtf89ZFMeaR9RKS2LoDqU/help/9269)。 此致  - Dropbox 团队 |  | |  | | | |  |  | | --- | |  | | |  |  | | --- | --- | |  | © 2017 Dropbox | | |

![](https://www.dropbox.com/l/AABLUGtHofQ8cAGPlg58lguzIn3qgNoSWlM)

[📎 在印象笔记中打开](evernote:///view/207087/s1/f40467c1-4b8a-4134-9952-01221b7ee610/f40467c1-4b8a-4134-9952-01221b7ee610/)