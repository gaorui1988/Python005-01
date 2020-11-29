#!/usr/bin/env python


import os
import sys
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
    sys.stdout.write('Daemon started with pid %d\n' % os.getpid())
    while True:
        now = time.strftime("%X", time.localtime())
        sys.stdout.write(f'{time.ctime()}\n')
        # 清空缓存
        sys.stdout.flush()
        # 每隔1秒
        time.sleep(1)

    
if __name__ == '__main__':
    log_func()