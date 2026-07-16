---
title: "RAID 5 和热备盘的关系？RAID 5 需要热备盘吗_百度知道"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/RAID 5 和热备盘的关系？RAID 5 需要热备盘吗_百度知道.md
tags: [印象笔记]
---

# RAID 5 和热备盘的关系？RAID 5 需要热备盘吗_百度知道

# RAID 5 和热备盘的关系？RAID 5 需要热备盘吗_百度知道 --- RAID 5 和热备盘的关系？RAID 5 需要热备盘吗 ============================ 代码

---

# RAID 5 和热备盘的关系？RAID 5 需要热备盘吗_百度知道

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
当 RAID5 中有一块[硬盘](https://www.baidu.com/s?wd=%E7%A1%AC%E7%9B%98&tn=SE_PcZhidaonwhc_ngpagmjz&rsv_dl=gh_pc_zhidao)发生损坏时，需要手动将故障盘替换，然后进行 RAID 重建。可是要知道，这个过程所有磁盘的读写负荷是非常大的，如果再有一块[硬盘](https://www.baidu.com/s?wd=%E7%A1%AC%E7%9B%98&tn=SE_PcZhidaonwhc_ngpagmjz&rsv_dl=gh_pc_zhidao)损坏的话 RAID5 就会失败（失败就是数据全丢的意思）。  
因此对应的解决方案就是使用热备盘，热备盘在磁盘发生轻微故障但仍然可以读写的时候就会提前通过某种方式得到即将故障[硬盘](https://www.baidu.com/s?wd=%E7%A1%AC%E7%9B%98&tn=SE_PcZhidaonwhc_ngpagmjz&rsv_dl=gh_pc_zhidao)的内容，然后接替即将故障的硬盘从而确保可靠。  
PS：至于什么叫轻微故障，可以参考 S.M.A.R.T.  
  
第二个问题：  
需要，但不是必须  
这个其实要看情况，如果资金充裕的话 3-6 盘的 RAID5 至少要保证有一块热备盘，大于 6 块盘的 RAID5 要考虑 2 块甚至更多的热备。但总之，非常需要。

Measure

Measure

---

[🌐 原始链接](https://zhidao.baidu.com/question/489601902186217052.html?push=keyword&entry=qb_home_keyword)

[📎 在印象笔记中打开](evernote:///view/207087/s1/007b67e5-3e3c-4c1b-b031-790013ed9cba/007b67e5-3e3c-4c1b-b031-790013ed9cba/)