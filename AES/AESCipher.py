# coding=utf-8
import base64
import binascii
import gzip
import json
from Crypto.Cipher import AES
import random


KEY = "C8203D38A63070188EE3DC62C9919744"


def pkcs7padding(text):
    """
    明文使用PKCS7填充
    最终调用AES加密方法时，传入的是一个byte数组，要求是16的整数倍，因此需要对明文进行处理
    :param text: 待加密内容(明文)
    :return:
    """
    bs = AES.block_size  # 16
    length = len(text)
    bytes_length = len(bytes(text, encoding='utf-8'))
    # tips：utf-8编码时，英文占1个byte，而中文占3个byte
    padding_size = length if(bytes_length == length) else bytes_length
    padding = bs - padding_size % bs
    # tips：chr(padding)看与其它语言的约定，有的会使用'\0'
    padding_text = chr(padding) * padding
    return text + padding_text


def pkcs7unpadding(text):
    """
    处理使用PKCS7填充过的数据
    :param text: 解密后的字符串
    :return:
    """
    length = len(text)
    unpadding = ord(text[length-1])
    return text[0:length-unpadding]


def encrypt(content):
    KEY_bytes = bytes(KEY,encoding="utf-8")
    vi = b"\0"
    cipher = AES.new(KEY_bytes, AES.MODE_CBC,vi*16)
    # 处理明文
    content_padding = pkcs7padding(content)
    # 加密
    encrypt_bytes = cipher.encrypt(content_padding)
    # print(encrypt_bytes)
    # 二进制处理成16进制
    binascii_text = binascii.b2a_hex(encrypt_bytes)
    # print("密文:",str(binascii_text,'utf-8').upper())
    #
    # gzip压缩
    compress_bytes = gzip.compress(binascii_text)
    # # base64重新编码
    result = base64.b64encode(compress_bytes)
    return str(result,"utf-8")
    # return (binascii_text,result)


def decrypt(content):
    KEY_bytes = bytes(KEY, encoding='utf-8')
    # iv = KEY_bytes
    iv = b'\0'
    cipher = AES.new(KEY_bytes, AES.MODE_CBC, iv*16)
    # base64解码
    encrypt_bytes = base64.b64decode(content)
    # gzip解压
    decompress_data = gzip.decompress(encrypt_bytes)
    decompress_data = decompress_data.decode('utf-8')
    # 解密
    decrypt_bytes = cipher.decrypt(decompress_data)
    # 重新编码
    result = str(decrypt_bytes)
    # 去除填充内容
    result = pkcs7unpadding(result)
    return result


def get_KEY(n):
    """
    获取密钥 n 密钥长度
    :return:
    """
    c_length = int(n)
    source = 'ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz12345678'
    length = len(source) - 1
    result = ''
    for i in range(c_length):
        result += source[random.randint(0, length)]
    return result


if __name__ == '__main__':
    with open("test.json",'r',encoding="utf-8") as f:
        string = str(json.load(f))
        print(encrypt(string))




