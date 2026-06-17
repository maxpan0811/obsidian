---
title: DeepSeek官方推荐：R1要这样设置
type: source
created: 2026-06-17
updated: 2026-06-17
source: 印象笔记管理工具
source_path: 印象笔记管理工具/DeepSeek官方推荐：R1要这样设置.html
tags: [网文推荐, AI技术, 教育]
---

# DeepSeek官方推荐：R1要这样设置

原文链接: https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&mid=224777...

关注前沿科技  量子位 
金磊 发自 凹非寺量子位 | 公众号 QbitAI家人们，咱们到底该如何部署DeepSeek-R1，才能体验最佳啊？
对于这个问题，DeepSeek官方发话了：

DeepSeek推荐的设置非常简单，只有四项内容。
其中三项，其实在此前相关文档中有所涉及，我们在这里再来回顾一下。
首先，是别用系统提示词（No system prompt），所有的指令都应该包含在用户提示词中。
至于原因，网友认为是因为R1就是这么被训练而来的。

其次，是把Temperature设置为0.6。
DeepSeek在GitHub文档中的解释是：
将Temperature设置在0.5-0.7（建议0.6）的范围内，以防止无休止的重复或输出不一致。

第三点，则是一份缓解模型绕过思维的指南，包含两个细分内容：
对于数学问题，建议在你的提示中包含一个指令，如：“请一步一步地推理，并将你的最终答案放在\boxed{}内。”
在评估模型性能时，建议进行多次测试并对结果进行平均。

新的设置推荐除了上述已有的三点之外，这次DeepSeek官方在推文中引入了一个新的推荐——
官方提示搜索和文件上传。
DeepSeek表示：
上传文件时，请按照模板创建提示，其中{file_name}， {file_content}和{question}是参数。

file_template = \
"""[file name]: {file_name}
[file content begin]
{file_content}
[file content end]
{question}"""

对于Web搜索，{search_results}， {cur_data}和{question}是参数。
对于中文查询，使用提示词：

相应内容在DeepSeek官方GitHub的README文档中也有更新，感兴趣的小伙伴可以进一步了解下~
DeepSeek官方GitHub：https://github.com/deepseek-ai/DeepSeek-R1/blob/main/README.md
参考链接：[1]https://x.com/deepseek_ai/status/1890324295181824107[2]https://www.reddit.com/r/LocalLLaMA/comments/1i9k284/why_should_one_avoid_adding_a_system_prompt_with/
— 完 —

评选报名｜2025年值得关注的AIGC企业&产品
下一个AI“国产之光”将会是谁？
本次评选结果将于4月中国AIGC产业峰会上公布，欢迎参与！

一键关注 👇 点亮星标
科技前沿进展每日见

一键三连「点赞」「转发」「小心心」
欢迎在评论区留下你的想法！
