---
title: "用ubuntu建立《我的世界》国际版服务器"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/用ubuntu建立《我的世界》国际版服务器.md
tags: [印象笔记]
---

# 用ubuntu建立《我的世界》国际版服务器

# 用ubuntu建立《我的世界》国际版服务器 --- * 购买云服务器：4核8G5M，ubuntu系统20.04 64位。据介绍可以承载10人同时在线。 * 天翼云IP：180.102.25.12 

---

# 用ubuntu建立《我的世界》国际版服务器

---

* 购买云服务器：4核8G5M，ubuntu系统20.04 64位。据介绍可以承载10人同时在线。
* 天翼云IP：180.102.25.12
* 阿里云IP：106.14.249.205
* ubuntu系统中通过鼠标左键选中即为拷贝，点右键即为粘贴
* 升级apt软件：sudo apt-get update
* 安装java软件：sudo apt-get install openjdk-17-jdk
* 查看java安装是否正确：java -version
* 建立minecraft目录：mkdir minecraft\_server\_1.18.2
* 进入minecraft目录：
  cd minecraft\_server\_1.18.2
* 安装minecraft国际版的java server 1.18.2：sudo wget <https://launcher.mojang.com/v1/objects/c8f83c5655308435b3dcf03c06d9fe8740a77469/server.jar>
* 安装minecraft国际版的java server 1.19.3 sudo get <https://piston-data.mojang.com/v1/objects/c9df48efed58511cdd0213c56b9013a7b5c9ac1f/server.jar>
* 安装screen软件：sudo apt install screen
* 用screen软件启动server，可以保证server在远程连接关闭后继续运行：sudo screen java -jar server.jar --nogui
* screen -ls
* screen -r ：重新远程登录后通过r参数回到之前运行的程序
* 停止server软件运行用stop命令
* 在退出远程登录后再回到系统，用命令：sudo screen -r 回到minecraft server，注意因为是root账号在运行的，所以必须加上sudo
* 在用screen运行server程序过程中，按ctrl-a后再输入相关参数，比如d，切回到主界面
* 用top命令实时查看系统资源的占用情况，按q退出
* 用VI编辑server.properties文件，输入i进入编辑模式，按ESC，输入:wq保存退出。
* 第一次启动会失败，用VI编辑EULA.txt文件，将eulaFalse改为Ture。
* 下载对应版本的Forge软件：sudo wget [https://maven.minecraftforge.net/net/minecraftforge/forge/1.18.2-40.2.0/forge-1.18.2-40.2.0-installer.jar](https://adfoc.us/serve/sitelinks/?id=271228&url=https://maven.minecraftforge.net/net/minecraftforge/forge/1.18.2-40.2.0/forge-1.18.2-40.2.0-installer.jar)
* 安装Forge：
  java -jar forge-1.18.2-40.2.0-installer.jar nogui --installServer
* 把原服务器存档传输到本服务器：
  rsync -v -u -a --rsh=ssh --stats root@106.14.249.205:/root/minecraft\_server\_1.18.2/world/  ~/minecraft\_server\_1.18.2/world/
* 在run.sh文件中java命令前加上screen命令
* 启动服务器端的Forge服务器:./run.sh
* 移动/更名目录：sudo mv former\_name/ new\_name/
* 彻底删除目录/文件无提示：rm -r world/
* 新建mods目录：mkdir mods

Minecraft help

[13:13:52] [Server thread/INFO]: /advancement (grant|revoke)

[13:13:52] [Server thread/INFO]: /ban <targets> [<reason>]

[13:13:52] [Server thread/INFO]: /ban-ip <target> [<reason>]

[13:13:52] [Server thread/INFO]: /banlist [ips|players]

[13:13:52] [Server thread/INFO]: /bossbar (add|get|list|remove|set)

[13:13:52] [Server thread/INFO]: /clear [<targets>]

[13:13:52] [Server thread/INFO]: /clone <begin> <end> <destination> [filtered|masked|replace]

[13:13:52] [Server thread/INFO]: /data (get|merge|remove)

[13:13:52] [Server thread/INFO]: /datapack (disable|enable|list)

[13:13:52] [Server thread/INFO]: /debug (start|stop)

[13:13:52] [Server thread/INFO]: /defaultgamemode (adventure|creative|spectator|survival)

[13:13:52] [Server thread/INFO]: /deop <targets>

[13:13:52] [Server thread/INFO]: /difficulty [easy|hard|normal|peaceful]

[13:13:52] [Server thread/INFO]: /effect (clear|give)

[13:13:52] [Server thread/INFO]: /enchant <targets> <enchantment> [<level>]

[13:13:52] [Server thread/INFO]: /execute (align|anchored|as|at|facing|if|in|positioned|rotated|run|store|unless)

[13:13:52] [Server thread/INFO]: /experience (add|query|set)

[13:13:52] [Server thread/INFO]: /fill <from> <to> <block> [destroy|hollow|keep|outline|replace]

[13:13:52] [Server thread/INFO]: /forceload (add|query|remove)

[13:13:52] [Server thread/INFO]: /function <name>

[13:13:52] [Server thread/INFO]: /gamemode (adventure|creative|spectator|survival)

[13:13:52] [Server thread/INFO]: /gamerule (announceAdvancements|commandBlockOutput|disableElytraMovementCheck|doDaylightCycle|doEntityDrops|doFireTick|doLimitedCrafting|doMobLoot|doMobSpawning|doTileDrops|doWeatherCycle|keepInventory|logAdminCommands|maxCommandChainLength|maxEntityCramming|mobGriefing|naturalRegeneration|randomTickSpeed|reducedDebugInfo|sendCommandFeedback|showDeathMessages|spawnRadius|spectatorsGenerateChunks)

[13:13:52] [Server thread/INFO]: /give <targets> <item> [<count>]

[13:13:52] [Server thread/INFO]: /help [<command>]

[13:13:52] [Server thread/INFO]: /kick <targets> [<reason>]

[13:13:52] [Server thread/INFO]: /kill <targets>

[13:13:52] [Server thread/INFO]: /list [uuids]

[13:13:52] [Server thread/INFO]: /locate (Buried\_Treasure|Desert\_Pyramid|EndCity|Fortress|Igloo|Jungle\_Pyramid|Mansion|Mineshaft|Monument|Ocean\_Ruin|Shipwreck|Stronghold|Swamp\_Hut|Village)

[13:13:52] [Server thread/INFO]: /me <action>

[13:13:52] [Server thread/INFO]: /msg <targets> <message>

[13:13:52] [Server thread/INFO]: /op <targets>

[13:13:52] [Server thread/INFO]: /pardon <targets>

[13:13:52] [Server thread/INFO]: /pardon-ip <target>

[13:13:52] [Server thread/INFO]: /particle <name> [<pos>]

[13:13:52] [Server thread/INFO]: /playsound <sound> (ambient|block|hostile|master|music|neutral|player|record|voice|weather)

[13:13:52] [Server thread/INFO]: /recipe (give|take)

[13:13:52] [Server thread/INFO]: /reload

[13:13:52] [Server thread/INFO]: /replaceitem (block|entity)

[13:13:52] [Server thread/INFO]: /save-all [flush]

[13:13:52] [Server thread/INFO]: /save-off

[13:13:52] [Server thread/INFO]: /save-on

[13:13:52] [Server thread/INFO]: /say <message>

[13:13:52] [Server thread/INFO]: /scoreboard (objectives|players)

[13:13:52] [Server thread/INFO]: /seed

[13:13:52] [Server thread/INFO]: /setblock <pos> <block> [destroy|keep|replace]

[13:13:52] [Server thread/INFO]: /setidletimeout <minutes>

[13:13:52] [Server thread/INFO]: /setworldspawn [<pos>]

[13:13:52] [Server thread/INFO]: /spawnpoint [<targets>]

[13:13:52] [Server thread/INFO]: /spreadplayers <center> <spreadDistance> <maxRange> <respectTeams> <targets>

[13:13:52] [Server thread/INFO]: /stop

[13:13:52] [Server thread/INFO]: /stopsound <targets> [\*|ambient|block|hostile|master|music|neutral|player|record|voice|weather]

[13:13:52] [Server thread/INFO]: /summon <entity> [<pos>]

[13:13:52] [Server thread/INFO]: /tag <targets> (add|list|remove)

[13:13:52] [Server thread/INFO]: /team (add|empty|join|leave|list|modify|remove)

[13:13:52] [Server thread/INFO]: /teleport (<destination>|<location>|<targets>)

[13:13:52] [Server thread/INFO]: /tell -> msg

[13:13:52] [Server thread/INFO]: /tellraw <targets> <message>

[13:13:52] [Server thread/INFO]: /time (add|query|set)

[13:13:52] [Server thread/INFO]: /title <targets> (actionbar|clear|reset|subtitle|times|title)

[13:13:52] [Server thread/INFO]: /tp -> teleport

[13:13:52] [Server thread/INFO]: /trigger <objective> [add|set]

[13:13:52] [Server thread/INFO]: /w -> msg

[13:13:52] [Server thread/INFO]: /weather (clear|rain|thunder)

[13:13:52] [Server thread/INFO]: /whitelist (add|list|off|on|reload|remove)

[13:13:52] [Server thread/INFO]: /worldborder (add|center|damage|get|set|warning)

[13:13:52] [Server thread/INFO]: /xp -> experience

[📎 在印象笔记中打开](evernote:///view/207087/s1/12043127-7c97-451d-bc83-958e3d667c63/12043127-7c97-451d-bc83-958e3d667c63/)