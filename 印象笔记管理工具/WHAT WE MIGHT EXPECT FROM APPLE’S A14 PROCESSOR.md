# WHAT WE MIGHT EXPECT FROM APPLE’S A14 PROCESSOR

---

Macworld Digital Magazine U.S.
==============================

FEATURE

WHAT WE MIGHT EXPECT FROM APPLE’S A14 PROCESSOR

APPLE MAKES THE FASTEST MOBILE CHIPS IN THE BUSINESS, AND WE EXPECT NOTHING LESS FROM THE A14 THIS FALL.

**BY JASON CROSS**

![](.evernote-content/F8C66CE8-1949-4025-8DFA-694CEA152BD0/E16B580F-116A-4F65-B559-85E8D161F35C.jpg)

(IMAGE: ANDY / GETTY IMAGES)

**W**e aren’t likely to hear anything about Apple’s new phone processor until September, when the company unveils the iPhone 12. But it takes years to design these chips and months to get production ramped up, so the A14 is likely already set in stone and has probably begun test production.

Year after year, Apple’s phone chips have held the crown for overall performance, and despite some big promises from the likes of the Qualcomm Snapdragon 865, we expect Apple to hold the crown when the new iPhones are released this year.

One can never tell exactly what features or performance an unannounced A-series processor will deliver, but we can make some informed guesses. Here’s what we think we might see from Apple’s A14 SoC later this year.

![](.evernote-content/F8C66CE8-1949-4025-8DFA-694CEA152BD0/9CF9C018-132F-413F-A20F-24E44A5D9FB8.jpg)

**A JUMP TO 5NM MANUFACTURING**
-------------------------------

For the third year in a row, Apple will benefit from manufacturing process improvements at its manufacturing partner TSMC. The A12 was built on a 7nm process, the A13 was made on an enhanced 7nm process that primarily allowed for faster clock speeds and lower power consumption (when running at the same speeds as chips made with the prior 7nm process).

This year, Apple could make the jump to TSMC’s brand-new 5nm process. In fact, it’s likely to be the first large-scale consumer chip to ship using it.

This is a big upgrade. The 5nm mode is not a half-step by any stretch, but it is the next “full node” after 7nm. It uses extreme ultraviolet (EUV) lithography extensively throughout the process, and TSMC says it delivers 80 percent more logic density and can run either 15 percent faster at the same power as its 7nm chips, or 30 percent lower power at the same performance level.

Of course, design matters, too. Apple won’t necessarily meet these exact figures. But on manufacturing process alone, the A14 would be a significantly faster and more power-efficient chip.

**A BIG TRANSISTOR BUDGET**
---------------------------

The A13 measures around 98.5mm2, which is roughly 20 percent larger than the 83.2mm2 A12. That’s only slightly smaller than my original prediction last year, but my assumption about transistor budget was way off.

I assumed Apple would use TSMC’s N7+ node, which affords increased transistor density. Instead, Apple opted for the N7P mode, which does not. As a result, the A13 has about 8.5 billion transistors, rather than the 10 billion I predicted.

![](.evernote-content/F8C66CE8-1949-4025-8DFA-694CEA152BD0/1057FBA1-D8E1-4AD6-B813-E9976E923180.jpg)

**WikiChip has an excellent summary of the various process technologies from TSMC at go.macworld.com/wchp.**

For this year, I think Apple is likely to keep the processor around the same overall size. About 100mm2 is a good size for a high-performance premium mobile processor with a lot of stacked components.

If we take TSMC at its word about the improved transistor density of the 5nm process, we’re looking at an incredible 15 billion transistors. That’s more than all but the largest high-end desktop and server CPUs and GPUs. It’s huge. It’s so big that I wouldn’t be entirely surprised if Apple shrunk the total chip area a bit to around 85mm2 and around 12.5 billion transistors.

Transistor count by itself is a poor means of estimating processor performance, but it does tell us how much “room” Apple has to work with. It means more cores, or bigger cores, or more cache, or any combination of these improvements.

**CPU PERFORMANCE**
-------------------

For the A13, Apple didn’t do a lot to change its fundamental CPU architecture. It’s still the same number of cores, and the cores aren’t dramatically different. Instead, the company relied on the faster clock speeds afforded by the enhanced 7nm process to improve performance.

In single-threaded performance, the A13 delivers a 20 percent improvement on the A12 (in Geekbench 5). It’s a bit more than I predicted it would be last year, and the fastest mobile CPU around.

![](.evernote-content/F8C66CE8-1949-4025-8DFA-694CEA152BD0/B51509F4-EBEA-4B1A-ABC3-62D664ACBF50.jpg)

**Single-threaded performance is expected to improve, but not as much as multi-threaded performance.**

Simply following the trend line (which is quite consistent for recent A-series processors) we could expect the A14 to score close to 1,600. The 5nm process alone should be about 8 percent faster than the enhanced 7nm process Apple uses in the A13, which would give us a score in the mid-1,400s. My guess is that Apple will likely wind up in the 1,500-1,600 range, due to both higher peak clock speeds and some architectural improvements made possible by the much higher transistor budget.

Multi-core performance is harder to predict. The A12 and A13 had four small high-efficiency cores and two big high-performance cores. Apple already very efficiently schedules workloads to take advantage of all cores as much as possible, so it’s unlikely that we’ll see a big improvement from better scheduling. But with the big jump in transistor density from 5nm, Apple might add a third big core, or significantly boost performance of the high-efficiency cores, which would really boost multi-threaded performance.

![](.evernote-content/F8C66CE8-1949-4025-8DFA-694CEA152BD0/7020D465-0B70-4563-83F4-70718710BA4A.jpg)

**Multi-threaded performance would go up if Apple didn’t add more cores, but that’s a conservative prediction. I expect more.**

The trend line gives us a score around 4,500, but I think a combination of architectural changes and clock speed will give us a lot more. I wouldn’t be surprised if the Geekbench 5 multi-core score creeps up to 5,000 or so.

For what it’s worth, the fastest Android phones score around 3,000 on this test, and a score of 5,000 would be similar to 6-core mainstream desktop CPUs or high-end laptop CPUs. It’s 15-inch MacBook Pro territory.

**GRAPHICS PERFORMANCE**
------------------------

The iPhone has been, from the very debut of the App Store, a gaming device. But gaming has never been more important to Apple than it is now with its Apple Arcade service. Graphics performance makes games shine, true, but the GPU is also used for computational functions in image processing, machine learning, and plenty of other tasks.

In other words, GPU performance is critical and Apple is not going to tread water with the A14.

If we take a look at the 3DMark Sling Shot Extreme Unlimited test, performance took a dramatic leap in the A13—far beyond what recent trends would have predicted. I expected a score around 4,800, and Apple delivered well over 6,000! It was enough to beat the latest Android phones, but newer models have since pushed a little higher, and top-tier Android phones released this year will go much further.

![](.evernote-content/F8C66CE8-1949-4025-8DFA-694CEA152BD0/F353945A-FFFF-4D23-ACA8-FF1FFA1CCE5B.jpg)

**Graphics performance took a big leap with the A13. I think the A14 will deliver a similar leap.**

I expect Apple to expend significant transistor budget making the GPU more powerful. Along with more memory bandwidth, we can probably expect GPU performance well beyond the trend line’s prediction of the low 7,000 range in this test. Barring some new performance bottleneck, I think a score over 9,500 is certainly possible. In other words, I think we can expect a 50 percent improvement in graphics performance for the kind of high-end graphics used in games.

![](.evernote-content/F8C66CE8-1949-4025-8DFA-694CEA152BD0/177BFDAF-1E3D-457C-B59A-56F11402D447.jpg)

**GPU Compute is increasingly important. I wouldn’t be surprised if it’s 50 percent faster in the A14.**

When it comes to using the GPU for computation, I think we can expect a similar speed bump. A bigger GPU plus faster clock speeds and more memory bandwidth could give us 50 percent or more—making the Geekbench 5 compute score jump to the 9,500 to 10,000 range.

![](.evernote-content/F8C66CE8-1949-4025-8DFA-694CEA152BD0/E6A9AF67-0E14-4E60-AABF-AF35B64075BE.jpg)

**Apple added new matrix math hardware to the CPU in the A13. The A14 may not have a similar “new” feature but more Neural Engine cores seems like a reasonable expectation.**

**IMAGE PROCESSING AND NEURAL ENGINE**
--------------------------------------

The A-series processors do a lot more than just house CPU and GPU cores. They contain specialized hardware for specific tasks like image processing (to turn data from the cameras into stellar photos and video), video encoding and decoding, and a Neural Engine that powers machine learning tasks that are used throughout iOS.

In the A13, Apple added specialized hardware to handle matrix multiplications and an updated “machine learning controller” to balance those compute tasks among the various parts of the processor—CPU, GPU, and Neural Engine. It did not, as I predicted, add cores to the Neural Engine, but since all parts of the CPU, GPU, and NE run at higher clock speeds, performance improved.

This is an area Apple cares deeply about, and is a necessary part of improving photo and video quality, augmented reality, and many of Siri’s functions throughout the operating system. With the higher transistor budget afforded by the 5nm manufacturing process, I think Apple will add Neural Engine cores this time, and may make other architectural improvements as well.

It wouldn’t surprise me to see Apple claim that machine learning tasks are at least twice as fast as on the A13.

Apple doesn’t really provide performance details for its imaging processing engine, but the push for better camera quality is never-ending, so it’ll probably be better, too.

I’ll go out on a limb and say that I think the A14 will be Apple’s first chip with hardware decoding of the AV1 video codec, and might even have hardware encoding support. If so, expect Apple to spend some time on stage talking about how videos shot with the iPhone 12 are smaller and higher quality than ever before.

![](.evernote-content/F8C66CE8-1949-4025-8DFA-694CEA152BD0/E77B086A-B90B-4265-A239-12003DE95A6E.jpg)

**Samsung’s making LPDDR5 now, for phones shipping this year. Apple may be one of them.**

**FASTER LPDDR5 RAM**
---------------------

Apple has been using LPDDR4 memory in its iPhone SoCs for years. It first made the jump from LPDDR3 to LPDDR4 in the A9 in 2015, and then to LPDDR4x (a faster and slightly more power-efficient version) in the A11 in 2017. The A12 and A13 used the same RAM, as far as the teardowns can determine.

But we’re on the cusp of the next generation of low-power mobile memory. The spec for LPDDR5 was finalized last year, and already Samsung has begun production, with SK-Hynix (another popular RAM supplier for Apple) to begin soon. High-end Android phones will first ship with the RAM in the first half of this year, making it likely that the iPhone (at least the high-end models) will follow suit at the end of the year.

What’s the benefit? Well, the current LPDDR5 being produced by Samsung is about 30 percent faster than the LPDDR4x used in the iPhone 11, and at least 30 percent more power efficient. Memory bandwidth is a critical bottleneck for lots of tasks, but especially mobile graphics performance and image processing.

Of note: Samsung is currently only mass-producing 12-gigabit LPDDR5 chips. If Apple uses it as a supplier, it would likely mean an upgrade to 6GB of RAM in the iPhone 12. You can’t neatly produce 4GB of RAM using 12 gigabit chips, but you can easily use four chips to produce a 6GB (48 gigabit) package.

**5G SUPPORT VIA SNAPDRAGON X55 MODEM**
---------------------------------------

While wireless modems and radios are part of the A14 chip itself, it’s such a critical part of the iPhone that it’s worth dissecting what we might expect.

This year, Apple is widely expected to include 5G support in the new iPhones. It seems likely, in part thanks to the settled lawsuits and licensing agreements between Apple and Qualcomm, that all premium iPhones will have the X55 modem. Lower-end models might even have that modem, but with the 5G radio disabled via software.

![](.evernote-content/F8C66CE8-1949-4025-8DFA-694CEA152BD0/87E8AAA7-B130-4AB9-9B55-EF4B6FA32C3A.jpg)

**Apple will almost certainly use Qualcomm’s Snapdragon X55 modem in the iPhone 12.**

This would give iPhones one of the very best cellular modems around, with support for lots of LTE features and global networks as well as the most advanced 5G available at the time. It doesn’t necessarily put it ahead of anything on the Android front, though: Android phones with the X55 modem will ship throughout 2020.

As far as other wireless features go we can expect continued support for Wi-Fi 6, Bluetooth 5, NFC, and ultra-wideband (UWB). The latter was a surprise addition for the iPhone 11, but I don’t expect another wireless surprise is in the works for the iPhone 12. ■

Measure

Measure

---

[🌐 原始链接](https://macworldbax.zinioapps.com/reader/readhtml/471218/60839)

[📎 在印象笔记中打开](evernote:///view/207087/s1/f3700998-e3e7-4006-9b1f-06d4afded16d/f3700998-e3e7-4006-9b1f-06d4afded16d/)