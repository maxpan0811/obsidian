# 谷歌悄悄发了个命令行工具Colab CLI，你的GPU从此不用靠浏览器"续命"了

---

原文链接: [https://mp.weixin.qq.com/s?chksm=f0a6021dc7d18b0bc210df4e475d669...](https://mp.weixin.qq.com/s?chksm=f0a6021dc7d18b0bc210df4e475d669407af5101db6a5dec8a11add10eed40d563bf85a1d884&exptype=unsubscribed_card_recommend_item_heat_tlfeeds&ranksessionid=1782340110_2&req_id=1782342212142578&scene=169&mid=2247484143&sn=261eb3a3e4aea11f0a7e1ecb40b5a2d5&idx=1&__biz=MzYzMzg4NzEzMw==&sessionid=1782340109&subscene=200&clicktime=1782344677&enterid=1782344677&flutter_pos=18&biz_enter_id=5&jumppath=WAWebViewController_1782344495645,WAWebViewController_1782344496170,20020_1782344520289,1104_1782344673515&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b2b&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ/7SWPZtqjZi9e0Xo382iMBLTAQIE97dBBAEAAAAAACDkDMk8V2cAAAAOpnltbLcz9gKNyK89dVj0Z8IIkzS+rWC86rYKCE4dt6z6ofDu5V+EbLY6Fv2zoelC9TUPlmqoSoaat+gg9g4rcbnZwrSUTqNV+aUbEzTzKIg+ml71vssSNkjhqtAOViqA/WDy3ZSIidOEe5BiVawWulGZZrAYeOnesCMea9et5o/Hs2kAiXOqXWoAnfmsoTZYU3zjZvMF3Ss0rBmNghpvQKhb8QFWdc6FS3pSRjGUMAC4OPFbD2INiHOz0qg=&pass_ticket=eH8st0JxklTrWIGGuJ8QU3pr/WJlZZogOzj6Bgu5okliRq771Wuw1gTM6Xsd7aCk&wx_header=3)

Original秃秃问花花秃秃问花花

![](.evernote-content/8B0D5D46-9C1B-40E0-9FC1-232F308D4E9F/B19F850F-27BA-4297-9B9E-1251DEF60BCA.png)

想象一个场景：你训练模型到凌晨三点，浏览器标签页不小心关了，Colab 断了，三小时白跑。

别笑，这事儿每个用过 Colab 的人都经历过。

好消息是，谷歌终于想通了这件事。2026年6月16日，他们在 PyPI 上悄悄发了一个叫 google-colab-cli 的包。没有发布会，没有博客文章，甚至连个像样的宣传页都没有。但这个不到一周前上线的工具，可能比你今年见过的任何AI新玩具都实用。

它到底干了啥？一句话：把Colab从浏览器里"拽"到了终端

以前用 Colab，你得开浏览器、点按钮、祈祷别断网。现在装好 CLI，一行 colab new --gpu A100 就能拉起一台 A100 虚拟机。想跑脚本？colab exec -f train.py。跑完收工？colab stop。全程不用碰浏览器。

更狠的是 colab run 命令：新建VM → 跑脚本 → 拿结果 → 自动销毁，一条龙。你甚至可以把它写进 shebang 行，让 Python 脚本自己声明"我需要一块 L4 GPU"，然后直接 ./script.py 就跑起来了。

这哪是命令行工具啊，这是把云算力变成了你本地工作流的一个函数调用。

![](.evernote-content/8B0D5D46-9C1B-40E0-9FC1-232F308D4E9F/D81ADCCE-BBBE-429F-BDD3-23AD7F1AE10D.png)

为什么这件事值得你关心？
============

因为它解决了一个被所有人忽略的真问题：AI时代的算力瓶颈，不是GPU不够强，而是人和机器之间的摩擦太大。

CLI 提供了 24 个子命令，覆盖会话管理、代码执行、文件操作、GCP认证、Drive挂载、日志导出全套流程。它还内置了 keep-alive daemon——你再也不用开着浏览器标签页给 VM "续命"了。

而且注意一个细节：官方文档特意提到，如果你想要 notebook 内的交互式 Agent 编码，应该去看 Colab MCP Server，CLI 是给自动化和管道用的。这说明谷歌很清楚自己在做什么：CLI 不是给人聊天用的，是给机器干活用的。

目前只支持 Linux 和 macOS，Windows 用户先等等。安装推荐用 uv tool install google-colab-cli，比 pip 快。

所以下次有人说"Colab 就是个网页版 Jupyter"，你可以笑着告诉他：那是上周的事了。

---

[🌐 原始链接](https://mp.weixin.qq.com/s?chksm=f0a6021dc7d18b0bc210df4e475d669407af5101db6a5dec8a11add10eed40d563bf85a1d884&exptype=unsubscribed_card_recommend_item_heat_tlfeeds&ranksessionid=1782340110_2&req_id=1782342212142578&scene=169&mid=2247484143&sn=261eb3a3e4aea11f0a7e1ecb40b5a2d5&idx=1&__biz=MzYzMzg4NzEzMw==&sessionid=1782340109&subscene=200&clicktime=1782344677&enterid=1782344677&flutter_pos=18&biz_enter_id=5&jumppath=WAWebViewController_1782344495645,WAWebViewController_1782344496170,20020_1782344520289,1104_1782344673515&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b2b&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ/7SWPZtqjZi9e0Xo382iMBLTAQIE97dBBAEAAAAAACDkDMk8V2cAAAAOpnltbLcz9gKNyK89dVj0Z8IIkzS+rWC86rYKCE4dt6z6ofDu5V+EbLY6Fv2zoelC9TUPlmqoSoaat+gg9g4rcbnZwrSUTqNV+aUbEzTzKIg+ml71vssSNkjhqtAOViqA/WDy3ZSIidOEe5BiVawWulGZZrAYeOnesCMea9et5o/Hs2kAiXOqXWoAnfmsoTZYU3zjZvMF3Ss0rBmNghpvQKhb8QFWdc6FS3pSRjGUMAC4OPFbD2INiHOz0qg=&pass_ticket=eH8st0JxklTrWIGGuJ8QU3pr/WJlZZogOzj6Bgu5okliRq771Wuw1gTM6Xsd7aCk&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/bbfce6ee-2938-4ce9-9408-1c39bc018c94/bbfce6ee-2938-4ce9-9408-1c39bc018c94/)