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
    logging.info('The log_func function is called .')
    #获取当前进程pid
    sys.stdout.write('Daemon started [ PID : %d ]\n' % os.getpid())

    
if __name__ == '__main__':
    log_func()



