---
title: "Python jieba库的使用说明 - 王陸 - 博客园"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/Python jieba库的使用说明 - 王陸 - 博客园.md
tags: [印象笔记]
---

# Python jieba库的使用说明 - 王陸 - 博客园

# Python jieba库的使用说明 - 王陸 - 博客园 --- Python jieba库的使用说明 ================== 一、jieba库基本介绍 ------------ 

---

# Python jieba库的使用说明 - 王陸 - 博客园

---

Python jieba库的使用说明
==================

一、jieba库基本介绍
------------

  (1)、jieba库概述

         jieba是优秀的中文分词第三方库

         - 中文文本需要通过分词获得单个的词语  
         - jieba是优秀的中文分词第三方库，需要额外安装

         - jieba库提供三种分词模式，最简单只需掌握一个函数

  (2)、jieba分词的原理

         Jieba分词依靠中文词库

         - 利用一个中文词库，确定汉字之间的关联概率  
         - 汉字间概率大的组成词组，形成分词结果

         - 除了分词，用户还可以添加自定义的词组

二、jieba库使用说明
------------

  (1)、jieba分词的三种模式

         精确模式、全模式、搜索引擎模式

         - 精确模式：把文本精确的切分开，不存在冗余单词  
         - 全模式：把文本中所有可能的词语都扫描出来，有冗余

         - 搜索引擎模式：在精确模式基础上，对长词再次切分

  (2)、jieba库常用函数

![](.evernote-content/E13AEE58-5341-4450-B0C3-5BD6836294C1/1DA3E161-E969-4BBF-8573-FD9BD01CC79B.png)

三、jieba应用实例
-----------

![](.evernote-content/E13AEE58-5341-4450-B0C3-5BD6836294C1/62BF19F8-BDFE-460A-83FE-0C4018BAE3F1.png)

四、利用jieba库统计三国演义中任务的出场次数
------------------------

```
import  jieba

txt = open("D:\\三国演义.txt", "r", encoding='utf-8').read()
words = jieba.lcut(txt)     # 使用精确模式对文本进行分词
counts = {}     # 通过键值对的形式存储词语及其出现的次数

for word in words:
    if  len(word) == 1:    # 单个词语不计算在内
        continue
    else:
        counts[word] = counts.get(word, 0) + 1    # 遍历所有词语，每出现一次其对应的值加 1
        
items = list(counts.items())#将键值对转换成列表
items.sort(key=lambda x: x[1], reverse=True)    # 根据词语出现的次数进行从大到小排序

for i in range(15):
    word, count = items[i]
    print("{0:<5}{1:>5}".format(word, count))
```

![](.evernote-content/E13AEE58-5341-4450-B0C3-5BD6836294C1/456ABEB9-1978-4572-BAFE-0E67AC28833E.png)

统计了次数对多前十五个名词，曹操不愧是一代枭雄，第一名当之无愧，但是我们会发现得到的数据还是需要进一步处理，比如一些无用的词语，一些重复意思的词语。

五、去停用词的jieba分词
--------------

停用词表：https://github.com/goto456/stopwords

```
import jieba

# 创建停用词列表
def stopwordslist():
    stopwords = [line.strip() for line in open('stop_words.txt', encoding='UTF-8').readlines()]
    return stopwords

# 对句子进行中文分词
def seg_depart(sentence):
    # 对文档中的每一行进行中文分词
    print("正在分词")
    sentence_depart = jieba.cut(sentence.strip())
    # 创建一个停用词列表
    stopwords = stopwordslist()
    # 输出结果为outstr
    outstr = ''
    # 去停用词
    for word in sentence_depart:
        if word not in stopwords:
            if word != '\t':
                outstr += word
                outstr += " "
    return outstr

# 给出文档路径
filename = "Init.txt"
outfilename = "out.txt"
inputs = open(filename, 'rb')
outputs = open(outfilename, 'w')

# 将输出结果写入ou.txt中
for line in inputs:
    line_seg = seg_depart(line)
    outputs.write(line_seg + '\n')
    print("-------------------正在分词和去停用词-----------")
outputs.close()
inputs.close()
print("删除停用词和分词成功！！！")
```

---

[🌐 原始链接](https://www.cnblogs.com/wkfvawl/p/9487165.html)

[📎 在印象笔记中打开](evernote:///view/207087/s1/4433b2da-81e5-4690-8539-c6e73e9845b6/4433b2da-81e5-4690-8539-c6e73e9845b6/)