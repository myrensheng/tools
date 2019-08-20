from aip import AipOcr

APP_ID = '15995895'
API_KEY = "MnsAVWCtPUIdHPIhcjLnHSlu"
SECRET_KEY = "G2MsM6Udu7RewFXnlaqxanS1GoTiXbjP"
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


file_path = r"D:\PycharmProjects\taobao\jie_ping\pictures\18309169600\hua_bei.jpg"
image = get_file_content(file_path)
""" 调用通用文字识别, 图片参数为本地图片 """
result = client.basicGeneral(image)
# str1 = ""
# for i in result["words_result"]:
#     str1 += i["words"]
# print(str1)
print(result)
