---
title: "RAID 5 和热备盘的关系？RAID 5 需要热备盘吗_百度知道"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/RAID 5 和热备盘的关系？RAID 5 需要热备盘吗_百度知道.md
tags: [印象笔记]
---


RAID 5 和热备盘的关系？RAID 5 需要热备盘吗
============================

代码

提交回答匿名

2 个回答

[#热议#
提高警惕：1 分钟识破电信诈骗](https://zhidao.baidu.com/special/topic/view?name=dianxinzhapian)

lel1996

2019-12-04

先回答第一个问题：  
RAID5 是一种阵列格式，而热备盘是一种可靠机制，所以原则上 RAID5 和热备盘是两回事，但热备盘确实能够提升 RAID5 的稳定性。  
因为，RAID 当中磁盘也是有损坏几率的，即使 RAID5 原生支持一块磁盘的冗余能力  
当 RAID5 中有一块[硬盘](https://www.baidu.com/s?wd=%E7%A1%AC%E7%9B%98&tn=SE_PcZhidaonwhc_ngpagmjz&rsv_dl=gh_pc_zhidao)发生损坏时，需要手动将故障盘替换，然后进行 RAID 重建。可是要知道，这个过程所有磁盘的读写负荷是非常大的，如果再有一块[硬盘](https

<!-- [摘要] 规则提取，如需全文请查看 vault 原始笔记 -->