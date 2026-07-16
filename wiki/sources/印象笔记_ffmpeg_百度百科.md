---
title: "ffmpeg_百度百科"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/ffmpeg_百度百科.md
tags: [印象笔记]
---

# ffmpeg_百度百科

# ffmpeg_百度百科 --- ffmpeg ====== [编辑](#) [锁定](https://baike.baidu.com/view/10812319.htm "锁定") FFmpeg是

---

# ffmpeg_百度百科

---

ffmpeg
======

[编辑](#)
[锁定](https://baike.baidu.com/view/10812319.htm "锁定")

FFmpeg是一套可以用来记录、转换数字音频、视频，并能将其转化为流的开源计算机程序。采用LGPL或GPL许可证。它提供了录制、转换以及流化音视频的完整解决方案。它包含了非常先进的音频/视频编解码库libavcodec，为了保证高可移植性和编解码质量，libavcodec里很多code都是从头开发的。

FFmpeg在Linux平台下开发，但它同样也可以在其它操作系统环境中编译运行，包括Windows、Mac OS X等。这个项目最早由Fabrice Bellard发起，2004年至2015年间由Michael Niedermayer主要负责维护。许多FFmpeg的开发人员都来自MPlayer项目，而且当前FFmpeg也是放在MPlayer项目组的服务器上。项目的名称来自MPEG[视频编码标准](https://baike.baidu.com/item/%E8%A7%86%E9%A2%91%E7%BC%96%E7%A0%81%E6%A0%87%E5%87%86)，前面的"FF"代表"Fast Forward"。[1]

软件名称
:   Fast Forward Mpeg

开发商
:   FFmpeg team

软件平台
:   Linux、Windows、Mac OS X

软件版本
:   4.1

更新时间
:   2018-11-6

软件语言
:   C、汇编

软件授权
:   开源

标准协议
:   LGPL/GPL

ffmpeg功能
--------

[编辑](#)

多媒体视频处理工具FFmpeg有非常强大的功能包括[视频采集](https://baike.baidu.com/item/%E8%A7%86%E9%A2%91%E9%87%87%E9%9B%86)功能、[视频格式转换](https://baike.baidu.com/item/%E8%A7%86%E9%A2%91%E6%A0%BC%E5%BC%8F%E8%BD%AC%E6%8D%A2)、视频抓图、给视频加水印等。

**视频采集功能**

ffmpeg视频采集功能非常强大，不仅可以采集[视频采集卡](https://baike.baidu.com/item/%E8%A7%86%E9%A2%91%E9%87%87%E9%9B%86%E5%8D%A1)或USB摄像头的图像，还可以进行屏幕录制，同时还支持以RTP方式将视频流传送给支持RTSP的[流媒体服务器](https://baike.baidu.com/item/%E6%B5%81%E5%AA%92%E4%BD%93%E6%9C%8D%E5%8A%A1%E5%99%A8)，支持直播应用。

**ffmpeg在Linux下的[视频采集](https://baike.baidu.com/item/%E8%A7%86%E9%A2%91%E9%87%87%E9%9B%86)**

在Linux平台上，ffmpeg对[V4L2](https://baike.baidu.com/item/V4L2)的视频设备提供了很好的支持，如：

./ffmpeg -t 10 -f video4[linux](https://baike.baidu.com/item/linux)2 -s 176\*144 -r 8 -i /dev/video0 -vcodec h263 -f rtp rtp://192.168.1.105:5060 > /tmp/ffmpeg.sdp[![](.evernote-content/81D2140F-0F58-4AAB-BA06-7027F489F9D5/3101DF88-CF83-49CC-B89A-803CCB244425.jpg)

FFMpeg(4张)](https://baike.baidu.com/pic/ffmpeg/2665727/23190084/d50735fae6cd7b89450ef2f6032442a7d9330e61?fr=lemma&ct=cover "FFMpeg")

以上命令表示：采集10秒钟视频，对video4linux2视频设备进行采集，采集QCIF(176\*144)的视频，每秒8帧，视频设备为/dev/video0，[视频编码](https://baike.baidu.com/item/%E8%A7%86%E9%A2%91%E7%BC%96%E7%A0%81)为[H263](https://baike.baidu.com/item/H263)，输出格式为RTP，后面定义了IP地址及端口，将该码流所对应的SDP文件重定向到/tmp/ffmpeg.sdp中，将此SDP文件上传到[流媒体服务器](https://baike.baidu.com/item/%E6%B5%81%E5%AA%92%E4%BD%93%E6%9C%8D%E5%8A%A1%E5%99%A8)就可以实现直播了。

**ffmpeg在windows下的[视频采集](https://baike.baidu.com/item/%E8%A7%86%E9%A2%91%E9%87%87%E9%9B%86)**

在windows下关于ffmpeg视频采集的资料非常少，但是ffmpeg还是支持windows下视频采集的。ffmpeg支持windows下video for windows(VFW)设备的视频采集，不过[VFW](https://baike.baidu.com/item/VFW)设备已经过时，正在被WDM的视频设备所取代，但是ffmpeg还没有支持[WDM](https://baike.baidu.com/item/WDM)的计划，不过好像有将WDM转为VFW的工具，因此ffmpeg还是可以在windows下进行视频采集的。

**视频格式转换功能**

ffmpeg视频转换功能。[视频格式转换](https://baike.baidu.com/item/%E8%A7%86%E9%A2%91%E6%A0%BC%E5%BC%8F%E8%BD%AC%E6%8D%A2)，比如可以将多种视频格式转换为flv格式，可不是视频信号转换 。

ffmpeg可以轻易地实现多种视频格式之间的相互转换(wma,rm,avi,mod等)，例如可以将摄录下的视频[avi](https://baike.baidu.com/item/avi/213655)等转成视频网站所采用的[flv](https://baike.baidu.com/item/flv)格式。

**视频截图功能**

对于选定的视频，截取指定时间的缩略图。视频抓图，获取静态图和动态图，不提倡抓gif文件;因为抓出的gif文件大而播放不流畅。

**给视频加水印功能**

使用ffmpeg 视频添加水印(logo)。

ffmpeg项目组成
----------

[编辑](#)

FFmpeg是一套可以用来记录、转换数字音频、视频，并能将其转化为流的开源计算机程序。它包括了领先的音/视频编码库libavcodec等。

**libavformat**：用于各种音视频[封装格式](https://baike.baidu.com/item/%E5%B0%81%E8%A3%85%E6%A0%BC%E5%BC%8F)的生成和解析，包括获取解码所需信息以生成解码上下文结构

和读取音视频帧等功能；

**libavcodec**：用于各种类型声音/图像编解码；

**libavutil**：包含一些公共的工具函数；

**libswscale**：用于视频场景比例缩放、色彩映射转换；

**libpostproc**：用于后期效果处理；

**ffmpeg**：该项目提供的一个工具，可用于格式转换、解码或[电视卡](https://baike.baidu.com/item/%E7%94%B5%E8%A7%86%E5%8D%A1)即时编码等；

**ffsever**：一个 HTTP 多媒体即时广播串流服务器；

**ffplay**：是一个简单的播放器，使用ffmpeg 库解析和解码，通过SDL显示；

ffmpeg命令集
---------

[编辑](#)

ffmpeg 命令集举例

1.获取视频的信息

ffmpeg -i video.avi

2.将图片序列合成视频

ffmpeg -f image2 -i image%d.jpg video.mpg

上面的命令会把当前目录下的图片（名字如：image1.jpg. image2.jpg. 等...）合并成video.mpg

3.将视频分解成图片序列

ffmpeg -i video.mpg image%d.jpg

上面的命令会生成image1.jpg. image2.jpg. ...

支持的图片格式有：PGM. PPM. PAM. PGMYUV. JPEG. GIF. PNG. TIFF. SGI

4.为视频重新编码以适合在iPod/iPhone上播放

ffmpeg -i source\_video.avi input -acodec aac -ab 128kb -vcodec mpeg4 -b 1200kb -mbd 2 -flags +4mv+trell -aic 2 -cmp 2 -subcmp 2 -s 320x180 -title X final\_video.mp4

说明：

\* 源视频：source\_video.avi

\* 音频编码：aac

\* 音频位率：128kb/s

\* 视频编码：mpeg4

\* 视频位率：1200kb/s

\* 视频尺寸：320 X 180

\* 生成的视频：final\_video.mp4

5.为视频重新编码以适合在PSP上播放

ffmpeg -i source\_video.avi -b 300 -s 320x240 -vcodec xvid -ab 32 -ar 24000 -acodec aac final\_video.mp4

说明：

\* 源视频：source\_video.avi

\* 音频编码：aac

\* 音频位率：32kb/s

\* 视频编码：xvid

\* 视频位率：1200kb/s

\* 视频尺寸：320 X 180

\* 生成的视频：final\_video.mp4

6.从视频抽出声音.并存为Mp3

ffmpeg -i source\_video.avi -vn -ar 44100 -ac 2 -ab 192 -f mp3 sound.mp3

说明：

\* 源视频：source\_video.avi

\* 音频位率：192kb/s

\* 输出格式：mp3

\* 生成的声音：sound.mp3

7.将wav文件转成Mp3

ffmpeg -i son\_origine.avi -vn -ar 44100 -ac 2 -ab 192 -f mp3 son\_final.mp3

8.将.avi视频转成.mpg

ffmpeg -i video\_origine.avi video\_finale.mpg

9.将.mpg转成.avi

ffmpeg -i video\_origine.mpg video\_finale.avi

10.将.avi转成gif动画（未压缩）

ffmpeg -i video\_origine.avi gif\_anime.gif

11.合成视频和音频

ffmpeg -i son.wav -i video\_origine.avi video\_finale.mpg

12.将.avi转成.flv

ffmpeg -i video\_origine.avi -ab 56 -ar 44100 -b 200 -r 15 -s 320x240 -f flv video\_finale.flv

13.将.avi转成dv

ffmpeg -i video\_origine.avi -s pal -r pal -aspect 4:3 -ar 48000 -ac 2 video\_finale.dv

或者：

ffmpeg -i video\_origine.avi -target pal-dv video\_finale.dv

14.将.avi压缩成divx

ffmpeg -i video\_origine.avi -s 320x240 -vcodec msmpeg4v2 video\_finale.avi

15.将Ogg Theora压缩成Mpeg dvd

ffmpeg -i film\_sortie\_cinelerra.ogm -s 720x576 -vcodec mpeg2video -acodec mp3 film\_terminate.mpg

16.将.avi压缩成SVCD mpeg2

NTSC格式：

ffmpeg -i video\_origine.avi -target ntsc-svcd video\_finale.mpg

PAL格式：

ffmpeg -i video\_origine.avi -target pal-svcd video\_finale.mpg

17.将.avi压缩成VCD mpeg2

NTSC格式：

ffmpeg -i video\_origine.avi -target ntsc-vcd video\_finale.mpg

PAL格式：

ffmpeg -i video\_origine.avi -target pal-vcd video\_finale.mpg

18.多通道编码

ffmpeg -i fichierentree -pass 2 -passlogfile ffmpeg2pass fichiersortie-2

19.从flv提取mp3

ffmpeg -i source.flv -ab 128k dest.mp3

ffmpeg格式
--------

[编辑](#)

**支持的编码**

源自FFmpeg项目组的两个[视频编码](https://baike.baidu.com/item/%E8%A7%86%E9%A2%91%E7%BC%96%E7%A0%81)：

Snow

FFV1

**支持的格式**

ASF

AVI

BFI[7]

IFF[8]

RL2[9]

FLV

MXF, Material eXchange Format, SMPTE 377M

Matroska

Maxis XA[10]

MSN Webcam stream[11]

MPEG transport stream

TXD[6]

OMA[12]

GXF, General eXchange Format, SMPTE 360M

mov,mp4,m4a,3gp,

ffmpeg协议
--------

[编辑](#)

**支持的协议**

HTTP

RTP

RTSP

RealMedia RTSP/RDT

Gopher

RTMP

RTMPT, RTMPE, RTMPTE, RTMPS (via librtmp)

SDP

MMS over TCP

ffmpeg相关版权
----------

[编辑](#)

(Hall Of Shame)

FFmpeg被许多开源项目采用，比如ffmpeg2theora,[VLC](https://baike.baidu.com/item/VLC), MPlayer, HandBrake, Blender, Google Chrome等。还有[DirectShow](https://baike.baidu.com/item/DirectShow)/[VFW](https://baike.baidu.com/item/VFW)的[ffdshow](https://baike.baidu.com/item/ffdshow)(external project)和QuickTime的Perian (external project)也采用了FFmpeg。

由于FFmpeg是在LGPL/GPL协议下发布的（如果使用了其中一些使用GPL协议发布的模块则必须使用GPL协议），任何人都可以自由使用，但必须严格遵守LGPL/GPL协议。有很多播放软件都使用了FFmpeg的代码，但它们并没有遵守LGPL/GPL协议，没有公开任何[源代码](https://baike.baidu.com/item/%E6%BA%90%E4%BB%A3%E7%A0%81)。我们应该对这种侵权行为表示耻辱。

2009年加入FFmpeg的播放软件：**[暴风影音](https://baike.baidu.com/item/%E6%9A%B4%E9%A3%8E%E5%BD%B1%E9%9F%B3)、QQ影音、KMP**、GOM Player****、**PotPlayer**（2010）都在其列。

2009年2月，韩国名软KMPlayer被FFmpeg[开源项目](https://baike.baidu.com/item/%E5%BC%80%E6%BA%90%E9%A1%B9%E7%9B%AE)发现使用了它们的代码和[二进制文件](https://baike.baidu.com/item/%E4%BA%8C%E8%BF%9B%E5%88%B6%E6%96%87%E4%BB%B6)，但是没有按照规定/惯例开放相应说明/源码。因此被人举报，进入了FFmpeg官网上的耻辱黑名单。

2009年5月，网友cehoyos下载了暴风影音软件，解压之后发现其安装程序内包含了大量的开源和私有解码器：avcodec，avformat，avutil，x264，xvid，bass，wmvdmod等，之后暴风影音被正式加入到FFmpeg耻辱名单。

2009年7月22日，陈俊豪([格式工厂](https://baike.baidu.com/item/%E6%A0%BC%E5%BC%8F%E5%B7%A5%E5%8E%82)作者)因用到了ffmpeg和RMVB的编码库，用到了FFmpeg的译码/编码算法，违反FFmpeg的LGPL协议，登上了2009年7月22日FFmpeg的“耻辱柱”上。

2009年11月，网友roo\_zhou向FFmpeg举报，指出QQ影音的credit只给出了修改的FFmpeg源码下载，声称是LGPL许可证。但实际是修改过的[ffdshow](https://baike.baidu.com/item/ffdshow)，采用的是GPL许可证，之后QQ影音被正式加入到FFmpeg耻辱名单之列。

Libav项目启动之后，FFmpeg官方版本也仍然在一直维护中。FFmpeg与libav属于独立的两个项目。[2]

ffmpeg版本发布
----------

[编辑](#)

2014-12-5, FFmpeg2.5发布

2014-09-15, FFmpeg2.4发布[3]

2013-07-10, FFmpeg2.2发布

2012年01月27日，FFmpeg 0.9.1 发布，修复了很多 bug 和安全方面的补丁，包括： CVE-2011-3893 and CVE-2011-3895，同时显著提升对 H.264 的检索支持。[4]

2012年01月29日，FFmpeg 0.10 发布，这是一个主要的发行版本，包含大量的新特性和bug修复。[5]

2012年04月07日，FFmpeg 0.10.1 发布，FFmpeg 0.10.1 修复了很多安全漏洞，超过 100 个 bug 修复，新增 swapuv 过滤器。[6]

2012年05月07，FFmpeg 0.10.3 发布，该版本修复了 4xm 分路器、cook 解码器、mm 分路器、mpeg 视频解码器、vqavideo 解码器、xmv 分路器的安全问题，以及包含一些重要的 bug 修复。[7]

2012年06月09日，FFmpeg 0.11.1 发布，该版本修复了 70 个 bug，其中有一些安全方面的问题。[8]

词条图册
[更多图册](https://baike.baidu.com/pic/ffmpeg/2665727?fr=lemma)

参考资料
:   * 1.
      [多媒体处理工具 ffmpeg](https://baike.baidu.com/reference/2665727/35a1P6SWdkm1gm3GvZV3dDVuBWAaG26FUvrgYGwUGXh9_xfFCu-VZTRx8d2-AVxZlJqUPCsP_4Uubej7) 
      ．开源社区网[引用日期2012-09-08]
    * 2.
      [libav 关于页面](https://baike.baidu.com/reference/2665727/2c52rahM1EmGGQNm8WmCFmK6Dr9RFTNld_X1-gPWntJfRUwYM1RuWNRs2tqt5B1cVWWNHVuL_Jg)
      ．libav[引用日期2015-05-04]
    * 3.
      [ffmpeg 2.4发布](https://baike.baidu.com/reference/2665727/4e3e3dbXGZ_esv74MVaiFWfjVYEEjEFzuSKUdhGu8jdpKDRtekiNIkjzTZmGL8rKLxAzKfYTllhPBTPZ2-mzuoF6)
      ．ffmpeg[引用日期2014-11-24]
    * 4.
      [FFmpeg 0.9.1 发布，多媒体处理工具](https://baike.baidu.com/reference/2665727/069dDCA0Rbg0LRxdbUnjCLJAiVTkiVAu1O3lEfqdVZEVdr8LwlpEYj0TD51Ok_NGVX6lpVeeQq_-4WMl_-jGQjn4HGvaGl_0OED1A2AnjvVmdYsy)
      ．开源社区网[引用日期2012-09-23]
    * 5.
      [FFmpeg 0.10 发布](https://baike.baidu.com/reference/2665727/fa1c8VRrzUMtDzC5hpOJ0k93nD_92OGgmRxW8cyJ6sesGcJVSsDVKEhC2bWeW_a3GMSIRzzqd6Mrxla2uWq46TDxs8fWeLEYT-A)
      ．开源社区网[引用日期2012-09-23]
    * 6.
      [FFmpeg 0.10.1 发布](https://baike.baidu.com/reference/2665727/224aYozbk5TN1JE4t8hr9WUC_LFLHjqGYDniG0rOhIgcH35DUz1guuUQu2WykY4VSj-tSs62skX-AgXb2FSEjH_dno4lKjAibi2gvdk8FEuZ_m2kNA)
      ．开源社区网[引用日期2012-09-24]
    * 7.
      [FFmpeg 0.10.3 发布](https://baike.baidu.com/reference/2665727/79103R8xQbxwH1Qr9cxtHbyK2C258uShrBwR2gzDF8BI6TyWG8FQBtvTl-1DD66ZpD2pG2PusVnztVbzjOvYkAy9r9F500SvM4w0VqzeC8UUFMjeQA)
      ．开源社区网[引用日期2012-09-24]
    * 8.
      [FFmpeg 0.11.1 发布](https://baike.baidu.com/reference/2665727/6a90fSMpqwenceOGuQxHdmyp9ed0e1nK1zZ31dx9dh1dW0omfEbOhafkKdBHL3JYOe4vTXEjV_-7aFdJ36nFg5a1jeqfmkNU3hMIIQ)
      ．开源社区网[引用日期2012-09-24]

:   科学
    ，
    技术

Measure

Measure

---

[🌐 原始链接](https://baike.baidu.com/item/ffmpeg/2665727?fr=aladdin)

[📎 在印象笔记中打开](evernote:///view/207087/s1/fbefff62-ebc9-4caa-a89d-1d241e80d610/fbefff62-ebc9-4caa-a89d-1d241e80d610/)