# 使用deepseek自动处理Excel工作表

---

原文链接: [https://mp.weixin.qq.com/s?chksm=8484926fb3f31b79db3c3f7f3db0437...](https://mp.weixin.qq.com/s?chksm=8484926fb3f31b79db3c3f7f3db04375b7469e72fdaa30fefb9cb729f895e2101821929e1504&exptype=unsubscribed_card_recommend_article_u2i_mainprocess_coarse_sort_tlfeeds&ranksessionid=1738667202_1&scene=169&mid=2650938856&sn=6e5923e1f6b959ec9f31509ceda97ed1&idx=1&__biz=MzA3NTMzMjMyOA==&sessionid=1738667202&subscene=200&clicktime=1738667512&enterid=1738667512&flutter_pos=9&biz_enter_id=5&ascene=56&devicetype=iOS18.3&version=1800382d&nettype=3G+&abtest_cookie=AAACAA==&lang=zh_CN&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQTFRwk53aLbP1MRmF9HddXxLWAQIE97dBBAEAAAAAAOIaEH8VZZoAAAAOpnltbLcz9gKNyK89dVj04mg8uk1iUXhpvqA+ddKiq6bKNvmN/nT238Bcz/yLHOsyoonS4O2/nBDthc9OlXGAmauTOTI3M6rBvhm+aZDvz7rCu9AX3fzXilDtAt4mVrXtpO90R5F7CLZv+i0OnNhPc6beJWx030+B65KjUmbjHzGMNZDb8ZB3KVp331TbLu47TMfdlrhiNBwIbG9nR4/UB+ez3npxEQfYMX0xN8Ds7GD5HwKTr21IgRfAIwnlTQ4=&pass_ticket=orw9bzutongcNGOVICQDfHhYaCthkU1BqyiNQhwTi9DYUxHhD84QnfKyJr9EC33Y&wx_header=3)

原创fanjy完美Excel

学习Excel技术，关注微信公众号：

*excelperfect*

**标签：**AI，大模型，deepseek

完美Excel要转行了，否则就要关号了！因为deepseek来了。

确实太强大了！

搞了这么多年VBA，结果人家deepseek几秒钟搞定！

**示例**

如下图1所示的工作表，我想根据列A中的数据拆分工作表，即将相同的区域拆分到独立的工作表中。

![](.evernote-content/CAA6EEBF-BE7E-4E5C-B4BB-8A98C676BA25/76528AB7-33E3-4181-AABB-A7166D191D74.jpg)

图1

**第****1****步：**打开deepseek网站，给DeepSeek发送消息：

“我有一个Excel工作表，第一行是标题行，我想根据列A中的数据拆分该工作表，将列A中相同的数据及其所在行放置到单独的工作表中，如何用VBA来实现？请多思考几次”

几秒后，DeepSeek给出了答案，如下图2所示。

![](.evernote-content/CAA6EEBF-BE7E-4E5C-B4BB-8A98C676BA25/7A60C813-1970-47CE-9C83-5F6A1FCFF26F.jpg)

图2

**第****2****步：**单击代码右上角的“复制”，复制deepseek给出的vba代码。

详细代码如下：

```
Sub SplitDataByColumnA()  
 Dim wsSource As Worksheet  
 Dim wsDest As Worksheet  
 Dim lastRow As Long  
 Dim lastCol As Long  
 Dim i As Long  
 Dim dict As Object  
 Dim key As Variant  
 Dim rng As Range  
 Dim cell As Range  
  
 ' 设置源工作表  
 Set wsSource = ThisWorkbook.Sheets("Sheet1") ' 修改为你的工作表名称  
  
 ' 获取源工作表的最后一行和最后一列  
 lastRow = wsSource.Cells(wsSource.rows.Count, 1).End(xlUp).Row  
 lastCol = wsSource.Cells(1, wsSource.Columns.Count).End(xlToLeft).Column  
  
 ' 创建一个字典来存储唯一值和对应的行  
 Set dict = CreateObject("Scripting.Dictionary")  
  
 ' 遍历列A中的数据  
 For Each cell In wsSource.Range("A2:A" & lastRow)  
   If Not dict.exists(cell.Value) Then  
     dict.Add cell.Value, cell.Row  
   Else  
     dict(cell.Value) = dict(cell.Value) & "," & cell.Row  
   End If  
 Next cell  
  
 ' 遍历字典中的每个键（唯一值）  
 For Each key In dict.keys  
   ' 创建一个新的工作表  
   Set wsDest = ThisWorkbook.Sheets.Add  
   wsDest.Name = key ' 将工作表命名为当前键值  
  
   ' 复制标题行到新工作表  
   wsSource.rows(1).Copy Destination:=wsDest.rows(1)  
  
   ' 获取当前键值对应的行号  
   Dim rows As Variant  
   rows = Split(dict(key), ",")  
  
   ' 复制对应的行到新工作表  
   For i = LBound(rows) To UBound(rows)  
     wsSource.rows(rows(i)).Copy Destination:=wsDest.rows(wsDest.Cells(wsDest.rows.Count, 1).End(xlUp).Row + 1)  
   Next i  
 Next key  
  
 ' 释放对象  
 Set dict = Nothing  
 Set wsSource = Nothing  
 Set wsDest = Nothing  
  
 MsgBox "数据拆分完成！"  
End Sub
```

规范、清晰，还有详细的注释。

**第****3****步：**回到Excel工作簿中，按Alt+F11键打开VBE，插入一个标准模块，然后在代码窗口粘贴代码，如下图3所示。

![](.evernote-content/CAA6EEBF-BE7E-4E5C-B4BB-8A98C676BA25/F1AE7B6F-904F-4208-92F1-8B2E4B6C3BF3.jpg)

图3

**第****4****步：**运行SplitDataByColumnA过程，结果如下图4所示。

![](.evernote-content/CAA6EEBF-BE7E-4E5C-B4BB-8A98C676BA25/7CDBBE7D-DE95-45A6-AD61-8B7EF1A4013B.jpg)

图4

拆分得到的工作表“东区”如下图5所示。

![](.evernote-content/CAA6EEBF-BE7E-4E5C-B4BB-8A98C676BA25/2F8B6574-5CAD-4B78-9CE7-472EAAB229CD.jpg)

图5

**提示：**如果deepseek生成的代码不符合要求，你可以叫它多思考几次，就像我提问的最后一句。实际上，对于这个示例，deepseek对我的问题第一次生成的代码有错误，我在提问的后面加了一句“请多思考几次”，结果第二次生成的代码完美实现了我的需求。

**欢迎在下面留言，完善本文内容，让更多的人学到更完美的知识。**

欢迎到知识星球：***完美******Excel******社群***，进行技术交流和提问，获取更多电子资料，并通过社群加入专门的微信讨论群，更方便交流。

![](.evernote-content/CAA6EEBF-BE7E-4E5C-B4BB-8A98C676BA25/4D045DB5-A3EC-4D19-9957-CD80A613604E.jpg)

个人观点，仅供参考

---

[🌐 原始链接](https://mp.weixin.qq.com/s?chksm=8484926fb3f31b79db3c3f7f3db04375b7469e72fdaa30fefb9cb729f895e2101821929e1504&exptype=unsubscribed_card_recommend_article_u2i_mainprocess_coarse_sort_tlfeeds&ranksessionid=1738667202_1&scene=169&mid=2650938856&sn=6e5923e1f6b959ec9f31509ceda97ed1&idx=1&__biz=MzA3NTMzMjMyOA==&sessionid=1738667202&subscene=200&clicktime=1738667512&enterid=1738667512&flutter_pos=9&biz_enter_id=5&ascene=56&devicetype=iOS18.3&version=1800382d&nettype=3G+&abtest_cookie=AAACAA==&lang=zh_CN&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQTFRwk53aLbP1MRmF9HddXxLWAQIE97dBBAEAAAAAAOIaEH8VZZoAAAAOpnltbLcz9gKNyK89dVj04mg8uk1iUXhpvqA+ddKiq6bKNvmN/nT238Bcz/yLHOsyoonS4O2/nBDthc9OlXGAmauTOTI3M6rBvhm+aZDvz7rCu9AX3fzXilDtAt4mVrXtpO90R5F7CLZv+i0OnNhPc6beJWx030+B65KjUmbjHzGMNZDb8ZB3KVp331TbLu47TMfdlrhiNBwIbG9nR4/UB+ez3npxEQfYMX0xN8Ds7GD5HwKTr21IgRfAIwnlTQ4=&pass_ticket=orw9bzutongcNGOVICQDfHhYaCthkU1BqyiNQhwTi9DYUxHhD84QnfKyJr9EC33Y&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/323d5fee-dfc7-4c3d-8869-88493e5c141e/323d5fee-dfc7-4c3d-8869-88493e5c141e/)