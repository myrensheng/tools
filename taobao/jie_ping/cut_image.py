# 截取指定图片的指定位置
from PIL import Image

import os
# 以用户id创建文件夹，保存图片
base_path = "../jie_ping/pictures/"
user_id = '1458010081'  # 变量，用作文件夹的命名
full_path = base_path + user_id
# 路径不存在就自动创建
if not os.path.exists(full_path):
    os.makedirs(full_path)

img_path = full_path+"/"+"zhifubao.png"
img = Image.open(img_path)
# print(img.size)
yu_e = img.crop((360, 525, 440, 560))
yu_e.save(full_path + "/yue_e.jpg")
# 余额宝位置
yu_e_bao = img.crop((370, 690, 450, 720))
yu_e_bao.save(full_path + "/yue_e_bao.jpg")
# 花呗位置
hua_bei = img.crop((1080, 520, 1230, 620))
hua_bei.save(full_path + "/hua_bei.jpg")