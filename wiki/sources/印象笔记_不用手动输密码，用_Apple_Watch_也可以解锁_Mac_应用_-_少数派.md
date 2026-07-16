---
title: "不用手动输密码，用 Apple Watch 也可以解锁 Mac 应用 - 少数派"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/不用手动输密码，用 Apple Watch 也可以解锁 Mac 应用 - 少数派.md
tags: [印象笔记]
---

# 不用手动输密码，用 Apple Watch 也可以解锁 Mac 应用 - 少数派

# 不用手动输密码，用 Apple Watch 也可以解锁 Mac 应用 - 少数派 --- 不用手动输密码，用 Apple Watch 也可以解锁 Mac 应用 ==================

---

# 不用手动输密码，用 Apple Watch 也可以解锁 Mac 应用 - 少数派

---

不用手动输密码，用 Apple Watch 也可以解锁 Mac 应用
==================================

如果你使用过带 Touch ID 的 MacBook Air 或者 MacBook Pro，那么一定会被指纹解锁的便捷性所深深打动。除了解锁 Mac，Touch ID 现在还被 1Password、Day One、MoneyWiz 等第三方 App 用来登录解锁，真的是属于用过就回不去的一个功能。特别是对于 1Password 这类密码管理类应用，主密码一般会设置地又长又复杂，如果每次都要手动输入，可谓是「苦不堪言」。

可是，如果你的 MacBook 没有配备 Touch ID 或者你将 MacBook 合盖外接显示器使用，就难免要手动输入主密码来解锁 1Password。为了解决这个问题，我最初采用的方法是通过 Keyboard Maestro 来获取预先储存在钥匙串访问 App 中的 1Password 主密码，然后再自动完成「输入文本（密码）- 按下回车键」等操作。但是，这个方案最大的问题是你必须让 Keyboard Maestro 获得对钥匙串访问 App 的访问权限，同时第三方剪切板 App 也会记录主密码的明文。

关联阅读：[Keyboard Maestro 入门指南](https://sspai.com/post/36442)

如果你像我一样不愿意信赖一款第三方 App 获得系统密码管理工具的访问权限，那么可以试试我今天介绍的这个方法，前提是你要有一块 Apple Watch，并且保证所有设备都升级到了最新的系统。

契机与思路
-----

我设计这个方案，最关键的一点是 Apple 在 macOS Catalina 中增加了 Apple Watch 的功能，除了在登录的时候解锁，还可以在备忘录 App、Safari 中的密码、系统偏好设置等场景下用来提供授权。虽然 Ulysses 已经提供了通过 Apple Watch 来解锁 App 的功能，但是我不清楚是不是利用了这个新特性，1Password 也至今没有推出这个功能。

所以，这套方案的思路大致如下：

1. 打开 Safari，并依次点击「偏好设置…- 密码」，这时候系统会提示你输入密码，你可以直接手动输入密码、使用 Touch ID，**也可以通过在 Apple Watch 上双击电源键来解锁**；
2. 预先在密码中新增一个登录项，网址可以设置为 1password.com，密码一栏填写为 1Password 的主密码；
3. 选择并聚焦于第一行，这时候密码一列会显示一定长度的密码，所以务必把你的 1Password 主密码设置地「又臭又长」；
4. 打开 1Password 并模拟键盘输入「储存于 Safari 密码中的 1Password 主密码」，然后继续模拟键盘输入「回车键」。

其中，第二点是可以优化的，如果你了解 AppleScript，那么可以尝试让脚本自动搜索到你填写 1Password 主密码的那一行。如果你像我一样不怎么了解，那么不管网址填什么，只要确保**这个登录项在按网址排序后位于第一行就行**。你只需在 Safari 的「偏好设置 - 密码」中排序一次，系统就会永远记住你的排序，直到你重新排序。

操作过程
----

首先，在「系统偏好设置 - 安全性与隐私 - 隐私」中的「辅助功能」中确保添加并启用了相关的自动化 App，如 Keyboard Maestro、脚本编辑器、自动操作、LaunchBar、Alfred 等。因为这一套自动化流程是通过 AppleScript 来完成的，所以你可以根据自己的喜好来选择触发的工具。

![](.evernote-content/90A8C506-5BD8-49C1-9494-7F0561DF514B/759FE0B4-9078-4F95-8124-47DE740CA0FE.png)

其次，在「系统偏好设置 - 安全性与隐私 - 通用」中勾选「使用您的 Apple Watch 来解锁 App 和 Mac」。

![](.evernote-content/90A8C506-5BD8-49C1-9494-7F0561DF514B/E04D66B5-E5DD-4224-9D4C-E6A76CFB9620.png)

最后，以 Keyboard Maestro 为例，新建一个 macro，trigger 设置为「This hot key」，然后录入自己喜欢的快捷键，action 中使用「Execute an AppleScript」，然后粘贴如下代码：

```
tell application "Safari"
	activate
end tell

tell application "System Events" to tell application process "Safari"
	set frontmost to true
	delay 0.1
	keystroke "," using {command down}
	set tb to toolbar 1 of window 1
	set buttonName to (name of button 4 of tb as string)
	click button 4 of tb
	tell application "System Events" to tell application process "Safari"
		set frontmost to true
	end tell
	
	delay 2
	
	set prefsWin to window 1
	set theTable to table 1 of scroll area 1 of group 1 of group 1 of prefsWin
	
	tell theTable
		select the row 1
		set focused to true
		set thePass to the value of static text of item 1 of UI element 3 of row 1
		
		do shell script "ps -ef | grep 'Safari' | grep -v grep | awk '{print $2}' | xargs kill -9"
		
		do shell script "ps -ef | grep '1Password 7' | grep -v grep | awk '{print $2}' | xargs kill -9"
		
		delay 0.1
		
		tell application "1Password 7"
			activate
		end tell
		
		tell application "System Events" to tell application process "1Password 7"
			set frontmost to true
		end tell
		
		delay 1
		
		tell application "System Events" to keystroke thePass
		tell application "System Events" to key code 36
	end tell
end tell
```

**这里我必须得说明一下，我知道代码写得烂，大家看一下思路就行，有能力的可以自己动手改造，和我一样不太会的可以直接搬用上面的代码到触发工具里使用。**

![](.evernote-content/90A8C506-5BD8-49C1-9494-7F0561DF514B/BFFE1EED-F081-491C-B560-16856B8E52EA.png)

最后的实现效果如下：

![](.evernote-content/90A8C506-5BD8-49C1-9494-7F0561DF514B/8498935B-2012-407D-A1E0-33E371B6047C.gif)

小结
--

最后再重申几个比较重要的点：

* 在 Safari 的密码中选中 1Password 这一栏时会显示一定长度的密码，这是此方案最大的隐患，但是只要你的 1Password 主密码足够长，就可以消除这个隐患；
* 不管是用哪个自动化工具来触发，一定要记得给「辅助功能」的权限；
* AppleScript 中很多参数都可以自己调，大家按需更改

如果你对这套方案有什么改进的建议，或者你有其他更好的方案，欢迎在评论区一起交流。

**免责声明：本方案同样不能保证绝对的安全，请大家根据自己的需求来自行决定是否采用。若出现信息泄漏问题，本人概不负责。**

> 下载少数派 [客户端](https://sspai.com/page/client)、关注 [少数派公众号](https://sspai.com/s/J71e) ，让你更有效率地使用 Mac ⏱

> 特惠、好用的硬件产品，尽在 [少数派 sspai 官方店铺](https://shop549593764.taobao.com/?spm=a230r.7195193.1997079397.2.2ddc7e0bPqKQHc)

Measure

Measure

---

[🌐 原始链接](https://sspai.com/post/58270)

[📎 在印象笔记中打开](evernote:///view/207087/s1/daadc9c3-fd4f-4f2c-a13a-dc0911073321/daadc9c3-fd4f-4f2c-a13a-dc0911073321/)