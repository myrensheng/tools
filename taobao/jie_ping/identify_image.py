from PIL import Image
from aip import AipOcr
from io import BytesIO


class IdentifyImage:
    """
    通过userid找到图片，切割指定的位置，识别图片中的数字
    """
    # 百度api的调用参数
    __APP_ID = '15995895'
    __API_KEY = "MnsAVWCtPUIdHPIhcjLnHSlu"
    __SECRET_KEY = "G2MsM6Udu7RewFXnlaqxanS1GoTiXbjP"
    # 图片文件路径
    __BASE_PATH = r"D:\project\spiderProject\taobao\jie_ping\pictures"

    def __init__(self):
        self.client = AipOcr(self.__APP_ID, self.__API_KEY, self.__SECRET_KEY)

    def get_image_content(self, user_id):
        """
         通过user_id获取到用户支付宝信息
        :param user_id:用户id
        :return:用户支付宝上的文字信息
        """
        results = {}
        full_path = self.__BASE_PATH + "\\" + str(user_id)
        img = Image.open(full_path + r"\zhifubao.png")
        yu_e = img.crop((360, 525, 440, 560))  # 截取余额位置
        results["balance"] = self.image_2_content(yu_e)[0]["words"].split("元")[0]
        yu_e_bao = img.crop((370, 690, 450, 720))  # 余额宝位置
        results["yue_e_bao"] = self.image_2_content(yu_e_bao)[0]["words"].split("元")[0]
        hua_bei = img.crop((1080, 520, 1230, 620))  # 花呗位置
        hua_bei_info = self.image_2_content(hua_bei)
        total_profit = img.crop((720, 700, 770, 715))  # 累计收益位置
        results["total_profit"] = self.image_2_content(total_profit)[0]["words"]
        # 花呗剩余额度
        results["hua_bei_creditamount"] = hua_bei_info[1]["words"].split("元")[0]
        # 花呗额度
        hua_bei_totalcrediamount = hua_bei_info[2]["words"].split("元")[0].split(":")[-1]
        results["hua_bei_totalcreditamount"] = hua_bei_totalcrediamount
        return results

    def image_2_content(self, image):
        """
        将图片对象转为字节对象，方便百度API调用
        :param image: 图片对象
        :return: 图片上的文字
        """
        output_buffer = BytesIO()  # 初始化一个字节流对象
        image.save(output_buffer, format='JPEG')  # 其他格式不行
        byte_data = output_buffer.getvalue()  # 得到字节数据
        # 调用百度API，获取图片文字
        result = self.client.basicGeneral(byte_data)
        return result['words_result']


if __name__ == '__main__':
    ii = IdentifyImage()
    print(ii.get_image_content(18309169600))
