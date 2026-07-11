# 怎么在家用笔记本上轻松部署和使用DeepSeek R1?

---

原文链接: [https://mp.weixin.qq.com/s?chksm=e8877171dff0f8678b71f57aa068bb7...](https://mp.weixin.qq.com/s?chksm=e8877171dff0f8678b71f57aa068bb75194cf9761181a5a8ebddd622292aaa797ed6a164670e&exptype=unsubscribed_card_recommend_article_u2i_mainprocess_coarse_sort_tlfeeds&ranksessionid=1738571309_2&scene=169&mid=2247493295&sn=491286a5a24fa0350dc31182fc73a9cb&idx=1&__biz=MzIzMzQyMzUzNw==&sessionid=1738572539&subscene=200&clicktime=1738574788&enterid=1738574788&flutter_pos=54&biz_enter_id=5&ascene=56&devicetype=iOS18.3&version=1800382d&nettype=3G+&abtest_cookie=AAACAA==&lang=zh_CN&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQx806+GVkR5cH4QoCrg+M4BLWAQIE97dBBAEAAAAAAKsgD3303D0AAAAOpnltbLcz9gKNyK89dVj0HPpOZeQrHuOt4+jUoBj5V7Ri7PH4oGp58vZ6VdMhU4Z3QFUy3VXzwZ9lL3NQOgLZnbYZKOe2fo6GdHab7ic7fvoDEv1nmPNcZVwnaxqQz71FpttJp2ySix44uFEJCxPRRdMidUW6Q3PAUEX4AgHTQul8PgMKUYXlLrNuqHeur9/uZXconKLlrQGKZ+/UZzyPu1r60j25seYWxKFw/94yYRYj+6SeU6rqJwgg6WhNFoQ=&pass_ticket=WZfVbqnDXDvLrXHxBBqIKjLGq1cVwoCWPN2RhS2TNZa/6MDUDNalwACemoSBSi9Y&wx_header=3)

原创 node 字节笔记本

DeepSeek R1 是由国内团队开发的高性能开源大模型。详细介绍可以看这里：[甚至比 OpenAI-O1表现更好! 我测了 DeepSeek R1,结论只有两个字:牛逼!](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247493159&idx=1&sn=be20c7c3fd5b27df0a6ea8744b34028a&scene=21#wechat_redirect)

![](.evernote-content/DC04E8AF-7A42-4A71-9948-EBB71216993E/479F7478-B384-4554-8E6E-1A67AAD58E68.jpg)

那本文将介绍其蒸馏版本在普通家用笔记本上的部署和使用，之所以选择蒸馏版本，是因为蒸馏版本通过模型蒸馏技术实现了算力需求的大幅降低。而且在数学、编程等领域表现出众，可处理复杂逻辑推理任务，如果你不了解蒸馏技术文末也会提供相关的拓展知识

运行环境准备
------

—

1 支持 AVX2 指令集的 CPU（近几年的笔记本通 常都支持）  
2 内存建议 32GB 以上获得流畅体验  
3 存储空间预留 10GB 以上  
4 可选 NVIDIA 显卡实现 CUDA 加速

部署步骤详解
------

—

环境安装：

```
curl -sSf https://raw.githubusercontent.com/WasmEdge/WasmEdge/master/utils/install_v2.sh | bash -s -- -v 0.14.1  
source /home/$USER/.bashrc
```

获取模型：

```
curl -LO https://huggingface.co/second-state/DeepSeek-R1-Distill-Llama-8B-GGUF/resolve/main/DeepSeek-R1-Distill-Llama-8B-Q5_K_M.gguf
```

下载服务端：

```
curl -LO https://github.com/LlamaEdge/LlamaEdge/releases/latest/download/llama-api-server.wasm
```

部署界面：

```
curl -LO https://github.com/LlamaEdge/chatbot-ui/releases/latest/download/chatbot-ui.tar.gz  
tar xzf chatbot-ui.tar.gz
```

启动服务：

```
wasmedge --dir .:. --nn-preload default:GGML:AUTO:DeepSeek-R1-Distill-Llama-8B-Q5_K_M.gguf llama-api-server.wasm --prompt-template llama-3-chat --ctx-size 8096
```

然后访问 http://localhost:8080 开始对话

如果是想通过 API访问，因为提供了OPENAI 接口的兼容处理，请求接口直接就是"http://localhost:8080/v1",大模型调用时使用 DeepSeek-R1-Distill-Llama-8B

技术解析
----

—

模型蒸馏技术是通过大模型对小模型的"教导"实现知识迁移

在这个过程中，教师模型（大模型）会将其学到的特征、决策边界和推理能力等知识，通过特殊的训练方式传授给学生模型（小模型）

具体来说，大模型会生成带有软标签的训练数据，这些软标签包含了更丰富的分布信息，而不是简单的 0/1 分类

学生模型通过模仿教师模型的输出分布进行学习，从而在保持核心能力的同时大幅减少参数量，最终实现模型的轻量化

DeepSeek R1 正是通过这种技术，将原始的数百亿参数压缩到了 8B，同时保持了优秀的性能表现

Rust + WebAssembly 技术栈的选择体现了现代应用部署的革新思路。Rust 语言以其内存安全和高性能著称，编译后的代码性能接近 C++。而 WebAssembly 作为一种底层字节码格式，可以将高级语言编译成在浏览器中近乎原生速度运行的代码。

这两种技术的结合，整个运行时环境仅需 30MB，还实现了真正的跨平台部署能力。由于 WebAssembly 的沙箱特性，应用运行在隔离的环境中，提供了额外的安全保障。

同时，这种架构天然支持容器化部署，可以无缝集成到现代云原生基础设施中，在大模型部署场景下，这种技术组合相比传统的 Python 方案，显著减少了环境依赖，提升了部署效率，降低了维护成本。

本地有哪些应用场景？
----------

—

本地部署的 DeepSeek R1 成为知识管理的得力工具。比如上下文理解，建立文档间的知识图谱，发现潜在关联，对话形式为用户提供精准的文档解读服务

在软件开发领域，类似于实时的代码补全建议，分析代码中的潜在问题。根据代码上下文自动生成单元测试，确保代码质量。对于复杂的重构需求，能提供详细的重构建议和实施步骤，大大提升开发效率

数据分析场景下，本地部署的 DeepSeek R1 可以智能识别数据特征，提供个性化的数据清洗策略。基于数据内容和分析目标，生成专业的分析报告，包括数据趋势、异常值检测和相关性分析。甚至能数据可视化，可深成适合的图表类型，直观地展示数据的变化！

欢迎加入我们的星球：[字节笔记本星球]，共同探索 AI 技术的无限可能！

修改于

---

[🌐 原始链接](https://mp.weixin.qq.com/s?chksm=e8877171dff0f8678b71f57aa068bb75194cf9761181a5a8ebddd622292aaa797ed6a164670e&exptype=unsubscribed_card_recommend_article_u2i_mainprocess_coarse_sort_tlfeeds&ranksessionid=1738571309_2&scene=169&mid=2247493295&sn=491286a5a24fa0350dc31182fc73a9cb&idx=1&__biz=MzIzMzQyMzUzNw==&sessionid=1738572539&subscene=200&clicktime=1738574788&enterid=1738574788&flutter_pos=54&biz_enter_id=5&ascene=56&devicetype=iOS18.3&version=1800382d&nettype=3G+&abtest_cookie=AAACAA==&lang=zh_CN&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQx806+GVkR5cH4QoCrg+M4BLWAQIE97dBBAEAAAAAAKsgD3303D0AAAAOpnltbLcz9gKNyK89dVj0HPpOZeQrHuOt4+jUoBj5V7Ri7PH4oGp58vZ6VdMhU4Z3QFUy3VXzwZ9lL3NQOgLZnbYZKOe2fo6GdHab7ic7fvoDEv1nmPNcZVwnaxqQz71FpttJp2ySix44uFEJCxPRRdMidUW6Q3PAUEX4AgHTQul8PgMKUYXlLrNuqHeur9/uZXconKLlrQGKZ+/UZzyPu1r60j25seYWxKFw/94yYRYj+6SeU6rqJwgg6WhNFoQ=&pass_ticket=WZfVbqnDXDvLrXHxBBqIKjLGq1cVwoCWPN2RhS2TNZa/6MDUDNalwACemoSBSi9Y&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/60e43f15-0cab-4ab8-9e67-1764557c60be/60e43f15-0cab-4ab8-9e67-1764557c60be/)