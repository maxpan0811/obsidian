# Excel 菜鸟PP周记（一）为什么PowerPivot-Excel数据透视表-ExcelHome技术论坛 -

---

|  |
| --- |
| [[原创]](http://club.excelhome.net/forum.php?mod=forumdisplay&fid=123&filter=typeid&typeid=127) 菜鸟PP周记（一）为什么PowerPivot   [[复制链接]](http://club.excelhome.net/thread-1029448-1-1.html) |

|  |  |
| --- | --- |
|  |  |

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| [tc0098](http://club.excelhome.net/home.php?mod=space&uid=1684828)    |  |  |  | | --- | --- | --- | | [16](http://club.excelhome.net/home.php?mod=space&uid=1684828&do=thread&type=thread&view=me&from=space) 主题 | [137](http://club.excelhome.net/home.php?mod=space&uid=1684828&do=thread&type=reply&view=me&from=space) 帖子 | [22](http://club.excelhome.net/home.php?mod=space&uid=1684828&do=profile) 鲜花 |  .  *[EH初级](http://club.excelhome.net/home.php?mod=spacecp&ac=usergroup&gid=11)*    积分  [137](http://club.excelhome.net/home.php?mod=space&uid=1684828&do=profile)  技术  0 .  .   * [发消息](http://club.excelhome.net/home.php?mod=spacecp&ac=pm&op=showmsg&handlekey=showmsg_1684828&touid=1684828&pmid=0&daterange=2&pid=7017603&tid=1029448 "发消息") .  *[TA的精华主题](http://club.excelhome.net/plugin.php?id=k_thread_echome:guide&view=myfdigest&fuid=1684828)*  *[TA的得分主题](http://club.excelhome.net/plugin.php?id=k_thread_echome:guide&view=myffen&fuid=1684828)* | 电梯直达 **[*1*楼](http://club.excelhome.net/thread-1029448-1-1.html)** *发表于 2013-6-22 16:29* | [只看该作者](http://club.excelhome.net/forum.php?mod=viewthread&tid=1029448&page=1&authorid=1684828) |[只看大图](http://club.excelhome.net/forum.php?mod=viewthread&tid=1029448&from=album)  [★财务、会计、人力资源、行政、生管、销售、市场：Excel 行业应用系列视频课程精彩放送中★](http://club.excelhome.net/thread-1118002-1-1.html)  本帖已被收录到知识树中，索引项：[Powerpivot](http://club.excelhome.net/tree/index-39.html)  |  | | --- | | *本帖最后由 tc0098 于 2013-6-22 16:29 编辑*     最近接触了PowerPivot，打心底觉得这是一个很好很强大的东西，借ExcelHome这块宝地分享一下这个强大的Excel新功能，同时也记录一下自己的学习历程吧！    如果把Pivot Table比作是计算器的话，那么PowerPivot就是科学计算器。以前用Pivot很复杂或者根本做不到的事情，PowerPivot可以以简单的方式解决。    先来说一下为什么要用PowerPivot吧。    PowerPivot是一个Self-ServicedBusiness Intelligence System。比起SAP, Oracle等 ERP系统，PowerPivot虽然没有那么多功能，容纳不了全球化的数据，但灵活程度和对数据的分析能力远超过它们；比起Excel，灵活度稍稍降低（比Pivot Table要更灵活，但所用的公式会受到限制），但处理大的数据没有任何压力（Excel超过10万行，来点公式就开始死机）。    理论上PowerPivot的每个sheet可以容纳1万亿（1 million million）的行和列，一个文件可以有几GB，还能以很快的速度处理这么大的数据，对于一般的公司数据，容量上完全不成问题（虽然我没有试过几亿行的数据，但运行个几百万行，50MB的文件没有任何问题，而且我还用的是32位的Office系统（适用于XP），运算能力远低于64位office系统（适用于Win7））。    PowerPivot最有趣的地方是引入了强大的新功能，度量值Measure，一个类似于公式的东西（叫DAX Formula），大大加强了Pivot的灵活性。    上个很有意思的度量值应用例子：    一个小小的PowerPivot数据库，然后可以写一个Dax formula （度量值）： =Sum(data[Sales])，把Data表中的Sales这个列求和     然后你可以把这个度量值拉到Pivot里边！（和普通的pivot很不同吧，但好像没什么用啊？）      然后想知道上年的Sales是多少做比较，同样道理，先要写个度量值Measure关于上年的Sales  PY Sales:=IF(HASONEVALUE(data[Year]),CALCULATE([SalesValue],ALL(data[year]),FILTER(all(data[year]),data[year]=VALUES(data[year])-1)),blank())  （先不要理会这些细节了，意思是什么以后再说）   同样，把这个度量值拉到Measure里边可以得到这样的结果：  （2011因为是第一年就没有了上年的Sales）     再写一个增长率的度量值：  Growth:=IFERROR( [SalesValue]/[PY Sales]-1,BLANK())     如果你只想看增长率，直接把其他的度量值弄走就好了：     感觉很酷对吗？至少我觉得是的！    作为一个非IT专业的小员工，对SQL，SAP什么的高级工具一窍不通（不要让个学会计金融的搞编程了吧。。。），PowerPivot大大加强了我分析复杂大量数据的能力，而且简单易学，这就是我极力推荐这款Self-Served BI的原因了！    如果你也像我这样，不懂复杂的IT技术，却又需要分析大量的数据，请加个好友，一起来讨论PowerPivot的技术吧！ | |

---

[🌐 原始链接](http://club.excelhome.net/thread-1029448-1-1.html)

[📎 在印象笔记中打开](evernote:///view/207087/s1/58cef2a1-1784-4e61-8482-72cd1b98bdf9/58cef2a1-1784-4e61-8482-72cd1b98bdf9/)