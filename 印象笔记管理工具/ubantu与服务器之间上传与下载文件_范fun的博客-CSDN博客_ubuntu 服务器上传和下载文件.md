# ubantu与服务器之间上传与下载文件_范fun的博客-CSDN博客_ubuntu 服务器上传和下载文件

---

ubantu与服务器之间上传与下载文件
===================

![](.evernote-content/E42B92F4-0EB9-4771-B6C4-8B464F029434/71FAEF9E-92C6-44CB-A237-85D43F54A831.png)

[MinJinFan](https://blog.csdn.net/qq_37264323/article/details/90548776?spm=1001.2101.3001.6650.1&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1.no_search_link&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1.no_search_link&utm_relevant_index=2undefined)
2019-05-29 13:21:45
![](.evernote-content/E42B92F4-0EB9-4771-B6C4-8B464F029434/8D463FF0-C5FD-4408-A4EB-093AEEB3E1E6.png)
729

分类专栏：
[Linux](https://blog.csdn.net/qq_37264323/article/details/90548776?spm=1001.2101.3001.6650.1&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1.no_search_link&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1.no_search_link&utm_relevant_index=2undefined)

版权

专栏收录该内容

6 篇文章
0 订阅

订阅专栏

首先在ubantu本机上安装 SSH(Secure Shell) 服务以提供远程管理服务

sudo apt-get install ssh

一.文件近距离传输
---------

SSH 远程登入 [Ubuntu](https://blog.csdn.net/qq_37264323/article/details/90548776?spm=1001.2101.3001.6650.1&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1.no_search_link&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1.no_search_link&utm_relevant_index=2undefined) 机
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

ssh username@192.168.0.1
------------------------

将 文件/文件夹 从远程 Ubuntu 机拷至本地(scp)

scp -r username@192.168.0.1:/home/file.txt ./

将 文件/文件夹 从本地拷至远程 Ubuntu 机(scp)
------------------------------

scp -r localfile.txt username@192.168.0.1:/home/

二.这是重点，就是将文件在本地和远程(云服务器)之间传输
============================

1将 文件/文件夹 从远程 Ubuntu 机拷至本地(rsync)

rsync -v -u -a --delete --rsh=ssh --stats username@192.168.0.1:/home/file.txt ~/download

### 后面的~/download是你本地目录，也就是你想把文件保存的地方;前面IP地址冒号后面的就是你想下载的文件在远程服务器中的目录，可以是文件也可以是文件夹。

2将 文件/文件夹 从本地拷至远程 Ubuntu 机(rsync)
---------------------------------

rsync -v -u -a --delete --rsh=ssh --stats localfile.txt username@192.168.0.1:/home/

---

[🌐 原始链接](https://blog.csdn.net/qq_37264323/article/details/90548776?spm=1001.2101.3001.6650.1&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1.no_search_link&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1.no_search_link&utm_relevant_index=2)

[📎 在印象笔记中打开](evernote:///view/207087/s1/e596f30e-8dfa-4590-a87b-cb2247bbb505/e596f30e-8dfa-4590-a87b-cb2247bbb505/)