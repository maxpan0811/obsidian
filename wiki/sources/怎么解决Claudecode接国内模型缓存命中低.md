---
title: 怎么解决Claudecode接国内模型缓存命中低
type: source
created: 2026-06-17
updated: 2026-06-17
tags: [综合]
source_path: 印象笔记管理工具/怎么解决Claudecode接国内模型缓存命中低.html
updated: 2026-06-27
updated: 2026-06-27
updated: 2026-06-27
updated: 2026-06-27
---

---
title: "怎么解决Claudecode接国内模型缓存命中低"
source: evernote
type: note
export_date: 2026-06-26
guid: d3d29c5a-e495-48f7-afa8-a9c7e7019c24
---

# 怎么解决Claudecode接国内模型缓存命中低

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzkxODYxOTc0Ng==&mid=224748...](https://mp.weixin.qq.com/s?__biz=MzkxODYxOTc0Ng==&mid=2247483886&idx=1&sn=dd60b713c9ccec59813b0610210a36fa&chksm=c1afd2e3f6d85bf552d185bd236444ac8c9cacb16f3535025c0f73f81f270e94c387398996bd&exptype=servicebox_1781522094676719&subscene=0&scene=288&clicktime=1781522140&enterid=1781522140&flutter_pos=1&biz_enter_id=5&ascene=56&devicetype=iOS26.5&version=18004a2f&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQdsjbPqt/ZSgxT9CTxCv8tBLTAQIE97dBBAEAAAAAAIiHFsd4tjMAAAAOpnltbLcz9gKNyK89dVj0OAUiXVp0YuGjL/WZmyD4d2hFtW75Z1w1MRfDDP/yu8dje7BQXv0F+mvE+OxEtCBGmRDQULM4A7mjIQb+XCCqOlSu3kiltEnWs4xKR9T46CGOc5tq3g6VHZIiF1N6EN/7gaHcQeobS3gNuexq077Uy0X4r3YCh4+hP3PgM/Qh/8CBsGI+RzpzcM6ei43ivbjZhusPOEGVrkfi/EJwgfCm5KqJUF0lEo5Zw0QZtnM=&pass_ticket=SoiKI/HEZjd8ONUVmZos6+6rK3oXsfEqCZVUochxnsOpI/1jw/PNB8nTdbqpe/Uk&wx_header=3)

![](attachments/b341a69253e4aee3.png)![](attachments/cfe4c83bd5014ad7.jpg)![](attachments/50ac8b23ab941daa.png)![](attachments/1e0af681194d31cd.png)

Claude Code接deep seekv4pro缓存命中只有60%，一句话修改可以直接提高缓存命中到95%。

跟着图片操作就行了，首先第1步在c盘里面用户文件夹找到【.claude】这个文件夹进去。

然后找到【.settings】这个json文件打开

在env这个大框里面复制这一行代码进去【"CLAUDE\_CODE\_ATTRIBUTION\_HEADER": "0"】，如果在最后复制，记得上一行要加逗号不然有语法错误。

修改后直接进文件夹运行claudecode，在deepseek后台就能看到命中率直接提上来了。

造成这个问题的原因是claudecode在2.1.36版本之后增加了一个随机请求头cch的hex字段，自家模型会跳过字段来识别内容，但外接模型会直接用这个随机字段建立哈希值，导致同样的上下文内容，下一轮对不上上一轮的缓存前缀hash，这部分的缓存命中直接归零。

解决原理是直接把关掉这个的代码复制到环境变量里面。

方法二是直接用国产针对性优化的agent【Reasonix】，一个国内大佬开发的工具，可以把deepseek的缓存命中优化到99%，这个工具开发的初衷就是长对话加低成本，但是如果只有成本，没有任务完成率还是不行，纯高频低智能业务降成本的话可以用这个。

#deepseek#内存优化#deepseek工具#Claudecode#AI#大模型

Like the Author

Close
