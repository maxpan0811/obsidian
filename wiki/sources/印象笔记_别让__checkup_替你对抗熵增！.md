---
title: "别让 _checkup 替你对抗熵增！"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/别让 _checkup 替你对抗熵增！.md
tags: [印象笔记]
---

# 别让 _checkup 替你对抗熵增！

# 别让 /checkup 替你对抗熵增！ --- 原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzIzMzQyMzUzNw==&mid=224751...](

---

# 别让 /checkup 替你对抗熵增！

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzIzMzQyMzUzNw==&mid=224751...](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247518753&idx=1&sn=7060ac57e2d071b63d66d81289c2271e&chksm=e9cd847ecd8ffc0b9f558bb4ece5e4c5de0228f11c9c9f7dfc37e89dff362d85534eff9144cc&scene=90&xtrack=1&req_id=1783588483046277&sessionid=1783588607&subscene=93&clicktime=1783588617&enterid=1783588617&flutter_pos=0&biz_enter_id=4&ranksessionid=1783588483&jumppath=1001_1783588607003,1104_1783588608616,MMFlutterViewController_1783588609451,1104_1783588613320&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b37&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQXj4s5v+rWpooAeYNoCqfjBLTAQIE97dBBAEAAAAAAL5XJAj/61kAAAAOpnltbLcz9gKNyK89dVj0Lc8hxbfJZURwkwZAKxa/Y+RCgLU45fpyCiJFQD/xQQbafRr64O1pnNjQZhdgAmgWQ8OdW6gMdrs63jNaQPmwKe+XrE/e8hXw569i+zbOyL2r9rdqxOI0kOuADeUuM/T/cGw2yTkQ7ecOZT1g/22rAcauLUuIWv67/4L47PpN3UU90VbNqCh1+oy9jT/YIUlGnPAtXa/Chb/PpmYd9xKBVOAPnmF/xI+QbUfJ620=&pass_ticket=H1ufKQqmQJd/vbYizo9l3Qp+CAYQf8e16Yd/0vvTNHownZ/Mlm9GMVdP1rPM433y&wx_header=3)

Original字节笔记本字节笔记本

Claude Code 最近上线了 /checkup 命令，可以一键清理。

就跟电脑安装360 卫士一样，点一下就能来清理掉没用的 skills、MCP、plugins。

给臃肿的 CLAUDE.md 去重拆分，关掉拖慢速度的 hooks，预批准总被拒绝的只读命令。

听起来很是贴心，但我想说的是，一个 Agent 环境如果需要靠这个命令来救场，说明你从一开始就用错了。  
  
原因很简单，/checkup 现在修的每一项，对应的都是一个坏习惯。  
  
skills、MCP 装了却用不上，说明当初引入时没想清楚要不要全局常驻，还是该按项目隔离。

MCP 反正我是一个都没有装，Skills 全部由我写的工具做统一管理，甚至其中大部分大部分都已经文件化、目录化了，详细可以看这里：[看山是山，看山不是山，看山还是山，我用 Skills 的三个阶段](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247518394&idx=1&sn=a096ec4304557cdb2674aecc5261f5c8&scene=21#wechat_redirect)

CLAUDE.md 膨胀到要拆分，说明你把它当成了垃圾抽屉。[你的CLAUDE.md 写错了！别怪 Claude Code降智不好用](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247509447&idx=1&sn=8e33735d2bb9686024d96091ef132ac1&scene=21#wechat_redirect)。

我现在基本很少去动这个文件，如果去修改的话，那也是在为我的知识库加上索引链接。

Hooks 用的极其少，除了使用 rtk，不加入任何的 Hooks [节省至少60%的Token消耗！Claude Code 会话智能过滤器](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247514014&idx=1&sn=3d1433480e0f7372a03b016231ca872f&scene=21#wechat_redirect)。

至于说权限总被拒绝，说明 settings.json 里从来没提前声明过规则，权限的修改方式非常的简单，完全没有必要每次都手动确认：[Claude Code 常用操作和配置备忘录](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247505789&idx=1&sn=c1074b799b61abf6d1cebac4da1b0879&scene=21#wechat_redirect)

总结下来，我用Claude Code 这类 CLI 工具最基础的原则就是：如无必要，勿增实体。

/checkup 对于像我这种使用习惯的人来说，基本没啥用，它更像是给熵只增不减的系统兜底的工具。

这玩意也能用，但如果你每次用都能清出一堆东西，说明用法从头就错了。

CLI Agent 真正理想状态是模块化、按需加载、条件触发，系统本身不增熵，自然也就不需要定期清理。

[花费近5亿Token收集的国内外设计DESIGN.md](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247518718&idx=1&sn=5105750eadddaedc997b12853853e038&payreadticket=HKrn21RKmXnuFcFpuaqrT7DxsoCVkwNXhr3OKs9K4gpqDCqHpMu94ckcgP_I0cjymhL6wbU&scene=21#wechat_redirect)

[用 Fable 5 炼丹！](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247518705&idx=1&sn=e600de0544aaa41e2f406d46c2ed1e47&scene=21#wechat_redirect)

[以后 AI 每读一次你的网站，都得给钱！](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247518692&idx=1&sn=f7fbb884f7b9e7a8bb1d98bd1dbfd21a&scene=21#wechat_redirect)

[Fable 5 最后一天！写了一个微信文件传输助手](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247518681&idx=1&sn=31e4b34e1ed5cfeda32396e46bb0fd98&scene=21#wechat_redirect)

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247518753&idx=1&sn=7060ac57e2d071b63d66d81289c2271e&chksm=e9cd847ecd8ffc0b9f558bb4ece5e4c5de0228f11c9c9f7dfc37e89dff362d85534eff9144cc&scene=90&xtrack=1&req_id=1783588483046277&sessionid=1783588607&subscene=93&clicktime=1783588617&enterid=1783588617&flutter_pos=0&biz_enter_id=4&ranksessionid=1783588483&jumppath=1001_1783588607003,1104_1783588608616,MMFlutterViewController_1783588609451,1104_1783588613320&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b37&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQXj4s5v+rWpooAeYNoCqfjBLTAQIE97dBBAEAAAAAAL5XJAj/61kAAAAOpnltbLcz9gKNyK89dVj0Lc8hxbfJZURwkwZAKxa/Y+RCgLU45fpyCiJFQD/xQQbafRr64O1pnNjQZhdgAmgWQ8OdW6gMdrs63jNaQPmwKe+XrE/e8hXw569i+zbOyL2r9rdqxOI0kOuADeUuM/T/cGw2yTkQ7ecOZT1g/22rAcauLUuIWv67/4L47PpN3UU90VbNqCh1+oy9jT/YIUlGnPAtXa/Chb/PpmYd9xKBVOAPnmF/xI+QbUfJ620=&pass_ticket=H1ufKQqmQJd/vbYizo9l3Qp+CAYQf8e16Yd/0vvTNHownZ/Mlm9GMVdP1rPM433y&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/e7640067-a5cb-47ad-8d91-6be06547383e/e7640067-a5cb-47ad-8d91-6be06547383e/)