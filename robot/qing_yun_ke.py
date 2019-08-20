#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/6 17:35
# @Author  : 郑帅
# @File    : qing_yun_ke.py
# @Software: win10  python3.6.7
import requests

url = "http://api.qingyunke.com/api.php"
params = {
    "key":"free",
    "appid":"0",
    "msg":"你是谁"
}
res = requests.get(url,params)
res.encoding = "utf-8"
res_dict = eval(res.text)
print(res_dict["content"])