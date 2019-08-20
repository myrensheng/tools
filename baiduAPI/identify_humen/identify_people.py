# 通用图像分析——通用物体和场景识别高级版
import requests
from aip import AipImageClassify

appID = "16322459"
APIKey = "azFqdo7taHaeFBsY2vGyQHUR"
SecretKey = "sifO8kCVhIVlw1YvM7aMvNG2kB6ajUj6"

client = AipImageClassify(appID,APIKey,SecretKey)


def get_file_content(file_path):
    with open(file_path,"rb") as f:
        return f.read()


image_path = r"D:\project\myProject\baiduAPI\identify_humen\images\324152.jpg"
image = get_file_content(image_path)

# 可选参数
options = {}
options["baike_num"] = 5
# 调用通用物体识别
res = client.advancedGeneral(image,options)
print(res)


