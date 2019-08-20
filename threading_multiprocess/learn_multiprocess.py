#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/5 16:02
# @Author  : 郑帅
# @File    : learn_multiprocess.py
# @Software: win10  python3.6.7
from multiprocessing import Pool
import os, time, random

"""
进程：
简单的多进程：
1、from multiprocessing import Pool 导入进程池
2、创建进程池对象：p=Pool(4)
3、for 循环开启线程：p.apply_async(func=函数名,args=(元组数据，))
4、p.close()关闭进程池
5、p.join()主进程等待子进程完成后关闭
父进程中的各个子进程之间的通信：
from multiprocessinng import Process,Queue
父进程创建q=Queue()对象，子进程中使用q.put()设置值，q.get()获取值
"""


def long_time_task(name):
    print("Run task %s (%s)..." % (name, os.getpid()))
    start = time.time()
    time.sleep(random.randint(3, 6))
    end = time.time()
    print("Task %s runs %0.2f seconds." % (name, (end - start)))


if __name__ == '__main__':
    print("Parent process %s." % os.getpid())
    p = Pool(4)
    i = 2
    for _ in range(5):
        p.apply_async(func=long_time_task, args=(i,))
        print("Waiting for all subprocesses done...")
    p.close()
    p.join()
    print("All subprocesses done.")
