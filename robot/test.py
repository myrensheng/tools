import json

import requests
import itchat  # 这是一个用于微信回复的库

# KEY = '8edce3ce905a4c1dbb965e6b35c3834d'  # 这个key可以直接拿来用
KEY = "e888f3db9409463fabe1eac894504cbe"


# 向api发送请求

def get_response(msg):
    api = 'http://openapi.tuling123.com/openapi/api/v2'
    dat = {
        "perception": {
            "inputText": {
                "text": msg
            },
            "inputImage": {
                "url": "imageUrl"
            },
            "selfInfo": {
                "location": {
                    "city": "北京",
                    "province": "北京",
                    "street": "信息路"
                }
            }
        },
        "userInfo": {
            "apiKey": KEY,
            "userId": "123456"
        }
    }
    dat = json.dumps(dat)
    r = requests.post(api, data=dat).json()
    print(r)

get_response("你好")

