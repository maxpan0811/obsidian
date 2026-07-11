# Claude Code进阶指南

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzkyNzY5MTM5OA==&mid=224748...](https://mp.weixin.qq.com/s?__biz=MzkyNzY5MTM5OA==&mid=2247488463&idx=1&sn=52fb9310f689996e411bc161e7523226&chksm=c2257426f552fd308991a5f7e3e95aea7cfad18851d74cefc291c936459a4ff267a23f993955&from_masonry=1&sessionid=0&subscene=288&scene=132&ascene=0&devicetype=iOS26.5&version=18004a2a&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQjkJkSC+qZPzTF/ybPrzdeRLTAQIE97dBBAEAAAAAAOeKChZ1CdAAAAAOpnltbLcz9gKNyK89dVj0UonEnjWHwteSqONv45ijzw112KCH+MpeQ1pDB5QNhNrNApAFH41rpTVlfIZX0PQ5jeBzIuWyQmB8MmxIC1IYOGfn6KZH5HDbsSBRyXgaNS4oXOMC318PTp9AoFp9WJo+SfiyCfdzReouYHRj/K84aWIoxWNLoFcxtH3C4jvAM0jl2cN0HwjEMi3vK3oph5f8l1GbH0TZ2I2aI/O0OaH6uCHGwlKhQl60bzeQ+zY=&pass_ticket=KC8CXC9iUVg997m0oPGDJvPpibc83Vxee6bGw2rHdQT1vSWA1JOobnN/XWj2EBo+&wx_header=3)

![](.evernote-content/D910E74D-C632-4546-9DEA-C4FFF6B442D5/6992E3C1-3314-4D01-B37D-BA67B7F2A292.png)![](.evernote-content/D910E74D-C632-4546-9DEA-C4FFF6B442D5/89A88A7F-ECC5-42C4-93C7-FCC527969959.png)![](.evernote-content/D910E74D-C632-4546-9DEA-C4FFF6B442D5/3BA334DC-DC6B-4544-9A69-CB66067A1034.png)![](.evernote-content/D910E74D-C632-4546-9DEA-C4FFF6B442D5/4D400D64-85B9-4067-AADB-9FC616FF3BAA.png)![](.evernote-content/D910E74D-C632-4546-9DEA-C4FFF6B442D5/B2C2641E-541C-4F41-96C7-36B808E63358.png)![](.evernote-content/D910E74D-C632-4546-9DEA-C4FFF6B442D5/BB997F7C-52BE-4B79-912D-6509441D123C.png)![](.evernote-content/D910E74D-C632-4546-9DEA-C4FFF6B442D5/F8308686-07E5-4B90-AEA6-A9E30C1F8F86.png)![](.evernote-content/D910E74D-C632-4546-9DEA-C4FFF6B442D5/44AF3B3E-0BF1-4D9F-9E01-EC72CB8E5708.png)![](.evernote-content/D910E74D-C632-4546-9DEA-C4FFF6B442D5/FA3D7ED1-96F2-4F31-9BB5-69C9BB02F3AB.png)

很多人用 Claude Code 半年，仍停留在“会让 AI 写代码”的浅层阶段。真正拉开差距的，不是工具本身，而是是否建立了一套稳定、可控、可扩展的工作流。

文章提炼出 32 个 Claude Code 进阶用法：先用 /init 建立项目记忆，用 /context 管理 token，用计划模式减少返工；再通过子 Agent、Skills、Hooks、权限控制、模型选择，把任务拆分、规则约束和成本控制纳入系统；最后借助 git worktrees、/loop、Routines、Context7 MCP、动态工作流等能力，把 Claude Code 从单人工具升级为并行生产系统。

初学者长期停滞，往往不是不会用，而是没有 CLAUDE.md、不看上下文、不做计划、权限全开、模型乱用、忽视插件市场。真正的高手，不只是调用 AI，而是调度 AI 系统。

Close

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzkyNzY5MTM5OA==&mid=2247488463&idx=1&sn=52fb9310f689996e411bc161e7523226&chksm=c2257426f552fd308991a5f7e3e95aea7cfad18851d74cefc291c936459a4ff267a23f993955&from_masonry=1&sessionid=0&subscene=288&scene=132&ascene=0&devicetype=iOS26.5&version=18004a2a&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQjkJkSC+qZPzTF/ybPrzdeRLTAQIE97dBBAEAAAAAAOeKChZ1CdAAAAAOpnltbLcz9gKNyK89dVj0UonEnjWHwteSqONv45ijzw112KCH+MpeQ1pDB5QNhNrNApAFH41rpTVlfIZX0PQ5jeBzIuWyQmB8MmxIC1IYOGfn6KZH5HDbsSBRyXgaNS4oXOMC318PTp9AoFp9WJo+SfiyCfdzReouYHRj/K84aWIoxWNLoFcxtH3C4jvAM0jl2cN0HwjEMi3vK3oph5f8l1GbH0TZ2I2aI/O0OaH6uCHGwlKhQl60bzeQ+zY=&pass_ticket=KC8CXC9iUVg997m0oPGDJvPpibc83Vxee6bGw2rHdQT1vSWA1JOobnN/XWj2EBo+&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/db98238c-d97c-4fd8-ab71-d49f7d153311/db98238c-d97c-4fd8-ab71-d49f7d153311/)