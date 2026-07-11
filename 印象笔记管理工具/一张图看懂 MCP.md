# 一张图看懂 MCP

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzkwMjE5ODUxNg==&mid=224748...](https://mp.weixin.qq.com/s?__biz=MzkwMjE5ODUxNg==&mid=2247484985&idx=1&sn=8e1a0f28cdcc6768f9c71b7458b9fa1f&chksm=c1ddc3ee37ce44f0edbdcff163094ba513014362c67a9d73b4b0b8b8a9a52eeeb7f1dcfc089f&scene=90&xtrack=1&req_id=1780503214473499&sessionid=1780503385&subscene=93&clicktime=1780503730&enterid=1780503730&flutter_pos=4&biz_enter_id=4&ranksessionid=1780503390&jumppath=WAWebViewController_1780503700114,WAWebViewController_1780503700588,20020_1780503725093,1104_1780503725772&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004a25&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQN5Mp+Xbn2wJuIR52rxlITBLTAQIE97dBBAEAAAAAAL+CME06k+UAAAAOpnltbLcz9gKNyK89dVj0lJTLBML8kCFWtFMp35hnCZDM9TDzGj2khLDs+Y3//TPSD4e0xndyHjSGKgujcOUsUIeUcpgQydTzaf5xjxDjKNV7TqJtpbU6ccTHA2mnE1LRwo+k2pQKcFG+DZy7dW4pkRAKIp967nM+4b/j6p1a6Zsl/SJa6qNLbKYFlnoAl1HYE1lKY5eeB3DFv5WzXnhf5jUx/8yXGdCGFQ/o4KGbBxarHmiqtPez0YHsNCM=&pass_ticket=6n9GSeFcOWrJ9PhLk9l07yi6f4xGAfgZDPi5nuxPO/IvXOEklEoPdKXqcdg564bu&wx_header=3)

![](.evernote-content/4633ED5A-57EE-4D28-BEC3-328CCF3CD0B9/ED98F1E3-71FA-4119-8CF9-80AFF4C2C443.png)

通过这张图可以看到，MCP 不是简单的“插件列表”，而是一套让 AI Agent 接入外部世界的标准协议。左侧是 AI Agent / Host，负责对话、推理和任务编排；中间是 MCP Client 和协议层，负责连接管理、初始化握手、能力发现、JSON-RPC 消息和传输方式；右侧是 MCP Server，把文件系统、数据库、API 服务和业务工具封装成可发现、可调用的能力。Agent 先知道有哪些 Tools、Resources 和 Prompts，再按权限调用对应 Server，并把结果带回上下文继续推理。

Close

Name cleared

Like the AuthorOther Amount

赞赏后展示我的头像

作品

暂无作品

Back

**Other Amount**

赞赏金额

¥

最低赞赏 ¥0

1

2

3

4

5

6

7

8

9

0

.

江苏,3 hours ago,

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzkwMjE5ODUxNg==&mid=2247484985&idx=1&sn=8e1a0f28cdcc6768f9c71b7458b9fa1f&chksm=c1ddc3ee37ce44f0edbdcff163094ba513014362c67a9d73b4b0b8b8a9a52eeeb7f1dcfc089f&scene=90&xtrack=1&req_id=1780503214473499&sessionid=1780503385&subscene=93&clicktime=1780503730&enterid=1780503730&flutter_pos=4&biz_enter_id=4&ranksessionid=1780503390&jumppath=WAWebViewController_1780503700114,WAWebViewController_1780503700588,20020_1780503725093,1104_1780503725772&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004a25&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQN5Mp+Xbn2wJuIR52rxlITBLTAQIE97dBBAEAAAAAAL+CME06k+UAAAAOpnltbLcz9gKNyK89dVj0lJTLBML8kCFWtFMp35hnCZDM9TDzGj2khLDs+Y3//TPSD4e0xndyHjSGKgujcOUsUIeUcpgQydTzaf5xjxDjKNV7TqJtpbU6ccTHA2mnE1LRwo+k2pQKcFG+DZy7dW4pkRAKIp967nM+4b/j6p1a6Zsl/SJa6qNLbKYFlnoAl1HYE1lKY5eeB3DFv5WzXnhf5jUx/8yXGdCGFQ/o4KGbBxarHmiqtPez0YHsNCM=&pass_ticket=6n9GSeFcOWrJ9PhLk9l07yi6f4xGAfgZDPi5nuxPO/IvXOEklEoPdKXqcdg564bu&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/d9ded25d-2bf2-451d-b377-55258ecb0804/d9ded25d-2bf2-451d-b377-55258ecb0804/)