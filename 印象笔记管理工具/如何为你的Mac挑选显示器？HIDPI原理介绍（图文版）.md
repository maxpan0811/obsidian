# 如何为你的Mac挑选显示器？HIDPI原理介绍（图文版）

---

原文链接: [https://mp.weixin.qq.com/s?chksm=c1ec815bf69b084d82b67792404710e...](https://mp.weixin.qq.com/s?chksm=c1ec815bf69b084d82b67792404710e3317ab4b75515fd6f2374841c03ba677868d77074ecea&exptype=unsubscribed_card_recommend_article_u2i_mainprocess_coarse_sort_tlfeeds&ranksessionid=1745847913_3&scene=169&mid=2247483951&sn=e1d6692f81550435f1bb8426af186984&idx=3&__biz=MzkyMjg2NzIyNw==&sessionid=1745847822&subscene=200&clicktime=1745849771&enterid=1745849771&flutter_pos=40&biz_enter_id=5&jumppath=20020_1745849713424,1104_1745849714106,20020_1745849732705,1104_1745849744143&jumppathdepth=4&ascene=56&devicetype=iOS18.4.1&version=18003b24&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ7YeUHQdkhZ9f28veXj26BRLVAQIE97dBBAEAAAAAAMH1A+RCyOYAAAAOpnltbLcz9gKNyK89dVj0xK8si0j4cqYUxyApi4TIr/CO7qnVX5NYZ5eZe5qWu6kLYcEPwXA7ZNIMbLnvyX4yev1R2BLIS8FnR3gLQHGnTsnPDWMD5dEM1g7X49b1t3zvYPMPTzAqf6YxG0FzgPLgrQvLaDhC07TA5dQhbAJOiN0C9wLHj+GoxD/UK3uM7SWy1GSdH3Z23N/5vryPZWoEU3Gd8W6u6aj297jFdpUNKRWD40/0pohtDWYZUYiuyw==&pass_ticket=XNc9bnUlYwCIXCW0s2EMtlDnmy1Ye5xZiPROEQU8AjoFG7suskkfAPEnsHR7GMO6&wx_header=3)

OriginalTech科技小迷糊Tech科技小迷糊

hello，大家好，我是小迷糊，最近有很多人在问我如何为他的Mac mini挑选一个合适的显示器。恰好我前段时间也一直在挑选显示器，那今天就来讲一讲苹果Hidpi的显示原理，了解了这个原理之后，我将通过这个原理来教大家如何为你的Macmini挑选一款合适的显示器，那我们开始吧~

苹果显示器HiDPI的显示原理

如果你为你的Mac电脑外接了一台4K的显示器，你或许会在设置中发现，系统为他默认选择的分辨率是1920\*1080，也就是1080P的分辨率，那这是不是浪费了你的4K显示器呢？此时，如果你把你的显示器调整到4k，你就会发现，所有窗口和文字变得非常的小，我们需要离得非常近才能看清显示器所显示的内容。而在1080P分辨率的旁边，你可能会发现一个括号，上面写的Hidpi，没错，这就是苹果的Hidpi技术。如果要了解这个技术，我们先来了解一下Mac系统显示内容的原理。当然，我们今天讲到的只是简单易懂的原理解释，而实际上的显示步骤要比我今天讲的复杂得多。首先我们要知道，我们的屏幕之所以能显示不同的内容，是因为，屏幕是由一个个像素点组成的，像素点越小，在相同大小的屏幕上的像素点就越密集，我们屏幕的分辨率就越高。显示的效果也就越精细，所以看起来也就越清晰。我们所说的1080P的分辨率，通常情况下是说这个屏幕的长是由1920个像素点组成，而宽由1080个像素点组成。

![](.evernote-content/F4099269-8145-4315-928D-3470E1BD1D01/16AC9B5F-AEFB-4F26-B3CA-F9F5F5C15586.png)

在正常渲染分辨率的时候，我们的窗口和字体大小是由像素作为单位来渲染的，也就是说一个像素将渲染成显示器上的一个像素点，比如我们打开一个500\*300的窗口，就会将他的长用500个像素点来显示，而宽用300个像素点来显示。那它显示在1080P分辨率的屏幕上时就是这么大。

![](.evernote-content/F4099269-8145-4315-928D-3470E1BD1D01/3E5ED97D-3E84-4521-8DDD-5B09B42B5F09.png)

那如果此时我换成了4K分辨率，由于4K分辨率的像素密度更大，在同样的屏幕大小下的长和宽正好是1080P分辨率的2倍，所以同样的屏幕大小，每个像素点的大小也就变成了之前的1/4，那同样显示500\*300的一个窗口，大小也就变成了之前的1/4。

![](.evernote-content/F4099269-8145-4315-928D-3470E1BD1D01/66D4CACB-8515-4020-BFFB-68BF0E1B06B2.png)

如果按照这种显示的话，分辨率越高的屏幕，文字和视图就越小，这显然并不是用户想要达到的效果，我们想要的效果其实是分辨率越高，字体和视图的大小都不变的情况下变得清晰。苹果为了解决这个问题就诞生了Hidpi的显示模式。简单说就是苹果将多个像素点融合成了一个虚拟的显示单位，苹果将它叫做Dot，也就是点。而这些融合之后的点构成了一个新的分辨率，苹果将它称之为逻辑分辨率，那我们之前说的屏幕真正像素点所对应的分辨率被称之为物理分辨率。苹果将屏幕上像素的大小换算成点，并且配合成一定的算法，处理一下点和像素的对应关系，就有了我们所能在Mac上看到的清晰的图像。以我刚刚购买的这块4K显示器为例，它的物理分辨率为3840\*2160，连接Mac之后的默认逻辑分辨率是1920\*1080，我们发现他们的关系刚好是4倍，也就是苹果会将屏幕的4个像素点共同配合来显示1个点的内容，换算成1个像素点来显示，所以显示在屏幕中的图像大小和1080分辨率时的大小相同，但是由于每个点其实是包含4个物理像素，并且Hidpi会使用一些算法来处理边缘，使其变得更加的清晰，所以我们虽然看到的大小相同，但是内容却更加的清晰锐利。

![](.evernote-content/F4099269-8145-4315-928D-3470E1BD1D01/5F671F5C-2DC8-4EEB-9C90-17175A27AE2F.png)

所以结论就是，在4K显示器上显示1080P的内容，你并没有浪费你显示器的像素。相反，他变得更加清晰了。以上就是Hidpi的简单的原理介绍。刚才也说了，真正显示的时候其实比这个要复杂的多，比如如果缩放的倍数是非整数倍，最常见的例子就是用4K的物理分辨率显示2K的逻辑分辨率，那由于4K的长宽是2K的1.5倍，那这个时候就出现了0.5个像素的情况，而此时苹果会先渲染超过你显示器分辨率的布局，也就是将显示放大到5K分辨率然后在缩小到你屏幕大小来显示，而最终才显示你选择的逻辑分辨率。这其实也是苹果所有27寸显示器都使用5K分辨率的原因。他省去了一步放大和缩小的步骤，节省了处理器的性能。

![](.evernote-content/F4099269-8145-4315-928D-3470E1BD1D01/CD5979EA-CB58-4B9E-94ED-5912CA17B039.png)

如何挑选合适的显示器？

那了解完Hidpi，我们接下来就来了解下如何选择合适的显示器了。根据刚才的原理，只有缩放达到整数倍的时候，才不会消耗系统的性能。我们可以看到目前主流的分辨率，

4K的长宽是1080P的2倍，而5K的长宽是2K的2倍，也就是说如果你有一个5K分辨率的显示器，那4像素合一显示之后，可以达到逻辑分辨率2K的效果，刚刚我们说过了，这也是为什么苹果自己的27寸显示器都做成5K的原因，因为他可以很轻松的显示成2K分辨率。

![](.evernote-content/F4099269-8145-4315-928D-3470E1BD1D01/A59F7CE3-4BE9-4BE4-B57F-4E2A71703E11.png)

那如果你买 的是一块4K屏幕，最适合的方式是将逻辑分辨率调整到1080P，那么问题来了，如果你是使用27寸的显示器，逻辑分辨率选择1080p的话，字体和图标仍然会较大，不能充分的利用这块屏幕。所以，正确的做法是将分辨率调整成2K，但是这必然会损失Hidpi的效果。那经过以上的介绍，我们开始得出购买显示器的最佳结论，如果你想要为你的新Mac选择显示器，最低选择4K分辨率。如果你购买的是24寸显示器，那么4K分辨率可以达到你想要的效果，如果你购买的是27寸显示器，最佳的分辨率是5K，但是当前市面上5K分辨率的显示器很少，除了苹果自家的studio Display，也就小众的几个厂家在做。比如我之前看的未来视野的这款，感觉也很不错。如果你想购买大厂的显示器，那只能退而求其次，购买4K分辨率的显示器。目前市面上27寸4K分辨率的显示器是非常多的，也不乏有一些性价比的产品，比如红米的那款27寸4K显示器。那我呢因为我桌面大小的限制。我自己前段时间购买的是24寸显示器，其实，24寸4k的显示器在市面上也是不多的。我在网上一共也就找到了三四款。 我购买的这款是AOC的这款24寸4K显示器，显示效果还是不错的。

![](.evernote-content/F4099269-8145-4315-928D-3470E1BD1D01/5476BE36-2B75-4CA8-9CD6-FB004A7A1643.png)

另外大家要注意的点就是最好购买具有充电和显示二合一的这种接口的显示器，这样如果你以后接MacBook的话，一根线就能搞定充电和显示。另外因为我的显示器支持HDR400，我发现如果我连接的是HDMI接口的话，如果在系统中开启高动态范围显示，在显示一些鲜艳颜色比如红色的时候会有色彩溢出，后来查阅了一些资料发现是苹果HDMI传输数据的限制，换成TypeC接口连接显示器就正常了。

OK，这就是本期的全部内容了，如果大家觉得对你有所帮助的话，欢迎点赞收藏，同时别忘了关注我了解更多科技内容。我是科技小迷糊，带你玩转数码不迷糊，我们下篇文章再见喽~

个人观点，仅供参考

---

[🌐 原始链接](https://mp.weixin.qq.com/s?chksm=c1ec815bf69b084d82b67792404710e3317ab4b75515fd6f2374841c03ba677868d77074ecea&exptype=unsubscribed_card_recommend_article_u2i_mainprocess_coarse_sort_tlfeeds&ranksessionid=1745847913_3&scene=169&mid=2247483951&sn=e1d6692f81550435f1bb8426af186984&idx=3&__biz=MzkyMjg2NzIyNw==&sessionid=1745847822&subscene=200&clicktime=1745849771&enterid=1745849771&flutter_pos=40&biz_enter_id=5&jumppath=20020_1745849713424,1104_1745849714106,20020_1745849732705,1104_1745849744143&jumppathdepth=4&ascene=56&devicetype=iOS18.4.1&version=18003b24&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ7YeUHQdkhZ9f28veXj26BRLVAQIE97dBBAEAAAAAAMH1A+RCyOYAAAAOpnltbLcz9gKNyK89dVj0xK8si0j4cqYUxyApi4TIr/CO7qnVX5NYZ5eZe5qWu6kLYcEPwXA7ZNIMbLnvyX4yev1R2BLIS8FnR3gLQHGnTsnPDWMD5dEM1g7X49b1t3zvYPMPTzAqf6YxG0FzgPLgrQvLaDhC07TA5dQhbAJOiN0C9wLHj+GoxD/UK3uM7SWy1GSdH3Z23N/5vryPZWoEU3Gd8W6u6aj297jFdpUNKRWD40/0pohtDWYZUYiuyw==&pass_ticket=XNc9bnUlYwCIXCW0s2EMtlDnmy1Ye5xZiPROEQU8AjoFG7suskkfAPEnsHR7GMO6&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/7031ec5e-0af2-4d65-97cc-aa41fa85abae/7031ec5e-0af2-4d65-97cc-aa41fa85abae/)