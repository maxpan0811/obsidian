---
title: "巧用官方 ODT 清爽安装 Office _ 一日一技"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/巧用官方 ODT 清爽安装 Office _ 一日一技.md
tags: [印象笔记]
---

# 巧用官方 ODT 清爽安装 Office _ 一日一技

# 巧用官方 ODT 清爽安装 Office | 一日一技 --- 巧用官方 ODT 清爽安装 Office | 一日一技 =========================== 07 月 12 日 

---

# 巧用官方 ODT 清爽安装 Office | 一日一技

---

巧用官方 ODT 清爽安装 Office | 一日一技
===========================

07 月 12 日

[![](.evernote-content/49892071-BB99-4707-8555-F9F0A4D7B1AE/76C4B365-710C-43D2-9B9E-2B8BE03F70A5)](https://sspai.com/user/711187/updates) 

#### [Unbinilium](https://sspai.com/user/711187/updates)

目录
:   1. [准备工作](#)
    2. [定制你的 Office](#)
    3. [手动编写配置文件](#)
    4. [ODT 定制安装 Office](#)
    5. [写在最后](#)

### **Matrix 精选**

[Matrix](https://sspai.com/matrix) 是少数派的写作社区，我们主张分享真实的产品体验，有实用价值的经验与思考。我们会不定期挑选 Matrix 最优质的文章，展示来自用户的最真实的体验和观点。

文章代表作者个人观点，少数派仅对标题和排版略作修改。

---

Office 2019 专业增强版中，依然捆绑着 2016 版的 OneNote，Outlook 以及 Skype for Business 等，相较 Windows 10 自带的体验良好的 UWP 版，显然没有必要保留臃肿的 2016 桌面版全部组件。但 Office 2019 并不像之前的版本在「控制面板」的「卸载程序」中就能调整相关组件的增减，而无论是在线安装还是镜像安装，均无法去掉不需要的组件。

屡试无果，终寻得可使用官方提供的 ODT 即 [Office Deployment Tool](https://docs.microsoft.com/en-us/deployoffice/configuration-options-for-the-office-2016-deployment-tool) 来实现 Office 的定制安装。

准备工作
----

首先需要卸载之前已经安装的 Office，建议使用 [官方的卸载器](https://support.office.com/en-us/article/uninstall-office-from-a-pc-9dd49b83-264a-477a-8fcc-2fdf5dbf61d8) 进行完整卸载，此外非 365 用户在卸载前要注意备份 Office 密钥。完成卸载后在官网 [下载 Office Deployment Tool](https://www.microsoft.com/en-us/download/details.aspx?id=49117)。

![](.evernote-content/49892071-BB99-4707-8555-F9F0A4D7B1AE/8E056263-F3BF-46FE-B3DE-C6CEEC5F8E7B.png)

下载 Office Deployment Tool

运行 Office Depolyment Tool，按照提示将配置文件提取到某个位置，笔者选择将其提取到桌面上。可以看到一共提取出三个文件。包括主程序 `setup.exe` 和三个后缀为 `.xml` 配置文件，默认配置文件是安装 Office 356 或 Office 2019 Enterprise 全部组件的，并不能达到我们的目的，因此我们需要对配置文件进行修改。

定制你的 Office
-----------

对于主流预装版本的 Office，可以在官网直接 [自定义配置文件](https://config.office.com/) 并下载到计算机，点击首页左下角的 「Create a new configuration」来创建一个新的配置文件。

![](.evernote-content/49892071-BB99-4707-8555-F9F0A4D7B1AE/A3027C2D-A09F-45D3-88F5-F5E0FD3FBF44.png)

config.office.com

定制页面提供了大量可供定制的选项，例如 Office 的发行版本（如果其中没有适用你的 Office 版本，参照段末的手动配置步骤），捆绑安装的组件，语言包以及更新选项等，按照提示结合自己的实际需求一步步进行即可。在此关注 「Products and releases」中「Apps」一栏，只选择自己需要的组件。

![](.evernote-content/49892071-BB99-4707-8555-F9F0A4D7B1AE/6B378EDE-A3AE-4C91-AC9A-D353C3F323CF.png)

Office Customization Tool

在完成所有定制后，点击右上角的「Export」导出配置文件。

![](.evernote-content/49892071-BB99-4707-8555-F9F0A4D7B1AE/F3B8424A-8182-4476-AD68-41367ECF0A21.png)

Export

导出时需要选择默认的文件格式，在这里选择第二个「Office Open XML fomarts」，以默认文件名 `Configuration.xml` 储存到此前提取 Office Depolyment Tool 的同一目录下即可。

手动编写配置文件
--------

对于在官网定制页面中没有找到符合自己需求版本的 Office 的小伙伴，需要使用如 [VS Code](https://code.visualstudio.com/) 等编辑器自己创建配置文件，笔者在这里提供一个通用模板。

```
<Configuration>  
  <Add OfficeClientEdition="64" Channel="Monthly">  
    <Product ID="LanguagePack">  
      <Language ID="en-us" />  
      <Language ID="zh-cn" />  
      <ExcludeApp ID="Access" />  
      <ExcludeApp ID="Excel" />  
      <ExcludeApp ID="Groove" />  
      <ExcludeApp ID="Lync" />  
      <ExcludeApp ID="OneDrive" />  
      <ExcludeApp ID="OneNote" />  
      <ExcludeApp ID="Outlook" />  
      <ExcludeApp ID="PowerPoint" />  
      <ExcludeApp ID="Publisher" />  
      <ExcludeApp ID="Word" />  
    </Product>  
    <Product ID="ProPlus2019Volume">  
      <Language ID="en-us"  
      <Language ID="zh-cn" />  
      <ExcludeApp ID="Access" />  
      <ExcludeApp ID="Excel" />  
      <ExcludeApp ID="Groove" />  
      <ExcludeApp ID="Lync" />  
      <ExcludeApp ID="OneDrive" />  
      <ExcludeApp ID="OneNote" />  
      <ExcludeApp ID="Outlook" />  
      <ExcludeApp ID="PowerPoint" />  
      <ExcludeApp ID="Publisher" />  
      <ExcludeApp ID="Word" />  
      </Product>  
  </Add>  
</Configuration>
```

其中 `<OfficeClientEdition="64" />` 可选 `32`（32 位）和 `64`（64 位）；`Language ID="en-us"` 可选 `en-us`（英语 - 美国）和 `zh-cn`（中文 - 中国大陆）等；`<Product ID="LanguagePack" />` 是安装的语言包，不做修改；在这里主要修改 `<Product ID="ProPlus2019Volume" />` 双引号内的参数，参考下方表格选择适合的 Product ID（引自 [Tenfourms](https://www.tenforums.com/tutorials/123233-custom-install-change-microsoft-office-office-deployment-tool.html)）。不同版本的激活方式缩写已经标出。

* P = Retail product key
* S = O365 Personal, Home, Business or Enterprise subscription / license
* V = Volume licensing (KMS or MAK)

![](.evernote-content/49892071-BB99-4707-8555-F9F0A4D7B1AE/27652420-0D35-4BC8-A67C-492B6525B002.png)

Table

最后编辑 `<ExcludeApp ID="" />` 配置**不安装的组件**。需要注意的是每个 `Product` 部分的配置都需要同步修改。最后将编辑好的配置文件命名为 `Configuration.xml` 储存到此前提取 Office Depolyment Tool 的同一目录下。有关 ODT 配置文件的更多信息，可以阅读[官方文档](https://docs.microsoft.com/en-us/deployoffice/overview-of-the-office-2016-deployment-tool)。

ODT 定制安装 Office
---------------

快捷键「Win」+「R」在运行内输入 `CMD` 打开命令提示符，用命令 `cd` 进入此前提取的 Office Depolyment Tool 的目录，运行命令 `setup.exe /download Configuration.xml` 下载 Office，目录下会出现名为 Office 的文件夹，文件大小在 2.5G 左右，耐心等待下载完毕（命令运行结束）。

![](.evernote-content/49892071-BB99-4707-8555-F9F0A4D7B1AE/A4D4884D-EAA3-434C-AC08-083DB8FF9C5B.png)

Fluent Terminal CMD

接着运行命令 `setup.exe /configure Configuration.xml` 安装定制好的 Office，定制安装的组件会以图标的形式呈现在安装界面，可以再加确认。

![](.evernote-content/49892071-BB99-4707-8555-F9F0A4D7B1AE/4A965E07-64F6-4DF5-840E-365D5E562C9B.png)

ODT Install

待安装结束后，方可清理目录内的文件。使用 ODT 安装的 Office 一般分为多个包，逐一卸载不便，如需完整卸载，建议使用官方的 [卸载工具](https://aka.ms/SaRA-officeUninstallFromPC)。

写在最后
----

白驹过隙，一晃眼醒来发现已经 2019 了，一键式的软件安装也愈加普遍，只是忆起十几年前繁琐的软件安装，到头来恍然发觉，过于简易的软件安装似乎并没有为我省下时间或提高效率。重度强迫症和虚伪完美主义，一中午恼怒折腾配置软件，下午还要卑微写稿发泄情绪，心心念换回 macOS。相信繁和简之间定能找到一个舒适且高效率的平衡点，这需要设计师和开发者的共同努力。

另欢迎交流建议以及错误斧正，毕读愉快。

**关联阅读：**[Office 安装卸载太麻烦？用这个工具帮你解决：Office Tool Plus](https://sspai.com/post/43839)

> 下载少数派 [客户端](https://sspai.com/page/client)、关注 [少数派公众号](http://sspai.com/s/KEPQ)，发现更多实用玩机技巧

> 特惠、好用的硬件产品，尽在 [少数派 sspai 官方店铺](https://sspai.com/post/https-//shop549593764.taobao.com/?spm=a230r.7195193.1997079397.2.2ddc7e0bPqKQHc)

---

[🌐 原始链接](https://sspai.com/post/55644)

[📎 在印象笔记中打开](evernote:///view/207087/s1/ebf3119b-b605-4382-993c-f7f41a8480bd/ebf3119b-b605-4382-993c-f7f41a8480bd/)