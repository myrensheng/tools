#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/5 9:19
# @Author  : 郑帅
# @File    : learn_threading.py
# @Software: win10  python3.6.7

import threading
from time import ctime,sleep
"""
线程：操作系统能够调度的最小单元
学习python中的多线程:
1、适用于io操作密集的情况：比如查询数据库、读写文件等
2、不适用于大量计算的情况。（多进程处理）
简单的使用方法：
1、导入threading模块
2、创建进程组和进程对象
3、进程对象中传入target和args
4、start和join启动进程
中级的使用方法：
如果多个线程要操作同一对象，先创建一个threadLock=threading.Lock()对象
然后在该对象的前加上threadLock.acquire()
在该对象后面加上threadLock.release()
高级点的使用方法：
线程间同步数据，使用队列进行数据的传递，创建队列对象work_queue=queue.Queue(10)
填充数据：work_queue.put(data)，获取数据：work_queue.get(data)
判断队列是否为空：work_queue.empty()
"""
def music(name,loop):
    for i in range(loop):
        print("I was listing to %s.%s"%(name,ctime()))
        sleep(1)


def movie(name,loop):
    for i in range(loop):
        print("I was watching %s.%s"%(name,ctime()))
        sleep(2)


# 创建线程组
threads = []
# 创建线程对象，并加入线程组中
t1 = threading.Thread(target=music,args=("失眠飞行",2))
threads.append(t1)
t2 = threading.Thread(target=movie,args=("哪吒",3))
threads.append(t2)
if __name__ == '__main__':
    # 启动线程
    for t in threads:
        t.start()
    for t in threads:
        # 使用join，等待子线程全部结束后，主线程在结束
        t.join()
    print("all over %s"%ctime())




