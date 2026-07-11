# SHR（计算机术语）_百度百科

---

Synology Hybrid RAID
--------------------

[**编辑](#)

### 简介

Synology Hybrid RAID（直译：群晖混合[磁盘阵列](http://baike.baidu.com/item/%E7%A3%81%E7%9B%98%E9%98%B5%E5%88%97)）是一种**自动**磁盘阵列管理系统（Automated RAID Management system），设计初衷为简化管理的同时增加磁盘空间利用率。SHR适合那种从不关心也不想关心NAS中支持哪种RAID模式的、不明白RAID细节的、而又想很方便的最大化利用空间的用户。SHR最大支持单[硬盘故障](http://baike.baidu.com/item/%E7%A1%AC%E7%9B%98%E6%95%85%E9%9A%9C)，当两个或更多硬盘故障时将出现数据丢失，所以官方说法为“Note that a RAID volume (whether classic RAID or SHR) **is not**a backup system”，不适合作为备份用途。

### SHR是很必要的么？

Synology并没有非常推荐使用SHR，如果用户比较熟悉RAID的种类与管理方法，完全可以使用传统RAID，比如管理员与高级用户。SynologyWiki中用以下语句描述SHR：“SHR基于一种Linux下的磁盘管理系统，而且完全是一种可选项。”（The SHR is based on a Linux RAID management system, and is completely optional to use.）

### SHR的空间使用方式

如图所示，系统中包含500GB、1TB、1.5TB、2TB、2TB一共5块硬盘，图中左边为传统的磁盘阵列模式，此时系统总可用空间只为2TB，因为每一块磁盘可用空间以系统中容量最小的硬盘为基准，所以可用总量是500GBX4=2TB（其中一块硬盘为冗余用途），阵列总使用2.5TB，

[![](.evernote-content/0B0D63C7-D9D3-437D-B110-9364FE9180DE/61302265-5D91-4C6C-95EA-C0AAF9043DE9.png)](http://baike.baidu.com/pic/SHR/5670561/0/9f510fb30f2442a71919e010d143ad4bd113026b?fr=lemma&ct=single "传统RAID与SHR的管理方式")

传统RAID与SHR的管理方式

剩余的4.5TB无效。

图中右方为使用SHR的情形，整个系统建立的4套独立的阵列系统，每个系统中有500GB为[冗余](http://baike.baidu.com/item/%E5%86%97%E4%BD%99)空间，其余为可用空间，所以除掉500X4=2TB的冗余空间外，其他的5TB均为可用空间，所以SHR的空间利用率是很高的，整个空间没有丝毫浪费。

但是需要注意的是，SHR的安全性并不高，比如最坏的情况，当图中最右方的2TB硬盘出现故障时，所有独立阵列都会收到牵连。

### SHR的扩展

当替换磁盘扩展阵列容量时，传统RAID与SHR的容量变化如图所示，可以看到在替换完成之前，RAID的可用空间并不会随着硬盘容量增大而增大；而SHR的容量是即时增加，这样可以满足在替换过程中对容量增加的需求的需求。

[![](.evernote-content/0B0D63C7-D9D3-437D-B110-9364FE9180DE/510F08E9-692C-47DD-8DDD-63F640A7A523.png)](http://baike.baidu.com/pic/SHR/5670561/0/3812b31bb051f81967c01cffdab44aed2f73e79a?fr=lemma&ct=single "RAID与SHR在更换硬盘时容量变化")

RAID与SHR在更换硬盘时容量变化

### SHR的硬盘更换

1.SHR卷可以将硬盘替换成更高容量而不丢失数据。（比如将某块硬盘从1TB更换为3TB，在群晖的NAS上。）

2.SHR卷可以增加硬盘。（比如从5个1TB硬盘增加至15个。）

3.现有硬盘不能更换为更小的硬盘，起码要相等。

---

[🌐 原始链接](http://baike.baidu.com/link?url=l9bp4q2n-CuFCemx7pUgxqyeAQ29AdfHda2EGN_gEA2t156O4gJ727G3coXsjJnJsUz0r5NH_uHfSsZc_ESaVK#2)

[📎 在印象笔记中打开](evernote:///view/207087/s1/ef8d9f27-b244-4fe1-8766-34244d043234/ef8d9f27-b244-4fe1-8766-34244d043234/)