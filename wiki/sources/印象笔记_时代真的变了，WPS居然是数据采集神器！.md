---
title: "时代真的变了，WPS居然是数据采集神器！"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/时代真的变了，WPS居然是数据采集神器！.md
tags: [印象笔记]
---

# 时代真的变了，WPS居然是数据采集神器！

# 时代真的变了，WPS居然是数据采集神器！ --- 原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzU2NTIyMTI3OA==&mid=224750...]

---

# 时代真的变了，WPS居然是数据采集神器！

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzU2NTIyMTI3OA==&mid=224750...](https://mp.weixin.qq.com/s?__biz=MzU2NTIyMTI3OA==&mid=2247508920&idx=1&sn=21bc36bb577c6700f63ac40db6da37e4&chksm=fd338ce49c384a9e52d9bb8128419f56098f927aea259c7ea05567afd794cedcd7f1170f206f&scene=90&xtrack=1&sessionid=1747697459&subscene=93&clicktime=1747702292&enterid=1747702292&flutter_pos=7&biz_enter_id=4&ranksessionid=1747698193&jumppath=WAWebViewController_1747702238338,WAWebViewController_1747702238869,20020_1747702282362,1104_1747702286838&jumppathdepth=4&ascene=56&devicetype=iOS18.4.1&version=18003b2a&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQV8GQyMLJs5qsQhFKYfJx3xLVAQIE97dBBAEAAAAAAMUlBYQflJMAAAAOpnltbLcz9gKNyK89dVj0wa+ewgACMN4H/7J79b6MaRcIlsBe2Hrp8iqU8ixwn6XKNzQduAr0Ev1nMBSDD+8cFvJaRUazALgfVybhwCAOEvktLTWYqKj9UJEGwClV8KZ7AW0vogMfY11lDGK4+glrS8Qy1nKBOiYAlH4HMKzWIkOZzcGAO0lVGYPetd0QnY6fk6fa8q5sX9j5N1IB1xBkZiON9hHF1LQifY9JK53eDYNIiazxgorotlE0qqEAFA==&pass_ticket=koB5K1QA4+aKXKzpDtDPFq7iOGAOWbVNvNNprvO+6UJ1Ytb9Vs6C2Zj32csprCFY&wx_header=3)

Original E精精 Excel办公实战

这两年微软和金山办公软件迭代速度要比过去十几年都要快的多且更新的功能特殊特别丰富，今天我们就拿数据采集这一块来聊聊！

01 | WPS中用PY采集

前几天，我们聊了一下Excel中的Python支持，很多同学由于版本问题不支持，今天我们来就看看大家都可以使用的WPS，他也是支持的！

我们点击新建-【智能表格】

![](.evernote-content/B75A9AC5-7A6D-4039-B2A1-ACC49FE0D1DF/0903FC99-D776-4A13-8DE6-4152EF8ABBB6.png)

在【效率】选项卡下面可以看到【PY脚本】，点击后点击【新建脚本】

![](.evernote-content/B75A9AC5-7A6D-4039-B2A1-ACC49FE0D1DF/30008242-71DA-446C-B1F1-F53197D95067.png)

在设置中，勾选【网络API】这样，我们就可以使用一下常用的网络相关库了，比如requests、bs4等，更多库也可以点击官方的帮助文档进行查看！同样也是网络，非本地部署，降低新手使用门槛！

![](.evernote-content/B75A9AC5-7A6D-4039-B2A1-ACC49FE0D1DF/81E46EED-464F-4380-8686-7E25EF91B1C2.png)

下面我们写一个简单的数据采集，作为练习 豆瓣 TOP250 比较合适，作为练习我们只采集了第一页25个！

![](.evernote-content/B75A9AC5-7A6D-4039-B2A1-ACC49FE0D1DF/79615ED3-5D9E-422E-A8D1-731BA779F266.gif)

有同学可能说了，我不懂PY呀，其实也简单学点基础，结合现在的AI写点代码还是挺简单的！

```
# 友情提醒：学习使用，请勿频繁发送请求，这是一种很刑的行为  
import requests  
from bs4 import BeautifulSoup  
  
deffetch_top250_books():  
    url = 'https://book.douban.com/top250'  
    headers = {  
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}  
      
    response = requests.get(url, headers=headers)  
    if response.status_code == 200:  
        soup = BeautifulSoup(response.text, 'html.parser')  
        items = soup.find_all('tr', class_='item')  
        books = []  
        for item in items:  
            # 书名  
            title = item.find('div', class_='pl2').a['title'].strip()  
              
            # 作者、出版社、年份信息  
            pub_info = item.find('p', class_='pl').get_text().split('/')  
            author = pub_info[0].strip()  
            publisher = pub_info[-3].strip() iflen(pub_info)>=3else'未知'  
            pub_year = pub_info[-2].strip()  
              
            # 评分与评论数  
            rating = item.find('span', class_='rating_nums').text.strip()  
            comments = item.find('span', class_='pl').text.strip().replace('(', '').replace(')', '')  
              
            # 简介  
            quote_tag = item.find('span', class_='inq')  
            quote = quote_tag.text.strip() if quote_tag else'无简介'  
              
            books.append([title, author, publisher, pub_year, rating, comments, quote])  
        return books  
    else:  
        print("Failed to retrieve the web page")  
        returnNone  
  
if __name__ == '__main__':  
  top250_books = fetch_top250_books()  
  # 写入表格的接口函数  
  write_xl(top250_books,"A1")
```

02 | WPS中用JS采集

除了PY的支持，目前WPS也支持JS了，所以我们还可以使用JS来处理类似的需求！

下面我们来看一下，如何在WPS中使用JS完成数据采集！

点击【工具】-【开发工具】

![](.evernote-content/B75A9AC5-7A6D-4039-B2A1-ACC49FE0D1DF/4CC7F66A-0335-4FAD-8EF4-A69BAF510799.png)

下面就可以看到 WPS宏编辑器，如果你的显示是VB编辑器

![](.evernote-content/B75A9AC5-7A6D-4039-B2A1-ACC49FE0D1DF/B8615B9C-F2AE-4CF7-BB99-3269328F4038.png)

点击旁边的【切换到JS环境】即可！

![](.evernote-content/B75A9AC5-7A6D-4039-B2A1-ACC49FE0D1DF/C3E177FA-E24F-42E0-9B81-859ACFDD6644.png)

点击进去编辑，我们就要可以写我们的JS代码了！

▼ 动画演示-WPS\_JS数据采集

![](.evernote-content/B75A9AC5-7A6D-4039-B2A1-ACC49FE0D1DF/4DE660EB-3E11-4812-B811-6D56A91959FA.gif)

JS大体代码如下！目前可以使用传统的XMLHttpRequest对象或者fetch

配合JS字符串正则完成数据的清洗！在WPS中已经实现了对应的工作表相关模型接口，基本是使用了JS实现了一下VBA中的对象模型，只是部分略有不同！

▼ 核心代码如下▼

![](.evernote-content/B75A9AC5-7A6D-4039-B2A1-ACC49FE0D1DF/D12A21BA-A28E-4D40-A750-1C1EA648536B.png)

你一般使用WPS来干嘛呢？时代真的不同了，这两年随着AI的发展，我们的学习成本降低了很多，同时国内外的办公软件迭代的速度也在大大加快。个人挡不住时代，唯有拥抱并学习才能更好的适应未来的生活！

关注我，带你一起提高办公自动化效率！

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzU2NTIyMTI3OA==&mid=2247508920&idx=1&sn=21bc36bb577c6700f63ac40db6da37e4&chksm=fd338ce49c384a9e52d9bb8128419f56098f927aea259c7ea05567afd794cedcd7f1170f206f&scene=90&xtrack=1&sessionid=1747697459&subscene=93&clicktime=1747702292&enterid=1747702292&flutter_pos=7&biz_enter_id=4&ranksessionid=1747698193&jumppath=WAWebViewController_1747702238338,WAWebViewController_1747702238869,20020_1747702282362,1104_1747702286838&jumppathdepth=4&ascene=56&devicetype=iOS18.4.1&version=18003b2a&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQV8GQyMLJs5qsQhFKYfJx3xLVAQIE97dBBAEAAAAAAMUlBYQflJMAAAAOpnltbLcz9gKNyK89dVj0wa+ewgACMN4H/7J79b6MaRcIlsBe2Hrp8iqU8ixwn6XKNzQduAr0Ev1nMBSDD+8cFvJaRUazALgfVybhwCAOEvktLTWYqKj9UJEGwClV8KZ7AW0vogMfY11lDGK4+glrS8Qy1nKBOiYAlH4HMKzWIkOZzcGAO0lVGYPetd0QnY6fk6fa8q5sX9j5N1IB1xBkZiON9hHF1LQifY9JK53eDYNIiazxgorotlE0qqEAFA==&pass_ticket=koB5K1QA4+aKXKzpDtDPFq7iOGAOWbVNvNNprvO+6UJ1Ytb9Vs6C2Zj32csprCFY&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/69f4b0b0-df38-4b25-b6ac-163f44b65524/69f4b0b0-df38-4b25-b6ac-163f44b65524/)