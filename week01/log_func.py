#!/usr/bin/env python


import os
import sys
import logging
import time
import pathlib



def log_func():
    today = time.strftime("%Y-%m-%d", time.localtime())
    
    #文件路径
    dirPath = '/var/log/python-' + today
    logfile = "log_func.log"
    
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
    
    #log_func函数被调用时
    #现在/var/log路径下创建python-2020-11-29目录(命名python-系统当前日期)
    #日志文件名：log_func.log
    logging.info('The log_func function is called')

    #终端的标准输出显示log_func函数被调用时的进程pid
    sys.stdout.write('log_func function is called [ PID : %d ]\n' % os.getpid())
    #清理缓存
    sys.stdout.flush()
