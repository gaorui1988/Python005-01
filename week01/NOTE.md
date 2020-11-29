学习笔记


#python训练营学习手册  
- 如何获取学分  
- GitHub使用  
- 作业如何fork到自己的Github账号下，如何提交作业到fork后的仓库  


#Git&GitHub操作指南  
- 配置个人信息（多人协作情况下会知道是谁更新了代码）  
```
git config --global user.email "2295463072@qq.com"  
git config --global user.name "gaorui"  

[root@host54 python5]# git config --global --list  
user.email=2295463072@qq.com  
user.name=gaorui  
```

- 如何跟GitHub交互（免密：将公钥信息放到GitHub中，如何设置可自行百度）  
- 如何从第一次拉取代码-->将代码push到自己fork的仓库中  
1）pull代码（强烈建议使用免密方式，只需要第一次设置即可）  
2）更新代码  
3）将代码add到暂存区  
4）将代码commit（备注信息必须详细，方便自己方便他人）  
5）添加远程仓库  
6）push代码（有多个分支情况，可提交到对应的branch下）  
7）查看log（git log）  


#第一周：从其他语言平滑迁移到python开发  
- 区分多版本python  
- 安装多版本python  
- 如何通过调整$PATH环境变量方式设置python版本优先级  
- 多版本python解释器共存的问题及规避方式（注：强烈建议产线不要存在多版本）  
- pip安装python库  
```
[root@host54 ~]# python  
python     python2    python2.7  python3  
[root@host54 ~]# python -V   
Python 2.7.5  
[root@host54 ~]# python3 -V  
Python 3.7.9  
[root@host54 ~]#  
[root@host54 ~]# ls -al /usr/bin/|grep python  
lrwxrwxrwx.   1 root root           7 Apr 14  2020 python -> python2  
lrwxrwxrwx.   1 root root           9 Apr 14  2020 python2 -> python2.7  
-rwxr-xr-x.   1 root root        7216 Oct 31  2018 python2.7  
[root@host54 ~]#  
[root@host54 ~]#  
[root@host54 ~]# ls -al /usr/local/bin/|grep python  
lrwxrwxrwx   1 root root  27 Nov 26 00:05 pip3 -> /usr/local/python3/bin/pip3 
lrwxrwxrwx   1 root root  30 Nov 26 00:04 python3 -> /usr/local/python3/bin/python3  
[root@host54 ~]#  
```

- ipython安装及使用（python交互增强、语法高亮、命令不全等）  
```
[root@host54 ~]# cat /etc/profile |grep python 
alias ipython='python3 -m IPython'  
[root@host54 ~]#  
[root@host54 ~]# ipython  -V 
7.19.0  
[root@host54 ~]#  
[root@host54 ~]# ipython  
Python 3.7.9 (default, Nov 26 2020, 00:01:45)  
Type 'copyright', 'credits' or 'license' for more information  
IPython 7.19.0 -- An enhanced Interactive Python. Type '?' for help.  

In [1]: x="hello,python."  

In [2]: print(x) 
hello,python.  

In [3]:  
```


- 如何通过虚拟环境隔离多版本python环境（包括pip安装的第三方库）
- python及其依赖库迁移
```

[venv001]
1）创建venv001虚拟环境
2）pip安装库

创建虚拟环境venv001  
[root@host54 test]# python3  -m venv  venv001  
[root@host54 test]# ll
total 0
drwxr-xr-x 5 root root 74 Nov 27 21:17 venv001  

激活并进去venv001虚拟环境
[root@host54 test]# source  venv001/bin/activate   

查看venv001虚拟环境中的python3版本  
(venv001) [root@host54 test]# python3 -V  
Python 3.7.9  

查看python3可执行程序路径
(venv001) [root@host54 test]# which  python3  
/opt/test/venv001/bin/python3   

查看venv001虚拟环境中安装了哪些第三方库（默认没有任何三方库）    

(venv001) [root@host54 test]# pip3 freeze    
在venv001虚拟化环境中安装ipython第三方库  
(venv001) [root@host54 test]# pip3 install ipython   
Collecting ipython
  Using cached ipython-7.19.0-py3-none-any.whl (784 kB)
Collecting jedi>=0.10
  Using cached jedi-0.17.2-py2.py3-none-any.whl (1.4 MB)
Collecting pickleshare
  Using cached pickleshare-0.7.5-py2.py3-none-any.whl (6.9 kB)
Collecting pexpect>4.3; sys_platform != "win32"
  Using cached pexpect-4.8.0-py2.py3-none-any.whl (59 kB)
Collecting backcall
  Using cached backcall-0.2.0-py2.py3-none-any.whl (11 kB)
Collecting traitlets>=4.2
  Using cached traitlets-5.0.5-py3-none-any.whl (100 kB)
Collecting pygments
  Using cached Pygments-2.7.2-py3-none-any.whl (948 kB)
Requirement already satisfied: setuptools>=18.5 in ./venv001/lib/python3.7/site-packages (from ipython) (47.1.0)
Collecting prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0
  Using cached prompt_toolkit-3.0.8-py3-none-any.whl (355 kB)
Collecting decorator
  Using cached decorator-4.4.2-py2.py3-none-any.whl (9.2 kB)
Collecting parso<0.8.0,>=0.7.0
  Using cached parso-0.7.1-py2.py3-none-any.whl (109 kB)
Collecting ptyprocess>=0.5
  Using cached ptyprocess-0.6.0-py2.py3-none-any.whl (39 kB)
Collecting ipython-genutils
  Using cached ipython_genutils-0.2.0-py2.py3-none-any.whl (26 kB)
Collecting wcwidth
  Using cached wcwidth-0.2.5-py2.py3-none-any.whl (30 kB)
Installing collected packages: parso, jedi, pickleshare, ptyprocess, pexpect, backcall, ipython-genutils, traitlets, pygments, wcwidth, prompt-toolkit, decorator, ipython
Successfully installed backcall-0.2.0 decorator-4.4.2 ipython-7.19.0 ipython-genutils-0.2.0 jedi-0.17.2 parso-0.7.1 pexpect-4.8.0 pickleshare-0.7.5 prompt-toolkit-3.0.8 ptyprocess-0.6.0 pygments-2.7.2 traitlets-5.0.5 wcwidth-0.2.5
WARNING: You are using pip version 20.1.1; however, version 20.2.4 is available.  
You should consider upgrading via the '/opt/test/venv001/bin/python3 -m pip install --upgrade pip' command. 

这个时候再次查看就会发现ipython库及其依赖库列表
(venv001) [root@host54 test]# pip3 freeze
backcall==0.2.0
decorator==4.4.2
ipython==7.19.0
ipython-genutils==0.2.0
jedi==0.17.2
parso==0.7.1
pexpect==4.8.0
pickleshare==0.7.5
prompt-toolkit==3.0.8
ptyprocess==0.6.0
Pygments==2.7.2
traitlets==5.0.5
wcwidth==0.2.5

查看第三方库路径下是否存在 
(venv001) [root@host54 test]# ls venv001/lib/python3.7/site-packages/  
backcall/                         IPython/                          jedi-0.17.2.dist-info/            pickleshare-0.7.5.dist-info/      prompt_toolkit/                   pygments/                         traitlets-5.0.5.dist-info/
backcall-0.2.0.dist-info/         ipython-7.19.0.dist-info/         parso/                            pickleshare.py                    prompt_toolkit-3.0.8.dist-info/   Pygments-2.7.2.dist-info/         wcwidth/
decorator-4.4.2.dist-info/        ipython_genutils/                 parso-0.7.1.dist-info/            pip/                              ptyprocess/                       setuptools/                       wcwidth-0.2.5.dist-info/
decorator.py                      ipython_genutils-0.2.0.dist-info/ pexpect/                          pip-20.1.1.dist-info/             ptyprocess-0.6.0.dist-info/       setuptools-47.1.0.dist-info/
easy_install.py                   jedi/                             pexpect-4.8.0.dist-info/          pkg_resources/                    __pycache__/                      traitlets/





创建虚拟环境venv002  
[root@host54 test]# python3 -m venv venv002  
[root@host54 test]# ll  
total 0  
drwxr-xr-x 6 root root 87 Nov 27 21:18 venv001  
drwxr-xr-x 5 root root 74 Nov 27 21:41 venv002  

激活并登录虚拟环境venv001  
[root@host54 test]# source  venv001/bin/activate  

导出虚拟环境venv001（python及其安装的库）  
(venv001) [root@host54 test]# pip3 freeze  
backcall==0.2.0
decorator==4.4.2
ipython==7.19.0
ipython-genutils==0.2.0
jedi==0.17.2
parso==0.7.1
pexpect==4.8.0
pickleshare==0.7.5
prompt-toolkit==3.0.8
ptyprocess==0.6.0
Pygments==2.7.2
traitlets==5.0.5
wcwidth==0.2.5

(venv001) [root@host54 test]# pip3 freeze > requirements.txt  
(venv001) [root@host54 test]# cat requirements.txt  
backcall==0.2.0
decorator==4.4.2
ipython==7.19.0
ipython-genutils==0.2.0
jedi==0.17.2
parso==0.7.1
pexpect==4.8.0
pickleshare==0.7.5
prompt-toolkit==3.0.8
ptyprocess==0.6.0
Pygments==2.7.2
traitlets==5.0.5
wcwidth==0.2.5
(venv001) [root@host54 test]# deactivate

激活并进入虚拟环境venv002  
[root@host54 test]# source venv002/bin/activate  

确认venv002虚拟环境中的python版本及其库相关信息
(venv002) [root@host54 test]# pip3 -V  
pip 20.1.1 from /opt/test/venv002/lib/python3.7/site-packages/pip (python 3.7)  
(venv002) [root@host54 test]# python3 -V  
Python 3.7.9
(venv002) [root@host54 test]# which  python3  
/opt/test/venv002/bin/python3  
未安装库（列表为空）
(venv002) [root@host54 test]# pip3 freeze  

使用venv001虚拟环境中导出的库列表，在venv002虚拟环境中安装库（可以理解为venv001环境中库的模板）
(venv002) [root@host54 test]# pip install -r ./requirements.txt
Collecting backcall==0.2.0
  Using cached backcall-0.2.0-py2.py3-none-any.whl (11 kB)
Collecting decorator==4.4.2
  Using cached decorator-4.4.2-py2.py3-none-any.whl (9.2 kB)
Collecting ipython==7.19.0
  Using cached ipython-7.19.0-py3-none-any.whl (784 kB)
Collecting ipython-genutils==0.2.0
  Using cached ipython_genutils-0.2.0-py2.py3-none-any.whl (26 kB)
Collecting jedi==0.17.2
  Using cached jedi-0.17.2-py2.py3-none-any.whl (1.4 MB)
Collecting parso==0.7.1
  Using cached parso-0.7.1-py2.py3-none-any.whl (109 kB)
Collecting pexpect==4.8.0
  Using cached pexpect-4.8.0-py2.py3-none-any.whl (59 kB)
Collecting pickleshare==0.7.5
  Using cached pickleshare-0.7.5-py2.py3-none-any.whl (6.9 kB)
Collecting prompt-toolkit==3.0.8
  Using cached prompt_toolkit-3.0.8-py3-none-any.whl (355 kB)
Collecting ptyprocess==0.6.0
  Using cached ptyprocess-0.6.0-py2.py3-none-any.whl (39 kB)
Collecting Pygments==2.7.2
  Using cached Pygments-2.7.2-py3-none-any.whl (948 kB)
Collecting traitlets==5.0.5
  Using cached traitlets-5.0.5-py3-none-any.whl (100 kB)
Collecting wcwidth==0.2.5
  Using cached wcwidth-0.2.5-py2.py3-none-any.whl (30 kB)
Requirement already satisfied: setuptools>=18.5 in ./venv002/lib/python3.7/site-packages (from ipython==7.19.0->-r ./requirements.txt (line 3)) (47.1.0)
Installing collected packages: backcall, decorator, parso, jedi, ipython-genutils, traitlets, Pygments, wcwidth, prompt-toolkit, pickleshare, ptyprocess, pexpect, ipython
Successfully installed Pygments-2.7.2 backcall-0.2.0 decorator-4.4.2 ipython-7.19.0 ipython-genutils-0.2.0 jedi-0.17.2 parso-0.7.1 pexpect-4.8.0 pickleshare-0.7.5 prompt-toolkit-3.0.8 ptyprocess-0.6.0 traitlets-5.0.5 wcwidth-0.2.5
WARNING: You are using pip version 20.1.1; however, version 20.2.4 is available.
You should consider upgrading via the '/opt/test/venv002/bin/python3 -m pip install --upgrade pip' command.

确认venv002虚拟环境中安装的库是否与venv001中一致
(venv002) [root@host54 test]# pip3 freeze
backcall==0.2.0
decorator==4.4.2
ipython==7.19.0
ipython-genutils==0.2.0
jedi==0.17.2
parso==0.7.1
pexpect==4.8.0
pickleshare==0.7.5
prompt-toolkit==3.0.8
ptyprocess==0.6.0
Pygments==2.7.2
traitlets==5.0.5
wcwidth==0.2.5
(venv002) [root@host54 test]# ls venv002/lib/python3.7/site-packages/
backcall                   IPython                           jedi-0.17.2.dist-info    pickleshare-0.7.5.dist-info  prompt_toolkit                  pygments                     traitlets-5.0.5.dist-info
backcall-0.2.0.dist-info   ipython-7.19.0.dist-info          parso                    pickleshare.py               prompt_toolkit-3.0.8.dist-info  Pygments-2.7.2.dist-info     wcwidth
decorator-4.4.2.dist-info  ipython_genutils                  parso-0.7.1.dist-info    pip                          ptyprocess                      setuptools                   wcwidth-0.2.5.dist-info
decorator.py               ipython_genutils-0.2.0.dist-info  pexpect                  pip-20.1.1.dist-info         ptyprocess-0.6.0.dist-info      setuptools-47.1.0.dist-info
easy_install.py            jedi                              pexpect-4.8.0.dist-info  pkg_resources                __pycache__                     traitlets
(venv002) [root@host54 test]#


```





- IDE安装及使用  
1）vscode安装及使用  
2）vscode常用插件安装及使用  
远程调试Linux：Remote - SSH  

- 将远程服务器的公钥放到GitHub上  
- 测试拉取/提交代码（正常后进入下面设置）  
- IDE安装远程插件并设置config（添加远程服务器主机信息），通过这里的配置找到远程服务器（connect to host in ）  
- IDE中从pull代码到最后push代码到GitHub仓库中  



- 基本数据类型   
1）列表  
方括号  
2）元组  
括号  
3）字典  
花括号  
4）python编程逻辑  


```

None赋值给变量
In [3]: var001 = None

In [4]: print(var001)
None

In [5]:

In [5]: var001 is None
Out[5]: True


002赋值给变量就不符合语法
In [6]: var002 = 002
  File "<ipython-input-6-2dd6ca7c8644>", line 1
    var002 = 002
               ^
SyntaxError: invalid token


In [7]: var002 = 2

In [8]: print(var002)
2


布尔运算、关系运算符
In [9]: var002 is None
Out[9]: False

In [10]: x=100

In [11]: y=200

In [12]: x == y
Out[12]: False

In [13]: x > y
Out[13]: False

In [14]: x < y
Out[14]: True

In [15]: x != y
Out[15]: True







xx列表
In [16]: xx=['aa','bb','cc']

In [17]: xx
Out[17]: ['aa', 'bb', 'cc']

只接受一个参数，输入两个就会出现如下报错
In [18]: xx.append('dd','ee')
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-18-f7c9f4846b93> in <module>
----> 1 xx.append('dd','ee')

TypeError: append() takes exactly one argument (2 given)

追加一个参数并打印
In [19]: xx.append('dd')

In [20]: xx
Out[20]: ['aa', 'bb', 'cc', 'dd']

In [21]: print(xx)
['aa', 'bb', 'cc', 'dd']


字典
In [27]: dict001 = {'k11':'v11','k22':'v22'}

In [28]: dict001
Out[28]: {'k11': 'v11', 'k22': 'v22'}

查看key对应的value
In [29]: dict001['k11']
Out[29]: 'v11'

In [30]: dict001['k22']
Out[30]: 'v22'

修改key值
In [31]: dict001['k22'] = 'value33'

In [32]: dict001['k22']
Out[32]: 'value33'

In [33]: dict001
Out[33]: {'k11': 'v11', 'k22': 'value33'}

In [34]:






python编程逻辑（python之禅）
In [22]: import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!






```






- 高级数据类型  
collections     容器数据类型  
nametuple()     命名元组  
deque           双端队列  
Counter         计数器  
OrderedDict     有顺序的字典  

- 官方文档  
https://docs.python.org/zh-cn/3.7/



```

引入标准库deque（双端队列）
In [34]: from collections import deque

获取库的帮助
In [35]: help(deque)

创建双端队列atoz
In [36]: atoz = deque('defg')


In [37]: atoz
Out[37]: deque(['d', 'e', 'f', 'g'])

在队列右边侧追加h
In [38]: atoz.append('h')

In [39]: atoz
Out[39]: deque(['d', 'e', 'f', 'g', 'h'])

在队列左边追加c
In [40]: atoz.appendleft('c')

In [41]: atoz
Out[41]: deque(['c', 'd', 'e', 'f', 'g', 'h'])


扩展deque的左侧，通过添加iterable参数中的元素。注意，左添加时，在结果中iterable参数中的顺序将被反过来添加。
In [42]: atoz.extendleft('ab')

In [43]: atoz
Out[43]: deque(['b', 'a', 'c', 'd', 'e', 'f', 'g', 'h'])

for循环打印队列
In [45]: for name in atoz:
    ...:     print(name)
    ...:
b
a
c
d
e
f
g
h

In [46]:


```


- 控制流  
1）while循环（其他编程语言循环形式）  
2）for循环（python风格化中常用循环）  
```


while循环打印列表中元素
In [7]: list002 = ['aa','bb','cc']

In [8]: len(list002)
Out[8]: 3

In [9]: i=0

In [10]: while i < len(list002):
    ...:     print(list002[i])
    ...:     i += 1
    ...:
aa
bb
cc


for循环打印列表中元素
In [4]: list001 = ['aa','bb','cc']

In [5]: list001
Out[5]: ['aa', 'bb', 'cc']

In [6]:

In [6]: for i in list001:
   ...:     print(i)
   ...:
aa
bb
cc

```

- python函数及模块  
1）标准库    
2）第三方库  
3）自定义库  


- python标准库-日期时间处理  
1）time：https://docs.python.org/zh-cn/3.7/library/time.html  
2）datetime：https://docs.python.org/zh-cn/3.7/library/datetime.html  

```

In [1]: import time

In [2]: time.time()
Out[2]: 1606608976.4738708

时间格式
In [5]: time.localtime()
Out[5]: time.struct_time(tm_year=2020, tm_mon=11, tm_mday=29, tm_hour=8, tm_min=16, tm_sec=48, tm_wday=6, tm_yday=334, tm_isdst=0)

时间格式转换
In [6]: time.strftime("%Y-%m-%d %X",time.localtime())
Out[6]: '2020-11-29 08:18:17'

In [7]: time.strptime('2020-11-29 08:18:17',"%Y-%m-%d %X")
Out[7]: time.struct_time(tm_year=2020, tm_mon=11, tm_mday=29, tm_hour=8, tm_min=18, tm_sec=17, tm_wday=6, tm_yday=334, tm_isdst=-1)





In [1]: import datetime

In [2]: from datetime import *

显示当前时间
In [3]: datetime.today()
Out[3]: datetime.datetime(2020, 11, 29, 8, 22, 12, 693556)

In [4]: datetime.now()
Out[4]: datetime.datetime(2020, 11, 29, 8, 22, 18, 278382)


显示前一天时间
In [6]: datetime.today() - timedelta(days=1)
Out[6]: datetime.datetime(2020, 11, 28, 8, 24, 15, 282718)

In [7]: datetime.today() + timedelta(days=-1)
Out[7]: datetime.datetime(2020, 11, 28, 8, 24, 25, 387577)

```




- python标准库-日志处理  

```

In [8]: import logging

打印不同级别日志（默认不打印debug/info级别日志，需要修改日志参数）
In [10]: logging.debug('debug message')
    ...: logging.info('info message')
    ...: logging.warning('warning message')
    ...: logging.error('error message')
    ...: logging.critical('critical message')
    ...:
WARNING:root:warning message
ERROR:root:error message
CRITICAL:root:critical message


使用basicConfig函数将日志写入指定文件中（如：test.log）
In [2]: logging.basicConfig(filename='test.log')

In [3]: logging.debug('debug message')
   ...: logging.info('info message')
   ...: logging.warning('warning message')
   ...: logging.error('error message')
   ...: logging.critical('critical message')
   ...:

In [4]: exit()
[root@host54 test]# ll
total 8
-rw-r--r-- 1 root root 221 Nov 27 21:44 requirements.txt
-rw-r--r-- 1 root root  85 Nov 29 08:55 test.log
drwxr-xr-x 6 root root  87 Nov 27 21:18 venv001
drwxr-xr-x 6 root root  87 Nov 27 21:46 venv002
test.log日志文件中已经成功插入内容
[root@host54 test]# cat test.log
WARNING:root:warning message
ERROR:root:error message
CRITICAL:root:critical message
[root@host54 test]#





日志文件
打印的日志级别起始从DEBUG开始
时间戳
日志格式（时间戳、当前登录用户、日志级别、行号、对应级别打印的日志内容）
In [2]: logging.basicConfig(filename='test.log',
   ...:                     level=logging.DEBUG,
   ...:                     datefmt='%Y-%m-%d %H:%M:%S',
   ...:                     format='%(asctime)s %(name)-8s %(levelname)-8s [line: %(lineno)d] %(message)s'
   ...:                     )

In [3]: logging.debug('debug message')
   ...: logging.info('info message')
   ...: logging.warning('warning message')
   ...: logging.error('error message')
   ...: logging.critical('critical message')

In [4]:

In [4]: exit()
[root@host54 test]# ll
total 8
-rw-r--r-- 1 root root 221 Nov 27 21:44 requirements.txt
-rw-r--r-- 1 root root 399 Nov 29 09:09 test.log
drwxr-xr-x 6 root root  87 Nov 27 21:18 venv001
drwxr-xr-x 6 root root  87 Nov 27 21:46 venv002

再次查看日志（日志默认是追加模式，不会覆盖之前的日志）
内容及格式都发生了变化（时间戳、当前登录用户、日志级别、行号、对应级别打印的日志内容）
[root@host54 test]# cat test.log
WARNING:root:warning message
ERROR:root:error message
CRITICAL:root:critical message
2020-11-29 09:09:56 root     DEBUG    [line: 1] debug message
2020-11-29 09:09:56 root     INFO     [line: 2] info message
2020-11-29 09:09:56 root     WARNING  [line: 3] warning message
2020-11-29 09:09:56 root     ERROR    [line: 4] error message
2020-11-29 09:09:56 root     CRITICAL [line: 5] critical message
[root@host54 test]#



```




- python标准库-路径处理  

```
In [1]: from random import *

随机数：返回0.0 - 1.0之间的浮点数
In [2]: random()
Out[2]: 0.144908510413575

随机打印数字：从0-100，步长为2(偶数)
In [9]: randrange(0,101,2)
Out[9]: 0

In [10]: randrange(0,101,2)
Out[10]: 76

In [11]: randrange(0,101,2)
Out[11]: 78

In [12]: randrange(0,101,2)
Out[12]: 42

In [13]: randrange(0,101,2)
Out[13]: 40

In [14]: randrange(0,101,2)
Out[14]: 74

In [15]:


随机抽取列表中的单个元素
In [15]: choice(['aa','bb','cc'])
Out[15]: 'bb'

In [16]: choice(['aa','bb','cc'])
Out[16]: 'aa'

In [17]: choice(['aa','bb','cc'])
Out[17]: 'aa'

In [18]: choice(['aa','bb','cc'])
Out[18]: 'bb'

In [19]: choice(['aa','bb','cc'])
Out[19]: 'cc'

In [20]:


随机抽取列表中多个元素
In [20]: sample([1,2,3,4,5,6,7,8], k=4)
Out[20]: [8, 4, 2, 3]

In [21]: sample([1,2,3,4,5,6,7,8], k=4)
Out[21]: [8, 5, 2, 3]

In [22]: sample([1,2,3,4,5,6,7,8], k=4)
Out[22]: [2, 4, 6, 8]

In [23]: sample([1,2,3,4,5,6,7,8], k=4)
Out[23]: [6, 2, 4, 1]

In [24]:





# os模块


In [1]: from pathlib import  *

In [2]: p = Path()

In [3]: p.resolve()
Out[3]: PosixPath('/opt/test')



# Path函数：显示变量中的路径

# /opt/gaorui/test.py路径真实存在
In [4]: path='/opt/gaorui/test.py'

In [5]: p = Path(path)

In [6]: p
Out[6]: PosixPath('/opt/gaorui/test.py')

# /opt/gaorui/test.tar.gz文件及其路径不存在
In [7]: path='/opt/gaorui/test.tar.gz'

In [8]: p = Path(path)

In [9]: p
Out[9]: PosixPath('/opt/gaorui/test.tar.gz')

# 显示文件全名
In [10]: p.name
Out[10]: 'test.tar.gz'

# stem：显示文件名（去掉后缀）
In [11]: p.stem
Out[11]: 'test.tar'

# suffix：显示文件的最后一个后缀
In [12]: p.suffix
Out[12]: '.gz'

# suffixes：显示文件的所有后缀
In [13]: p.suffixes
Out[13]: ['.tar', '.gz']

# parent：显示p中目录部分
In [14]: p.parent
Out[14]: PosixPath('/opt/gaorui')

# parents：使用for循环遍历，递归出所有目录
In [15]: p.parents
Out[15]: <PosixPath.parents>

In [16]: for i in p.parents:
    ...:     print(i)
    ...:
/opt/gaorui
/opt
/

将p中的值以元组的方式打印
In [17]: p.parts
Out[17]: ('/', 'opt', 'gaorui', 'test.tar.gz')

In [18]:






In [18]: import os

打印文件所在绝对路径
In [19]: os.path.abspath('test.log')
Out[19]: '/opt/test/test.log'

将绝对路径赋值给path变量
In [20]: path='/opt/gaorui/test.py'

In [21]: p = Path(path)

In [22]: p
Out[22]: PosixPath('/opt/gaorui/test.py')

In [23]: os.path.basename(p)
Out[23]: 'test.py'

In [24]: os.path.dirname(p)
Out[24]: '/opt/gaorui'

确认文件所在路径是否真实存在
不存在返回False
In [25]: os.path.exists('/opt/gaorui/test.py')
Out[25]: False
存在返回True
In [26]: os.path.exists('/opt/test/test.log')
Out[26]: True
确认是否为文件
In [27]: os.path.isfile('/opt/test/test.log')
Out[27]: True
确认是否为目录
In [28]: os.path.isdir('/opt/test/test.log')
Out[28]: False
In [29]: os.path.isdir('/opt/test/')
Out[29]: True
目录拼接（相对路径/绝对路径）
In [30]: os.path.join('dir01','dir02')
Out[30]: 'dir01/dir02'
In [31]: os.path.join('/dir01','dir02')
Out[31]: '/dir01/dir02'




```








- python标准库-手动实现daemon守护进程  
1）跑在后台的守护进程  
2）类似Windows中的服务  
3）参考daemon进程的标准库（对于初学者不要自己去想象怎么实现，避免走弯路）  
https://www.python.org/dev/peps/pep-3143/  
https://www.jianshu.com/p/fbe51e1147af  
https://www.jianshu.com/p/2342a9299ee0  
https://stackoverflow.com/questions/473620/how-do-you-create-a-daemon-in-python   




```
//课程案例


#!/usr/bin/env python

#sys:标准的输入输出、错误输出
#os:创建子进程
#time:时间戳
import sys
import os
import time

#整个程序功能说明（）
'''
手动编写一个daemon进程
'''


#stdin：标准输入
#stdout标准输出
#stderror错误输出
def daemonize(stdin="/dev/null", stdout="/dev/null", stderror="/dev/null"):
    try:
        #创建子进程
        pid = os.fork()

        if pid > 0:
            
            #父进程先于子进程exit,会使子进程变为孤儿进程
            #这样子进程成功被init这个用户级守护进程收养（init是一号进程）
            #返回值是“0”为正常退出
            sys.exit(0)
    
    #捕获异常（创建子进程失败的话）
    except OSError as err:
        sys.stderr.write(f"_Fork #1 Failed: {0} \n")
        #如果程序执行返回值为非0就是异常（程序运行遇到的问题）
        sys.exit(1)
    
    # 从父进程环境脱离
    # decouple from parenet enviroment
    # chdir确认进程不占用任何目录，否则不能umount
    os.chdir("/")
    # 调用umask(0) 拥有写任何程序的权限，避免导致继承自父进程的umask被修改而导致自身权限不足
    os.umask(0)
    # setsid 被调用成功后，进程会成为新的会话租组长，与原来的对话和进程组脱离
    os.setsid()

    # 重定向标准文件描述符
    sys.stdout.flush()
    sys.stderr.flush()

    si = open(stdin, "r")
    so = open(stdout, "a+")
    se = open(stderror, "w")

    
    # dup2函数原子化关闭和复制文件描述符
    os.dup2(si.fileno(), sys.stdin.fileno())
    os.dup2(so.fileno(), sys.stdout.fileno())
    os.dup2(se.fileno(), sys.stderr.fileno())


#每秒显示一个时间戳，daemon后台运行时会一直打印日志
def test():
    sys.stdout.write('Daemon started with pid %d\n' % os.getpid())
    while True:
        now = time.strftime("%X", time.localtime())
        sys.stdout.write(f'{time.ctime()}\n')
        # 清空缓存
        sys.stdout.flush()
        # 每隔1秒
        time.sleep(1)



#标准输出改成文件d1.log，一般不会在此处指定标准输出的日志文件，会在其他地方定义日志输出（如可以在本例中的"test()"函数中定义）
if __name__ == "__main__":
    
    # 标准输出会追加打印到“d1.log”中
    daemonize('/dev/null', 'd1.log', '/dev/null')
    test()





```


- 正则表达式  
1）通读官方文档  
https://docs.python.org/zh-cn/3.7/library/re.html  



```





```















还未更新完，待续。。。。。  

