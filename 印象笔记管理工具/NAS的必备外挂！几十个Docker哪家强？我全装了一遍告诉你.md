# NAS的必备外挂！几十个Docker哪家强？我全装了一遍告诉你...

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MjM5MjAyNzg4MA==&mid=265293...](https://mp.weixin.qq.com/s?__biz=MjM5MjAyNzg4MA==&mid=2652933741&idx=1&sn=8030786c69e23b6f04df5dd7c1504263&chksm=bc846fad6d151d5d2bddaa123e8aecc2046303d8f605d823d7de81eab947566d705d2a9274c8&scene=90&xtrack=1&sessionid=1746802855&subscene=93&clicktime=1746803690&enterid=1746803690&flutter_pos=16&biz_enter_id=4&ranksessionid=1746803400&jumppath=20020_1746803628057,1104_1746803631139,20020_1746803638407,1104_1746803661986&jumppathdepth=4&ascene=56&devicetype=iOS18.4.1&version=18003b26&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQx17M6zNCockbUGjuTf8aqhLVAQIE97dBBAEAAAAAAEihL6KsAJUAAAAOpnltbLcz9gKNyK89dVj0IEoM7AEhHlGeby3dIgrf2Re2U5FJJtsX7Z3u2D/IqAKXDuilcqPs53YCVrqIUm3l41v7wNw1axLGyCSy6VQmD15y29QfI7pFg3BoWZTnUqGqCy757UWugElgjCANHemd9Q5P9gwHqsBUS/zzkEtwS6QfDGvZAr4vAIOz4wJO/emIuyI/kveAxg2pd9Q2Oh0UikSS+C1bMvzDsV5sHnq1OEIahlCplgwP5PI2lieSww==&pass_ticket=XR6euapzJIqKX461rAeABDOR5L89ZwsnVvgZs1mz2lJWJr83n3UErQEdosFeF1Mo&wx_header=3)

NAS的必备外挂！几十个Docker哪家强？我全装了一遍告诉你...
==================================

羊刀仙 什么值得买

点击上方名片**关注我们👆**

![](.evernote-content/0A2D1D05-9AF3-4AD0-99BB-6D71DAF49D49/DCFD3DAD-209F-4449-BE8E-3DA1CEBA46A7.jpg)

家人们，**玩NAS时间长了是不是都成了Docker收集狂魔？**

QB下载、Emby追剧、Alist网盘这些神器装得停不下来，结果没几个月服务器就塞了二十多个应用。更离谱的有时候每个服务都得搞反向代理配二级域名，什么emby.mydomain.com、qbit.mydomain.com记到脑壳疼...

这两天我们「**什么值得买App**」的生活家「**羊刀仙**」终于忍不了这“反人类”的操作了，**于是把全网导航页工具全折腾了一遍。**没想到这玩意儿简直像是给NAS开了外挂，**不仅能当服务目录用，有的还能监控服务器状态。**快去试试吧！反正部署就五分钟的事，不好用你回来找小值～

本文内容均以作者第一人称叙述。

**写在前面**
--------

NAS用久了，就会在使用过程中了解并安装很多Docker服务，**一台NAS装十几二十个应用程序应该很常见。**
--------------------------------------------------------

> QB、Emby、Jellyfin、Transmission、Plex、NASTOOL、IT-tools、uptime-kuma、ddns-go、Navidrome、Lcuky、Alist、reader等等各类实用软件工具。

不知道各位，我几乎为每款服务都做了反向代理，并通过**二级域名**进行访问。

虽然主域名和监听端口固定，但这么多前缀也蛮难的...除了NAS的WEB，以及常用的几个服务，**很多时候要先打开Lucky查看域名后才能访问。**

![](.evernote-content/0A2D1D05-9AF3-4AD0-99BB-6D71DAF49D49/6F0A91D6-E869-4202-BB12-039355710150.png)

为了解决这一窘境，本期来介绍几个项目，可以承担起NAS、服务器导服务导航的重任，**有的除了轻量易用之外，有些还附带其他实用功能，也可以将其作为浏览器首页。**

![](.evernote-content/0A2D1D05-9AF3-4AD0-99BB-6D71DAF49D49/34344CBF-08EB-49B3-A037-5FE6BF0E6A26.png)

以威联通NAS为例，通过Docker Compose进行部署。

***🍉 Sun-Panel***
-----------------

### **✅ 简评**

还是国人最懂国人需求，本篇首推。**界面简洁、功能强大、资源占用低、移动端支持好，操作极为简单。**总的来说就是一个轻量级、强可定制、开箱即用的 Web 控制面板。硬说缺点的话，就是1.3.0后不开源吧，但无可厚非。

建议大家先部署用一用，不用十分钟就能体验个大概。

### **✅ 部署使用**

部署代码如下，注意格式对齐：

```
version: "3.2" # 最新版Docker Compose可删除，已经弃用

services:

sun-panel:

image: "hslr/sun-panel:latest"

container_name: sun-panel

volumes:

- /share/Container/sunpanel/conf:/app/conf # 自行修改目录

- /var/run/docker.sock:/var/run/docker.sock # 挂载docker.sock

# - ./runtime:/app/runtime # 挂载日志，意义不大

# - /mnt/sata1-1:/os # 硬盘挂载点（根据自己需求修改）

ports:

- 3002:3002

restart: always
```

关于硬盘挂载点，每个NAS厂家都不同，例如威联通/share/CACHEDEV1\_DATA1，/share/CACHEDEV2\_DATA，或者是具体文件- /share/Multimedia:/os，- /share/Container/data:/os。

![](.evernote-content/0A2D1D05-9AF3-4AD0-99BB-6D71DAF49D49/F14E6753-9B71-40D3-BA0B-CBF93D34BDEA.jpg)

如按照上文部署，web输入NAS\_IP:3022即可访问服务。

**默认账号密码**

账号：admin@sun.cc 密码：12345678

![](.evernote-content/0A2D1D05-9AF3-4AD0-99BB-6D71DAF49D49/31880028-858C-40D0-8ABE-8A97742F5AF6.jpg)

上角的图标点击可以切换内外网环境，这点很不错。

![](.evernote-content/0A2D1D05-9AF3-4AD0-99BB-6D71DAF49D49/67A6B5BB-0855-49AE-9E04-01AA75CDC221.jpg)

右上角的四叶草图标点击可以进行更多设置，相当简单和便捷化。

![](.evernote-content/0A2D1D05-9AF3-4AD0-99BB-6D71DAF49D49/68788B6D-841D-4A2C-BF5A-F97EEBD8CB6A.jpg)

小配置了一下。自带的搜索，是可以快速定位APP的。

![](.evernote-content/0A2D1D05-9AF3-4AD0-99BB-6D71DAF49D49/087319B9-7A87-425C-8863-813714DEA265.jpg)

换换壁纸。

![](.evernote-content/0A2D1D05-9AF3-4AD0-99BB-6D71DAF49D49/D3A0C598-F032-4ED4-859A-DFFDE9680AFF.jpg)

![](.evernote-content/0A2D1D05-9AF3-4AD0-99BB-6D71DAF49D49/AD157C46-0230-40CC-B0C1-35C7BC6234D2.jpg)

如果嫌背景太花，**可以做模糊处理，**这个模糊程度也都支持自由调节，背景图也会根据窗口大小自适应缩放。

![](.evernote-content/0A2D1D05-9AF3-4AD0-99BB-6D71DAF49D49/03344366-2E1E-4B17-8055-4D2A2F1A737B.jpg)

虽然1.3.0版本之后推出了Pro功能，但基础版很够用，十分推荐此项目。

![](.evernote-content/0A2D1D05-9AF3-4AD0-99BB-6D71DAF49D49/67ED2E19-7672-4027-A592-BC13BD833124.jpg)

***🍉 Flare***
-------------

### **✅ 简评**

国人作者，有段时间不更了，估计是已经趋近完美，没啥能更的内容。

Flare拥有更简单透明的数据策略，**使用文本格式来存储书签。简约、快速、轻量且超级易于安装和使用。**支持欢迎词、时间日期、天气，编辑简**单，手机适配完美。**

**![](.evernote-content/0A2D1D05-9AF3-4AD0-99BB-6D71DAF49D49/53103B14-083E-4D67-886B-5DE35B84CCD1.jpg)**

**作者是这样形容的：**

> Flare 最大的优势是在拥有和 Flame 一样的美观界面的前提下，拥有着绝对的性能优势：不论是 10M 不到的容器镜像体积、还是平时运行起来30M 以内的内存消耗、亦或者 99% 情况下的页面秒开（成千上万条书签），并且不会触发笔记本等设备的风扇狂转。

```
services:

flare:

image: soulteary/flare

restart: always

# 默认无需添加任何参数，如有特殊需求

# 可阅读文档 https://github.com/soulteary/docker-flare/blob/main/docs/advanced-startup.md

command: flare

# 启用账号登录模式

# command: flare --nologin=0

# environment:

# 如需开启用户登录模式，需要先设置 `nologin` 启动参数为 `0`

# 如开启 `nologin`，未设置 FLARE_USER，则默认用户为 `flare`

# - FLARE_USER=flare

# 指定你自己的账号密码，如未设置 `FLARE_USER`，则会默认生成密码并展示在应用启动日志中

# - FLARE_PASS=your_password

# 是否开启“使用向导”，访问 `/guide`

# - FLARE_GUIDE=1

command: flare

ports:

- 5005:5005 # 左侧端口自行修改

volumes:

- /share/Container/flare/app:/app # 左侧路径自行修改
```

```
内网环境下，按照上文代码，WEB输入NAS_IP:5005即可访问。

![](.evernote-content/0A2D1D05-9AF3-4AD0-99BB-6D71DAF49D49/985A4466-A938-40AB-ADD3-BA6852FD2616.jpg)

上文也说过，需要在“应用书签”、“分类书签”以及“程序配置”的数据文件中配置链接名称、链接地址之类的东西，当然也包括icon（图标）。这点倒是与过去我分享过的Dashy有些类似。

![](.evernote-content/0A2D1D05-9AF3-4AD0-99BB-6D71DAF49D49/1225BE91-74B0-474F-B1CB-2CAC15DA675C.jpg)

更多详细提升体验的操作，我建议参照作者大大的教程。

在GHUB搜索soulteary/flare，点击右侧的链接即可。喜欢这种极简风的朋友可以部署起来。

![](.evernote-content/0A2D1D05-9AF3-4AD0-99BB-6D71DAF49D49/4DFF1414-6048-4FA3-BE5D-C58D54733859.jpg)

🍉 Homepage
----------

这里我在部署模版的书签部分塞了个小福利，请看本节最后的传送门。

### ✅ 简评

功能应该是最为强大的。界面布局在简约和花里胡哨之间吧，显示的内容和具备的功能也多，看着很饱满，手机端支持也很不错。

![](.evernote-content/0A2D1D05-9AF3-4AD0-99BB-6D71DAF49D49/3532E135-0998-40EA-B35F-A58DB89DA7BD.png)

部署也不算难，部署内容看着很多，但也就跟着作者注解改动即可。

（前天做大纲的时候是我轻敌了，断断续续花了一天搞模版...）
```

```
services:

homepage:

image: ghcr.io/gethomepage/homepage:latest

container_name: homepage

environment:

HOMEPAGE_ALLOWED_HOSTS: 访问地址 # 内网IP+端口/域名/域名+端口，必须填！

# QNAP admin账户为0，0

# 禁用admin的管理账户一般为1000，100

# 可SSH输入 id 自查

PUID: 1000

PGID: 100

ports:

- 3000:3000 # 端口自行修改

volumes:

- /share/Container/homepage/config:/app/config  # 路径可自定义

- /share/Container/homepage/images:/app/public/images # 本地图库路径，通常用于背景图，非必需

- /share/Container/homepage/icons:/app/public/icons # 本地图标文件路径，非必需

- /var/run/docker.sock:/var/run/docker.sock:ro

restart: unless-stopped
```

内网环境下，按照上文代码，WEB输入NAS\_IP:3000即可访问。

![](.evernote-content/0A2D1D05-9AF3-4AD0-99BB-6D71DAF49D49/9F020B84-A4D5-4608-A898-4496B0A1BA01.jpg)

界面简陋，与Flare相同也不支持在线修改，包括语言等配置需要编辑配置文件。

部署好后，在映射文件目录有settings.yaml，service.yaml，widgets.yaml，bookmarks.yaml四个配置文件供我们配置修改。

![](.evernote-content/0A2D1D05-9AF3-4AD0-99BB-6D71DAF49D49/36492CE8-7BA3-43A3-8157-315250037F78.jpg)

![](.evernote-content/0A2D1D05-9AF3-4AD0-99BB-6D71DAF49D49/C390C0C0-CC82-4DBA-BF4B-8D1054C475D0.jpg)

本节开头就是我修改后的效果图。因为是测试机，所以就填写了一个正确配置，就是那台威联通TS-673A。

全搞完实在是累，所以我还是直接放配置模版吧，大家整起来会轻松不少。

众口难调，如果你有不一样的需求，也可以去查看wiki自行配置。已经在配置文件中尽可能详细把用到的变量做了注释。

**传送门大家可以点击「阅读原文」跳转查看～**下载后把这个四个文件修改后替换即可。威联通比较方便，可以直接在NAS实时修改并刷新页面查看效果。

***🍉 Heimdall***
----------------

### ✅ 简评

已经有段时间不更新，不太建议用。

也属于简约派，对很多人来说也够用，**就是操作要稍微复杂些，使用逻辑不太符合国人习惯，手机端不舒服。**

可完全自定义图标（可选择用自带应用图标库，这点要比sun-panel稍微方便些）、改背景色、文字说明等。多应用可以创建大标签，也就是一级二级分类的意思。也支持更换背景图片（不能自适应）、更换搜索引擎、自定义CSS、自定义JavaScript。提供了一个应用库推荐，可以部署到NAS或服务器上。

![](.evernote-content/0A2D1D05-9AF3-4AD0-99BB-6D71DAF49D49/947C12DA-D7B4-4BD8-974C-BC0F99078B28.jpg)

### **✅ 部署使用**

代码如下：

```
services:

heimdall:

image: lscr.io/linuxserver/heimdall:latest

container_name: heimdall

environment:

# QNAP admin账户为0，0

# 禁用admin的管理账户一般为1000，100

# 可SSH输入 id 自查

- PUID=0

- PGID=0

- TZ=Asia/Shanghai

volumes:

- /share/Container/heimdall/config:/config  # 改为你的实际路径

ports:

- 9080:80                   # 避免与本地 80 端口冲突

- 9443:443                 # 避免与 HTTPS 端口冲突

restart: unless-stopped
```

这里提示，如果你本地http访问使用9080端口，如果https或强制https则使用9443，**也就是说你内网想通过9443访问必须手打https。**同理进行反向代理时也要注意区分！

内网环境下，按照上文代码，WEB输入NAS\_IP:9080即可访问。先点击设置，修改语言为中文。

![](.evernote-content/0A2D1D05-9AF3-4AD0-99BB-6D71DAF49D49/35F4AEEC-F299-47F4-B399-1135DD899A54.jpg)

然后点击账户，修改密码，或者新建账户。

![](.evernote-content/0A2D1D05-9AF3-4AD0-99BB-6D71DAF49D49/95A7391A-91A7-4023-9647-1D8743D64E7A.jpg)

外观背景图，等其他都可以在这边设置。

![](.evernote-content/0A2D1D05-9AF3-4AD0-99BB-6D71DAF49D49/C5B91079-51A6-44C7-B395-4B64D3C0935F.jpg)

上面说的自带图标库，过去我介绍过的Docker这里基本都有图标对应，但有些我不太喜欢，不过好在也支持自定义上传。不晓得这个图标纯国内网络能否成功拉取。

![](.evernote-content/0A2D1D05-9AF3-4AD0-99BB-6D71DAF49D49/94E2FEF4-2693-400F-B298-999C3C141286.jpg)

没想到还有QNAP和openwrt的图标。成品展示如下。关于大标签集合我就不整了。

![](.evernote-content/0A2D1D05-9AF3-4AD0-99BB-6D71DAF49D49/947C12DA-D7B4-4BD8-974C-BC0F99078B28.jpg)

***🍉 Dashy***
-------------

### **✅ 简评**

太重量级了！当时看文档就花了蛮久。

界面非常极客，亮出你的面板，瞬间群地位+1。我之所以想折腾这款，就是一眼帅。

![](.evernote-content/0A2D1D05-9AF3-4AD0-99BB-6D71DAF49D49/D5F039A0-80FE-4932-AA95-C0EB032AEF33.jpg)

**但是吧，比homepage还要麻烦，也是需要各种修改配置。**

### **✅ 部署使用**

这个就请移步往期教程吧：

https://post.smzdm.com/p/apmo4p90/

注意事项：

![](.evernote-content/0A2D1D05-9AF3-4AD0-99BB-6D71DAF49D49/61BE6B18-34BA-4AAA-B6B2-44A369436B09.jpg)

***🍉 LinkStack***
-----------------

### **✅****简评**

这个也属于简约类，喜欢这种形式可以试试，我当时是蛮喜欢这款的。

![](.evernote-content/0A2D1D05-9AF3-4AD0-99BB-6D71DAF49D49/05583D33-6515-45DA-995D-533621C90EF9.jpg)

### **✅ 部署使用**

往期教程：

https://post.smzdm.com/p/an9pzgv2/

***🍉 Homarr***
--------------

### **✅ 简评**

我个人觉得比较抽象，现在还不如以前...

![](.evernote-content/0A2D1D05-9AF3-4AD0-99BB-6D71DAF49D49/E7CE3B36-3228-40A8-9706-22A5AE31922E.jpg)

**有些新意，比如支持视频流之类的。**

**但用的时候，bug太多，直接放弃。**

![](.evernote-content/0A2D1D05-9AF3-4AD0-99BB-6D71DAF49D49/F0DF8946-29BD-49FD-9636-FAB2C958F619.jpg)

### ✅ **部署流程**

乐于尝试的朋友可以自己试试看。

```
services:

homarr:

container_name: homarr

image: ghcr.io/homarr-labs/homarr:latest

restart: unless-stopped

volumes:

- /var/run/docker.sock:/var/run/docker.sock

- /share/Container/homarr/appdata:/appdata

environment:

- SECRET_ENCRYPTION_KEY=d299fa7dd646dc5290c414e1a3b4aebe0085fd306c692be8b915da8804a809d2

ports:

- '7575:7575'
```

上面提供的环境变量密钥SECRET\_ENCRYPTION\_KEY是使用浏览器加密 API 随机生成的。每次生成的密钥都会不同。**可以使用以下命令自行生成密钥：**

```
openssl rand -hex 32
```

**总结：**
-------

**总的来说，以上几款服务导航面板各有千秋：**

* 想要轻量开箱即用、移动端适配好的，Sun-Panel 几乎是首选，也是目前我最为推荐的。
* 喜欢极简纯文本配置的，可以尝试 Flare；
* 如果追求模块丰富、功能自定义、API 状态展示，Homepage 无疑是当前最全能的选手。
* 极客向的 Dashy，B格则可一拉到最满。

***写在最后***

随着服务增多，NAS的魅力已经不只在于存储，一个清晰直观的面板不仅提升效率，也能让整个系统运维更有掌控感。如果你还在靠脑子记反代域名，不妨选一个仪表盘面板上车，轻松上网，从此不再迷路～

你还有哪些「**好用导航页**」推荐？欢迎来「**评论区**」告诉大家！或者点击「**阅读原文**」去了解更多！

**-阅读更多-**

![](.evernote-content/0A2D1D05-9AF3-4AD0-99BB-6D71DAF49D49/8C649C4A-37EE-4D5A-8E8D-EFCC4E969BC3.jpg)

![](.evernote-content/0A2D1D05-9AF3-4AD0-99BB-6D71DAF49D49/044BD413-2A89-4AAF-B865-C82F0BDA12C3.jpg)

**关注我们，设为星标👇**

![](.evernote-content/0A2D1D05-9AF3-4AD0-99BB-6D71DAF49D49/85E49AD0-5667-4873-BEF4-3B9544B2D112.gif)

Read more

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MjM5MjAyNzg4MA==&mid=2652933741&idx=1&sn=8030786c69e23b6f04df5dd7c1504263&chksm=bc846fad6d151d5d2bddaa123e8aecc2046303d8f605d823d7de81eab947566d705d2a9274c8&scene=90&xtrack=1&sessionid=1746802855&subscene=93&clicktime=1746803690&enterid=1746803690&flutter_pos=16&biz_enter_id=4&ranksessionid=1746803400&jumppath=20020_1746803628057,1104_1746803631139,20020_1746803638407,1104_1746803661986&jumppathdepth=4&ascene=56&devicetype=iOS18.4.1&version=18003b26&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQx17M6zNCockbUGjuTf8aqhLVAQIE97dBBAEAAAAAAEihL6KsAJUAAAAOpnltbLcz9gKNyK89dVj0IEoM7AEhHlGeby3dIgrf2Re2U5FJJtsX7Z3u2D/IqAKXDuilcqPs53YCVrqIUm3l41v7wNw1axLGyCSy6VQmD15y29QfI7pFg3BoWZTnUqGqCy757UWugElgjCANHemd9Q5P9gwHqsBUS/zzkEtwS6QfDGvZAr4vAIOz4wJO/emIuyI/kveAxg2pd9Q2Oh0UikSS+C1bMvzDsV5sHnq1OEIahlCplgwP5PI2lieSww==&pass_ticket=XR6euapzJIqKX461rAeABDOR5L89ZwsnVvgZs1mz2lJWJr83n3UErQEdosFeF1Mo&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/dd65d5ef-a88e-4bd2-817e-e1c94decf4af/dd65d5ef-a88e-4bd2-817e-e1c94decf4af/)