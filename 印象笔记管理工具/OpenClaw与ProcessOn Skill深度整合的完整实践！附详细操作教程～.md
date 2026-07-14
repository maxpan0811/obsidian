---
tags: [★★★★★]
---

# OpenClaw与ProcessOn Skill深度整合的完整实践！附详细操作教程～

---

来源：[打开原文](https://mp.weixin.qq.com/s/RGwjQrY1ofFenh31iPEmzA)

![](.evernote-content/9F32783C-22F3-44E9-BC98-413AE3D42C4F/07E7E3DC-2771-4E98-B428-A37978AF4AE6.png)

过去，画流程图是一项有门槛、重规范、需专业能力的工作，如今，它正逐渐变成一项可以直接交给AI完成的基础任务。

近期，ProcessOn上线了官方专属Skill——ProcessOn Diagram Generator，把它和OpenClaw组合使用，只需要一句话，它就能直接帮你把图生成。不是随便的草图哦，而是能直接放进工作文档、汇报PPT、论文中的专业图形！

如果你现在还在手动拖拽、连线、排版画流程图，这篇内容，大概率能帮你省下大把时间和精力。

接下来，我把如何安装OpenClaw、如何安装配置 ProcessOn Skill、如何使用ProcessOn Skill等方法整理给你，从0到1，直接上手。

01

OpenClaw和ProcessOn Skill

1.什么是OpenClaw小龙虾？

OpenClaw本质上不是一个普通的AI，而是一个可以帮你操作电脑的AI助手，和我们常用的只能聊天的AI不同，它不仅能聊天，还能帮你干活，多了一层能力。

比如，你对它说帮我做一张流程图、帮我整理文档，它会理解你的需求→调用对应的工具→自动执行→返回结果。

它就是一个会用工具的AI，而它真正厉害的地方在于可以调用各种Skill来扩展能力。

![](.evernote-content/9F32783C-22F3-44E9-BC98-413AE3D42C4F/25742C1F-E289-453C-BBD3-642216E4DB23.jpg)

OpenClaw使用场景图 ｜点击查看模板高清原图

2、什么是ProcessOn Skill？

在OpenClaw中，Skill是一个核心概念，可以简单理解为：

Skill=AI的“技能包/插件/专业能力模块”

它的本质是把复杂任务打包好，让AI一键调用，你不需要学工具、学操作、学流程，你只管提出问题和需求，AI能用“技能”帮你完成。

那么，ProcessOn Skill是什么呢？它是ProcessOn上线的官方专属Skill——ProcessOn Diagram Generator，你可以理解为把ProcessOn的画图能力，变成AI可以调用的一项技能。

它具体能帮你做什么呢？

当你在OpenClaw里安装了ProcessOn Skill之后，你只需要说：

帮我画一张XXX流程图

它就会理解你的需求→自动生成符合逻辑的图→调用ProcessOn生成图表→返回给你预览图、可编辑链接和DSL源代码。

ProcessOn Skill支持生成的图有流程图、时序图、架构图、ER 图、组织架构图、时间轴、信息图等，感兴趣的小伙伴往下看，马上给大家出详细的安装教程。

02

如何用OpenClaw和ProcessOn Skill画图？

在安装之前，一个安全风险提醒大家必看！！！

1、安全风险提醒！！！

1）OpenClaw一旦运行，将获得你办公电脑的极高控制权限，能够读取本地文件、通讯录等核心私密数据，对公司商业秘密与客户信息构成严重威胁，极易酿成大规模数据外泄事件，带来重大信息安全隐患。

2）某些操作执行后无法撤销，凡涉及修改、写入、删除等关键动作，请务必坚持“先预览、后确认”的原则，切勿让AI处于“全自动”运行状态，避免脱离人工监督。

3）使用建议：不建议在日常办公工作机上直接安装部署，优先在闲置测试设备上安全体验功能，待平台安全隔离、数据防护能力成熟完善后，再考虑接入真实办公协作环境。

4）怎么安全养虾？安全试用规范可参考（公开资料，仅供参考）：https://github.com/slowmist/openclaw-security-practice-guide/blob/main/README\_zh-CN.md

2、安装配置龙虾

主要通过3步就可以实现：安装龙虾→安装ProcessOn Skill→配置API Key

第一步：安装OpenClaw

目前，大家常用的安装方式有以下3种，你可以根据个人的情况进行选择。

![](.evernote-content/9F32783C-22F3-44E9-BC98-413AE3D42C4F/12A4FC84-65BE-4CD6-9547-627775C71BDB.jpg)

点击查看模板高清原图

第二步：安装ProcessOn Skill

部署好你的“小龙虾”后，可以为你的龙虾安装ProcessOn Skill，帮你干活生成各种图表！

1、和OpenClaw聊天，直接安装Skill

复制下面这段指令，粘贴到你和龙虾的对话输入框中，即可一键安装

请使用以下命令帮我安装Skill：

使用clawhub安装ProcessOn Diagram Generator Skill

![](.evernote-content/9F32783C-22F3-44E9-BC98-413AE3D42C4F/374E520B-81CE-4F68-9F45-AAC6A5D36D63.png)

如果提示clawhub限流、访问频繁，复制下面指令，粘贴到你和龙虾的对话输入框中，一键安装skill（安装相对慢，需耐心等待）。

npx skills add https://github.com/processonai/processon-skills.git --skill processon-diagram-generator --yes

2、在ClawHub、SkillHub、Github 技能商店下载安装Skill

1）在ClawHub的安装教程

Step1：进入ClawHub官网

Step2：搜索输入ProcessOn Diagram Generator

![](.evernote-content/9F32783C-22F3-44E9-BC98-413AE3D42C4F/9BACCB10-8D51-4327-BE6D-B97A0A67D08C.png)![](.evernote-content/9F32783C-22F3-44E9-BC98-413AE3D42C4F/4AF188A9-D6CD-4F2A-9D7B-64E525A3B6F2.png)

Step3：点击Download后即可下载ZIP技能包

![](.evernote-content/9F32783C-22F3-44E9-BC98-413AE3D42C4F/119DF91B-3BEB-474D-8664-A8E95E55F271.png)

Step4：将ZIP技能包发送给OpenClaw，即可帮你安装

补充：若OpenClaw没有上传文件入口，可将ZIP技能包拖动到桌面，输入指令安装

请帮我解压安装桌面上的processon-diagram-generator技能

2）在SkillHub的安装教程

Step1：进入SkillHub官方网站

Step2：搜索输入ProcessOn流程图

![](.evernote-content/9F32783C-22F3-44E9-BC98-413AE3D42C4F/5C5BC4A2-A2EF-49A8-8E8E-971332FB70A6.png)

Step3：找到ProcessOn官方技能包

![](.evernote-content/9F32783C-22F3-44E9-BC98-413AE3D42C4F/92596883-9718-4CCC-9F57-E6A8DDDFAF2B.png)

Step4：根据SkillHub的提供的3种安装方式，选择安装

![](.evernote-content/9F32783C-22F3-44E9-BC98-413AE3D42C4F/DF934D29-048E-4E38-9686-83F89BC0C9B5.png)

3）在Github的安装教程

Step1：进入ProcessOn技能仓库，https://github.com/processonai/processon-skills.git

Step2：点击Download ZIP下载技能

Step3：将ZIP技能包发给OpenClaw安装

![](.evernote-content/9F32783C-22F3-44E9-BC98-413AE3D42C4F/9D5E65E2-E19D-4D9B-AEAB-8E51F1B85C30.png)

第三步：配置API Key

为什么还要配置一个key呢？许多小伙伴可能有这个疑惑，这一步的本质就是授权AI帮你调用ProcessOn的能力，简单说，它和登录账号需要密码，用会员服务需要账号一个道理，如果不配置，使用ProcessOn Skill就差临门一脚，Skill无法真正开始工作。我们继续～

成功安装好ProcessOn Skill后，你将进入以下类似界面：

![](.evernote-content/9F32783C-22F3-44E9-BC98-413AE3D42C4F/BA3E19C3-2C90-4785-B7D0-5C0D5A5473C9.png)

具体获取密钥步骤如下：

Step1：访问网址https://smart.processon.com/user，扫码注册登录

Step2：创建你的专属令牌密钥

![](.evernote-content/9F32783C-22F3-44E9-BC98-413AE3D42C4F/93B54014-0607-4FD6-8F3C-8C9CA2E53D2A.png)

Step3：复制粘贴密钥到OpenClaw输入框，发送后可直接配置

![](.evernote-content/9F32783C-22F3-44E9-BC98-413AE3D42C4F/CA4E494B-56E2-498B-95C0-56DA52756DAF.png)

稳健方法：复制粘贴你获得的密钥替换下方指令中的“API Key”，再发送给OpenClaw

export PROCESSON\_API\_KEY=你的"API Key"

![](.evernote-content/9F32783C-22F3-44E9-BC98-413AE3D42C4F/42240DDD-CA2B-4B27-953C-6748528A9A55.png)

配置成功后，即可正式调用ProcessOn Skill生成可编辑可视化图表啦！

03

如何用ProcessOn Skill一键生图？

成功安装ProcessOn Skill后，只需要在OpenClaw输入类似下面的指令：

请帮我生成一张专业简洁的标准产品登录流程图，含正常流程、异常处理、第三方登录、忘记密码分支，要求专业规范，结构化展示。

OpenClaw就会自动调用ProcessOn AI，生成符合你需求的结构清晰的流程图和可编辑网址链接。

案例：生成一张APP账号注册流程图

请帮我生成一张专业简洁的APP注册流程图，包含输入验证、验证码校验、密码设置、信息完善等关键步骤。

返回结果：

·预览图片链接：点击链接可查看预览图

·可编辑图片链接：点击链接可进入编辑界面

·DSL源代码：复制DSL代码粘贴到上方“可编辑链接”，点击渲染即可自由编辑

![](.evernote-content/9F32783C-22F3-44E9-BC98-413AE3D42C4F/12EAA4B1-C5CF-451C-B5BA-ED1DDFB54A9A.png)

效果图展示：

![](.evernote-content/9F32783C-22F3-44E9-BC98-413AE3D42C4F/7104E172-2933-4A87-949C-DB9C0B52EE90.jpg)

以上就是本周分享的内容，感兴趣的大家赶紧去用起来吧～

现在，工具的使用门槛在不断降低，所以，在职场真正能拉开差价的不再是会不会用的问题，而是怎么用，用工具解决什么的问题，这中间的差距会让人和人之间拉开巨大的鸿沟。

用OpenClaw调用Processon Skill，流程图的绘制变成了即时生成，本质上是把时间还给思考本身，让大家把更多时间和精力放在逻辑、结构和决策上，这是我们一直致力在做的事情。希望今天的分享对大家有帮助～

![](.evernote-content/9F32783C-22F3-44E9-BC98-413AE3D42C4F/3B493307-D211-4F48-AB1F-BC2EB348B52A.gif)![](.evernote-content/9F32783C-22F3-44E9-BC98-413AE3D42C4F/3B493307-D211-4F48-AB1F-BC2EB348B52A.gif)

[📎 在印象笔记中打开](evernote:///view/207087/s1/eccca3ad-5d37-4211-b22e-39de42a951b6/eccca3ad-5d37-4211-b22e-39de42a951b6/)