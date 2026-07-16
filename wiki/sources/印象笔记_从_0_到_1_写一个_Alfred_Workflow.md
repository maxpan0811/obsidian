---
title: "从 0 到 1 写一个 Alfred Workflow"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/从 0 到 1 写一个 Alfred Workflow.md
tags: [印象笔记]
---

# 从 0 到 1 写一个 Alfred Workflow

# 从 0 到 1 写一个 Alfred Workflow --- 从 0 到 1 写一个 Alfred Workflow =========================== 10月29日 [![

---

# 从 0 到 1 写一个 Alfred Workflow

---

从 0 到 1 写一个 Alfred Workflow
===========================

10月29日

[![](.evernote-content/446B5CA6-1C38-4ACD-BE74-9D21C334A405/24294ADB-CF9C-45CB-A84B-F130A2D2EC00)](https://sspai.com/user/191570)

#### [bite](https://sspai.com/user/191570)

写作时经常需要给出引用来源，每次都需要徒手去复制网页标题和 URL 然后再拼成 Markdown 格式，实在是太繁琐了，所以我在想是不是可以简化一下？经过一番折腾后，我发现通过 Alfred 的 Workflow 功能可以完美解决这个问题。

你可以通过这个 [链接](https://pan.baidu.com/s/1SL6HKrvxVD07VFdYnIyYmg) 先下载试用这个 Alfred Workflow。

解决思路
----

先利用 Alfred 的 Snippet 作为 Triggers（触发器），来调用 AppleScript 获取当前网页标题和 URL，然后以 Markdown 格式粘贴到文本中。

![](.evernote-content/446B5CA6-1C38-4ACD-BE74-9D21C334A405/FD9D1924-F342-4944-BCD5-D8002A6A757B.png)

### Triggers: Snippet

Snippet 是「快捷短语」，如果将它作为触发器，在打字输入指定短语后会立刻执行后续动作。在这里我将短语设置为 `url`，用来触发后续的动作 Run Script。

在 Snippet 这个触发器中，默认前缀设置为 `\\`，那么当你需要触发短语时，就需要在你设置的短语前加上这个前缀，比如在这个 Workflow 中我需要输入 `\\url` 才会成功触发下一个动作。

至于为什么用 Snippet Trigger 嘛，因为可以省去使用快捷键唤出 Alfred 这一步，这样一来就不会打断写作过程了。

### Actions: Run Script

参考 Alfred 官方论坛上的 [这篇文章](https://www.alfredforum.com/topic/2013-how-to-get-frontmost-tab%E2%80%99s-url-and-title-of-various-browsers/)，并稍作修改，可以实现的功能是获取浏览器最近活跃标签页的标题和 URL。将下面的代码填入到 Run Script 的相应区域中，第二步就完成了。

```
set browser to do shell script "export VERSIONER_PERL_PREFER_32_BIT=yes; perl -MMac::InternetConfig -le 'print +(GetICHelper \"http\")[1]'"

if (browser = "Google Chrome") or (browser = "Google Chrome Canary") or (browser = "Chromium") or (browser = "Opera") or (browser = "Vivaldi") then
    using terms from application "Google Chrome"
        tell application browser to set currentTabTitle to title of active tab of front window
        tell application browser to set currentTabUrl to URL of active tab of front window
    end using terms from
else if (browser = "Safari") or (browser = "Safari Technology Preview") or (browser = "Webkit") then
    using terms from application "Safari"
        tell application browser to set currentTabTitle to name of front document
        tell application browser to set currentTabUrl to URL of front document
    end using terms from
else
    return browser
end if

return "[" & currentTabTitle & "](" & currentTabUrl & ")"
```

### Outputs: Copy to Clipboard

最后一步是 Copy to Clipboard，把结果放到剪贴板里。当你想在编辑器中插入引用来源时，只需按下 `⌘Command-V` 粘贴即可。当然，你也可以在 Alfred 里设置「自动粘贴到最前面的应用」，这样连 `⌘Command-V` 都省了。

另外，Copy to Clipboard 这个动作还可以将复制的项目标记为「transient」，这样一来它就不会「沾染」剪贴板内容。

如果你希望这个 Workflow 直接将链接粘贴到编辑器中，并且不要影响你的剪贴板，那么两个选框都打勾即可：

![](.evernote-content/446B5CA6-1C38-4ACD-BE74-9D21C334A405/CAEF4700-2DA6-4E04-BE8C-D929876DE031.png)

先在 iA Writer 上测试，通过 。

![](.evernote-content/446B5CA6-1C38-4ACD-BE74-9D21C334A405/3F09A31D-F16E-4462-9789-9B227B7A0FFB.gif)

但在 Ulysses 上测试失败了，因为它不⽀持直接输⼊ Markdown 格式的链接。

![](.evernote-content/446B5CA6-1C38-4ACD-BE74-9D21C334A405/0FE48CB4-F5F1-472E-A9FF-BC0EF5D16762.gif)

升级方案
----

### Ulysses 的兼容性

Ulysses 为兼容 Markdown 提供了 Paste from Markdown 功能，⽽且有快捷键 `⌥Alt-⌘Command-V` ，这样就可以⾃动化了。AppleScript 脚本如下：

```
tell application "System Events" to key code 9 using {option down, command down}
```

### 增加流程控制

因为在不同的编辑器中需要执⾏的动作有差异，所以需要在 Workﬂow 中进行判断。通过查阅 Alfred ⽂档， 我发现 [Filter Utility](https://www.alfredapp.com/help/workflows/utilities/filter/) 可以拿来⼀⽤。同样⾮常简单，改进后的流程图如下：

![](.evernote-content/446B5CA6-1C38-4ACD-BE74-9D21C334A405/21DA3B81-2936-4339-A1BF-684F34BAFC45.png)

橙⾊就是 Ulysses 的专属⽀线了。两个⼩漏⽃（Filter）就相当于 if 语句，橙色 Filter 配置如下：

![](.evernote-content/446B5CA6-1C38-4ACD-BE74-9D21C334A405/886DCF24-226A-40A4-B9CC-302ED4660E1C.png)

等⼀下，上图中的 `{var:editor}` 是什么？

其实它是 Focused App Variable（焦点软件变量），需要在 Triggers: Snippet 中进⾏配置。它的值就是当前具有焦点的 App 的 bundle id。

![](.evernote-content/446B5CA6-1C38-4ACD-BE74-9D21C334A405/360C35EC-C06A-4DBA-A8F9-5D65A2E4D47E.png)

那 `com.soulmen.ulysses-setapp` ⼜是什么？

就是 Setapp 中的 Ulysses 的 bundle id 啦。其他版本 Ulysses 的 bundle id 可以通过这个命令得到：

```
osascript -e 'id of app "Ulysses"'
```

### 测试

将 Ulysses 的 Paste from Markdown 脚本添加到 Ulysses 专属⽀线的最后一步后，这个升级版的 Alfred Workflow 就大功告成了。这样一来，你在普通编辑器上直接运行该 Workflow 时，会直接粘贴标准 Markdown 格式下的链接，当你在 Ulysses 上运行该 Workflow 时，会触发 Paste from Markdown 功能，将标准 Markdown 格式下的链接转换为 Ulysses 自己的格式。

![](.evernote-content/446B5CA6-1C38-4ACD-BE74-9D21C334A405/90748848-341B-46CC-B492-D42E29975880.gif)

### PS

看到有不少反馈 Ulysses 兼容性问题，更新了一个版本：[下载](https://github.com/cdpath/alfred_workflows/releases/download/0.1.0/url2md.alfredworkflow)。

这个版本改动较大，支持了 Evernote/Scapple/Notes 这类只允许复文本链接的编辑器。

> 下载少数派 [客户端](https://sspai.com/page/client)、关注 [少数派公众号](http://sspai.com/s/KEPQ) ，让你的工作更有效率 ⏱

> 获取特惠、正版、高品质软件，尽在 [少数派数字商城·正版软件](https://sspai.com/mall)

[#Markdown](https://sspai.com/tag/Markdown) [#效率工具](https://sspai.com/tag/%e6%95%88%e7%8e%87%e5%b7%a5%e5%85%b7) [#效率](https://sspai.com/tag/%e6%95%88%e7%8e%87) [#Alfred](https://sspai.com/tag/Alfred)

---

[68](#)

---

[![](.evernote-content/446B5CA6-1C38-4ACD-BE74-9D21C334A405/B454C42B-0310-4848-BC36-C46A8403764B)](https://sspai.com/user/191570)

#### 

#### [bite](https://sspai.com/user/191570)

[关注](#)

---

[🌐 原始链接](https://sspai.com/post/47710)

[📎 在印象笔记中打开](evernote:///view/207087/s1/aeac304b-fa45-4069-ab5a-e1953450c390/aeac304b-fa45-4069-ab5a-e1953450c390/)