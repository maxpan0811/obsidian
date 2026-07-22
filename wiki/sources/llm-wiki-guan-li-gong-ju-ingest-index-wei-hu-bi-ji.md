---
name: llm-wiki-guan-li-gong-ju-ingest-index-wei-hu-bi-ji
type: source
tags: [llm-wiki, ingest, faiss, chromadb, index-maintenance]
source_path: /Users/panbo/Obsidian/程序开发/LLM-Wiki管理工具-ingest索引维护笔记.md
---

[摘要]
本文是LLM-Wiki管理工具自2026年6月至7月的完整操作日志，记录了ingest管线从ChromaDB到FAISS的三代演变过程，以及多个关键故障的排查与修复。

第一代ChromaDB遇到954G HNSW索引膨胀：两个脚本(ingest.py/build_index.py)无锁并发操作同一ChromaDB，导致HNSW mmap偏移错位，coll.add()遍历链表找不到终止条件，每写几KB新文档就生成GB级新边。修复方案是加fcntl.flock互斥锁和单一写入入口原则。随后又遇到HNSW Compaction故障（删除2.md副本时触发），多session并发写入致compactor无法合并segment，最终需删除集合重建。

第二代FAISS v1方案（2026-07-10）：用FAISS+HNSW替代ChromaDB，引入原子写入+.bak检查点。但逐文件编码慢（0.9s/文件）、中断丢进度、无边分块。

第三代FAISS v2+v3（2026-07-11至07-14）：v2引入分块（1000字/块+150重叠）、批量编码（32文件一批）、checkpoint自动续传、3份版本备份。v3将引擎从sentence_transformers/bge-m3(PyTorch CPU)切换为Ollama/bge-m3(Metal GPU)，速度从0.08 files/s提升至2.0 files/s（25倍加速），内存从崩溃/泄漏降至700MB稳定。随后全库索引从仅wiki/sources扩展到Obsidian vault全部71,497篇，速度稳定在5.1 files/s。

关键陷阱记录包括：-newer时间戳遗漏旧文件、macOS大小写不敏感导致AI双倍入库、shell glob在14K+文件时返回空、HF_HUB_OFFLINE保障离线索引、PDF二进制提取62%成功率、含特殊字符文件名需用Python subprocess list传参绕过shell展开、ChromaDB并发写入崩溃后加PID文件锁、FAISS超长段落导致Ollama 400错误需MAX_PARA_CHARS=4000上限。

2026-07-16批量修复13,700个wiki源页缺失的印象笔记原始链接。2026-07-20新增CLAUDE.md中的Capture双写规则章节。
[摘要]

原文链接: /Users/panbo/Obsidian/程序开发/LLM-Wiki管理工具-ingest索引维护笔记.md