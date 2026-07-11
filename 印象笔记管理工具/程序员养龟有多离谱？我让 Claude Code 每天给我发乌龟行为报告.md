# 程序员养龟有多离谱？我让 Claude Code 每天给我发乌龟行为报告

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzU4Mjg3MDAyMQ==&mid=224761...](https://mp.weixin.qq.com/s?__biz=MzU4Mjg3MDAyMQ==&mid=2247611689&idx=1&sn=377ba9af569af2dfb2e26d4f609bf1ae&chksm=fc805fb897eb54782ae3c2530c5037f977ac3f486d5114a58af5c2dd082e5e51d94531e3e5ce&scene=90&xtrack=1&req_id=1776007940938855&sessionid=1776007097&subscene=93&clicktime=1776008152&enterid=1776008152&flutter_pos=12&biz_enter_id=4&ranksessionid=1776007941&jumppath=20020_1776007993713,WCWebImageBrowserViewController_1776008087901,20020_1776008092735,1104_1776008146325&jumppathdepth=4&ascene=56&devicetype=iOS26.4&version=18004635&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ2gwzJ3Rw4qRwboM4v3SichLTAQIE97dBBAEAAAAAACmBCNEGHxEAAAAOpnltbLcz9gKNyK89dVj0/c5gqDm6BN9uzQcFKJ0Ca+litNzIB7d7z+WltfxXj8hJmjSU8wMTa48WDOBhe1PmkOSHWv7poQ9uaH/9FX1Tgm5r1UpJ0q4xaY/8U2D4pmjvUqWL0Qp9EsmefPH44KfuWlYZCNIEhHR1tcF3SiOLTq9FAqontQ9TfE9hsoa6OSC+ZHvHHvxQLj9U6JZzYoIIEijX/pqMqKCbKNw2iK0656jLMSMcDIMJZjiQbYk=&pass_ticket=D61PUxfOJR6ZWPmg4opy/q4gxhfiqjjca5IV2ze8QNm7hdZHCF9CO51o4BF4DVVF&wx_header=3)

程序员养龟有多离谱？我让 Claude Code 每天给我发乌龟行为报告
====================================

Original叶水水 少数派

编注：我们会不定期挑选 Matrix 的优质文章，展示来自用户的最真实的体验和观点。 文章代表作者个人观点，少数派仅对标题和排版略作修改。

▍背景
---

最近对养龟产生了兴趣，家里陆续来了 6 只：草龟、地图龟、西非侧颈龟、三只黄喉拟水龟。龟缸上装了 TP-Link 摄像头，群晖 NAS 跑着 Surveillance Station 24 小时录像，水温传感器和加热棒也配齐了。

东西都有，但用起来全是分散的。看温度一个 APP，看摄像头另一个，加热棒手动开关。录了几百 GB 的视频从来没人翻。

刚好最近一直在用 Claude Code 折腾家里的 Home Assistant，上周才用它逆向了空气净化器的 API。这次想试试，纯靠对话，能把养龟这件事做到什么程度。

▍现在是什么样的
--------

打开手机 HA，龟缸的东西全在一个页面里，摄像头画面、乌龟活动状态、加热棒功率和用电量、水温湿度趋势。温度异常会聊天软件推送。

每半小时还会收到一段精华视频和一段 AI 写的行为分析：

![](.evernote-content/2A95C1B0-BBD4-44E8-B45B-C58BCADD7D55/90FDE77D-675A-45C3-BD00-19BCC4700297.jpg)![](.evernote-content/2A95C1B0-BBD4-44E8-B45B-C58BCADD7D55/92B9DC2A-655F-4198-BEF7-F5754519179B.jpg)

整个过程我没写一行代码。仪表盘、自动化、监控脚本、视频处理、AI 分析，都是和 Claude Code 聊出来的。

▍HA 仪表盘和自动化
-----------

跟 Claude Code 说的第一句话大概是「把乌龟摄像头加到 HA 仪表盘上」。

然后就是不停地提需求：

「加热棒的功率和用电量也显示出来」

「水温做个仪表盘，标出适宜温度区间」

「加个 24 小时和 7 天的水温趋势图」

「温度太低或太高给我发消息」

它每次直接改 HA 的配置文件和仪表盘数据，改完重启，我刷新手机看效果。不满意继续说，满意就下一个。跟一个懂 HA 的人聊天没什么区别，我不用管 YAML 怎么写、automation 怎么配。

![](.evernote-content/2A95C1B0-BBD4-44E8-B45B-C58BCADD7D55/46061CAC-81C0-4C8D-9C89-94E5FC6AB2E3.jpg)![](.evernote-content/2A95C1B0-BBD4-44E8-B45B-C58BCADD7D55/46061CAC-81C0-4C8D-9C89-94E5FC6AB2E3.jpg)

左：加热棒 7 天功率、水温湿度仪表盘；右：24 小时水温湿度趋势，带温区标注

水温趋势图标了过冷/偏冷/适宜/偏热/过热的区间。加热棒功率曲线能看出工作规律，比如图上 4 月 7 号之前加热棒是关着的，之后才开始工作。

自动化跑了温度过高和过低两条告警。温度异常聊天软件几分钟就能收到。

▍AI 活动监测
--------

仪表盘能看数据了，但龟在干嘛，水温曲线看不出来。

我问 Claude Code 能不能做个活动监测。它的方案：每 5 分钟从 SS 录像里抽帧对比，检测画面变化判断龟有没有在动。处理放在家里闲置的 Mac 16"（M1 Max 64GB）上，NAS 只管存录像。

### ▍抓帧对比

录像在 NAS，Mac 通过 SSH 读取。一开始传整个 100MB 的 mp4，12 秒。后来只传文件头 5MB（mp4 的 moov atom 在文件头，够解码出帧），降到 2 秒。

NAS 录像 → ssh head -c 5MB → OpenCV 读帧 → 灰度+高斯模糊 → 像素差值

变化超 2% 就算「活跃」，结果推到 HA sensor。

### ▍精华视频

「有活动时直接发视频给我」

Claude Code 做了每 30 分钟的精华视频。检测到活跃的时间点，从对应录像截取片段拼在一起。

一个细节：一开始用 OpenCV 逐帧重编码，25 秒出一个片段，画质还糊。后来装了 ffmpeg 用 `-c:v copy` 直接裁切，2 秒搞定，1080p 原始画质。工具选对了差十倍。

### ▍本地大模型看龟

精华视频解决了「看什么」。但我还想知道每只龟在干嘛。

我问有什么办法识别不同的乌龟。Claude Code 列了几种：OpenCV 颜色轮廓检测、YOLO、深度学习个体识别、Vision LLM。6 只龟品种差异大，草龟最小深色、地图龟最大有花纹、西非侧颈脖子侧扁、小青体型差不多，直接用视觉大模型就行，不用训练。

试了 Gemini API 配额不够。我说能不能跑本地的。最后用 Ollama 跑 Gemma 4（8B Q4 量化），M1 Max 64GB 没什么压力。

分析分两步。先逐帧：从 30 分钟录像均匀抽 30 帧，每帧单独让 Gemma 描述看到了什么。再汇总：30 条描述拼一起，让 Gemma 总结这半小时。

prompt 改了好几轮。一开始让它「分析哪只最活跃哪只最安静」，输出很八股。我说不关心这个，改成「像朋友聊天一样说说」，输出就对味了。

![](.evernote-content/2A95C1B0-BBD4-44E8-B45B-C58BCADD7D55/93E54DEC-CA9C-46C4-8643-2ECAD1B6487E.jpg)

摄像头视角。右上角是晒背台，中间红蘑菇是装饰。能看到龟在晒背台上叠罗汉，它们特别爱干这个。

▍架构
---

HA 管数据采集、展示、告警。Mac 管视频处理和 AI 推理。两边通过 HA REST API 连起来。launchd 定时跑，开机自启。

![](.evernote-content/2A95C1B0-BBD4-44E8-B45B-C58BCADD7D55/5041FDEA-CAF0-4FF4-ADB5-E35588AAA7A1.png)

▍关于没写代码
-------

系统里有 Python 脚本（OpenCV 图像对比、ffmpeg 调用、Ollama API、Telegram 通知）、HA 的 YAML 配置（sensor、automation、lovelace dashboard）、launchd 定时任务，代码量不算少。

但我确实一行都没手写。

每一步都是对话完成的。我说「把摄像头加到仪表盘」，它改 lovelace JSON。说「温度告警发聊天软件」，它写 automation YAML。说「用本地模型分析龟缸画面」，它装 Ollama、拉模型、写脚本、配定时任务。

我干的事更像是产品经理：说需求、看效果、给反馈。

不是说技术不重要了。这套系统里有不少技术判断，比如只传 mp4 头部 5MB 而不是整个文件、用 ffmpeg stream copy 而不是重编码、逐帧分析再汇总而不是多图一起扔给模型。只是这些判断现在 AI 也能做。

▍成本
---

几乎为零。硬件家里都有，软件全开源，AI 推理跑本地。Mac 每月多费大概 3 块钱电。

养龟是个慢节奏的事。但每天翻翻聊天软件的报告，看看谁又霸占了晒背台、谁偷偷换了个位置，比蹲在缸前看半天有意思多了。

原文链接：https://sspai.com/post/108453?utm\_source=wechat&utm\_medium=social作者：叶水水

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzU4Mjg3MDAyMQ==&mid=2247611689&idx=1&sn=377ba9af569af2dfb2e26d4f609bf1ae&chksm=fc805fb897eb54782ae3c2530c5037f977ac3f486d5114a58af5c2dd082e5e51d94531e3e5ce&scene=90&xtrack=1&req_id=1776007940938855&sessionid=1776007097&subscene=93&clicktime=1776008152&enterid=1776008152&flutter_pos=12&biz_enter_id=4&ranksessionid=1776007941&jumppath=20020_1776007993713,WCWebImageBrowserViewController_1776008087901,20020_1776008092735,1104_1776008146325&jumppathdepth=4&ascene=56&devicetype=iOS26.4&version=18004635&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ2gwzJ3Rw4qRwboM4v3SichLTAQIE97dBBAEAAAAAACmBCNEGHxEAAAAOpnltbLcz9gKNyK89dVj0/c5gqDm6BN9uzQcFKJ0Ca+litNzIB7d7z+WltfxXj8hJmjSU8wMTa48WDOBhe1PmkOSHWv7poQ9uaH/9FX1Tgm5r1UpJ0q4xaY/8U2D4pmjvUqWL0Qp9EsmefPH44KfuWlYZCNIEhHR1tcF3SiOLTq9FAqontQ9TfE9hsoa6OSC+ZHvHHvxQLj9U6JZzYoIIEijX/pqMqKCbKNw2iK0656jLMSMcDIMJZjiQbYk=&pass_ticket=D61PUxfOJR6ZWPmg4opy/q4gxhfiqjjca5IV2ze8QNm7hdZHCF9CO51o4BF4DVVF&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/52fe9eeb-ea57-4c6b-8655-e8bbb851867b/52fe9eeb-ea57-4c6b-8655-e8bbb851867b/)