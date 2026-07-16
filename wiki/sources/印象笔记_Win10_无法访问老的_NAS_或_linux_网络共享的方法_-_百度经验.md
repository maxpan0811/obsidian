---
title: "Win10 无法访问老的 NAS 或 linux 网络共享的方法 - 百度经验"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/Win10 无法访问老的 NAS 或 linux 网络共享的方法 - 百度经验.md
tags: [印象笔记]
---

# Win10 无法访问老的 NAS 或 linux 网络共享的方法 - 百度经验

# Win10 无法访问老的 NAS 或 linux 网络共享的方法 - 百度经验 --- Win10 无法访问老的 NAS 或 linux 网络共享的方法 =====================

---

# Win10 无法访问老的 NAS 或 linux 网络共享的方法 - 百度经验

---

Win10 无法访问老的 NAS 或 linux 网络共享的方法
================================

比较老的 NAS 设备或者一些 Linux 系统的 SAMBA 软件包可能都是使用的是 SMB1.x 协议，Win10 支持 SMB 3.1.1 协议。无法访问的话，就要确保系统内 SMB1.0 协议的安装。

[![](.evernote-content/ACD8E4D2-2DE9-4F0F-BA44-9402BAF1DDC0/083B4A39-D5DD-4D66-8696-58BBE0795EED.jpg)](http://jingyan.baidu.com/album/c33e3f48f57423ea15cbb507.html?picindex=1)

工具 / 原料
-------

* Windows 10 操作系统

方法 / 步骤
-------

1. 1

   按下 win 键 + X 键或者在开始菜单右键点击，出现的菜单中选择 “控制面板”。

   [![](.evernote-content/ACD8E4D2-2DE9-4F0F-BA44-9402BAF1DDC0/B6D8EA03-929C-4437-BA42-3C14AE2D9F56.jpg)](http://jingyan.baidu.com/album/c33e3f48f57423ea15cbb507.html?picindex=2)
2. 2

   找到 “卸载程序” 点击。

   [![](.evernote-content/ACD8E4D2-2DE9-4F0F-BA44-9402BAF1DDC0/9DCA3022-02F0-4BF3-84E6-1A34DD1CC517.jpg)](http://jingyan.baidu.com/album/c33e3f48f57423ea15cbb507.html?picindex=3)
3. 3

   选择 “启用或关闭 Windows 功能”。

   [![](.evernote-content/ACD8E4D2-2DE9-4F0F-BA44-9402BAF1DDC0/CF1E90A3-7AF5-47E3-8610-08B8B36CBFA8.jpg)](http://jingyan.baidu.com/album/c33e3f48f57423ea15cbb507.html?picindex=4)
4. 4

   确保选中 “SMB1.0/CIFS 文件共享支持”，然后重新启动电脑即可生效。

   [![](.evernote-content/ACD8E4D2-2DE9-4F0F-BA44-9402BAF1DDC0/785E81F0-E76B-4091-B155-A910CAE59065.jpg)](http://jingyan.baidu.com/album/c33e3f48f57423ea15cbb507.html?picindex=5)
5. 5

   然后就可以正常访问 NAS 里面的共享文件了。

   [![](.evernote-content/ACD8E4D2-2DE9-4F0F-BA44-9402BAF1DDC0/14A583E2-E0C5-408A-A448-C343BEF12C3B.jpg)](http://jingyan.baidu.com/album/c33e3f48f57423ea15cbb507.html?picindex=6)
6. 6

   我们可以通过在 powershell 命令行输入 **Get-SmbConnection** 命令查看当前的 samba 共享连接情况。

   我们发现这个 NAS 使用的 SMB 协议版本是 1.5。

   END

经验内容仅供参考，如果您需解决具体问题 (尤其法律、医学等领域)，建议您详细咨询相关领域专业人士。

[举报](#)*作者声明：*本篇经验系本人依照真实经历原创，未经许可，谢绝转载。

---

[🌐 原始链接](https://jingyan.baidu.com/article/c33e3f48f57423ea15cbb507.html)

[📎 在印象笔记中打开](evernote:///view/207087/s1/766509ff-9751-4453-a2a7-345693905781/766509ff-9751-4453-a2a7-345693905781/)