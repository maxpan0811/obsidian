---
title: 我把一年的乱账丢给 Claude 自动分析：清洗、算账、出报表，一条龙（附代码）
type: source
created: 2026-06-14
updated: 2026-06-14
source_path: 印象笔记管理工具/我把一年的乱账丢给 Claude 自动分析：清洗、算账、出报表，一条龙（附代码）.html
tags: [印象笔记, AI/编程]
updated: 2026-06-27
updated: 2026-06-27
updated: 2026-06-27
---

---
title: "我把一年的乱账丢给 Claude 自动分析：清洗、算账、出报表，一条龙（附代码）"
source: evernote
type: note
export_date: 2026-06-27
guid: 92a35c6f-c566-4842-bdef-086e0d6e151d
---

# 我把一年的乱账丢给 Claude 自动分析：清洗、算账、出报表，一条龙（附代码）

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzYzMjY1OTI0MA==&mid=224748...](https://mp.weixin.qq.com/s?__biz=MzYzMjY1OTI0MA==&mid=2247485997&idx=1&sn=88fa5dba9b0ae57fd8588ca5ce883e39&chksm=f108116c54bcb054823490f3e2405b41f4c04f00e9e183eba13f9528d8fa29c5c3c457087a7d&scene=90&xtrack=1&req_id=1780976600635237&sessionid=1780976559&subscene=93&clicktime=1780978092&enterid=1780978092&flutter_pos=7&biz_enter_id=4&ranksessionid=1780976600&jumppath=20020_1780978007019,1104_1780978013823,20020_1780978039363,1104_1780978081715&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004a2a&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQIYfHDWKroPDTDug8kLASKhLTAQIE97dBBAEAAAAAACmMGl7MzZIAAAAOpnltbLcz9gKNyK89dVj0KZmuBMEH/T5/8y3hQNXk3YVvui4mdPs+O+ANFfgvxiChsr24ikpXVdtDt7Qkx7hUjSyxn8vGfWLJUVNs3nHbSLoFTZA3cLNtM/oWuxiOFaHBFL0LNZxgirpAUro0ReCoBgm7963TLX++pijKCeuaif99vcHmJhKXH65p8k7FmIIKDEsICz28Rpm/XVtloMQxaNXed/06/7lTR1z8G1e9h5EL14iyfK9R4NHpfUc=&pass_ticket=UToqNFOJ1QLCLsi4tN4hvx5wPPD17T9vhkIkbQ2e2j65vHVGHNI6Ag0S6VavZh+z&wx_header=3)

Original莲花明 AI落地手记

![](attachments/5c5a48caa718c5d7.png)

先问你个事，看看戳不戳中：你是不是也干过——把一张Excel或者账单导出来，直接甩给AI，敲一句「**帮我分析一下这些数据**」，然后就等它给你惊喜？

我干过，而且被坑得不轻。它确实给了我一大段分析，**数字一个比一个具体**，「本月支出环比上涨23.6%」「餐饮占比41.2%」……看着特别专业。直到我自己用计算器核了一遍——**全是编的**。占比不对，涨幅不对，连总数都对不上。

这是用AI处理数据，**最值钱也最反直觉的一条认知**：**AI不是计算器。**你让它算一大堆数，它不会真去一笔笔加，而是凭语感「生成」一串看着合理的数字。越像，越坑人。

那AI在数据这块就没用了？恰恰相反，**用对了它能帮你省掉最烦的两头活**。关键是别让它干它不擅长的（算数），让它干它最在行的（看懂一张乱表、把结果说成人话）。

我后来理顺了一套姿势，自己叫它**「三明治」**——这篇就把它拆给你，**整段代码复制改一改就能跑**。例子我用最接地气的：**一年的个人记账流水**。

丑话说前头：**这篇带代码**。但你就算不写代码也别划走——**「AI不会算数、别让它算」这条认知，不写一行代码也能立刻改变你用AI的方式**；想真跑起来，文末那张卡转给身边会写两行Python的人，半小时给你搭好。

正确姿势是个「三明治」

AI管两头，算数那层夹在中间交给代码

上层 · 看懂 + 清洗Claude

读列名和几行样本，认出每列是啥、该怎么洗

中层 · 算账pandas

真正的加减乘除、分组汇总，交给代码，一分不差

下层 · 翻成人话Claude

把算好的干巴巴数字，写成你看得懂的结论

**💡 多数人不知道：**记住这个分工就够了：**凡是要"算"的，交给pandas；凡是要"懂"和"说"的，交给Claude**。AI把你那张鬼画符的表看明白、定好怎么洗，代码老老实实算账，最后AI再把干巴巴的数字翻成人话。三层各干各的，谁也别替谁。

---

## 先看看，要对付的是张什么样的乱表

随便从哪个App导出的账单，都长这副德行——**同一张表里，日期四种写法，金额三种格式，分类干脆没有**：

日 期

说明

金额

2025/3/1

美团 午饭

￥38

3月2日

打车 滴滴

21元

2025-03-02

超市买菜

88.5

3/3

瑞幸咖啡

35.0

日期四种写法、金额三种格式、分类全靠你脑补——这就是真实的导出账单

这种表，你手动整理一年的，能整理到怀疑人生。但它恰恰是**Claude最擅长啃的硬骨头**——人一眼能看懂「3月2日」和「2025-03-02」是一回事，AI也能，而且它能一次性把规则给你定出来。

---

## 上层：让Claude看懂这张表，定好清洗方案

第一层的活，是把「这表每列是啥、该怎么洗」搞清楚。诀窍有个**特别反直觉的点**：**别把整张表喂给它**。

**💡 多数人不知道：**几千行的账单别一股脑塞给AI——又贵、又容易超出它的上下文，关键是**它看完照样不会帮你算**。它要的只是**列名 + 头几行样本**，看懂"长什么样"就够了。结构它一眼就懂，剩下的交给代码批量干。

动手前先装包：**pip install anthropic pandas**，钥匙设成环境变量**ANTHROPIC\_API\_KEY**。然后把样本喂给它，让它返回一份**结构化的清洗方案**：

plan.py · 让Claude定清洗方案Python

`import json, re, pandas as pd`

`from anthropic import Anthropic`

`client = Anthropic()`

`df = pd.read_csv("账单.csv")`

`# 只取列名 + 前 5 行样本喂给它，够它看懂结构了`

`sample = df.head(5).to_string(index=False)`

`PROMPT = f"""这是一份个人记账流水的前几行：`

`{sample}`

`请帮我看懂它，只输出 JSON，不要多余的话，格式：`

`{{"日期列":"哪一列是日期", "金额列":"哪一列是金额",`

`"说明列":"哪一列是消费说明",`

`"分类规则":{{"吃饭":["美团","超市","买菜"], "出行":["滴滴","打车"],`

`"咖啡":["瑞幸","咖啡"], "购物":["淘宝","京东"]}}}}`

`分类规则里的关键词，请根据样本里的说明帮我总结。"""`

`def make_plan():`

`msg = client.messages.create(model="claude-sonnet-4-6", max_tokens=600,`

`messages=[{"role":"user","content":PROMPT}])`

`return json.loads(re.search(r"\{.*\}", msg.content[0].text, re.S).group())`

`plan = make_plan()`

`print("Claude 定的方案：", plan)`

它会返回类似这样一份方案——**哪列是日期、哪列是金额、每个分类对应哪些关键词，全给你列好**：

`{"日期列": "日期", "金额列": "金额", "说明列": "说明",`

`"分类规则": {"吃饭": ["美团", "超市", "买菜"],`

`"出行": ["滴滴", "打车"],`

`"咖啡": ["瑞幸", "咖啡"]}}`

注意：到这一步，它**一个数都没算**，只是把这张表「读懂」了。这正是我们要的——它干的是认字的活，不是算账的活。

---

## 中层：算账交给pandas，一分不差

拿到方案，真正的清洗和计算**全交给代码**。日期统一、金额转成数字、按关键词归类、再分组求和——这些是pandas的拿手好戏，**算多少是多少，绝不会编**：

crunch.py · 清洗 + 算账Python

`import re, pandas as pd`

`YEAR = 2025    # 这份账单是哪一年的；没年份的日期按它补，跨年就分两段`

`def clean_date(x):`

`# 中文日期「3月2日」、缺年份「3/3」都是 pandas 直接认不出的，先各个击破`

`s = str(x).strip().replace("年", "/").replace("月", "/").replace("日", "")`

`parts = re.split(r"[/\-]", s)`

`if len(parts) == 2:                 # 只有"月/日"没年份 → 补上`

`s = f"{YEAR}/{parts[0]}/{parts[1]}"`

`return pd.to_datetime(s, errors="coerce")`

`def clean_amount(x):`

`s = str(x)`

`neg = s.lstrip().startswith("-") or "退" in s   # 退款记成负数，别当支出`

`num = re.sub(r"[^0-9.]", "", s)     # 抠出数字："￥38""21元""88.5"`

`if not num: return None`

`try:`

`v = float(num)`

`except ValueError:                  # "3.5.0"这种多点脏数据，安静丢掉别让它崩脚本`

`return None`

`return -v if neg else v`

`def crunch(df, plan):`

`d, a, s = plan["日期列"], plan["金额列"], plan["说明列"]`

`df[d] = df[d].apply(clean_date)`

`df[a] = df[a].apply(clean_amount)`

`# 关键一步：先体检，看清洗丢了多少行（这步别省，这才叫不盲信）`

`print("日期没认出的行：", df[d].isna().sum())`

`print("金额没认出的行：", df[a].isna().sum())`

`# 按方案里的关键词归类`

`df["分类"] = df[s].apply(lambda t: next(`

`(c for c, ks in plan["分类规则"].items() if any(k in str(t) for k in ks)),`

`"其它"))`

`df = df.dropna(subset=[d, a])        # 认不出的行明确丢掉，不让它悄悄混进汇总`

`# 按月、按分类汇总——全文唯一"算账"的地方，交给代码`

`df["月份"] = df[d].dt.to_period("M").astype(str)`

`return df.groupby(["月份", "分类"])[a].sum().round(2).reset_index()`

**💡 多数人不知道：**两个细节是这段的灵魂：① **加减乘除一行都没让AI碰**，pandas算出来的￥2480就是￥2480，不会因为"语感"变成￥2486；② **清洗完先打印"丢了多少行"**——日期认不出、金额抠不出的，明明白白显示出来再dropna丢掉，**而不是让脏数据悄悄混进汇总把账算偏**。"不盲信AI"这条，对自己写的代码同样适用。

---

## 下层：让Claude把数字，翻成人话

算出来的汇总表是对的，但干巴巴一堆数字，你扫一眼也记不住。这时候**再请Claude出场**——把**算好的小结果**（不是原始大表）喂给它，让它写两句人话洞察：

insight.py · 让Claude写洞察Python

`def insight(summary):`

`table = summary.to_string(index=False)   # 已经算好的小表，就几行`

`msg = client.messages.create(model="claude-sonnet-4-6", max_tokens=400,`

`messages=[{"role":"user","content":`

`f"这是我按月、按分类汇总好的消费数据：\n{table}\n"`

`"用 2-3 句大白话告诉我：钱主要花哪了？有没有哪笔藏起来的大开销？"`

`"只说结论，别复述数字。"}])`

`return msg.content[0].text`

`print(insight(summary))`

它会给你这种一看就懂的话：

`这个月吃饭是绝对大头，快占了一半；咖啡看着每杯不贵，`

`攒一个月也是笔不小的开销，是容易被忽略的"隐形支出"。`

**💡 多数人不知道：**为什么这一步喂的是**汇总后的小表**，不是原始账单？因为它现在干的是**"解读"不是"计算"**——数字已经被pandas算准了，AI只负责把对的数字说成人话。**它说错话顶多不好听，说错数才要命**，而我们已经把"算数"这步彻底拿走了。

---

## 收尾：拼成一张报表，一条龙跑完

三层接起来，就是一个完整脚本：**python report.py账单.csv**，它自己看懂表 → 清洗算账 → 写洞察 → 吐出一张带条形图的HTML报表：

3月消费报表（示意）

数字是pandas算的，下面那句话是Claude写的

吃饭￥2480

出行￥1320

购物￥960

咖啡￥610

💬 这个月吃饭花了 ￥2480，占了快一半；咖啡单看不多，但￥610够你下馆子十几次了，是笔藏起来的大开销。

右边的金额一分不差（代码算的），下面那句人话是AI写的——两边各干各擅长的

报表这层不用AI，几行pandas + 一点HTML就够。把前面三段和它拼起来，完整长这样：

report.py · 完整可跑主程序

`# pip install anthropic pandas`

`import sys, json, re, pandas as pd`

`from anthropic import Anthropic`

`client = Anthropic()            # 读环境变量 ANTHROPIC_API_KEY`

`df = pd.read_csv(sys.argv[1])`

`# —— 上层：Claude 定方案 ——`

`sample = df.head(5).to_string(index=False)`

`PROMPT = (f"这是记账流水前几行：\n{sample}\n只输出 JSON："`

`'{{"日期列":"","金额列":"","说明列":"",'`

`'"分类规则":{{"吃饭":["美团","超市"],"出行":["滴滴","打车"],'`

`'"咖啡":["瑞幸","咖啡"]}}}}。分类关键词据样本总结。")`

`msg = client.messages.create(model="claude-sonnet-4-6", max_tokens=600,`

`messages=[{"role":"user","content":PROMPT}])`

`plan = json.loads(re.search(r"\{.*\}", msg.content[0].text, re.S).group())`

`# —— 中层：pandas 清洗 + 算账 ——`

`YEAR = 2025`

`d, a, s = plan["日期列"], plan["金额列"], plan["说明列"]`

`def clean_date(x):`

`t = str(x).strip().replace("年","/").replace("月","/").replace("日","")`

`ps = re.split(r"[/\-]", t)`

`if len(ps) == 2: t = f"{YEAR}/{ps[0]}/{ps[1]}"   # 补年份`

`return pd.to_datetime(t, errors="coerce")`

`def clean_amount(x):`

`neg = str(x).lstrip().startswith("-") or "退" in str(x)`

`num = re.sub(r"[^0-9.]", "", str(x))`

`if not num: return None`

`try: v = float(num)`

`except ValueError: return None      # 多小数点等脏值兜底,别崩`

`return -v if neg else v`

`df[d] = df[d].apply(clean_date)`

`df[a] = df[a].apply(clean_amount)`

`print("丢掉的行 —— 日期:", df[d].isna().sum(), " 金额:", df[a].isna().sum())`

`df["分类"] = df[s].apply(lambda t: next(`

`(c for c, ks in plan["分类规则"].items() if any(k in str(t) for k in ks)),`

`"其它"))`

`df = df.dropna(subset=[d, a])`

`summary = df.groupby("分类")[a].sum().round(2).sort_values(ascending=False)`

`# —— 下层：Claude 写洞察 ——`

`msg = client.messages.create(model="claude-sonnet-4-6", max_tokens=400,`

`messages=[{"role":"user","content":`

`f"按分类汇总好的消费：\n{summary.to_string()}\n"`

`"2-3 句大白话说钱花哪了、有没有隐形大开销。只说结论。"}])`

`tip = msg.content[0].text`

`# —— 出 HTML 报表 ——`

`bars = ""`

`top = summary.max()`

`for name, amt in summary.items():`

`w = int(amt / top * 100)`

`bars += (f'<div style="margin:8px 0;text-spacing:none;-webkit-text-spacing:none;text-autospace:no-autospace;">{name} ￥{amt}'`

`f'<div style="background:#eee;border-radius:5px;text-spacing:none;-webkit-text-spacing:none;text-autospace:no-autospace;">'`

`f'<div style="width:{w}%;background:#059669;height:14px;'`

`f'border-radius:5px;text-spacing:none;-webkit-text-spacing:none;text-autospace:no-autospace;"></div></div></div>')`

`html = f"<h2>消费报表</h2>{bars}<p>💬 {tip}</p>"`

`open("报表.html", "w").write(html)`

`print("✅ 报表已生成 报表.html")`

`print("洞察：", tip)`

跑完，文件夹里多出一张**报表.html**，双击就能看：**数字是代码算的、一分不差，结论是AI写的、一看就懂**。一份你导出来都不想看第二眼的乱账，**一两分钟**变成一张能用的报表。

---

## 我替你踩过的三个坑

**⚠ 我替你踩过的坑：****永远别问AI"帮我算总数/算占比"。**这是全文最该记住的一条。只要是"算"，就写进pandas；让AI算，它给你的数九成是编的，还编得特别像真的。把这条纹在脑门上，能省你一堆对不上账的冤枉时间。

**⚠ 我替你踩过的坑：****日期是最容易翻车的地方，别指望一行to\_datetime搞定。**账单里的「3月2日」（中文）和「3/3」（没年份）pandas直接认不出——前者变空值，后者更阴险，会被当成**公元1年**混进汇总，把账悄悄算偏。所以上面clean\_date里先把中文转成斜杠、给缺年份的补上年份，**再配errors="coerce" 兜底**。这也是为什么清洗完一定要打印"丢了多少行"——心里有数，才不会被悄悄吞掉的数据坑了。

**⚠ 我替你踩过的坑：****分类规则让AI起草，但你要扫一眼再用。**AI总结的关键词大方向对，但偶尔会漏（比如把"瑞幸"忘了归进咖啡）。它给的是**一份草稿不是定稿**，你瞄一眼补两个词，比从零自己列省十倍力气，又不会全错。

---

## 打包带走：一页纸记住全部

先给**不写代码的朋友**三句白话心法，记住这三句，你用AI看数据就不会再被坑：

① **AI不是计算器**——它给的总数、占比、涨幅，很多是"编"得像真的，别照单全收，重要的数自己核一遍。

② **让AI干"看"和"说"，别让它干"算"**——看懂一张乱表、把结果讲成人话，是它的强项。

③ **它给的永远是草稿不是定稿**——分类、结论你都瞄一眼再用。

下面这张是给**动手党**的代码版小抄：

`【一句话心法】 AI 管"懂"和"说"，pandas 管"算"`

`【三明治三层】`

`上层 Claude  看懂表 + 定清洗/分类方案（只喂列名+几行样本）`

`中层 pandas  清洗 + 分组求和（唯一算账的地方，焊死在代码里）`

`下层 Claude  把算好的小表，翻成两句人话洞察`

`【三条铁律】`

`· 别问 AI 算数 —— 要"算"就写进 pandas`

`· 别喂整张表 —— 列名 + 几行样本就够它懂结构`

`· 解读只喂"算好的小结果" —— 它说错话不要紧，说错数才要命`

`【关键代码】`

`日期清洗  中文「月/日」转斜杠 + 缺年份的补上，再 to_datetime(errors="coerce")`

`金额清洗  抠数字 float()，退款记负数，"3.5.0"等脏值 try/except 兜底成 None`

`丢脏数据  dropna 之前先 print isna 数，丢得明明白白`

`解析 JSON  json.loads(re.search(r"\{.*\}", text, re.S).group())`

说到底，**AI处理数据厉害不厉害，不在于你把多大的表塞给它，而在于你分得清——哪步该它干，哪步该代码干**。分清楚了，它帮你省掉最烦的清洗和最费脑的解读；分不清，它给你一堆编出来的漂亮数字，把你带沟里。

下次再有人甩给你一张乱七八糟的表，你就有底气了。

关注「AI落地手记」

一个人 + 一支AI团队，怎么干完一个团队的活

工具拆解 · 实战踩坑 · 不画饼只讲落地

这套三明治用法是我自己用AI分析数据踩了一堆坑才理顺的，代码也都跑通了才敢往外发。**整理不易，跑通更不易**。对你有用的话，**点个喜欢作者**，或**转发收藏**，下次再被一张乱表难住，直接照着抄。
