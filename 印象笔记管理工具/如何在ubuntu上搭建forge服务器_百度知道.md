# 如何在ubuntu上搭建forge服务器_百度知道

---

如何在ubuntu上搭建forge服务器
====================

1、安装必要组件，我很推荐装一个screen，因为这样你可以让服务器在后台跑

apt-get install screen default-jdk

在安装完java之后，用java -version看一下是否安装正确

2、创建一个MC服务器的目录并且切换过去

mkdir /yourpath/minecraft/

cd /yourpath/minecraft //yourpath改为自己想要的路径

3、下载MC服务器的压缩包

wget -O minecraft\_server.jar<https://s3.amazonaws.com/Minecraft.Download/versions/1.7.10/minecraft_server.1.7.10.jar>（这是一行）

cp minecraft\_server.jar minecraft\_server.1.7.10.jar

4、启动服务器

java -Xmx2048M -Xms2048M -jar minecraft\_server.jar nogui

提示没有同意EULA

5、签署“两个同意”文件

如果有不会用vi编辑器的同学，留言或者百度，我懒的写。。

vim eula.txt

eula=true 这里本来应该是false的

vim server.properties 这个文件里应该还有端口和地图名字、服务器欢迎语句的设置

online-mode=false

6、如果你想玩的是原版的MC服务器，那么再次启动服务器，你的服务器就这么架设好了

java -Xmx2048M -Xms2048M -XX:ParallelGCThreads=16 -jar minecraft\_server.jar nogui

（-Xmx最大内存 -Xms最小内存 -XX:ParallelGCThreads同时调用CPU数量，建议一半或1/4或者不设）

下面开始讲Forge

1、下载Forge必要组件

cd /yourpath/minecraft

wget <http://files.minecraftforge.net/maven/net/minecraftforge/forge/1.7.10-10.13.2.1291/forge-1.7.10-10.13.2.1291-installer.jar>

wget <http://files.minecraftforge.net/maven/net/minecraftforge/forge/1.7.10-10.13.2.1291/forge-1.7.10-10.13.2.1291-universal.jar>

2、安装forge server

java -jar forge-1.7.10-10.13.2.1291-installer.jar nogui --installServer

**3、启动forge server**

**java -jar forge-1.7.10-10.13.2.1291-universal.jar nogui**

启动完毕后输入 /stop 关闭服务器

4、将forge server合并到MC服务器

mkdir unzip

cd unzip

unzip ../minecraft\_server.1.7.10.jar

unzip ../forge-1.7.10-10.13.2.1291-universal.jar

Archive: ../forge-1.7.10-10.13.2.1291-universal.jar （这两句是上面那句命令的结果）

replace META-INF/MANIFEST.MF? [y]es, [n]o, [A]ll, [N]one, [r]ename: A

zip -r ../Forge-minecraft\_server.1.7.10.jar \*

5、启动服务器

java -Xmx8192M -Xms4096M -XX:ParallelGCThreads=16 -jar Forge-minecraft\_server.1.7.10.jar nogui （这是一整行）

搞定～

mod的安装和Windows上并没有什么区别，只要会用cp和wget命令就好了～

---

[🌐 原始链接](https://zhidao.baidu.com/question/1885899738895844108.html)

[📎 在印象笔记中打开](evernote:///view/207087/s1/cd54f278-b379-4625-8412-05aab2040c98/cd54f278-b379-4625-8412-05aab2040c98/)