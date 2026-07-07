---
title: DeepSeek 官方提示词 2
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/DeepSeek 官方提示词 2.md
tags: [evernote, impression, yinxiang]
---

# DeepSeek 官方提示词

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=Mzg4NTc1NTQ2OQ==&mid=224748...](https://mp.weixin.qq.com/s?__biz=Mzg4NTc1NTQ2OQ==&mid=2247483918&idx=1&sn=9ee2641c695446168f995466e2baec44&chksm=ce23fd850e8706615f9f86283ce5bc91d6ce146d7c59c50804f94555fe8a054d18bebc2f9981&scene=90&xtrack=1&sessionid=1738884937&subscene=93&clicktime=1738885177&enterid=1738885177&flutter_pos=2&biz_enter_id=4&ranksessionid=1738885082&ascene=56&devicetype=iOS18.3&version=1800382d&nettype=WIFI&abtest_cookie=AAACAA==&lang=zh_CN&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQiH4qzDZFjAnShYAYWLA6+RLWAQIE97dBBAEAAAAAAAEON9JYDOsAAAAOpnltbLcz9gKNyK89dVj0JaGX3dI9JDPn6Hs5bTOYlWwVx+95E19pfiLN1XtVj4vRHr31H5c4ASMI2aDpSqz7KkKj6puKuZfgJkxMg4UL+9oI9qmlCKZ9VlrWeM1xWY2sgqvRIZDYiCfC6j5j6ni9bMJsQ3KdP6dy5FU4t6QaCbNRcYD2qV4QVTIRfemn9TnhqobRSQ2sRcEQDqGmsiWuDpJrLweTbktXNHhmkspCqskdF5X7cIKQPbkuTz2oW/I=&pass_ticket=T1GPIWZjV6j7TLLllz2HqDbO5Q1OPHl5Fdij7ZQIAa0rIh2j3MduE6DM/zWKLj1z&wx_header=3)

![](.evernote-content/31265FAA-3432-41B2-A439-B3B23B0D8058/4FE8829A-B362-40A1-9BDD-EF59B0A7B322.png)![](.evernote-content/31265FAA-3432-41B2-A439-B3B23B0D8058/A048CC69-0423-41E6-A967-88145C5E2CAD.png)![](.evernote-content/31265FAA-3432-41B2-A439-B3B23B0D8058/18E6C2BB-7693-4F55-99A7-B32576440B56.png)![](.evernote-content/31265FAA-3432-41B2-A439-B3B23B0D8058/757FFDA9-A08A-4582-B341-10DBB9CF840A.png)![](.evernote-content/31265FAA-3432-41B2-A439-B3B23B0D8058/7992E367-79D0-4EE9-BF63-A3AAECC386C5.png)![](.evernote-content/31265FAA-3432-41B2-A439-B3B23B0D8058/01A359B1-022C-4392-96B8-5C60427C459B.png)![](.evernote-content/31265FAA-3432-41B2-A439-B3B23B0D8058/1D5561C0-5A95-49C8-86F9-386BAC44FBC1.png)![](.evernote-content/31265FAA-3432-41B2-A439-B3B23B0D8058/84FACCAE-812B-438B-89A2-4B61D2327184.png)![](.evernote-content/31265FAA-3432-41B2-A439-B3B23B0D8058/11993B29-7641-4EDA-A19E-38AF810D5332.png)![](.evernote-content/31265FAA-3432-41B2-A439-B3B23B0D8058/69D5341F-B007-4E21-A16C-806353F2EB95.png)![](.evernote-content/31265FAA-3432-41B2-A439-B3B23B0D8058/32C895CD-8F8D-4A7B-85A6-DC573316F748.png)![](.evernote-content/31265FAA-3432-41B2-A439-B3B23B0D8058/6630148D-AF50-4FE0-8229-FFF9D33C7C3F.png)![](.evernote-content/31265FAA-3432-41B2-A439-B3B23B0D8058/C92DE987-4E0A-4A23-8ED0-FB4F360E239F.png)![](.evernote-content/31265FAA-3432-41B2-A439-B3B23B0D8058/9B5009F3-3784-4AFE-AA3E-BE201585F712.png)

探索 DeepSeek 提示词样例，挖掘更多可能。

https://api-docs.deepseek.com/zh-cn/prompt-library

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=Mzg4NTc1NTQ2OQ==&mid=2247483918&idx=1&sn=9ee2641c695446168f995466e2baec44&chksm=ce23fd850e8706615f9f86283ce5bc91d6ce146d7c59c50804f94555fe8a054d18bebc2f9981&scene=90&xtrack=1&sessionid=1738884937&subscene=93&clicktime=1738885177&enterid=1738885177&flutter_pos=2&biz_enter_id=4&ranksessionid=1738885082&ascene=56&devicetype=iOS18.3&version=1800382d&nettype=WIFI&abtest_cookie=AAACAA==&lang=zh_CN&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQiH4qzDZFjAnShYAYWLA6+RLWAQIE97dBBAEAAAAAAAEON9JYDOsAAAAOpnltbLcz9gKNyK89dVj0JaGX3dI9JDPn6Hs5bTOYlWwVx+95E19pfiLN1XtVj4vRHr31H5c4ASMI2aDpSqz7KkKj6puKuZfgJkxMg4UL+9oI9qmlCKZ9VlrWeM1xWY2sgqvRIZDYiCfC6j5j6ni9bMJsQ3KdP6dy5FU4t6QaCbNRcYD2qV4QVTIRfemn9TnhqobRSQ2sRcEQDqGmsiWuDpJrLweTbktXNHhmkspCqskdF5X7cIKQPbkuTz2oW/I=&pass_ticket=T1GPIWZjV6j7TLLllz2HqDbO5Q1OPHl5Fdij7ZQIAa0rIh2j3MduE6DM/zWKLj1z&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/390d3a0b-f332-415d-ace8-10aae3292c2b/390d3a0b-f332-415d-ace8-10aae3292c2b/)
