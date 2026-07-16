---
title: Claude Code三大利器命令用法
type: source
created: 2026-06-17
updated: 2026-06-17
source: 印象笔记管理工具
source_path: 印象笔记管理工具/Claude Code三大利器命令用法.md
tags: [AI技术]
updated: 2026-06-27
---

---
title: "Claude Code三大利器命令用法"
source: evernote
type: note
export_date: 2026-06-26
guid: 5496e8a7-993d-4ac9-8c6e-2ba689e882dc
---

# Claude Code三大利器命令用法

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzkyNzY5MTM5OA==&mid=224748...](https://mp.weixin.qq.com/s?__biz=MzkyNzY5MTM5OA==&mid=2247489330&idx=1&sn=ac5caddc4eff1abc3355447adbc31ab1&chksm=c3abea55589589e9ee11933fd5e7b839148b4be6e158a621907a049ca7074b9a297d207c44fa&scene=90&xtrack=1&req_id=1781613613131826&sessionid=1781613664&subscene=93&clicktime=1781620323&enterid=1781620323&flutter_pos=1&biz_enter_id=4&ranksessionid=1781613613&jumppath=20020_1781615729839,1104_1781619301865,20020_1781619308190,1104_1781620321290&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004a30&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQDd5jyrBG7Q7TamUYFvN8EBLTAQIE97dBBAEAAAAAANGaJS2MyEIAAAAOpnltbLcz9gKNyK89dVj0jJHLYFNDz3ee7XGdAivcQ4nHl27UmkW72rKGdPtCzsgDmCm/pVmCrWkY9w44EdiOVP/QKCAZZ77aLjm4pMJviuOL/UekIRvTEhFsfYPWUrT+o+/SVEcLjzC9RyFgjCdenGIXAqF/4f3owjLq40hjzd7aXGhd6sIHmN9RIdN39CgTVxShhiGY7rcCr/0sgeaAbKpevi7mpJ/TyuNECM6cCHsAzDweHaURnLEv/nA=&pass_ticket=uzaGPQYK39i1Pr2bALmUzU2UNK9PG5mGhosjRN+fseP4Ft0mdcW+VN1GG95osiDA&wx_header=3)

![](attachments/60acf9274e855cbc.png)![](attachments/4415a4d970de2200.png)![](attachments/3d1adb183779ee92.png)![](attachments/215ef4dfaf8b1aae.png)![](attachments/2f550ce69a61ca06.png)![](attachments/ac3c01af5a8f0549.png)![](attachments/3571ffc7cdeb92c9.png)![](attachments/91eff182f15d14db.png)

Claude Code 的 /goal、/loop、/workflows 常被误解为“让 Claude 多干一会儿”，其实三者解决的是完全不同的问题。/goal 管终点：给出可验证的完成条件，Claude 会多轮执行，达标即停，适合测试全绿、编译通过、issue 清空等任务。/loop 管节奏：按固定时间间隔重复执行同一件事，适合轮询 CI、部署状态、PR 列表或远程任务队列。/workflows 管规模：它不是启动任务，而是查看已启动 Workflow 的并行进度，适合大任务拆分、多智能体协作、批量迁移和交叉验证。判断方法很简单：终点明确且可验证，用 /goal；需要定时值守，用 /loop；任务太大、需要分头并行，先发起 Workflow，再用 /workflows 看进度。选错命令，浪费的不是功能，而是停止逻辑、时间节奏和协作结构。

Close


---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzkyNzY5MTM5OA==&mid=2247489330&idx=1&sn=ac5caddc4eff1abc3355447adbc31ab1&chksm=c3abea55589589e9ee11933fd5e7b839148b4be6e158a621907a049ca7074b9a297d207c44fa&scene=90&xtrack=1&req_id=1781613613131826&sessionid=1781613664&subscene=93&clicktime=1781620323&enterid=1781620323&flutter_pos=1&biz_enter_id=4&ranksessionid=1781613613&jumppath=20020_1781615729839,1104_1781619301865,20020_1781619308190,1104_1781620321290&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004a30&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQDd5jyrBG7Q7TamUYFvN8EBLTAQIE97dBBAEAAAAAANGaJS2MyEIAAAAOpnltbLcz9gKNyK89dVj0jJHLYFNDz3ee7XGdAivcQ4nHl27UmkW72rKGdPtCzsgDmCm/pVmCrWkY9w44EdiOVP/QKCAZZ77aLjm4pMJviuOL/UekIRvTEhFsfYPWUrT+o+/SVEcLjzC9RyFgjCdenGIXAqF/4f3owjLq40hjzd7aXGhd6sIHmN9RIdN39CgTVxShhiGY7rcCr/0sgeaAbKpevi7mpJ/TyuNECM6cCHsAzDweHaURnLEv/nA=&pass_ticket=uzaGPQYK39i1Pr2bALmUzU2UNK9PG5mGhosjRN+fseP4Ft0mdcW+VN1GG95osiDA&wx_header=3)
[📎 在印象笔记中打开](evernote:///view/207087/s1/5496e8a7-993d-4ac9-8c6e-2ba689e882dc/5496e8a7-993d-4ac9-8c6e-2ba689e882dc/)
