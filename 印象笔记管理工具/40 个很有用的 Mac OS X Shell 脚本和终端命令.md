# 40 个很有用的 Mac OS X Shell 脚本和终端命令

---

[40 个很有用的 Mac OS X Shell 脚本和终端命令](http://www.oschina.net/question/12_62983)
===========================================================================

这里有一堆的 Mac OS X 下的终端命令，我将这些命令进行了简单的分类，这里很多命令在其他系统（Windows、Linux）一样有效，特别是 Linux/Unix。希望这些命令对你有帮助。

### 系统

重启 Mac OS X:

|  |  |
| --- | --- |
| `1` | `shutdown` `- r now` |

关闭 Mac OS X:

[view source](http://www.oschina.net/question/12_62983#viewSource "view source")[print](http://www.oschina.net/question/12_62983#printSource "print")[?](http://www.oschina.net/question/12_62983#about "?")

|  |  |
| --- | --- |
| `1` | `shutdown` `now` |

### 电源管理/省电

获取当前电源管理设置的信息

|  |  |
| --- | --- |
| `1` | `pmset -g` |

设置显示器无活动15分钟后关闭

|  |  |
| --- | --- |
| `1` | `sudo` `pmset displaysleep 15` |

让计算机在无活动30分钟后休眠

|  |  |
| --- | --- |
| `1` | `sudo` `pmset``sleep` `30` |

### OS X 外观

禁用仪表盘（别忘了将仪表盘 Dock 图标拖动出来）

|  |  |
| --- | --- |
| `1` | `defaults write com.apple.dashboard mcx-disabled -boolean YES` |

|  |  |
| --- | --- |
| `2` | `killall Dock` |

启用仪表盘

|  |  |
| --- | --- |
| `1` | `defaults write com.apple.dashboard mcx-disabled -boolean NO` |

|  |  |
| --- | --- |
| `2` | `killall Dock` |

强制 Finder 程序显示隐藏文件

|  |  |
| --- | --- |
| `1` | `defaults write com.apple.finder AppleShowAllFiles TRUE` |

强制 Finder 程序不显示隐藏文件

|  |  |
| --- | --- |
| `1` | `defaults write com.apple.finder AppleShowAllFiles FALSE` |

### 网络

ping 某个主机

|  |  |
| --- | --- |
| `1` | `ping` `-o oschina.net` |

使用 traceroute 诊断到某个主机的路由节点

|  |  |
| --- | --- |
| `1` | `traceroute` `oschina.net` |

检查某个主机是否运行 HTTP 服务，或者检查某网站是否可用

|  |  |
| --- | --- |
| `1` | `curl -I www.oschina.net |``head` `-n 1` |

管理 Windows 网络（相当于 Windows 下的 NET 命令），该命令有很多选项，运行下面命令来查看这些选项

|  |  |
| --- | --- |
| `1` | `man` `net` |

使用 dig 来诊断域名信息

|  |  |
| --- | --- |
| `1` | `dig` `www.oschina.net A` |

|  |  |
| --- | --- |
| `2` | `dig` `www.oschina.net MX` |

查看谁正在登录到你的 Mac 机器

|  |  |
| --- | --- |
| `1` | `w` |

显示系统路由表

|  |  |
| --- | --- |
| `1` | `netstat` `-r` |

显示活动网络连接

|  |  |
| --- | --- |
| `1` | `netstat` `-an` |

显示网络统计

|  |  |
| --- | --- |
| `1` | `netstat` `-s` |

### 故障诊断

列表所有打开的文件

|  |  |
| --- | --- |
| `1` | `lsof` |

重启 Bonjour – 当网络中没有 Mac 时很有用

|  |  |
| --- | --- |
| `1` | `sudo` `launchctl unload /System/Library/LaunchDaemons/com.apple.mDNSResponder.plist` |

|  |  |
| --- | --- |
| `2` | `sudo` `launchctl load /System/Library/LaunchDaemons/com.apple.mDNSResponder.plist` |

弹出 CD （注意不一定是 disk1）

|  |  |
| --- | --- |
| `1` | `diskutil``eject` `disk1` |

### 文本操作命令

*经常你需要从剪切板或者文件中获取某些文本，并对这些文本进行转换和使用，这里列举的命令都是跟文本处理相关的*

统计剪贴板中文本的行数

|  |  |
| --- | --- |
| `1` | `pbpaste |``wc` `-l` |

统计剪贴板中文本的单词数

|  |  |
| --- | --- |
| `1` | `pbpaste |``wc` `-w` |

对剪贴板中的文本行进行排序后重新写回剪贴板

|  |  |
| --- | --- |
| `1` | `pbpaste |``sort` `| pbcopy` |

对剪贴板中的文本行进行倒序后放回剪贴板

|  |  |
| --- | --- |
| `1` | `pbpaste | rev | pbcopy` |

移除剪贴板中重复的文本行，然后写回剪贴板

|  |  |
| --- | --- |
| `1` | `pbpaste |``sort` `|``uniq` `| pbcopy` |

找出剪贴板中文本中存在的重复行，并复制后写回剪贴板（包含重复行的一行）

|  |  |
| --- | --- |
| `1` | `pbpaste |``sort` `|``uniq` `-d | pbcopy` |

找出剪贴板中文本中存在的重复行，并复制后写回剪贴板（不包含重复行）

|  |  |
| --- | --- |
| `1` | `pbpaste |``sort` `|``uniq` `-u | pbcopy` |

对剪贴板中的 HTML 文本进行清理后写回剪贴板

|  |  |
| --- | --- |
| `1` | `pbpaste | tidy | pbcopy` |

显示剪贴板中文本的前 5 行

|  |  |
| --- | --- |
| `1` | `pbpaste |``head` `-n 5` |

显示剪贴板中文本的最后 5 行

|  |  |
| --- | --- |
| `1` | `pbpaste |``tail` `-n 5` |

将剪贴板中文本里存在的 Tab 跳格符号转成空格

|  |  |
| --- | --- |
| `1` | `pbpaste |``expand` `| pbcopy` |

### 其他有用的命令

#### A:

|  |  |
| --- | --- |
| `1` | `htpasswd -nb username password` |

#### B:

|  |  |
| --- | --- |
| `1` | `AuthType Basic` |

|  |  |
| --- | --- |
| `2` | `AuthName``"restricted area"` |

|  |  |
| --- | --- |
| `3` | `AuthUserFile /path/to/your/site/.htpasswd` |

|  |  |
| --- | --- |
| `4` | `require valid-user` |

显示终端窗口中之前输入的命令

|  |  |
| --- | --- |
| `1` | `history` |

将文件转成 HTML，支持格式包括 Text, .RTF, .DOC.

|  |  |
| --- | --- |
| `1` | `textutil -convert html``file``.extension` |

Nano 是一个很简单易用的文本编辑器，可用于快速更改文本文件，比 vim 功能弱很多，但很方便

|  |  |
| --- | --- |
| `1` | `nano [file_to_edit]` |

在 nano 编辑器中，可使用 ctrl+o 来保持，ctrl+x 来退出。

清理终端显示的内容

|  |  |
| --- | --- |
| `1` | `clear` |

### iTunes 相关

更改 iTunes 链接行为为本机 iTunes 库，而不是 iTunes Store

|  |  |
| --- | --- |
| `1` | `defaults write com.apple.iTunes invertStoreLinks -bool YES` |

更改 iTunes 链接行为为 iTunes Store，而不是本机 iTunes 库

|  |  |
| --- | --- |
| `1` | `defaults write com.apple.iTunes invertStoreLinks -bool NO` |

### 其他 Mac OS X 终端资源

[Mac OS X Hacking Tools](http://www.kernelthread.com/mac/osx/tools.html) (old but detailed list for the obsessive only).

[Cameron Hayne’s Bash Scripts](http://hayne.net/MacDev/Bash/)

[Mac OS X Hints](http://www.macosxhints.com/)

[Apple Forums](http://discussions.apple.com/)

注意: 前面的很多例子我们用了 pbpaste 来从剪贴板中获取数据，也可使用 cat 来从文件中获取数据

|  |  |
| --- | --- |
| `1` | `cat` `[/path/to/filename]` |

要将结果放到桌面的一个文件，可将 pbcopy 替换为：

|  |  |
| --- | --- |
| `1` | `> ~/Desktop/filename.txt` |

[📎 在印象笔记中打开](evernote:///view/207087/s1/f7393640-80ed-4091-96ed-1394825ab666/f7393640-80ed-4091-96ed-1394825ab666/)