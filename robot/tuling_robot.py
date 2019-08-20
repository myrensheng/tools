import json
import requests


class TuLing:
    KEY = "e888f3db9409463fabe1eac894504cbe"
    URL = "http://openapi.tuling123.com/openapi/api/v2"

    def __init__(self, info):
        self.info = info

    def get_repeat(self):
        data = {
            "reqType": 0,
            "perception": {
                "inputText": {
                    "text": self.info
                },
            },
            "userInfo": {
                "apiKey": self.KEY,
                "userId": "zhengshuai",
            }
        }
        query = json.dumps(data)
        r = requests.post(url=self.URL, data=query)
        content = json.loads(r.text)["results"][0]["values"]["text"]
        return content


if __name__ == '__main__':
    msg = u"你好"
    TL = TuLing(msg)
    print(TL.get_repeat())
