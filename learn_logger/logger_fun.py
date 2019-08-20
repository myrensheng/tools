#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/25 18:04
# @Author  : 郑帅
# @File    : test1.py
# @Software: win10  python3.6.7
import datetime
import logging.handlers
import os


def log(msg,file_name="run_file"):
    """
    创建一个日志对象
    """
    # 输出日志的格式
    file_time = datetime.datetime.now().strftime("_%Y_%m_%d")
    log_formatter = logging.Formatter(
        '%(asctime)s [%(filename)s %(funcName)s:%(lineno)d] %(thread)d %(levelname)s %(message)s')
    log_file = os.path.join(os.getcwd()+"\\logs", file_name+file_time+".log")
    my_handler = logging.handlers.RotatingFileHandler(
        log_file, mode='a',
        maxBytes=100 * 1024 * 1024,
        backupCount=4,
        encoding="utf-8",
        delay=0
    )

    my_handler.setFormatter(log_formatter)
    my_handler.setLevel(logging.DEBUG)

    logger = logging.getLogger('root')
    logger.setLevel(logging.DEBUG)
    logger.addHandler(my_handler)

    # logger.debug out log to the console
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    logger.addHandler(ch)
    logger.debug(msg)
    # 移除处理器
    logger.removeHandler(my_handler)
    logger.removeHandler(ch)




