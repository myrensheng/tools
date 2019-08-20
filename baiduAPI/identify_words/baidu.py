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
        # 从图片文件中读取文字
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
    filePath = r"D:\project\myProject\baiduAPI\identify_words\pictures\md5.jpg"
    result = baidu.get_file_content(filePath)
    print(baidu.get_words(result))
