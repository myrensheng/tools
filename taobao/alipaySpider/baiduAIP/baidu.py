from aip import AipOcr


class BaiDu(object):
    """
    调用百度接口，识别图片
    传入图片地址，返回图片内容
    """
    __APP_ID = '15995895'
    __API_KEY = "MnsAVWCtPUIdHPIhcjLnHSlu"
    __SECRET_KEY = "G2MsM6Udu7RewFXnlaqxanS1GoTiXbjP"

    def __init__(self):
        self.client = AipOcr(self.__APP_ID, self.__API_KEY, self.__SECRET_KEY)

    def get_file_content(self, file_path):
        with open(file_path, 'rb') as fp:
            image = fp.read()
            result = self.client.basicGeneral(image)
            # return self.get_words(result)
            return result["words_result"]

    @staticmethod
    def get_words(result_list):
        words = ""
        for i in result_list:
            words += i["words"]
        return words


if __name__ == '__main__':
    baidu = BaiDu()
    pic_list = [r"\hua_bei.jpg", r"\yue_e.jpg", r"\yue_e_bao.jpg"]
    base_path = r"D:\project\spiderProject\taobao\jie_ping\pictures"
    user_id = "18309169600"
    for pic in pic_list:
        # 循环识别图片
        file_path = base_path + r"\\" + user_id + pic
        # words_result列表形式，如：[{'words': '余额宝'}, {'words': '0.00元'}]
        words_result = baidu.get_file_content(file_path)
        print(words_result)
