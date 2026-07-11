# AI大佬在用的LLM Wiki是什么？

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MjM5NjE2NTUwMQ==&mid=224748...](https://mp.weixin.qq.com/s?__biz=MjM5NjE2NTUwMQ==&mid=2247484212&idx=1&sn=4c1f9358ef131706346689e1b30020bc&chksm=a7edf634bce2ce1965706fde4c49a4d6aa14581fef86ee146a149cbc2aeaf43eb5f73c25b4a9&scene=90&xtrack=1&req_id=1776225147031847&sessionid=1776225247&subscene=93&clicktime=1776225256&enterid=1776225256&flutter_pos=0&biz_enter_id=4&ranksessionid=1776225147&jumppath=50183_1776225206833,1101_1776225238996,1001_1776225241104,1104_1776225248148&jumppathdepth=4&ascene=56&devicetype=iOS26.4.1&version=18004637&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ9fXYsiYvWUBGnN28FBZXVxLVAQIE97dBBAEAAAAAAPDXEuBzKmoAAAAOpnltbLcz9gKNyK89dVj0N0883OC9d/FG4aGeBMGWjVa7M9tZre75XPQloQ744X1IXkUs31z/ylIcFWQx0ufSswAeqAh0BWCGRt+hv5rNSsJ0HDNnbnig2sGMLDGneo/rbBG9RYCvaGb/cCh8f88hcVGPIyW3gaR2vvWl/YUfGtl0nRShvkv55xG+cNGt1KjVpmGlFCZ9vqitfliUmqblMxTsWsbSmG1n5z3n+0FLPyqWhdcACSUWXxdb+E7QLg==&pass_ticket=Y9PxRAAwP0kJWNbpo0VDyRNSxqNB2v4mnNihRy2RZ4k8jhtYtKt/qQmsBBPoLTW3&wx_header=3)

![](.evernote-content/2F4ADE09-1791-4323-B44D-189179F9A66F/7441C387-9AF3-419A-A491-E825943EBFBA.png)![](.evernote-content/2F4ADE09-1791-4323-B44D-189179F9A66F/DFC92708-8FA2-40DC-B766-9EBD2F07B84E.png)![](.evernote-content/2F4ADE09-1791-4323-B44D-189179F9A66F/FC8187F2-7ACA-4198-9B26-2E1B7205179C.png)![](.evernote-content/2F4ADE09-1791-4323-B44D-189179F9A66F/97FF9B38-0ACA-42F8-9140-FB962AD27EE3.png)![](.evernote-content/2F4ADE09-1791-4323-B44D-189179F9A66F/FB912BA0-583F-47B4-A4AB-3C9F2E82E31D.png)![](.evernote-content/2F4ADE09-1791-4323-B44D-189179F9A66F/0616600A-2FDC-40F2-95BB-903A801A50D3.png)![](.evernote-content/2F4ADE09-1791-4323-B44D-189179F9A66F/22B68C08-F1AD-4081-900F-48F75162191F.png)![](.evernote-content/2F4ADE09-1791-4323-B44D-189179F9A66F/D79B3D9C-05F4-48B8-872D-8D9AC7186EB9.png)

在知识目录结构的主题下面，很多人在讨论Karpathy的知识管理体系思路，最近学习了下，初步总结如下：

首先是文件夹的三层体系：

raw/（原始资料层）

1、存放所有原始来源：网页文章、PDF、会议纪要、读书笔记、播客转录稿

2、核心原则：只读不修改（这是知识的"水源"，不可污染）

3、格式可以是 Markdown、TXT、PDF 路径引用

wiki/（知识沉淀层）

1、存放 AI 整理后的知识页面：概念解释、人物页面、主题总结、对比分析

2、每个页面聚焦一个主题

3、包含内部链接，连接相关页面形成知识网络

logs/（索引与日志层）

1、 index.md：整个 Wiki 的目录索引

2、log.md：按时间记录每次知识摄入的变更历史

三层体系解决了我们资料存储时需要思考文件夹架构的问题

按照目前的方式，我们完全可以直接将所有的原始资料全部丢到一个原始资料层文件夹；

wiki模块更像是针对原始资料进行二次处理，吸收转化为互为链接的知识体系，便于我们可以随时查看；

索引与日志层，则更像是一个规则、展示和维护界面，确保摄入工作流和查询工作流的正常运转。

这个是近期学习的一些感受，最近在尝试使用这个方法搭建一个基于巴菲特股东信以及演讲的知识库，目前搭建的七七八八了，看接下来应用的情况，觉得很有意思。

以上是目前的一些使用体验，欢迎大家一起讨论。

#obsidian#插件

Close

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MjM5NjE2NTUwMQ==&mid=2247484212&idx=1&sn=4c1f9358ef131706346689e1b30020bc&chksm=a7edf634bce2ce1965706fde4c49a4d6aa14581fef86ee146a149cbc2aeaf43eb5f73c25b4a9&scene=90&xtrack=1&req_id=1776225147031847&sessionid=1776225247&subscene=93&clicktime=1776225256&enterid=1776225256&flutter_pos=0&biz_enter_id=4&ranksessionid=1776225147&jumppath=50183_1776225206833,1101_1776225238996,1001_1776225241104,1104_1776225248148&jumppathdepth=4&ascene=56&devicetype=iOS26.4.1&version=18004637&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ9fXYsiYvWUBGnN28FBZXVxLVAQIE97dBBAEAAAAAAPDXEuBzKmoAAAAOpnltbLcz9gKNyK89dVj0N0883OC9d/FG4aGeBMGWjVa7M9tZre75XPQloQ744X1IXkUs31z/ylIcFWQx0ufSswAeqAh0BWCGRt+hv5rNSsJ0HDNnbnig2sGMLDGneo/rbBG9RYCvaGb/cCh8f88hcVGPIyW3gaR2vvWl/YUfGtl0nRShvkv55xG+cNGt1KjVpmGlFCZ9vqitfliUmqblMxTsWsbSmG1n5z3n+0FLPyqWhdcACSUWXxdb+E7QLg==&pass_ticket=Y9PxRAAwP0kJWNbpo0VDyRNSxqNB2v4mnNihRy2RZ4k8jhtYtKt/qQmsBBPoLTW3&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/be4edf0d-cb15-4b2d-b9f0-5fd034a10163/be4edf0d-cb15-4b2d-b9f0-5fd034a10163/)