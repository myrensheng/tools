# 截取屏幕指定位置
import os

from PIL import ImageGrab

# 以用户id创建文件夹，保存图片
base_path = "../jie_ping/pictures/"
user_id = '1458010081'  # 变量，用作文件夹的命名
full_path = base_path + user_id
# 路径不存在就自动创建
if not os.path.exists(full_path):
    os.makedirs(full_path)

# 账户余额位置(200,390,270,450),(200, 390, 270, 450)
yu_e = ImageGrab.grab((360, 525, 440, 560))
yu_e.save(full_path + "/yue_e.jpg")
# 余额宝位置(200,520,260,580),(200, 550, 260, 580)
yu_e_bao = ImageGrab.grab((370, 690, 450, 720))
yu_e_bao.save(full_path + "/yue_e_bao.jpg")
# 花呗位置(780,420,900,500),(780, 440, 850, 470)
hua_bei = ImageGrab.grab((1080, 520, 1230, 620))
hua_bei.save(full_path + "/hua_bei.jpg")
