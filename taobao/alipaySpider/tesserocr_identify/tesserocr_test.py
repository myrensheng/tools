from PIL import Image
import tesserocr
import pytesseract

# 测试tesserocr能否使用
# image = Image.open(r'D:\PycharmProjects\taobao\jie_ping\pictures\18309169600\hua_bei.jpg')
image = Image.open(r"D:\PycharmProjects\taobao\alipaySpider\baiduAIP\test.png")
# image = image.convert('L')
# threshold = 127
# table = []
# for i in range(256):
#     if i < threshold:
#         table.append(0)
#     else:
#         table.append(1)
# image = image.point(table, '1')
# result = tesserocr.image_to_text(image)
result = pytesseract.image_to_string(image)
print(result)
# print(tesserocr.tesseract_version())
