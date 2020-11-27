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


- IDE安装及使用  
1）vscode安装及使用  
2）vscode常用插件安装及使用  
远程调试Linux：Remote - SSH  

- 将远程服务器的公钥放到GitHub上  
- 测试拉取/提交代码（正常后进入下面设置）  
- IDE安装远程插件并设置config（添加远程服务器主机信息），通过这里的配置找到远程服务器（connect to host in ）  
- IDE中从pull代码到最后push代码到GitHub仓库中  


  
还未更新完，待续。。。。。  

