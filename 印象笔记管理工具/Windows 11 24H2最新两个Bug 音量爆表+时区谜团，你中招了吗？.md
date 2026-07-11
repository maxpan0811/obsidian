# Windows 11 24H2最新两个Bug 音量爆表+时区谜团，你中招了吗？

---

速读摘要

24H2版本中存在的两个重要Bug，分别涉及音频设置和时区修改功能。这一问题主要影响外接USB声卡或数字音频转换器(DAC)的用户。微软确认这是"设置"中的一个Bug，而非权限设置或系统策略的问题。这意味着即使IT管理员未对用户权限或策略做任何修改，问题依然会存在。主要受影响的是使用非管理员账户的企业员工。

原文约777 字|图片8张|建议阅读2分钟|[评价反馈](https://static.app.yinxiang.com/embedded-web/clipper/#/Evaluating?d=2024-11-24&nu=38e2f299-3c1f-416d-bd5d-c40f4c88453f&fr=myyxbj&ud=328ef&v=2&sig=1819E15DC72380AF8623E493A507BC1F)

原文链接: [http://mp.weixin.qq.com/s?\_\_biz=MzAwOTYyODk3Mw==&mid=2247488...](http://mp.weixin.qq.com/s?__biz=MzAwOTYyODk3Mw==&mid=2247488015&idx=1&sn=4d19f01c85452c2eb33075d732e3844e&chksm=9a43f20cce8a2e7f937f1e81ecaae732bd26c0cc7affbf5e8bdef0acf245a438ee4c76e42b4f&mpshare=1&scene=1&srcid=1124W5zOb5v0CGCsQX0pJU1J&sharer_shareinfo=b8895cf4bf6ceb930cf8d75989d25415&sharer_shareinfo_first=b8895cf4bf6ceb930cf8d75989d25415#rd)

原创 IT玩客 IT玩客

![](.evernote-content/30D8D1F1-706E-4C12-80C4-E6CF8AC8304D/B798AA7F-317C-40A0-9BB5-670676F9FF94.gif)

![](.evernote-content/30D8D1F1-706E-4C12-80C4-E6CF8AC8304D/7171CE8D-0EB5-483E-9F44-5B2C4E584DFA.png)

近日，微软确认了Windows 11 24H2版本中存在的两个重要Bug，分别涉及音频设置和时区修改功能。这些问题虽然不会普遍影响所有用户，但对于特定场景下的使用者来说，可能会带来一定困扰。以下是详细情况：

![](.evernote-content/30D8D1F1-706E-4C12-80C4-E6CF8AC8304D/19B90589-1035-4219-9C7B-085A0E8FD034.jpg)

### **音量自动升至100%的问题**

这一问题主要影响外接USB声卡或数字音频转换器（DAC）的用户。具体表现为在没有任何操作的情况下，音量会突然增加到100%。微软初步确认问题源于 **Microsoft AudioEndpointBuilder 服务** 的一个Bug，并表示正在研究解决方案。

#### **受影响的用户场景**

如果您的设备符合以下一个或多个条件，可能会遇到此问题：

1. 使用 **Creative Sound BlasterX G6 USB 数字音频转换器（DAC）**。
2. 系统运行 **Windows 11 24H2**。
3. 手动将系统进入休眠状态后，再手动唤醒。
4. 插入USB声卡后立即拔出。
5. 调整USB声卡音量后立即拔出。

#### **目前的现状**

* 问题出现时，音量会直接拉高至100%，没有任何错误提示或弹窗警告。
* 微软尚未提供临时解决方案，但承诺在未来的更新中解决此问题。

---

### **非管理员用户无法修改时区的问题**

另一个Bug则影响到非管理员权限的用户。在Windows 11 24H2版本的“设置”界面中，这些用户无法找到更改时区的选项，导致时区无法直接调整。

![](.evernote-content/30D8D1F1-706E-4C12-80C4-E6CF8AC8304D/C51670E0-CBF0-4C20-BF1C-820DCE284D6F.jpg)

#### **微软的说明**

微软确认这是“设置”中的一个Bug，而非权限设置或系统策略的问题。这意味着即使IT管理员未对用户权限或策略做任何修改，问题依然会存在。

#### **临时解决方法**

尽管“设置”界面无法修改时区，但用户可以通过传统的 **控制面板** 来实现：

![](.evernote-content/30D8D1F1-706E-4C12-80C4-E6CF8AC8304D/363B2AD1-7D38-421A-AC2F-AC4ECEDFEF24.png)

讽刺的是微软一直想要将 Windows 传统的控制面板彻底删除，不过事实证明真正到了某些关键时刻还是得靠控制面板解决问题。

**也可通过以下命令来更改时区**

1. 按下快捷键 **Win+R**，打开运行窗口。
2. 输入 **timedate.cpl**，按回车。
3. 在弹出的控制台窗口中，调整时间和时区设置。

#### **受影响人群**

* 家庭用户大多以管理员权限运行系统，因此影响较小。
* 主要受影响的是使用非管理员账户的企业员工。

#### **后续计划**

微软表示将在后续更新中修复此Bug，恢复在“设置”中修改时区的功能。

---

### **总结与建议**

### 针对上述问题，建议用户在遇到相关Bug时采取临时解决方法，同时保持系统更新，等待微软推出官方修复方案。如果您是企业用户，IT部门可提前告知员工这些Bug的应对措施，避免操作中断带来的不便。

![](.evernote-content/30D8D1F1-706E-4C12-80C4-E6CF8AC8304D/874211FD-E57F-480E-9333-9E97E57EF310.gif)

---

[🌐 原始链接](http://mp.weixin.qq.com/s?__biz=MzAwOTYyODk3Mw==&mid=2247488015&idx=1&sn=4d19f01c85452c2eb33075d732e3844e&chksm=9a43f20cce8a2e7f937f1e81ecaae732bd26c0cc7affbf5e8bdef0acf245a438ee4c76e42b4f&mpshare=1&scene=1&srcid=1124W5zOb5v0CGCsQX0pJU1J&sharer_shareinfo=b8895cf4bf6ceb930cf8d75989d25415&sharer_shareinfo_first=b8895cf4bf6ceb930cf8d75989d25415#rd)

[📎 在印象笔记中打开](evernote:///view/207087/s1/b85ac27c-624a-4921-86e1-2d906608539c/b85ac27c-624a-4921-86e1-2d906608539c/)