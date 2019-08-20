# coding: utf-8
import base64

import requests

host = "http://apigateway.jianjiaoshuju.com"
path = "/api/v_1/yzm.html"
appcode = "F50FCE4FB6561AAA67175E409403CCF3"
appkey = "AKIDca12Kxo5274w7BqU736fOufN0bi3YdB3sZ6j"
appsecret = "1t4u62qJ9824syt4adjx8re8v6qm8khxwcrtrc5x"
# image_path = "./zhifubao.png"
v_pic = "data:image/png;base64," + base64.b64encode(open("verificationCode.jpg", 'rb').read()).decode()
data = {
    "v_pic": v_pic,
    "v_type": "ne4",
}
headers = {
    'appcode': appcode,
    'appKey': appkey,
    'appSecret': appsecret,
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
}

result = requests.post(host + path, headers=headers, data=data)
result.encoding = 'utf-8'
print(result.text)
