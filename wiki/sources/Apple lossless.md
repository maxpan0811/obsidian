---
title: Apple lossless
type: source
created: 2026-07-09
updated: 2026-07-09
source_path: 印象笔记管理工具/Apple lossless.md
tags: [印象笔记]
---

# Apple lossless

---

**本文以Apple lossless为例，iTunes Plus AAC的转化与Apple lossless转化步骤完全相同，只是选择不同的编码器而已，见文章最后  
  
写在前面：什么是Apple lossless**   
Apple lossless是苹果公司推出的一种无损的可逆音频压缩格式，进行音频转化时，像mp3,wma这种有损格式，其实在压缩的过程中，都是采用不可逆的压缩方式，这样在压缩时通过减少数据得到高压缩率，起到节约磁盘空间的作用。可逆压缩(无损失压缩)与通常的文件压缩相同，可以将被压缩的数据完全回复成以前的数据。从原理性上来说,是完全不恶化音质的压缩方式。由于压缩率受到语音内容的很大影响,不能一概而论,但如果把音乐CD等作为音源，与其他的可逆压缩方式相比,常常可以压缩到一半到1/3左右。   
   
  
由于ipod，iphone目前只支持wav，apple lossless两种无损格式，wav这种格式想必大家再了解不过了，音质虽然非常好，但缺点也非常明显：文件体积太大！不少拥有ipod,iphone的朋友都是音乐发烧友，对于音质的追求也是相当之高，在电脑上听ape,flac无损，买了ipod却用来听mp3，想必心里不太舒服吧……而且ipod系列一直不支持ape,flac格式无损音频的播放，wav的体积又过于庞大，apple lossless这个格式更是鲜有人知，不过不用担心，下面我介绍一下自己转化apple lossless的方法，非常方便快捷，希望对追求无损音质的朋友们能有所帮助~   
   
  
**1.****准备：**  
1）要转化的音乐源（CD光盘，APE，FLEC格式的音频文件）   
2）Itunes，这个就不用说了   
3）WinMount（这是个什么东西？先别管他，下面详细介绍）官方下载地址：   
<http://cn.winmount.com/>   
   
  
什么是WinMount?(这里直接引用官方介绍)：   
  
WinMount是一款功能强大且免费的Windows小工具，具有压缩、解压、浏览压缩包的功能，也具有挂载DVD， CD，虚拟机硬盘镜像的功能。最大特色在于其首创读取压缩包新理念Mount，可以将压缩包直接挂载到虚拟盘中使用，无需解压，省时省空间。   
  
WinMount强力推出高压缩比高速率压缩格式MOU，用多少解多少。MOU采用随机解压算法，可以瞬时被Mount到虚拟路径中。   
  
   
  
**2.****开始转化：**   
  
注：这里讲的转化，不适用于分轨的ape,flac音频文件，分轨ape,flac的转化最后有介绍。   
  
1）首先在电脑上安装WinMount,然后打开itunes。   
2）在itunes的菜单栏中点“编辑—偏好设置”（下图）   

![](.evernote-content/3BFF6298-ADFF-4043-9424-52D5E826D937/2925C6E3-74B3-45EA-9712-B994D2B33708.jpg)

   
  
  
  
  
在新的窗口中点“**导入设置**”，此处如果你的电脑有internet连接，强烈建议勾选“**自动从****internet取回CD****轨道名称**”   

![](.evernote-content/3BFF6298-ADFF-4043-9424-52D5E826D937/EC0CAC25-E028-4258-A9FF-98F5927213F5.jpg)

   
  
  
选择“Apple Lossless编码器”，这样一旦插入CD时，itunes会使用Apple Lossless编码器进行对音频的转换，而且相应的，在itunes中对任意音乐文件点击右键，会出现“创建apple lossless版本”这一选项，此处要注明：如果你在前一步选择的是“选择Apple Lossless编码器”，那么这里对应出现的就是“创建apple lossless版本”，同理，如果选择的是AAC编码器，则此处显示的是“创建AAC版本”，以此类推。至于为什么要啰嗦这个，主要是为了以后的分轨ape,flac音频转apple lossless做好准备。   

![](.evernote-content/3BFF6298-ADFF-4043-9424-52D5E826D937/BCC6FC64-4EB3-4040-B8DE-4EBA1BFED416.jpg)

   
  
  
  

![](.evernote-content/3BFF6298-ADFF-4043-9424-52D5E826D937/1BA33001-F1E0-4F7B-A426-30EF9ADBBE33.jpg)

   
3）找到下载好的无损音频，这里以ape为例：   
  
你下完的无损音频，应该有两个文件，一个体积大的是.ape的音乐文件，一个体积很小的是.cue的索引文件，转化前，你需要确定下是否有这个.cue的索引文件和这个索引文件与ape音乐文件是否对应。   

![](.evernote-content/3BFF6298-ADFF-4043-9424-52D5E826D937/8DEB0F97-BEA3-4668-B67C-A02E96279C49.jpg)

   
  
右键单击.ape结尾的无损音乐文件，点击“Mount至新盘”   

![](.evernote-content/3BFF6298-ADFF-4043-9424-52D5E826D937/C0CC8436-3C54-4260-9FD3-65722CF7BF80.jpg)

   
  
  
此后会自动形成一个名为“Audio CD”虚拟光驱Z，然后你的ape文件就会以CD文件的形式展现：   

![](.evernote-content/3BFF6298-ADFF-4043-9424-52D5E826D937/C3401D66-54D8-44FB-BBC0-F1DE48E3645C.jpg)

   
  
  
与此同时，itunes也会自动读出虚拟光盘文件，并弹出是否导入CD文件的提示：   

![](.evernote-content/3BFF6298-ADFF-4043-9424-52D5E826D937/CD183FCF-9D49-405A-93D1-8675B4DD8829.jpg)

   
  
  

![](.evernote-content/3BFF6298-ADFF-4043-9424-52D5E826D937/B6AEC4C0-72C1-448A-B1AE-6B7107F012A2.jpg)

   
**这里说一下，为什么前面推荐勾选“自动从internet取回CD轨道名称”****，**原因很简单，如果勾选那个选项的话，如果你的电脑有internet连接，itunes就会自动联网搜索媒体库，找到相匹配的CD文件，自动为你的CD音乐添加分轨信息（名称，表演者，专辑，风格，发行年代，等等），再也不需要手动一个个的编辑音乐信息了，省去了大量的时间！   
4）点击“是”就开始了CD的导入，转化速度非常快，像这张专辑的11首歌，仅用了1分钟就转完了，转化平均速度在60x左右   
找不到音频转到哪里去了？不用着急，在媒体库找到转化完的专辑，右键，点击“在windows资源管理器中显示”，系统会自动给你找到音频的位置，vista下默认会在：   
**C:\Users\你的用户名\Music\iTunes\iTunes Media\Music**中   
  

![](.evernote-content/3BFF6298-ADFF-4043-9424-52D5E826D937/B6BB6717-7CFA-4B35-916D-7D9BD15E538A.jpg)

  
而且你会发现，转化后的音频非常有序，全部在Music文件夹下以“艺术家\专辑”的文件价格式保存，而且每个曲目的名字也都命名好了，是不是很方便啊~   
  
对于平均每首歌4分钟，共11首歌的CD专辑来说，整张专辑转化为Apple lossless大概需要300M的空间，对于那些觉得自己ipod填不满的朋友来说，用无损填满你的ipod吧~   
   
  
**对于分轨flac,ape音频的转化：**   
  
分轨flac,ape，就不能用winmount导入的方法来转apple lossless了，因为分轨很少附带.cue文件的，即使附带了，一个个地导入flac,ape文件也非常麻烦，常用转化方法有两种：   
   
  
1.先用foobar,千千静听将flac,ape转为wav格式，再用itunes导入wav音频，选中后右键“转化为apple lossless格式”：   
  
这种方法貌似比较复杂，而且很多人担心ape，flac转wav时，会造成音质损失，其实不然，wav可以算是最原始的音频格式了，音质也最接近CD音质，ape，flac的音质其实是不如wav的，因而进行转化的时候得到的仍是ape,flac音质，举个不是很恰当的例子，如果你用mp3音频来转apple lossless的话，得到的实际上仍是mp3质量的音频。此种方法虽然表面繁琐，但得到的音质一定是无损的apple lossless，而且操作多了也蛮快的，本人对于分轨文件一般都是这么转，主要因为不想装Foobar的原因= =   
   
  
2.用Foobar装载apple lossless解码器后，直接转化为Apple lossless音频：   
  
看这个帖子吧，虽然有些旧了，方法还是一样的，感谢cjwdljq：   
<http://bbs.feng.com/read-htm-tid-274167.html>   
   
  
**为什么不用Daemon Tool载入“.cue”文件？**   
  
Daemon Tool虽然表明支持导入.cue文件，但是实际导入的时候，会出BUG，无法识别cue文件，以致不能虚拟音乐CD（多数人都是这样，但也有少部分人一切正常，能够虚拟出音乐CD），相信我，winmount比daemon tool要好用得多……   
   
  
最后，给大家一个介绍itunes Plus AAC的网页，电驴上一位大大发的，非常详细地介绍了itunes Plus AAC，以及与Flac,Ape等无损音乐的对比，人家辛苦写的，我就不好转贴了，大家去看看吧~~   
<http://www.verycd.com/groups/@g2381491/757876.topic>   
   
  
希望能对大家有用~~~

---

[🌐 原始链接](http://bbs.feng.com/read-htm-tid-616230.html)

[📎 在印象笔记中打开](evernote:///view/207087/s1/650a8415-e18b-4bac-a658-c5495fc81644/650a8415-e18b-4bac-a658-c5495fc81644/)
