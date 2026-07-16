---
title: "Mac OS X：“安全启动”和“安全模式”是什么？_百度知道"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/Mac OS X：“安全启动”和“安全模式”是什么？_百度知道.md
tags: [印象笔记]
---

# Mac OS X：“安全启动”和“安全模式”是什么？_百度知道

# Mac OS X：“安全启动”和“安全模式”是什么？_百度知道 --- Mac OS X：“安全启动”和“安全模式”是什么？ ========================== [](#)[

---

# Mac OS X：“安全启动”和“安全模式”是什么？_百度知道

---

Mac OS X：“安全启动”和“安全模式”是什么？
==========================

[](#)[](http://v.t.sina.com.cn/share/share.php?url=http%3A%2F%2Fzhidao.baidu.com%2Fquestion%2F1510045416401069820%3Fsharesource%3Dweibo&title=Mac%20OS%20X%EF%BC%9A%E2%80%9C%E5%AE%89%E5%85%A8%E5%90%AF%E5%8A%A8%E2%80%9D%E5%92%8C%E2%80%9C%E5%AE%89%E5%85%A8%E6%A8%A1%E5%BC%8F%E2%80%9D%E6%98%AF%E4%BB%80%E4%B9%88%EF%BC%9F_%E7%99%BE%E5%BA%A6%E7%9F%A5%E9%81%93&pic=https%3A%2F%2Fgss0.bdstatic.com%2F70cFsjip0QIZ8tyhnq%2Fimg%2Fiknow%2Fzhidaologo.png)[](http://connect.qq.com/widget/shareqq/index.html?url=http%3A%2F%2Fzhidao.baidu.com%2Fquestion%2F1510045416401069820%3Fsharesource%3Dqq&title=Mac%20OS%20X%EF%BC%9A%E2%80%9C%E5%AE%89%E5%85%A8%E5%90%AF%E5%8A%A8%E2%80%9D%E5%92%8C%E2%80%9C%E5%AE%89%E5%85%A8%E6%A8%A1%E5%BC%8F%E2%80%9D%E6%98%AF%E4%BB%80%E4%B9%88%EF%BC%9F_%E7%99%BE%E5%BA%A6%E7%9F%A5%E9%81%93&pics=https%3A%2F%2Fgss0.bdstatic.com%2F70cFsjip0QIZ8tyhnq%2Fimg%2Fiknow%2Fzhidaologo.png)[](http://sns.qzone.qq.com/cgi-bin/qzshare/cgi_qzshare_onekey?url=http%3A%2F%2Fzhidao.baidu.com%2Fquestion%2F1510045416401069820%3Fsharesource%3Dqzone&title=Mac%20OS%20X%EF%BC%9A%E2%80%9C%E5%AE%89%E5%85%A8%E5%90%AF%E5%8A%A8%E2%80%9D%E5%92%8C%E2%80%9C%E5%AE%89%E5%85%A8%E6%A8%A1%E5%BC%8F%E2%80%9D%E6%98%AF%E4%BB%80%E4%B9%88%EF%BC%9F_%E7%99%BE%E5%BA%A6%E7%9F%A5%E9%81%93&pics=https%3A%2F%2Fgss0.bdstatic.com%2F70cFsjip0QIZ8tyhnq%2Fimg%2Fiknow%2Fzhidaologo.png)

[晴天270](http://zhidao.baidu.com/usercenter?uid=f07c4069236f25705e79891e)
| 浏览 13759 次

2013-10-15 17:04

2013-10-16 08:25

[# 厉害了，word芝麻！优质回答超级赛火热开赛~#](http://zhidao.baidu.com/activity/commact?name=chaoji)


最佳答案

```
“安全模式”是一种状态，可通过执行安全启动使 Mac 启动进入该状态。要执行“安全启动”，请在 Mac 启动后立即按住 Shift 键。继续按住 Shift 键直至一个灰色的 Apple 标志出现在屏幕上。启动至安全模式会执行以下几项操作：强制对启动宗卷进行目录检查。在此次检查过程中您可能会在屏幕上看到一个进度条，且电脑完成启动所需时间可能比平常更久。只载入必需的内核扩展（“/系统/资源库/Extensions”中的某些项目）。Mac OS X v10.5.6 或更高版本：安全启动会删除 (/var/db/dyld/) 处的动态载入程序共享缓存。缓存出现问题可能会导致启动时出现蓝屏，尤其是在进行软件更新后。正常重新启动即可重新创建此缓存。停用除“/系统/资源库/Fonts”（Mac OS X v10.4 或更高版本）中的字体之外的所有字体。将通常存储在“/资源库/Caches/com.apple.ATS/(uid)/”中的所有字体缓存移至废纸篓，其中 (uid) 是用户 ID 号，如 501（Mac OS X v10.4 或更高版本）。停用所有启动项和登录项（Mac OS X v10.4 或更高版本）。在Mac OS X v10.3.9 或更低版本中，安全模式仅会运行 Apple 安装的启动项（此类项目可能安装在“/资源库/StartupItems”或“/系统/资源库/StartupItems”中；这些与用户选定帐户登录项不同）。综合而言，这些变化有助于解决启动宗卷中可能存在的软件或目录问题。在安全模式下某些功能无法使用安全模式有助于进行故障诊断。不过，某些 Mac OS X 功能在安全模式下无法使用。例如，无法使用 DVD 播放器、无法在 iMovie 中拍摄视频、无法使用音频输入或输出设备、无法使用内置或外置 USB 调制解调器。某些设备（如无线联网）的行为可能会因电脑和 Mac OS X 的版本而有所不同。在Mac OS X v10.5 或更高版本中，安全模式还会停用 Quartz Extreme（硬件图形加速功能）。基于 Quartz Extreme 的应用软件将不会打开，而且即使在“桌面与屏幕保护程序”偏好设置中启用“半透明菜单栏”，Mac OS X 菜单栏仍会显示为实心。Mac OS X v10.6 或更高版本中的安全模式还会停用“文件共享”访问功能。其他信息另请参阅：Mac OS X：启动期间出现灰屏Mac OS X：以安全模式启动
```

---

[🌐 原始链接](http://zhidao.baidu.com/question/1510045416401069820.html)

[📎 在印象笔记中打开](evernote:///view/207087/s1/5a2526f7-7dae-414c-9db7-6bc47416ff34/5a2526f7-7dae-414c-9db7-6bc47416ff34/)