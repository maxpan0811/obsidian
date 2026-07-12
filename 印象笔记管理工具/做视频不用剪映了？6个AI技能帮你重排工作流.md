# 做视频不用剪映了？6个AI技能帮你重排工作流

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzAxNDIzNzc4MQ==&mid=264939...](https://mp.weixin.qq.com/s?__biz=MzAxNDIzNzc4MQ==&mid=2649399525&idx=1&sn=1d210a7d724a247b00d2dc2c76c3eca8&chksm=82cede53817c0148409d93743923237e6829ada72788449061f4b1fec6b6748833d5b7924a8c&scene=90&xtrack=1&req_id=1783824007497709&sessionid=1783823291&subscene=93&clicktime=1783824099&enterid=1783824099&flutter_pos=40&biz_enter_id=4&ranksessionid=1783824007&jumppath=WAWebViewController_1783824056541,WAWebViewController_1783824057046,20020_1783824076004,1104_1783824076915&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b38&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQirE0wAvhk0nI+iePvfH4bRLTAQIE97dBBAEAAAAAACQWC4RuSLQAAAAOpnltbLcz9gKNyK89dVj0JDtLQ0VRxjfWm9D4d8x7cOYONDmSCJ2c8EUMiGm1prEPa4tUKu5tbNfQg8A8wz920mHsdoqHc+PLYYPtG+RJzJaFHrNbWP0q9a/d5uMsxSxSrOeHhMxZu+fI0ZFEZYcB3W3ZyXw3O8cXgYiRBPMqiTv0CnXw7Oz2ynaK6cybxsgONfJoiQs0ZgPTcJAabFRf3BfJjzb5MeNM6FPxLcC5Rwn82vfqmLtmEM2Qq6k=&pass_ticket=NWJ3AXxnskjzSRupyxBeE7LRUkdJM+ugzfHAkSxu9Tpyyssb0FlN3b1UAsfL+9AJ&wx_header=3)

做视频不用剪映了？6个AI技能帮你重排工作流
======================

Original洞见AIIT开发者生活

做视频最费时间的，从来不是剪辑本身，而是脚本、素材、字幕、转码、批量导出——每一步都在重复消耗你的耐心。

你可能开着剪映、PR、字幕软件、压缩工具来回切半天，一条片子还没成型。

如果你手里已经有WorkBuddy、 Claude Code、Codex等 这类 AI 编程 Agent，可以换个思路：

**别再指望 AI 一键生成大片。真正省事的做法，是给 AI 装上视频技能（Skill），让它替你处理流程里那些重复到麻木的活。**

下面 6 个，覆盖了图文转视频、素材粗剪、字幕转码、批量出片到科普动画的大部分场景。**每个都附了可以直接复制的提示词**，你不用全装，对号入座就行。

**1. FFmpeg：最基础，也最该先装**

如果只能先学一个，就是它。压缩、裁剪、格式转换、提取音频、批量加字幕，视频处理的脏活累活它全包。500MB 压到 50MB、横屏转竖屏、20 条视频批量加字幕，交给它最稳。

直接把这段丢给 Agent：

```
请用 FFmpeg 把当前文件夹里的 mp4 视频批量压缩成 1080p，  
保留清晰度，尽量减小体积，输出到 compressed 文件夹。
```

它不是最惊艳的，但一定是你用得最多的。

**2. Video-Use：真人素材、口播剪辑最贴近**

有一堆口播、访谈、录屏、活动素材想剪成成片，它最合适。思路是：素材丢进文件夹，让 Agent 读取、分析、粗剪，最后吐出 final.mp4。

```
请把这个文件夹里的素材剪成一条 60 秒短视频。  
要求：1. 删除停顿和废话；2. 保留信息密度高的片段；  
3. 加中文大字幕；4. 节奏适合小红书/抖音；5. 输出 final.mp4。
```

说句实话：素材本身声音乱、没重点，AI 也救不了。它管粗剪和整理，不替你当导演。

**3. Remotion：固定栏目、批量出片真香**

它用 React 做视频，听不懂没关系，记住一句：适合模板化、批量化、结构固定的视频。每日 AI 快讯、每周工具榜、片头片尾、数据可视化——做好一个模板，后面换数据换文案就能批量生成。

```
用 Remotion 做一个 30 秒的固定栏目视频模板。栏目名：AI 工具日报。  
画面包含：1. 标题页；2. 今日 3 个工具；  
3. 每个工具一句话介绍；4. 结尾关注引导。  
要求后续可以替换数据批量生成。
```

如果你做的是"每天长得差不多、内容不同"的片子，它能帮你省下大把时间。

**4. HyperFrames：图文转视频、自媒体最顺手**

它不走传统剪辑，而是用 HTML、CSS、JS 这类网页技术生成视频。以前是拖时间线，现在是用代码描述画面。产品介绍、知识卡片、AI 工具推荐这类无真人出镜的解释视频，它做出来像"设计稿动起来"。

```
使用 HyperFrames，帮我做一个 30 秒的 AI 工具介绍视频。  
风格：科技感、深色背景、字幕清晰。  
结构：1. 开头提出痛点；2. 中间展示 3 个功能点；3. 结尾给一句总结。
```

做公众号、小红书、SaaS 介绍的人会爱它；但要剪真人素材，它不合适。

**5. Manim：数学、科技、科普动画专用**

想做"3Blue1Brown 式"的解释动画，就是它。公式推导、算法可视化、AI 原理演示都在射程内。

```
请用 Manim 做一个 45 秒的科普动画。主题：什么是神经网络。  
要求：1. 用圆点和连线表示神经元；2. 展示输入层、隐藏层、输出层；  
3. 用简单动画解释权重变化；4. 字幕用中文；5. 风格简洁，适合小白理解。
```

记住它的定位：它不是剪辑工具，是解释型动画工具。做科技科普的人值得收，纯口播博主用不上。

**6. OpenMontage：想把整条流水线串起来**

前面几个各管一段，它更像一套"视频生产系统"：一个选题进去，脚本、分镜、素材、配音、字幕、成片方案一条龙拆出来。

```
帮我做一个 60 秒的视频，主题：为什么普通人要学习 AI 自动化。  
要求：1. 先生成视频脚本；2. 再拆分镜；3. 规划画面素材；  
4. 加旁白和字幕；5. 最后输出成片方案。
```

但它偏工程化，通常要配 Python、Node.js、FFmpeg、API Key，小白别一上来就碰。

**不知道选哪个？照场景对号：**

压缩转码加字幕选 FFmpeg；真人素材粗剪选 Video-Use；固定栏目批量选 Remotion；图文转视频选 HyperFrames；科普动画选 Manim；完整流水线选 OpenMontage。

**入门顺序**：先 FFmpeg（最实用），再 Video-Use（最像真剪辑），然后 Remotion（适合批量），最后碰 HyperFrames、Manim、OpenMontage。

想上手的话，两条命令先试起来：

```
npx skills add heygen-com/hyperframes  
npx skills add remotion-dev/skills
```

动手前备好 Node.js、Git、FFmpeg，再加一个 AI 编程 Agent，部分工具还要 Python 或 API Key。Windows 用户认准项目 README 里的 PowerShell 命令，别硬抄 macOS 那套。

最后一句实话：这 6 个技能不会让你装完就变高手。**AI 替不了你的审美，也替不了你的选题；它替你扛的，是那些重复、繁琐、消耗耐心的流程。** 门槛降下来之后，剩下的好内容，还得你自己长出来。

以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～。

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzAxNDIzNzc4MQ==&mid=2649399525&idx=1&sn=1d210a7d724a247b00d2dc2c76c3eca8&chksm=82cede53817c0148409d93743923237e6829ada72788449061f4b1fec6b6748833d5b7924a8c&scene=90&xtrack=1&req_id=1783824007497709&sessionid=1783823291&subscene=93&clicktime=1783824099&enterid=1783824099&flutter_pos=40&biz_enter_id=4&ranksessionid=1783824007&jumppath=WAWebViewController_1783824056541,WAWebViewController_1783824057046,20020_1783824076004,1104_1783824076915&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b38&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQirE0wAvhk0nI+iePvfH4bRLTAQIE97dBBAEAAAAAACQWC4RuSLQAAAAOpnltbLcz9gKNyK89dVj0JDtLQ0VRxjfWm9D4d8x7cOYONDmSCJ2c8EUMiGm1prEPa4tUKu5tbNfQg8A8wz920mHsdoqHc+PLYYPtG+RJzJaFHrNbWP0q9a/d5uMsxSxSrOeHhMxZu+fI0ZFEZYcB3W3ZyXw3O8cXgYiRBPMqiTv0CnXw7Oz2ynaK6cybxsgONfJoiQs0ZgPTcJAabFRf3BfJjzb5MeNM6FPxLcC5Rwn82vfqmLtmEM2Qq6k=&pass_ticket=NWJ3AXxnskjzSRupyxBeE7LRUkdJM+ugzfHAkSxu9Tpyyssb0FlN3b1UAsfL+9AJ&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/6d1a8c42-fd6d-4282-822c-57b64d185836/6d1a8c42-fd6d-4282-822c-57b64d185836/)