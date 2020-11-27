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



还未更新完，待续。。。。。  

