---
title: 使用deepseek自动处理Excel工作表
type: source
created: 2026-06-17
updated: 2026-06-17
source: 印象笔记管理工具
source_path: 印象笔记管理工具/使用deepseek自动处理Excel工作表.html
tags: [AI技术, 教育]
---

# 使用deepseek自动处理Excel工作表

原文链接: https://mp.weixin.qq.com/s?chksm=8484926fb3f31b79db3c3f7f3db0437...

原创fanjy 完美Excel 
学习Excel技术，关注微信公众号：
excelperfect

标签：AI，大模型，deepseek
完美Excel要转行了，否则就要关号了！因为deepseek来了。
确实太强大了！
搞了这么多年VBA，结果人家deepseek几秒钟搞定！
示例
如下图1所示的工作表，我想根据列A中的数据拆分工作表，即将相同的区域拆分到独立的工作表中。

图1
第1步：打开deepseek网站，给DeepSeek发送消息：
“我有一个Excel工作表，第一行是标题行，我想根据列A中的数据拆分该工作表，将列A中相同的数据及其所在行放置到单独的工作表中，如何用VBA来实现？请多思考几次”
几秒后，DeepSeek给出了答案，如下图2所示。

图2
第2步：单击代码右上角的“复制”，复制deepseek给出的vba代码。
详细代码如下：
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

...' 复制对应的行到新工作表
   For i = LBound(row
