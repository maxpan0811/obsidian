---
title: Codex 从下载到入门
type: source
created: 2026-07-09
updated: 2026-07-09
source_path: 印象笔记管理工具/Codex 从下载到入门.md
tags: [印象笔记]
---

# Codex 从下载到入门

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzU1NjgxNTkzNw==&mid=224748...](https://mp.weixin.qq.com/s?__biz=MzU1NjgxNTkzNw==&mid=2247484649&idx=1&sn=44f20bc6a51bfb984fee6669d655e274&chksm=fdc650feb469b3ca21330d69ec8919d39bb6b149280674d866eb199006e058db1df12a120807&scene=90&xtrack=1&req_id=1779971223574457&sessionid=1779971136&subscene=93&clicktime=1779971294&enterid=1779971294&flutter_pos=43&biz_enter_id=4&ranksessionid=1779971223&jumppath=20020_1779971163760,1104_1779971174462,20020_1779971223005,1104_1779971258038&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004935&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQrK3tkx2isY6Tb1s8P5uVtBLTAQIE97dBBAEAAAAAAGV3IzN4G0EAAAAOpnltbLcz9gKNyK89dVj0qW4KrsbhacObyE4hIKJeVaLka0Kos/rnEK2+/N1BoVh8z1djjw69rsETzQoJSod34TVxsNFGP7Ns4nU/1c7Zn8LyBXDYncdHkyF7tj/fV180KwIH92mM9Gha+rlf//k7rTFc0jDax1xPP7aGY/jRgjGOjri0p29cPYrSs7i5mC2ZAFYzhJ6U33GLskJuquvQnskj9xSxE95h3gypgcoLxinwDEyg7NeO5ljSNAQ=&pass_ticket=Qd3b/hzfCDShDxkoZc7SXrv1jslSZZOfAk7OEw40DjzmCBuwEMtqktoPKJxrIdhh&wx_header=3)

Codex 从下载到入门
============

OriginalAl4ALL AI Prime

前几天发了一篇《Codex 从入门到精通》，好多朋友回复不知道怎么安装，手把手教了十多位朋友后，还是写了这篇《Codex 从下载到入门》。

1. 下载安装包
--------

先下载两个软件：

Codex 官方下载地址： https://openai.com/zh-Hans-CN/codex

CC Switch 下载地址： https://github.com/farion1231/cc-switch/releases

如果无法访问官方地址，可以私信我发送： **codex**，获取网盘下载地址。

![](.evernote-content/E70EE5BD-7CE4-42C2-8E8E-19345C4E4826/9C1F9E59-F920-4154-A79F-6AA20ED938A4.png)

2. 安装软件
-------

Codex 和 CC Switch 都推荐使用安装版，后续配置会省事很多。

Mac 用户直接双击 `.dmg` 文件安装即可。

Windows 用户优先使用：

Codex Installer.exe

如果还是因为网络问题无法正常安装，再尝试使用 `Codex.Msix`。

安装方式如下：

先找到 `Codex.Msix` 文件所在的文件夹，复制这个文件夹路径。

然后打开 PowerShell，输入下面这行命令，把里面的路径替换成你刚才复制的路径：

cd '粘贴你的 Codex.Msix 所在目录路径'

举个例子，如果 `Codex.Msix` 在下载目录里，就可能是这样：

cd C:\Users\你的用户名\Downloads

回车进入目录后，再执行安装命令即可：

Add-AppxProvisionedPackage -Online -PackagePath "Codex.Msix" -SkipLicense -Regions "all"

CC Switch 直接双击安装即可。win10系统无法安装 `.msi`文件，请使用免安装版。

3. 配置 API
---------

安装好软件后，打开下面这个地址：

https://open.sub2api.top

注册并登录后，按下面步骤操作：

1. 点击「API 密钥」
2. 创建一个新的密钥
3. 点击密钥后面的「导入到 CCS」
4. 弹窗出现后点「导入」

![](.evernote-content/E70EE5BD-7CE4-42C2-8E8E-19345C4E4826/DBCEE6AF-1FE3-488B-AE3D-F7A56880158E.png)![](.evernote-content/E70EE5BD-7CE4-42C2-8E8E-19345C4E4826/9213CBE9-98D0-4EB0-8CAD-9FCCC5E0F299.png)

正常情况下，CC Switch 会自动接收到这组配置。

如果你用的是 CC Switch 免安装版，可能不会自动弹窗。这种情况就手动配置：

打开 CC Switch，选择 Codex 栏目。 

![](.evernote-content/E70EE5BD-7CE4-42C2-8E8E-19345C4E4826/C1A9E2B4-416B-4461-9926-D616139134A6.png)

点击「新增」，然后填写：

API KEY：刚才创建的密钥API 请求地址：https://open.sub2api.top

点击「获取模型列表」，模型选择 `gpt-5.5`

点击最下面的添加后，返回列表后，点击「启用」。 

![](.evernote-content/E70EE5BD-7CE4-42C2-8E8E-19345C4E4826/E7981365-315D-45DE-827B-D47F94FB2E3E.png)

到这里，CC Switch 的部分就配置好了。

4. 启动 Codex
-----------

打开 Codex，登录方式选择「使用其他方式登录」。 

![](.evernote-content/E70EE5BD-7CE4-42C2-8E8E-19345C4E4826/99A4CFBC-8163-4F14-A6B2-ED0DCCCCDE87.png)

因为请求已经被 CC Switch 接管，所以这里的 API 密钥随便填即可：

![](.evernote-content/E70EE5BD-7CE4-42C2-8E8E-19345C4E4826/7DEB7F34-2D54-42DB-945B-CE2A31909533.png)

我这里随便输了个123，点继续，就正常进入了。

后续具体怎么提问、怎么让 Codex 修改代码、怎么接入本地项目，可以继续看我这篇文章：

[Codex 从入门到精通](https://mp.weixin.qq.com/s?__biz=MzU1NjgxNTkzNw==&mid=2247484498&idx=1&sn=78e161075c931dd0bafd65be102d0991&scene=21#wechat_redirect)

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzU1NjgxNTkzNw==&mid=2247484649&idx=1&sn=44f20bc6a51bfb984fee6669d655e274&chksm=fdc650feb469b3ca21330d69ec8919d39bb6b149280674d866eb199006e058db1df12a120807&scene=90&xtrack=1&req_id=1779971223574457&sessionid=1779971136&subscene=93&clicktime=1779971294&enterid=1779971294&flutter_pos=43&biz_enter_id=4&ranksessionid=1779971223&jumppath=20020_1779971163760,1104_1779971174462,20020_1779971223005,1104_1779971258038&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004935&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQrK3tkx2isY6Tb1s8P5uVtBLTAQIE97dBBAEAAAAAAGV3IzN4G0EAAAAOpnltbLcz9gKNyK89dVj0qW4KrsbhacObyE4hIKJeVaLka0Kos/rnEK2+/N1BoVh8z1djjw69rsETzQoJSod34TVxsNFGP7Ns4nU/1c7Zn8LyBXDYncdHkyF7tj/fV180KwIH92mM9Gha+rlf//k7rTFc0jDax1xPP7aGY/jRgjGOjri0p29cPYrSs7i5mC2ZAFYzhJ6U33GLskJuquvQnskj9xSxE95h3gypgcoLxinwDEyg7NeO5ljSNAQ=&pass_ticket=Qd3b/hzfCDShDxkoZc7SXrv1jslSZZOfAk7OEw40DjzmCBuwEMtqktoPKJxrIdhh&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/f58bddcd-2067-42b4-98d5-aab69ca5a84e/f58bddcd-2067-42b4-98d5-aab69ca5a84e/)
