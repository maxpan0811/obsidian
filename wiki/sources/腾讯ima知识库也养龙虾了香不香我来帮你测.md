---
title: 腾讯ima知识库也养龙虾🦞了？香不香，我来帮你测！
type: source
created: 2026-06-14
updated: 2026-06-14
source_path: 印象笔记管理工具/腾讯ima知识库也养龙虾🦞了？香不香，我来帮你测！.md
tags: [印象笔记, 其他]
updated: 2026-06-27
updated: 2026-06-27
updated: 2026-06-27
updated: 2026-06-27
---

---
title: "腾讯ima知识库也养龙虾🦞了？香不香，我来帮你测！"
source: evernote
type: note
export_date: 2026-06-26
guid: 415536b3-9ead-441c-9fce-062ea9485878
---

# 腾讯ima知识库也养龙虾🦞了？香不香，我来帮你测！

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzI2NzM4MTQwMg==&mid=224749...](https://mp.weixin.qq.com/s?__biz=MzI2NzM4MTQwMg==&mid=2247496131&idx=1&sn=65be3a54690f9704412e5691071457c1&chksm=eb1dc976b7e261d8e74cc2e476f95da5c78e1c4bda9d5e2ea14bd588cae0883e6eb7b89045ae&scene=90&xtrack=1&req_id=1779264918928133&sessionid=1779265009&subscene=93&clicktime=1779265014&enterid=1779265014&flutter_pos=0&biz_enter_id=4&ranksessionid=1779264918&jumppath=1001_1779265004645,1102_1779265005958,1001_1779265008870,1104_1779265010584&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=1800492d&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQfmzv20bfuLCKVlfAlGcKGxLTAQIE97dBBAEAAAAAAB33IiOMju0AAAAOpnltbLcz9gKNyK89dVj09JxrfvkXSQtG5Z24Irt8eBhMMj2o9MWEGK2EsswqBn0yx3MwWdGGPgV48z2v+Vv/tXNXm7OQBj1y+r6zmH5O60KgHzPPvDydn40wdTHPkq5oxdSrmf8GtAgUTjND48X+g1UYqN2qW0Eg/sxhgbHB0NU8GU+FdKcTspeK2hYBu+eamdtsgB1hs72OECgDPfkre3XboAb2RG7SK+pLRUm9hfrXD9WfvEgP8+l0/z0=&pass_ticket=CWO9op/1RyajkZSfUIxfuZRQ9DktNnzleL6zSX0FGwW3XTrZrwNh21rIghecyHVP&wx_header=3)

OriginalDracoVibeCodingDraco正在VibeCoding

没有Agent的知识库不是好龙虾！

这不，腾讯ima的Agent（copilot）也来了～

今天快测快评一下ima copilot的配置和使用方法：

---

## 基础配置

点击首页上“领养专属copilot”按钮（或者左侧边栏的熊猫头像）：

![](attachments/e409407117dc3d26.png)

点击“立即体验”：

![](attachments/e2a390713a83c418.png)

进入copilot创建页，填个名字选个形象点击“创建”按钮就行：

![](attachments/35c1893bd78fce6b.png)

一键创建完成后有个简单自我介绍（我这只叫“Panda君”）：

![](attachments/594389b3f3f1d018.png)

对话框选项中可以看到模型处于“默认”模式：

![](attachments/1cd2a01b4dbf0241.png)

点击“+添加自定义大模型”按钮可以看到具体是哪个模型（默认是GLM-5.1）：

![](attachments/67128c281e636b7c.png)

官方提供3种大模型可选：

![](attachments/f805a9bd61f331c6.png)

也可以点击“添加模型”来添加自定义模型，支持如下：

DeepSeek、Kimi、智谱、MiniMax、混元、千问

![](attachments/3dce994b12b67e7a.png)

我先把deepseek-v4-pro给配上（需要DeepSeek开放平台的API KEY，其他厂家也一样）：

![](attachments/d1bf49f771302378.png)

然后切回主界面选上deepseek-v4-pro：

![](attachments/a5912d0199d398fd.png)

再让我们看一下其他相关信息和配置~

•点击Skills按钮，可以看到官方默认提供了4个skills，等会儿我们在“使用场景”章节中来看如何使用

![](attachments/f11211f1255fea88.png)

•弹窗中还有“用量统计”，可以看到官方默认赠送500个算力（每天签到可以领100算力），当然，如果你使用的是自定义的模型，则基本不消耗算力：

![](attachments/e51d49a86c67608b.png)

•“记忆管理”窗口中是 SOUL.md、USER.md、MEMORY.md、AGENT.md 这四个文件，我的读者基本都比较熟悉OpenClaw或者Hermes了，就不展开详细介绍了；需要的时候，你可以在这里手动修改对应的文件～

所以，ima Copilot背后大概率是个根据OpenClaw进行了魔改的实例

![](attachments/c535d483c4e90bae.png)

## 使用场景

首先，我让ima copilot列出所有我拥有的知识库，copilot调用相关skills很快列出了全集：

![](attachments/a306a80f1f90ed46.png)

然后，我让它详细分析了“1000个思维模型”中的一篇几万字的长文，其中包含了79个思维模型：

![](attachments/d66ff16c1b3a1b76.png)

由于这篇文章是PDF格式的，所以它给自己的虚机安装了PyPDF2库之后才进行的内容的解析～

没多久，果然把全部79个思维模型都解析出来，还进行了分类：

![](attachments/f02ebc78df91be0f.png)

接下来，我给了一个重活儿：

在知识库里创建79个文件，然后为每个思维模型撰写一篇1万字以上的科普文章！

![](attachments/db526ea74e111a3c.png)

可能这个活儿实在太大了，所以deepseek-v4-pro在那自己琢磨了3分钟，才把具体的执行计划确定下来~

![](attachments/8312e4cdd20f46ef.png)

然后，copilot同时启动了4个子代理，每个子代理负责20个思维模型科普文章的撰写：

![](attachments/7d98bb334ed82ac2.png)

你可以在它撰写文章的过程中点击特定的文章，文章会在右侧打开（现在好像所有Agent的中间物料区都约定俗成放在右侧栏了吧？）

![](attachments/f0c8396d90805a90.png)

顺便，通过它的思维过程，果然，应该是OpenClaw没跑了～ “spawn sub-agent”这个是OpenClaw的terminology！

![](attachments/7b35950a722a08eb.png)

这个任务大概跑了有1个多小时（这个任务的确很重啊），然后你就看着每个sub-agent开始交付自己的任务：

![](attachments/7da51994fa31ef68.png)

![](attachments/e7cb798454e8f7e9.png)

## 写在最后

综合测下来，结论是：ima的确给自己身体里塞了只龙虾🦞OpenClaw（为啥不塞Hermes？惯性了？）

但是，我觉得在ima里面用copilot不如直接把ima skills安装到你已经在日常使用的Hermes/OpenClaw里！

具体安装方法可以访问：https://ima.qq.com/agent-interface

我之前也写过一篇文章来介绍：[喜大普奔！OpenClaw🦞腾讯ima知识库skills上线啦！](https://mp.weixin.qq.com/s?__biz=MzI2NzM4MTQwMg==&mid=2247494918&idx=1&sn=52aad2e73d08fa834257ad8abf931958&scene=21#wechat_redirect)

![](attachments/0563683135e4bb0f.png)

这样，你甚至可以在飞书/钉钉/企微 里操控ima知识库的内容，这样才是最香的吧？！

结论：

- 如果你已经在用Hermes/OpenClaw并且已经打开了ima skills，那上面评测的feature对你没啥用！就别浪费时间了！

- 如果你不是Hermes/OpenClaw这类Agent的用户，并且你是ima知识库的重度用户，那么这个feature的确比原有的ima ChatBot能力要强非常多！

根据自己的情况做出选择吧～ 

Have fun！
