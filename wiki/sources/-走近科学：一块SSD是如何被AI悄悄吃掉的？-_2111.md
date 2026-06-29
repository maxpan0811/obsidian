---
title: "走近科学：一块SSD是如何被AI悄悄吃掉的？"
type: source
created: 2026-06-27
updated: 2026-06-27
source_path: 印象笔记管理工具/走近科学：一块SSD是如何被AI悄悄吃掉的？.md
tags: [evernote, impression]
---

---
title: "走近科学：一块SSD是如何被AI悄悄吃掉的？"
source: evernote
type: note
export_date: 2026-06-23
guid: b4789ba9-71bd-4bec-bfc5-e20d09a60309
---

# 走近科学：一块SSD是如何被AI悄悄吃掉的？

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzIzMzQyMzUzNw==&mid=224751...](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247518375&idx=1&sn=04352343b6bc8409f636de5183ad9e76&chksm=e98410c4a904e800a3333e29d154fb2ad98cea11672beb69a5a44b0f0e788061253c8b76f459&mpshare=1&scene=24&srcid=0623dlFl5CC2FsAENEHPuByf&sharer_shareinfo=8d299f370eed018cab364e3bee76be30&sharer_shareinfo_first=8d299f370eed018cab364e3bee76be30&clicktime=1782178345&enterid=1782178345&ascene=14&devicetype=iOS26.5&version=18004b29&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ726EIAVLGeIJuMbG9HyVnxLTAQIE97dBBAEAAAAAAAM6AadGC54AAAAOpnltbLcz9gKNyK89dVj0xIvbOR7h8ss7yWYt++pOdwCKmAHSzLnDwDvpwXxQEpDmOFRVlWdaW25+6MP1fx8bcccOFGiTFEs5pzQ6+2JGa+n5IwPbQ3mT0EbdPYYMm1HS4s3pBX3DFDb5MqrvfkwsG+zADE8/0UgdV2EING3XI9VOHxLgtJNk1fHGf3GSGMcoCW8dzb7EEAxhjDSm/CUmLyI1phdR+sfUyHAamc31+5Ogfj4R5NttNEHxjco=&pass_ticket=1vh1z4acbB/RhMb3In8Gb2454uL92VDwrYFLWVUAyRj4Lu5UivzX5uSRdjskk3Nv&wx_header=3)

# 走近科学：一块SSD是如何被AI悄悄吃掉的？

Original字节笔记本 字节笔记本

 

![](attachments/4763b74a9d70392f.png)

到底是道德的沦丧，还是人性的扭曲？本期节目，将带您揭开一个发生在程序员电脑里的诡异现象。

事情的起因，要从一次普通的磁盘容量检查说起。

技术人员在例行排查时发现，一个叫 `logs_2.sqlite` 的文件，**已经悄悄长到了 199.4MB**。

![](attachments/6b6616529842b33c.png)

这个文件，没有人主动创建过，没有人手动写入过，它就这样，在用户毫不知情的情况下，一天天变大。

更诡异的是，伴随它出现的还有两个"小尾巴"。

`logs_2.sqlite-shm`，32KB；`logs_2.sqlite-wal`，9.6MB。

三个文件，像影子一样紧紧跟着，谁也不知道它们在干什么。

这一切的源头，指向了一我都很熟悉的名字：**Codex**。

### 第一现场：文件在"呼吸"

技术人员决定深入调查。

第一步，他们用一个叫 `lsof` 的命令，查看这个文件到底被谁占用着。

结果让人意外：**三个 Codex 进程，同时占着同一个文件**。

![](attachments/3f4d3aa0700f94ee.png)

三个进程，一个文件，只要这三个 Codex 还活着，这个文件就有三重压力在同时往里灌数据。

但文件大小在短时间内看起来没有变化，这是不是说明它已经"安静"下来了？

技术人员没有轻易下结论，而是做了一个更精细的检查，**连续两次读取文件的修改时间，间隔10秒**。

结果：

mtime = 19:12:27
（等待10秒）
mtime = 19:12:36

修改时间，在跳动。**文件大小没变，但内容在不停被刷新。**

说明这个文件在原地被反复覆写。

技术人员后来确认，这正是 SQLite 数据库的WAL，Write-Ahead Log，预写日志模式的典型特征。

数据先写入 WAL 日志，定期再合并回主文件，文件涨到一定大小后开始循环利用空间，但每一次循环，都是一次真实的磁盘写入。

### 第二现场：揭开幕后黑手

文件在写，但写的是什么内容？为什么会写这么频繁？

技术人员追溯到了 Codex 的运行机制，发现了三个叠加在一起的因素：

**第一，Codex 默认开着最详尽级别的日志，也就是 TRACE。**

Trace 记录几乎记录过程中的每一个细节"。哪怕你通过环境变量调低日志级别，它依然在写 TRACE， 这个开关，没有真正生效。

**第二，Codex 用的是流式输出SSE。**

AI 每生成一个字、一个 token，就会触发一次日志写入。你在屏幕上看到文字像打字机一样跳出来，而硬盘那边，是同样的频率在被触发写入。

**第三，日志的载体是 SQLite，写入方式是 WAL。**

数据要先进缓存，再写日志文件，再做合并，一份数据，在底层被多次搬运。

三件事叠在一起：**逐字触发 + 全量记录 + 写入放大**。

这才是文件持续写入的真正原因。

### 第三现场：把"凶手"请到实验室

发现规律是一回事，证明它的破坏力是另一回事。技术人员决定做一次**对照实验**。

实验设计是在 Codex 正常运行的状态下，用系统级工具 `fs_usage`，精确监控这三个进程**对这一个文件**的读写行为，持续 30 秒。

![](attachments/a95a23d9f959bd3a.png)

结果很明显：

*30秒内，2033次 I/O 事件，写入 33.6MB 数据。设备编号* `1,14`*，对应真实的 SSD 分区。*

30秒，33.6MB。这是什么概念？

如果按这个速度持续运行一整天，理论上能在真实磁盘上写下接近 100GB 的垃圾数据。

而这一切，只是为了记录一些本该用于调试、却没人会去看的过程日志。

### SSD的读写，正常应该是什么样？

节目播到这里，有必要停下来，给观众补一点常识。

**33.6MB/30秒，到底算不算多？**

SSD 不是无限寿命的存储介质。它的颗粒NAND闪存每个存储单元能被擦写的次数是有限的，这个上限，厂商会用一个叫 **TBW（Total Bytes Written，总写入字节数）** 的指标标出来。

比如一块 1TB 消费级 SSD，常见的 TBW 标定在 300～600TB 左右——也就是说，理论上你可以往这块盘里写个几百TB的数据，它才会真正写到报废。

![](attachments/0a28663146539de4.png)

那日常使用，写入量大概是什么水平？

正常办公、刷网页、写文档，每天写入量通常在 **几百MB到几GB**。

重度开发场景（编译、跑测试、装依赖）：可能到 **十几GB甚至几十GB/天**。

而本期节目里的异常情况，**一个后台日志进程，持续以 5～16 MiB/s 的速度空转写入**，一天24小时不停，理论写入量能轻松突破 **百GB级**，这已经超出了正常使用模式的写入量级，长期下去会显著消耗 SSD 的寿命余量。

![](attachments/93ab44974d6a2605.png)

更关键的问题不是"一次写多少"，而是**持续性，**这次案例里的写入，是只要程序在跑，就不会停的磨损磁盘行为，最容易在几个月后积累成真实损耗。

需要查看健康度，可以看这里：[Codex报重大 bug！SSD正在被加速磨损](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247518338&idx=1&sn=4c96d9ca3d661924f30e042d81b765c9&scene=21#wechat_redirect)

### 第四现场：手术方案

问题的本质找到了，一套只该在开发调试阶段使用的全量日志系统，被原样带进了正式版本，绑定在每一次 AI 流式输出上，持续不断地写向真实磁盘。

**既然写的内容没人需要长期保留，那就别让它碰真实磁盘，写到内存里去。**

这就是 **tmpfs（内存文件系统）** 方案的原理。它是操作系统提供的一种特殊"磁盘"，挂载之后，看起来和普通文件夹一模一样，但它的存储介质其实是内存（RAM），不是 SSD。系统重启，内存清空，这个"磁盘"上的所有内容自动消失。

操作步骤分四步，每一步对应的命令如下：

**第1步：退出所有 Codex 进程**

# 先确认还有哪些codex进程在跑
pgrep -fl codex
# 手动逐个退出(Ctrl+C / exit),不建议用 kill -9,避免正在进行的会话丢内容

**第2步：挂载一块内存盘**

# 建挂载点
mkdir -p ~/.codex/log\_ramdisk
# 挂载512MB的内存文件系统(tmpfs),这一步需要sudo密码
sudo mount\_tmpfs -s 512m ~/.codex/log\_ramdisk
# 验证挂载成功
mount | grep log\_ramdisk
# 应该看到: tmpfs on /Users/pan/.codex/log\_ramdisk (tmpfs, local)

**第3步：备份旧日志，建符号链接接管**

# 把旧的199MB日志文件挪走,不直接删,留个底
mv ~/.codex/logs\_2.sqlite\* ~/Downloads/ 2>/dev/null
# 关键一步:用符号链接把原路径指向内存盘里的同名文件
ln -s ~/.codex/log\_ramdisk/logs\_2.sqlite ~/.codex/logs\_2.sqlite
# 验证链接生效
ls -la ~/.codex/logs\_2.sqlite
# 应该看到: logs\_2.sqlite -> /Users/pan/.codex/log\_ramdisk/logs\_2.sqlite

![](attachments/5dd9e779171270c4.png)

第4步：重新启动 Codex，验证写入介质确实变了

# 重新打开一个codex会话,正常使用一会儿
codex
# 另开一个终端,确认当前持有日志文件的进程,及其写入设备
lsof ~/.codex/logs\_2.sqlite
# 关键判断:对比DEVICE字段,是否还是之前的真实磁盘编号(如 1,14)
# 如果变成了类似 52,28 这种不同的编号,说明已经切换到内存盘

### 第五现场：复检

手术做完了，有没有效果，用数据说话。

技术人员把同样的 `lsof` 检查重新跑了一遍：

codex 44584 ... /Users/pan/.codex/log\_ramdisk/logs\_2.sqlite
DEVICE = 52,28

设备编号，从原来的 `1,14`（真实SSD分区）变成了 `52,28`（内存盘）。**同一个程序，同一份日志，写入的物理介质，彻底换了。**

几分钟的使用之后，这个文件已经在内存里涨到了将近8MB。这些数据，如果是之前，会一字不差地刻进SSD，现在，它们只存在于内存里，系统重启的瞬间，会和那些垃圾日志一起，彻底消失，不留一丝痕迹在硬盘上。

### 真相大白！

本期节目录制期间，一份来自 Codex 官方仓库的 issue（#28224）浮出水面，把之前所有的猜测，变成了有据可查的事实。

提交者在自己的机器上连续跑了21天，统计出主SSD在这21天里被写入了约37TB数据。按这个速度换算一年——**约640TB**。一块1TB的SSD，一年被这么写，相当于把整块盘从头到尾完整擦写640遍。而市面上主流消费级SSD的寿命标定（TBW）通常在600TB左右——**这意味着，光是这一个后台日志进程，理论上能在不到一年的时间里，把一块全新SSD的质保寿命基本耗尽。**

issue 里附的数据库内部统计，比我们之前的实验测得更细：

| 级别 | 占用空间 | 占比 |
| --- | --- | --- |
| TRACE | 732.5 MiB | 70.7% |
| INFO | 266.5 MiB | 25.7% |
| DEBUG | 30.6 MiB | 3.0% |
| WARN | 5.9 MiB | 0.6% |

issue 作者还做了一个和本期节目如出一辙的实验。

15秒的采样窗口里，数据库保留的行数完全没变，但内部的行ID往前跳了**36211。**

证明这是一种"插入-裁剪"循环。数据先写进去，建索引，写进WAL，再被裁剪掉，表面上数据库大小不变，底层却经历了好几轮真实的磁盘写入。这和我们之前观察到的"文件大小不变，但mtime一直在跳"，是同一个现象的两种验证方式。

而真正的"案发现场"，是一行代码：

Targets::new().with\_default(Level::TRACE)

这一行，把SQLite日志接收端的**全局默认级别钉死在了TRACE**。

这也解释了一个之前没想明白的细节，为什么有人设置了环境变量 `RUST_LOG=warn` 却完全没用。

因为这个开关控制的是别的日志通道，专门往SQLite里写的这一路，压根没有看它的脸色，一直按自己钉死的TRACE级别往里灌。

截至本期节目录制时，已经有多名社区开发者准备好了修复分支，但提交PR时都遇到了同一个权限报错（`does not have the correct permissions to execute CreatePullRequest`）。

### 民间偏方大全

官方修复还没落地，社区已经先一步交出了几种本地应对方案，思路各不相同，值得放在一起比较：

**方案一：SQL触发器，从数据库层面直接拒收**

有开发者在 `logs` 表上加了一个 `BEFORE INSERT` 触发器，专门拦截：

CREATE TRIGGER IF NOT EXISTS codex\_drop\_noisy\_logs
BEFORE INSERT ON logs
WHEN
  NEW.level IN ('TRACE', 'DEBUG')
  OR NEW.target IN ('codex\_otel.log\_only', 'codex\_otel.trace\_safe', 'log')
  OR NEW.target LIKE 'hyper\_util%'
  OR NEW.target LIKE 'opentelemetry\_sdk%'
BEGIN
  SELECT RAISE(IGNORE);
END;

效果立竿见影——实测同样20秒的窗口，插入量从几千条降到个位数。但提出方案的人自己也坦白了局限：**这条日志在被SQLite拒绝之前，Codex内部还是要先把它格式化、排进队列**，触发器只是在最后一步把它挡在门外，CPU上的那部分开销并没有真正消失，只是没让它落盘。

**方案二：定时截断WAL，配合cron**

如果不想动数据库结构，更轻量的办法是定期手动执行一次checkpoint，把WAL文件主动收回：

sqlite3 ~/.codex/logs\_2.sqlite "PRAGMA wal\_checkpoint(TRUNCATE);"

配合 `crontab` 每15分钟跑一次，能防止WAL文件无限膨胀，但治标不治本——背后的写入行为照样在发生。

**方案三：暴力清场，适合磁盘已经告急**

如果磁盘已经被写满，需要立刻抢救空间，社区也给出了更激进的脚本：找出所有占用着这几个文件的进程，先 `SIGTERM` 再 `SIGKILL`，然后直接删掉 `-wal`/`-shm` 文件释放空间。这种方式简单粗暴，但代价是会强制中断正在运行的Codex会话。

第六现场：双重加固

理论讲完了，节目组决定不只是纸上谈兵，在已经做完内存盘迁移的这台机器上，再叠加一层"方案四"，亲手验证一次"双重防护"到底能不能落地。

用的是社区里流传的一个更简单粗暴的版本，不挑级别、不挑target，直接对`logs`表的所有插入说不。

import sqlite3, pathlib
p = pathlib.Path.home() / '.codex' / 'logs\_2.sqlite'
con = sqlite3.connect(p)
con.execute(
    'CREATE TRIGGER IF NOT EXISTS block\_log\_inserts '
    'BEFORE INSERT ON logs BEGIN SELECT RAISE(IGNORE); END;'
)
con.commit()
con.close()
print(p)

值得注意的是，这台机器上 `~/.codex/logs_2.sqlite` 此刻已经是一个指向内存盘的符号链接——但脚本完全不需要关心这一点。`sqlite3.connect()` 只是按路径打开文件，操作系统会自动帮它跳转到符号链接背后的真实位置，不管那个位置是真实磁盘还是内存盘，这一层对程序是透明的。

执行完，立刻做了一次验证查询，确认触发器真的挂上了：

con.execute(
    "SELECT name, tbl\_name FROM sqlite\_master WHERE type=? AND name=?",
    ('trigger', 'block\_log\_inserts')
).fetchall()
# 返回: [('block\_log\_inserts', 'logs')]

到这一步，这台机器同时叠了两层防护：**内存盘负责兜底，**就算还有日志漏网写进来，也只会落在内存里，绝不沾SSD，**触发器负责掐源头，**绝大多数新日志行，连写进数据库这一步都过不去，直接在插入语句层面被拒绝。

### 尾声

整件事说到底，不是什么离奇的故障，而是一个再普通不过的设计疏漏。一套用于调试的日志系统，忘了在正式发布前关掉它的"详尽模式"，又恰好绑在了一个高频触发的流式接口上，日积月累，变成了悬在SSD寿命头上的一把钝刀。

截至本期节目录制，根因已经被精确定位到一行代码，社区也已经准备好了修复分支，但卡在权限问题上，还没能真正合并进主线，在官方版本发布之前，普通用户能做的，依然只有本地自救。

科学的尽头，有时候只是少一个空格的配置开关，但找到它的过程，本身就值得被记录下来。

本期节目，到这里就结束了。

 

作者提示: 内容由AI生成
