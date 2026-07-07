---
title: 这下，VS Code 也没有安装的必要了！
type: source
created: 2026-06-11
updated: 2026-06-11
source_path: 印象笔记管理工具/这下，VS Code 也没有安装的必要了！.md
tags: [ide, vscode, warp, zed, ai-agent, trend]
updated: 2026-06-27
updated: 2026-06-27
updated: 2026-06-27
updated: 2026-06-27
---

---
title: "这下，VS Code 也没有安装的必要了！"
source: evernote
type: note
export_date: 2026-06-27
guid: 8939d4b6-e0c3-41c9-a74f-47d2415fa7db
---

# 这下，VS Code 也没有安装的必要了！

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzIzMzQyMzUzNw==&mid=224751...](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247517656&idx=1&sn=f84908515540f2169a811b4224096588&chksm=e91cb6ac7a4a1f154d19d6182e070231eb06656933636ade9cb833ab3bb0d3d33ae0a7732355&scene=90&xtrack=1&req_id=1780477858551484&sessionid=1780477974&subscene=93&clicktime=1780477977&enterid=1780477977&flutter_pos=0&biz_enter_id=4&ranksessionid=1780477858&jumppath=1001_1780477970264,1102_1780477971345,1001_1780477973425,1104_1780477975763&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004a25&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ8vbko8FcDYEmeNmCtODu9hLTAQIE97dBBAEAAAAAAD+nNDN0IlEAAAAOpnltbLcz9gKNyK89dVj0pdLZdX2MlMmVbBc1ZfXz+3Jdi9HmgWRd8fctOfroc1C7UztuoDEm62lBsR2TbXgiZglzr2y2sE2txMDoeNaebANTQXELQGR0kuCBSnnfCiRajpdoF7fFkX5AWHtMGGxNNULxzHOqimGciEvL7OTEYHY2AUMlZMzoOYhBjShUDESftTTwsrxWc9Gb0WQxNqlLb6mpbxdMepXDHneo+oKQU48YPMa8ppZzGP4r+jY=&pass_ticket=FKmmW2PIWQU/jBDdSoGeyNQD7TtNcxaPalBTMG+VTJb7ZdAPA4gu0AVA5KfEULE9&wx_header=3)

Original字节笔记本字节笔记本

VS Code 的核心代码仓库叫 Code - OSS，这部分是 MIT 开源的，我们所熟知的Cursor，Trae都是基于它来二次开发的。

VS Code有一个让我离不开的插件Remote - SSH。这个插件可以说是GitHub的宝藏应用，丝滑远程连接服务器，远程即是本地，实现实时编辑同步，不过它却是闭源的。

这个功能也被其它的IDE给彻底地取代了。

最新版本的Warp 现在也支持通过 SSH 连接的文件树和代码审查功能。

对话启动后，安装SSH扩展即可。

![](attachments/9df607fb54c8c483.png)

点击Tools panel就可以展开远程服务器的文件列表，和你在本地使用完全一致的体验。

![](attachments/eab8bfa47eba66c6.png)

连接后，Warp Agent还能通过 SSH实现完整编码功能，比如文件编辑和代码库索引等，，直接就可以使用本地的Agent能力来控制远端的代码编写。

不需要像Remote - SSH那样连接之后，还需要在命令行里面再起一个Agent CLI工具。

![](attachments/b6a7dfb84ce0531c.png)

也不需要另外再订阅付费， Warp增加了 DeepSeek 这类第三方供应商的，可用性和可玩性进一步增强。

不只是 Warp，Zed现在也支持SSH 打开远程项目，本地只保留轻量 UI，语言服务器、终端、任务都在远程跑。

![](attachments/8cdeb5da8e8bdbc5.png)

这类第三方的IDE功能集成越来越多之后，VS Code成为了非必选项。

我反正是挺讨厌VS Code这类Electron应用的，既占空间运行内存也大，目前所有类VS Code的全部卸载了。

查看代码使用Sublime，轻量便捷，IDE本地就只剩下Zed，Rust跨平台，启动快、界面美观干净，也没有那么多历史包袱。

之所以要这么做，是因为现在的工作流彻底变了，在 CLI 里描述目标，让 Agent 读项目、改代码、跑命令、修错误。

我更多是在做方向判断、方案取舍和结果验收，IDE 不再是工作中心，更像一个预览器、审查器、手动做部分修改的地方。

新的趋势也越来越明显：去IDE化，越来越云端化。

同样二开的VS Code的Windsurf如今也改名 Devin Desktop了。

![](attachments/ddde2a6e0e009be6.png)

配合Devin Cloud 主打云端Agent，不再强调打造一个聪明的编辑器，而是把自己变成 Agent Command Center。

界面不重要了，以后我们面对的一组正在工作的 Agent，这个在修 bug，那个在写测试，另一个在改 UI，还有一个在开 PR。

过去我们把所有能力都塞进 IDE，现在恰好反过来，AI 把很多能力重新拆了出来，编辑归编辑，远程归远程，执行归 CLI，复杂任务交给 Agent。

当 AI Agent 可以自己读项目、跑命令、修复问题、提交结果之后，IDE 的价值就不再是中心舞台，而是后台工具。

突然发现，已经大半年没有打开 JB 家的 IDE了。

现在你还亲自打开 IDE 吗？

修改于
