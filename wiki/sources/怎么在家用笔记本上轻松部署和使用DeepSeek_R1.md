---
title: 怎么在家用笔记本上轻松部署和使用DeepSeek R1?
type: source
created: 2026-06-17
updated: 2026-06-17
source: 印象笔记管理工具
source_path: 印象笔记管理工具/怎么在家用笔记本上轻松部署和使用DeepSeek R1？.html
tags: [AI技术, 教育]
---

# 怎么在家用笔记本上轻松部署和使用DeepSeek R1?

原文链接: https://mp.weixin.qq.com/s?chksm=e8877171dff0f8678b71f57aa068bb7...

原创 node  字节笔记本 
DeepSeek R1 是由国内团队开发的高性能开源大模型。详细介绍可以看这里：甚至比 OpenAI-O1表现更好! 我测了 DeepSeek R1,结论只有两个字:牛逼!

那本文将介绍其蒸馏版本在普通家用笔记本上的部署和使用，之所以选择蒸馏版本，是因为蒸馏版本通过模型蒸馏技术实现了算力需求的大幅降低。而且在数学、编程等领域表现出众，可处理复杂逻辑推理任务，如果你不了解蒸馏技术文末也会提供相关的拓展知识
运行环境准备—
1 支持 AVX2 指令集的 CPU（近几年的笔记本通 常都支持）2 内存建议 32GB 以上获得流畅体验3 存储空间预留 10GB 以上4 可选 NVIDIA 显卡实现 CUDA 加速
部署步骤详解—
环境安装：
curl -sSf https://raw.githubusercontent.com/WasmEdge/WasmEdge/master/utils/install_v2.sh | bash -s -- -v 0.14.1
source /home/$USER/.bashrc

获取模型：
curl -LO https://huggingface.co/second-state/DeepSeek-R1-Distill-Llama-8B-GGUF/resolve/main/DeepSeek-R1-Distill-Llama-8B-Q5_K_M.gguf

下载服务端：
curl -LO https://github.com/LlamaEdge/LlamaEdge/releases/latest/download/llama-api-server.wasm

部署界面：
curl -LO https://github.com/LlamaEdge/chatbot-ui/releases/latest/download/chatbot-ui.tar.gz
tar xzf chatbot-ui.tar.gz

启动服务：
wasmedge --dir .:. --nn-preload default:GGML:AUTO:DeepSeek-R1-Distill-Llama-8B-Q5_K_M.gguf llama-api-server.wasm --prompt-template llama-3-chat --ctx-size 8096

...然后访问 http://localhost:8080 开始对话
如果是想通过 API访问，因为提供了OPENAI 接口的兼容处理，请求接口直接就是"http://localhost:8080/v1",大模型调用时使用 DeepSeek-R1-Distill-Llama-8B
技术解析—
模型蒸馏技术是通过大模型对小模型的"教导"实现知识迁移
在这个过程中，教师模型（大模型）会将其学到的特征、决策边界和推理能力等知识，通过特殊的训练方式传授给学生模型（小模型）
具体来说，大模型会生成带有软标签的训练数据，这些软标签包含了更丰富的分布信息，而不是简单的 0/1 分类
学生模型通过模仿教师模型的输出分布进行学习，从而在保持核心能力的同时大幅减少参数量，最终实现模型的轻量化
DeepSeek R1 正是通过这种技术，将原始的数百亿参数压缩到了 8B，同时保持了优秀的性能表现
Rust + WebAssembly 技术
