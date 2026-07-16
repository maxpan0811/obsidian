---
title: "如何开发1个LaunchBar action-自己动手，丰衣足食"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/如何开发1个LaunchBar action-自己动手，丰衣足食.md
tags: [印象笔记]
---

# 如何开发1个LaunchBar action-自己动手，丰衣足食

# 如何开发1个LaunchBar action-自己动手，丰衣足食 --- 如何开发 1 个 LaunchBar action - 自己动手，丰衣足食 =======================

---

# 如何开发1个LaunchBar action-自己动手，丰衣足食

---

如何开发 1 个 LaunchBar action - 自己动手，丰衣足食
=====================================

2017 年 04 月 14 日

[![](.evernote-content/3AB2312C-13CD-49CA-BC5C-DD202BDF529F/B79CD8ED-023C-4680-AAA3-2B7BC63B6A08)](https://sspai.com/user/711285/updates) 

#### [watsy0007](https://sspai.com/user/711285/updates)

最近看到 1 个效率启动神器 LaunchBar  
详细可以查看 [LaunchBar，加速并简化 Mac 操作的必备利器 | Matrix 精选](https://sspai.com/post/36732)  
在体验过程中，体会到 Instant Send 功能非常强大，可以把 mac 下各个独立的应用，脚本和服务无缝的连接起来提升 mac 使用体验。  
随着深入使用发现 launchBar 无论是自带还是三方的 action 实在是太少了，远没有 alfred 那么多的可供选择，翻了下 action 的开发资料，开发 1 个 action 并不难。  
本文写 1 个杀死进程的 action 抛砖引玉，希望能帮助大家快速上手，编写提高自己工作效率的插件  
执行效果

![](.evernote-content/3AB2312C-13CD-49CA-BC5C-DD202BDF529F/8FA01843-9490-485E-84D7-F2F802D206AF)

1. 准备工作
-------

通读 [LaunchBar 6 Developer](https://developer.obdev.at/launchbar-developer-documentation/#/welcome)  
主要了解 action 的

1. 配置
2. 支持的脚本和代码示例
3. 脚本输出格式

脚本类型大家可以选择自己擅长的，我个人习惯 ruby，所以示例选用的脚本是 ruby

2. 步骤
-----

### 2.1 新建 1 个 Action 并配置

LaunchBar 弹出菜单中选择 “Index” -> “Show Index”

![](.evernote-content/3AB2312C-13CD-49CA-BC5C-DD202BDF529F/3E4E83AB-A242-4B90-9205-FD4744CA6A52)

  
按照图中标的打开 **Action Editor**  

![](.evernote-content/3AB2312C-13CD-49CA-BC5C-DD202BDF529F/B6F25544-0441-42C2-893D-F331331EC855)

  

![](.evernote-content/3AB2312C-13CD-49CA-BC5C-DD202BDF529F/4252F991-96DA-4931-888A-895FEFAC3E36)

  
按照文档和上面 2 张图，填写基本配置  
这里需要特别标注，在开发过程中最好勾选 **Enable Debug Log**，通过系统程序 “控制台” 查看输出日志  
接下来看脚本配置页面  

![](.evernote-content/3AB2312C-13CD-49CA-BC5C-DD202BDF529F/2A669D6B-7925-43C6-930F-0A34F97ED240)

  
这里做一下说明

```
Live feedback enabled     # 立即执行，并返回
Keep window active         # 保持launchBar的输入框激活状态
Requires argument            # 需要参数 
Accepts string argument    # 字符串类型
Returns result            # 返回类型，这里选择item，列表形式返回
```

默认执行的脚本为 **default.rb** 文件

2.2 编写代码
--------

在 **Action Editor** 左侧的列表中，右键 **Kill Process** action，执行 “Show in Finder” 功能，之后 右键 KillProecss.lbaction 文件执行 “显示包内容”  
当然大家也可以在 shell 中执行

```
open ~/Library/Application\ Support/LaunchBar/Actions/KillProcess.lbaction/Contents/
```

编辑 Scripts 目录下的 default.rb 文件

```
#!/usr/bin/env ruby
#
# LaunchBar Action Script
#
require 'json'
items = []
# 进程名
process_name = ARGV.first
# 获取 ps -eo .... | grep -i 进程名 的返回值
results = IO.popen("ps -eo pid,ppid,%cpu,%mem,stat,start,ucomm,comm | grep -i #{process_name}").readlines
# 拆分返回值
results = results.map do |result|
  result.delete("\n").split(' ')
end
# 得到进程pid
pids = results.map { |res| res[0] }
# 过滤掉子进程，只保留父进程
results.delete_if { |res| pids.include? res[1] }
# 根据 action 需要格式 生成返回值
# 这里 需要注意的是 action 和 actionArgument 对应为后续执行的脚本和传递参数
results.each do |result|
  items << {
    title: result[6],
    subtitle: "cpu: #{result[2]}% mem: #{result[3]}% #{result[7]}",
    action: 'kill.rb',
    actionArgument: "#{result[0]},#{result[6]}"
  }
end
puts items.to_json
```

在 default.rb 同一目录中新建 kill.rb 文件，输入代码

```
require 'json'
pid, name = ARGV.first.split ','
`kill -9 #{pid}`
puts [{title: "#{name} killed"}].to_json
```

至此，1 个杀死进程的 action 就完成了

3 说点什么
------

写完以后想和大家分享，看了下官方论坛的 action 板块，发帖量少的可怜，大都是很老版本的。  
Google 搜索，结果也不多。  
估计还是 LaunchBar 上手有一定难度影响的。  
我建了个 [launch bar action](https://github.com/watsy0007/launchbar-actions/) github 仓库，欢迎大家在 issue 里留言自己希望开发的功能。大家多交流

---

[🌐 原始链接](https://sspai.com/post/38815)

[📎 在印象笔记中打开](evernote:///view/207087/s1/8f9b324d-7763-4888-9694-6acc356d2aa8/8f9b324d-7763-4888-9694-6acc356d2aa8/)