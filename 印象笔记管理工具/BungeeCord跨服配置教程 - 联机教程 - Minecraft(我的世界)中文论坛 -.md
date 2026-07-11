# BungeeCord跨服配置教程 - 联机教程 - Minecraft(我的世界)中文论坛 -

---

Minecraft(我的世界)中文论坛 -
=====================

### **您尚未登录，立即登录享受更好的浏览体验！**

您需要 [登录](https://www.mcbbs.net/) 才可以下载或查看，没有帐号？[注册(register)](https://www.mcbbs.net/ "注册帐号")

x

 *本帖最后由 LZX6238 于 2016-1-20 22:23 编辑* 

**BungeeCord跨服配置教程**

**1.准备:**

* 租用或拥有一台独立服务器/vps
* 足够的内存[按需要连接的服务端数量计算|4个服务端大约需要8-10G的内存(这里自己换算下)]
* 足够的带宽[通常大约配置5M-10M足够(中型服40-80人左右)]
* 理解BungeeCord是什么

**2****.****理解BungeeCord跨服:**

你可以把BungeeCord看成一个服务端，中转站(并非插件)

BungeeCord可以把不同的服务端连接在一起

ps:这样写小白都看的懂吧？

**3.运行&配置BungeeCord:**

**运行篇**

* 新建一个文件夹，把BungeeCord.jar单独放在里面
* 在上述文件夹内，创建一个bat用于运行BungeeCord.jar
* 运行bat

**bat代码如下:**

> 1. @echo OFF
> 2. title BC控制端
> 3. [这里是java7的位置，如"C:Program FilesJavajre7binjava.exe"] -Xincgc -Xmx250M -XX:MaxPermSize=128M -jar bungeecord.jar -nojline
> 4. pause
>
> *复制代码*
>
> **上述内容完成以后****应为这样:**
>
> **配置篇**
>
> 在BungeeCord文件中找到config打开，开始配置
>
> 1. groups:
> 2. md\_5:
> 3. - admin
> 4. disabled\_commands:
> 5. - disabledcommandhere
> 6. player\_limit: -1
> 7. stats: 5725e7e4-e536-44f1-97a3-c72087ed0fcb[不可修改!]
> 8. permissions:
> 9. default:
> 10. - bungeecord.command.server
> 11. - bungeecord.command.list
> 12. admin:
> 13. - bungeecord.command.alert   [权限列表,一般不用管]
> 14. - bungeecord.command.end
> 15. - bungeecord.command.ip
> 16. - bungeecord.command.reload
> 17. listeners:
> 18. - max\_players: 1
> 19. fallback\_server: lobby[默认服务器（新玩家入服的第一个服务器）]
> 20. host: 0.0.0.0:25565[这个端口是公开的，用于给玩家进入服务器]
> 21. bind\_local\_address: true
> 22. ping\_passthrough: false
> 23. tab\_list: GLOBAL\_PING
> 24. default\_server: lobby[默认服务器（新玩家入服的第一个服务器）]
> 25. forced\_hosts:
> 26. pvp.md-5.net: pvp
> 27. tab\_size: 60
> 28. force\_default\_server: false[默认服务器，改为true]
> 29. motd: '&1Another Bungee server'[服务器的标语，可中文]
> 30. query\_enabled: false
> 31. query\_port: 25577
> 32. timeout: 30000
> 33. connection\_throttle: 4000
> 34. servers:[需要跨服的服务器列表]
> 35. lobby:
> 36. [这里是服务器大厅（新玩家入服的第一个服务器），你想改什么名就什么，必须英文，改完后需要同时修改上面的default\_server: xxx]
> 37. address: localhost:25565
> 38. restricted: false
> 39. motd: '&1Just another BungeeCord - Forced Host'
> 40. ====================================================
> 41. #打个比方你需要多个服务端链接
> 42. servers:[需要跨服的服务器列表]
> 43. server1:[你要把server1设置为服务器大厅（新玩家入服的第一个服务器），就要修改上面的default\_server: server1]
> 44. address: localhost:25566
> 45. restricted: false
> 46. motd: '&1Just another BungeeCord - Forced Host'
> 47. server2:
> 48. address: localhost:25567
> 49. restricted: false
> 50. motd: '&1Just another BungeeCord - Forced Host'
> 51. server3:
> 52. address: localhost:25568
> 53. restricted: false
> 54. motd: '&1Just another BungeeCord - Forced Host'
> 55. server4:
> 56. address: localhost:25569
> 57. restricted: false
> 58. motd: '&1Just another BungeeCord - Forced Host'</P>
> 59. <P align=left> 注意：以上的端口不可和上面host: 0.0.0.0:25565[这个端口是公开的，用于给玩家进入服务器]的一样！
> 60. ====================================================
> 61. ip\_forward: false[改为true]
> 62. online\_mode: true[设置为false,除非你想开正版服]
>
> *复制代码*
>
> **4.选择适合的服务端**
>
> * 选择bukkit或者spigot服务端，推荐spigot！
> * 版本必须一致！
> * 这里提供一个十分便利的spigot端，为多版本可连！1.7-1.8版本都可连接！[[点我下载](https://www.mcbbs.net/)]
> * 最后设置服务端的端口为上述配置的端口即可：
>
>   1. server1:[你要把server1设置为服务器大厅（新玩家入服的第一个服务器），就要修改上面的default\_server: server1]
>   2. address: localhost:25566
>   3. restricted: false
>   4. motd: '&1Just another BungeeCord - Forced Host'
>   5. server2:
>   6. address: localhost:25567
>   7. restricted: false
>   8. motd: '&1Just another BungeeCord - Forced Host'
>   9. server3:
>   10. address: localhost:25568
>   11. restricted: false
>   12. motd: '&1Just another BungeeCord - Forced Host'
>   13. server4:
>   14. address: localhost:25569
>   15. restricted: false
>   16. motd: '&1Just another BungeeCord - Forced Host'
>
>   *复制代码*
>
> **安全篇**
>
> * **1.防止玩家绕过默认服务器的登陆插件到了子服务器**
>
> BC权限设置得当，管理员也删除了，但是仍然发现有人绕过了登陆插件到了子服务器取得OP权限  
> 这种问题比较隐蔽，也是最近才发现的。有的群组服务器设置了登陆服务器，并且强制玩家只能先从登陆服务器进入群组，其他子服务器的spigot.yml里面设置了 bungeecord: true ，也就是不能直接用IP+端口访问到子服务器，而是需要通过BC端。  
> 然后，这些服务器在登陆服务器设置了authme等登陆插件，其他子服务器没设置，并且也关闭了/server等命令权限而使用牌子或星门等传送方式。但是，却发现有人竟然能神不知鬼不觉的绕过了登录服务器直接进入了子服务器，并用OP账号做了乱七八糟的事情。  
> 这个问题是为什么呢？  
> 其实，bungeecord: true 只是限制了想登入此服务器必须通过bungeecord端，但是他并没说这个BC端是在哪里的！  
> 也就是说，其实这些人是在自己电脑本地部署了BungeeCord端，然后直接指向了子服务器，从而能直接不验证密码登入进去。  
> 事实上，我记得在1.6的时代spigot.yml里面bungeecord: true这附近还有个设置源IP的选项，但是1.7的时候不见了，可能是为了一些多BC指向同子服务器方便吧，但是这给了一些熊孩子可乘之机，让他们不是用密码便登录了OP的账号。  
> 解决方案：
>
> **额外篇**
>
> **1.****玩家跨服聊天|出生|地标(warp)|传送(tp)|****回家(home)**  
> BungeeSuite端:
>
> * 首先必须安装MySQL数据库(别告诉我你不知道数据库是什么东东...)
> * 下载BungeeSuite【这个是跨服聊天|出生|地标(warp)|传送(tp)|回家(home)的前置必须安装】
> * 将BungeeSuite放进BC端内的plugins，重启bc！
> * 重启后，在BC端内的plugins会出现一个BungeeSuite文件夹，打开它
>
> 如图
>
> * 打开config开始配置
>
> 1. <font size="3"><font color="#000000"><font color="#333333">Database:
> 2. Host: localhost
> 3. Database: bungee
> 4. Port: '3306'
> 5. Username: root[MySQL用户名]
> 6. Password: \*\*\*\*\*\*\*\*[MySQL密码]
> 7. Threads: 5
> 8. MOTD:
> 9. Enabled: false
> 10. NewPlayerBroadcast: false
> 11. BroadcastProxyConnectionMessages: false
> 12. PlayerDisconnectDelay: 10
> 13. </font></font></font>
>
> *复制代码*
>
> * 保存即可
>
> 附加:
>
> * tab列表:[http://www.mcbbs.net/thread-330902-1-1.html](https://www.mcbbs.net/)[可显示各个服务器人数]
>
> 服务端:  
> 附加：
>
> **2.跨服玩家数据同步**
>
> **推荐使用**
>
> * playerSQL:[http://www.mcbbs.net/thread-272905-1-1.html](https://www.mcbbs.net/)
>
> **至此教程就结束了！**
>
> **ps：可能以后还会添加详细教程**

---

[🌐 原始链接](https://www.mcbbs.net/thread-424117-1-1.html)

[📎 在印象笔记中打开](evernote:///view/207087/s1/6261073b-c434-4c9b-ba31-132d7834c7cd/6261073b-c434-4c9b-ba31-132d7834c7cd/)