# DeepSeek官方推荐：R1要这样设置

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzIzNjc1NzUzMw==&mid=224777...](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&mid=2247777462&idx=2&sn=b4e7c75aa62a7de6ac418aa3f05b9151&chksm=e93cc4bda8f3f9bdd29d238a045316ae9cd5b493499f12749306b1206414d53b43e88c1fead0&scene=90&xtrack=1&sessionid=1739627794&subscene=93&clicktime=1739628771&enterid=1739628771&flutter_pos=12&biz_enter_id=4&ranksessionid=1739628521&ascene=56&devicetype=iOS18.3.1&version=18003830&nettype=WIFI&abtest_cookie=AAACAA==&lang=zh_CN&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQGUL2LOMEEz2L7Wq26R2uTxLYAQIE97dBBAEAAAAAAIcwGTGPkgwAAAAOpnltbLcz9gKNyK89dVj0bA/MM1vtlXOUY7Pe9gGrFYSDbbW0bGt7yGSzMQmTJlOL+5zipjfkysHOx8Kpj0fyDpyyx70GKIM4H5Cu7VnLO2VoYNEqloMkfILlgbuX/Xn44mrB9krCnCpKmQVO25zRBOXLiO5mQjB5ykSh7nvzBvW2JIgD1ThdOJfxvQ2o7XToAjtPsWV+BWs0r3q5XGxI13mjmiKrO/kUjN2RG47qFju7/oavyhSxvapcumQoqC6UQg==&pass_ticket=u2OkXJ0z5sltMwRKH3N8i2hrvtwt4gLyK4+AeoueJoi6FUsyF9zch5RNzejiAJaF&wx_header=3)

关注前沿科技 量子位

##### 金磊 发自 凹非寺 量子位 | 公众号 QbitAI

家人们，咱们到底该如何部署DeepSeek-R1，才能体验最佳啊？

对于这个问题，DeepSeek官方发话了：

![](.evernote-content/34386270-3CAE-43ED-95B2-17D80381BCBB/98F831A6-5CEE-4A87-A018-D88A78FC3DB7.png)

DeepSeek推荐的设置非常简单，只有四项内容。

其中三项，其实在此前相关文档中有所涉及，我们在这里**再来回顾**一下。

首先，是**别用系统提示词**（No system prompt），所有的指令都应该包含在用户提示词中。

至于原因，网友认为是因为R1就是这么被训练而来的。

![](.evernote-content/34386270-3CAE-43ED-95B2-17D80381BCBB/91617E80-650E-4059-8D89-8C034035D538.png)

其次，是把**Temperature设置为0.6**。

DeepSeek在GitHub文档中的解释是：

将Temperature设置在0.5-0.7（建议0.6）的范围内，以防止无休止的重复或输出不一致。

第三点，则是一份**缓解模型绕过思维**的指南，包含两个细分内容：

* 对于数学问题，建议在你的提示中包含一个指令，如：“请一步一步地推理，并将你的最终答案放在\boxed{}内。”
* 在评估模型性能时，建议进行多次测试并对结果进行平均。

![](.evernote-content/34386270-3CAE-43ED-95B2-17D80381BCBB/339A39A1-F199-4625-9E59-3698619398BD.png)

新的设置推荐
------

除了上述已有的三点之外，这次DeepSeek官方在推文中引入了一个新的推荐——

**官方提示搜索和文件上传**。

DeepSeek表示：

上传文件时，请按照模板创建提示，其中{file\_name}， {file\_content}和{question}是参数。

```
file_template = \  
"""[file name]: {file_name}  
[file content begin]  
{file_content}  
[file content end]  
{question}"""
```

对于Web搜索，{search\_results}， {cur\_data}和{question}是参数。

对于中文查询，使用提示词：

![](.evernote-content/34386270-3CAE-43ED-95B2-17D80381BCBB/71713554-41E7-41D1-A5FA-681AD6D1BDBF.png)

对于英文查询，使用提示词：

![](.evernote-content/34386270-3CAE-43ED-95B2-17D80381BCBB/05CF52D6-DA4B-4153-905B-21415B6E14AE.png)

相应内容在DeepSeek官方GitHub的README文档中也有更新，感兴趣的小伙伴可以进一步了解下~

DeepSeek官方GitHub：  
https://github.com/deepseek-ai/DeepSeek-R1/blob/main/README.md

参考链接：  
[1]https://x.com/deepseek\_ai/status/1890324295181824107  
[2]https://www.reddit.com/r/LocalLLaMA/comments/1i9k284/why\_should\_one\_avoid\_adding\_a\_system\_prompt\_with/

— **完** —

**评选报名**｜**2025年值得关注的****AIGC企业&产品**

下一个AI“国产之光”将会是谁？

本次评选结果将于4月中国AIGC产业峰会上公布，欢迎参与！

![](.evernote-content/34386270-3CAE-43ED-95B2-17D80381BCBB/5D15AEBE-5FF9-4C8E-8923-5E12AA6D0D20.png)

**一键关注 👇 点亮星标**

**科技前沿进展每日见**

**一键三连****「点赞」「转发」「小心心」**

**欢迎在评论区留下你的想法！**

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&mid=2247777462&idx=2&sn=b4e7c75aa62a7de6ac418aa3f05b9151&chksm=e93cc4bda8f3f9bdd29d238a045316ae9cd5b493499f12749306b1206414d53b43e88c1fead0&scene=90&xtrack=1&sessionid=1739627794&subscene=93&clicktime=1739628771&enterid=1739628771&flutter_pos=12&biz_enter_id=4&ranksessionid=1739628521&ascene=56&devicetype=iOS18.3.1&version=18003830&nettype=WIFI&abtest_cookie=AAACAA==&lang=zh_CN&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQGUL2LOMEEz2L7Wq26R2uTxLYAQIE97dBBAEAAAAAAIcwGTGPkgwAAAAOpnltbLcz9gKNyK89dVj0bA/MM1vtlXOUY7Pe9gGrFYSDbbW0bGt7yGSzMQmTJlOL+5zipjfkysHOx8Kpj0fyDpyyx70GKIM4H5Cu7VnLO2VoYNEqloMkfILlgbuX/Xn44mrB9krCnCpKmQVO25zRBOXLiO5mQjB5ykSh7nvzBvW2JIgD1ThdOJfxvQ2o7XToAjtPsWV+BWs0r3q5XGxI13mjmiKrO/kUjN2RG47qFju7/oavyhSxvapcumQoqC6UQg==&pass_ticket=u2OkXJ0z5sltMwRKH3N8i2hrvtwt4gLyK4+AeoueJoi6FUsyF9zch5RNzejiAJaF&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/9dfb561b-e07a-4b9d-b684-4fe04e003095/9dfb561b-e07a-4b9d-b684-4fe04e003095/)