---
name: faiss向量索引pipeline
type: source
tags: [FAISS, 向量索引, ChromaDB迁移, bge-m3, 知识库]
source_path: /Users/panbo/Obsidian/程序开发/FAISS向量索引Pipeline.md
---

[摘要]

本文档记录了从ChromaDB迁移到FAISS的完整演进历程。ChromaDB的HNSW图索引因并发写入和批量删除脆弱已崩溃三次：2026-06-19两脚本无锁并发致link_lists.bin膨胀至954GB、2026-07-07 bulk delete触发compaction失败、2026-07-10残留进程并发写入segfault全库归零。

FAISS方案经过三个版本迭代：v1逐文件编码太慢（0.9s/文件）；v2引入分块+批量编码+checkpoint+版本备份，全量构建约1.8h；v3修复OOM（BATCH_SIZE 32→8，+gc.collect+time.sleep 0.5s）。存储结构包括embedding_cache.pkl、embedding.faiss（FlatIP索引）、metadata.pkl和版本备份（最近3份）。分块策略按`\n\n`拆分，合并至1000字/块，相邻块重叠150字。查询管线支持自动fallback、同文件多chunk去重和multi-hop查询。

v3最终结果：71,498文件缓存，374,168 chunks（dim=1024），embedding.faiss 1,461.6MB，metadata.pkl 152.0MB。关键经验：del变量不够必须显式gc.collect()+time.sleep()（Metal GPU内存释放异步）；ChromaDB崩了3次而FAISS一次没崩过，纯numpy数组稳定性远超HNSW图。

2026-07-16全量构建进度评估：52,209个.md文件已完成33,242个缓存。发现Ollama 400错误和vault实际100,004文件等修复。2026-07-18扩展FAISS至RAW二进制文档（PDF/Excel/Word/PPT全文），wiki/sources退出FAISS只用于grep。新增多种格式提取（PyMuPDF→PDF，openpyxl+xlrd→Excel，python-docx→Word，python-pptx+ZIP XML→PPT），文本截断逐步重试（4000→2000→1000字符）。最终2,821/2,984个RAW文件成功嵌入（99.5%），15个损坏文件不可恢复。

原文链接：/Users/panbo/Obsidian/程序开发/FAISS向量索引Pipeline.md