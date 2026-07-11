# jieba · PyPI

---

jieba 0.42.1
============

pip install jieba

[Latest version](https://pypi.org/project/jieba/)

Released: Jan 20, 2020

Chinese Words Segmentation Utilities

Project description
-------------------

jieba
-----

“结巴”中文分词：做最好的 Python 中文分词组件

“Jieba” (Chinese for “to stutter”) Chinese text segmentation: built to
be the best Python Chinese word segmentation module.

完整文档见 README.md

GitHub: <https://github.com/fxsjy/jieba>

特点
--

* 支持三种分词模式：
  + 精确模式，试图将句子最精确地切开，适合文本分析；
  + 全模式，把句子中所有的可以成词的词语都扫描出来,
    速度非常快，但是不能解决歧义；
  + 搜索引擎模式，在精确模式的基础上，对长词再次切分，提高召回率，适合用于搜索引擎分词。
* 支持繁体分词
* 支持自定义词典
* MIT 授权协议

在线演示： <http://jiebademo.ap01.aws.af.cm/>

安装说明
----

代码对 Python 2/3 均兼容

* 全自动安装： easy\_install jieba 或者 pip install jieba / pip3 install jieba
* 半自动安装：先下载 <https://pypi.python.org/pypi/jieba/> ，解压后运行
  python setup.py install
* 手动安装：将 jieba 目录放置于当前目录或者 site-packages 目录
* 通过 import jieba 来引用

---

[🌐 原始链接](https://pypi.org/project/jieba/)

[📎 在印象笔记中打开](evernote:///view/207087/s1/d66e5b25-3e99-4255-8d29-74e7c2b5d6ec/d66e5b25-3e99-4255-8d29-74e7c2b5d6ec/)