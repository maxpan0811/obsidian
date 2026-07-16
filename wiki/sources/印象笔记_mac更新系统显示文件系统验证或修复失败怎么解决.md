---
title: "mac更新系统显示文件系统验证或修复失败怎么解决"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/mac更新系统显示文件系统验证或修复失败怎么解决.md
tags: [印象笔记]
---

# mac更新系统显示文件系统验证或修复失败怎么解决

# mac更新系统显示文件系统验证或修复失败怎么解决 --- [红颜一笑丿寓w](http://zhidao.baidu.com/usercenter?uid=dd0d4069236f25705e79

---

# mac更新系统显示文件系统验证或修复失败怎么解决

---

[红颜一笑丿寓w](http://zhidao.baidu.com/usercenter?uid=dd0d4069236f25705e79891e) | 浏览 356 次  2016-05-02 17:28

2016-05-20 13:20

[# 厉害了，word芝麻！优质回答超级赛火热开赛~#](http://zhidao.baidu.com/activity/commact?name=chaoji)

最佳答案

1、当遇到上面的情况时，这是因为 Mac OS 系统内部文件系统在验证时出错，导致不能将空余的分区合并到 Mac OS 分区中。这时请重新启动 Mac 系统，在重启时请按住键盘上的 Command+S 键，进入安全模式。如果没成功的话，请多尝试几次，在重启听到声音前按下。

  2、随后你会在屏幕上看到一串串字条在跳动，当不动时请按键盘上的“回车”键，出现命令提示符，如图所示  
  3、接着请输入 fsck -f 命令，并按下键盘上的“回车”键执行命令。  
  4、随后请等待修复文件系统，修复的速度会根据硬盘速度的快慢，如图所示  
  5、当修复完成以后并看到屏幕上提示“ The volume Macintosh HD was reaired successfully”时，说明已经成功，如图所示  
  6、接下来请输入 reboot 命令，从安全模式下重新启动电脑。  
  7、重启以后，再打开磁盘工具，对分区进行合并就可以了。

[📎 在印象笔记中打开](evernote:///view/207087/s1/fd882df0-d511-4cd4-a10f-f340c33d60a2/fd882df0-d511-4cd4-a10f-f340c33d60a2/)