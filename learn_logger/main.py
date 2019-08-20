#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/20 12:00
# @Author  : 郑帅
# @File    : main.py
# @Software: win10  python3.6.7
import traceback

from learn_logger.logger_fun import log
from test2 import Test2
from test3 import Test3



if __name__ == '__main__':
    log("运行第二个文件的start行数")
    try:
        t2 = Test2()
        t2.strat()
    except:
        log("账号"+traceback.format_exc(),file_name="traceback")
    finally:
        log("运行第三个文件的start行数")
        t3 = Test3()
        t3.strat()
    pass