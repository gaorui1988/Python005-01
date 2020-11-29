## 学习笔记





## 本周作业

- 建立自己的 Python 开发环境
正确安装 Python3.7 和 pip, 正确配置环境变量，并能够查看 Python 的版本（Linux 可以使用虚拟机或最低配置的公有云主机）。
```
[root@host54 Python005-01]# cat /etc/redhat-release 
CentOS Linux release 7.6.1810 (Core) 
[root@host54 Python005-01]# 
[root@host54 Python005-01]# python3  -V
Python 3.7.9
[root@host54 Python005-01]# pip3 -V
pip 20.2.4 from /usr/local/python3/lib/python3.7/site-packages/pip (python 3.7)
[root@host54 Python005-01]# 


[root@host54 test]# ll /usr/bin|grep python
lrwxrwxrwx.   1 root root           7 Apr 14  2020 python -> python2
lrwxrwxrwx.   1 root root           9 Apr 14  2020 python2 -> python2.7
-rwxr-xr-x.   1 root root        7216 Oct 31  2018 python2.7
[root@host54 test]# ll /usr/local/bin|grep python
lrwxrwxrwx 1 root root 27 Nov 26 00:05 pip3 -> /usr/local/python3/bin/pip3
lrwxrwxrwx 1 root root 30 Nov 26 00:04 python3 -> /usr/local/python3/bin/python3
[root@host54 test]#

[root@host54 test]# cat /etc/profile|grep python
alias ipython='python3 -m IPython'
[root@host54 test]# ipython  -V
7.19.0


```



- 熟悉 Visual Studio Code 或者 PyCharm 等任一 IDE 的使用, 熟练配置虚拟环境，并能够使用 debug 和 run 功能运行和调试程序。
```

//IDE
vscode
Remote - SSH远程Linux插件
实现远程调试程序
通过插件远程pull代码-->本地使用vscode写代码-->add代码到暂存区-->commit代码-->push代码到GitHub远程仓库

```


- 通过 Python 官方文档, 找到 Python 支持的基本数据类型，并列举各类型的定义和赋值操作（可以通过文本文档或思维导图形式提交总结）。
```

标准数据类型
Python3 中有六个标准的数据类型：

Number（数字）
String（字符串）
List（列表）
Tuple（元组）
Set（集合）
Dictionary（字典）
Python3 的六个标准数据类型中：

不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。

注：
操作见学习笔记

```

- 编写一个函数, 当函数被调用时，将调用的时间记录在日志中, 日志文件的保存位置建议为：/var/log/python- 当前日期 /xxxx.log (此作业需提交至 GitHub)
```
#!/usr/bin/env python


import os
import logging
import time
import pathlib



def log_func():
    #获取当前时间日期
    today = time.strftime("%Y-%m-%d", time.localtime())
    
    #文件路径
    dirPath = '/var/log/python-' + today
    logfile = "test.log"
    
    #判断当前路径是否存在
    if not os.path.exists(dirPath):
        # 不存在则创建
        os.makedirs(dirPath)
    #切换操作目录
    os.chdir(dirPath)
    #日志格式
    logging.basicConfig(filename=logfile,
                        level=logging.DEBUG,
                        datefmt='%Y-%m-%d %H:%M:%S',
                        format="%(asctime)s [%(name)s : %(message)s]"
                        )
    logging.info('函数调用')
    
if __name__ == '__main__':
    log_func()

```



5、想想自己工作中哪些手动的工作可以用 Python 程序自动完成，并亲自尝试一下。
```
python监控自定义指标并定时上报至pushgateway
prometheus获取从pushgateway中推送上来的数据
grafana展示prometheus获取到的监控指标


```

