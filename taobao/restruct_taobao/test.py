# class Login():
#     def __init__(self):
#         self.name = "zs"
#
#
#class Userinfos(Login):
#     useronfo = {}
#     def __init__(self):
#         Login.__init__(self)
#         self.parse()
#     def parse(self):
#         self.useronfo["sex"]="man"
#
#
# a = Login()
# print(a.name)
#
# b = Userinfos()
# print(b.useronfo)
# from dateutil.parser import parse
# import datetime
# now_time = datetime.datetime.now()
# trade_time = parse('2019-2-18')
# print(now_time)
# print(trade_time)
# print((now_time-trade_time).days)

# str1 = '//store.taobao.com/shop/view_shop.htm?user_number_id=1954228235'
# print(str1.split("=")[-1])

# trade_status_dict = {'等待买家付款': 'WAIT_BUYER_PAY',
#                      '等待卖家发货': 'WAIT_SELLER_SEND_GOODS',
#                      '卖家部分发货': 'SELLER_CONSIGNED_PART',
#                      '等待买家确认收货': 'WAIT_BUYER_CONFIRM_GOODS',
#                      '交易成功': 'TRADE_FINISHED',
#                      '交易关闭': 'TRADE_CLOSED',
#                      '交易被淘宝关闭': 'TRADE_CLOSE_BY_TAOBAO',
#                      '没有创建外部交易（支付宝交易）': 'TRADE_NO_CREATE_PAY',
#                      '外卡支付付款确认中': 'PAY_PENDING',
#                      }
# print(trade_status_dict.get("交易成功"))

# from restruct_taobao.parse_order import *
# dict1 = {'0': 'https://buyertrade.taobao.com/trade/detail/trade_item_detail.htm?bizOrderId=272628102681755198', '1': 'https://buyertrade.taobao.com/trade/detail/trade_item_detail.htm?bizOrderId=272021286272755198', '2': 'https://buyertrade.taobao.com/trade/detail/trade_item_detail.htm?bizOrderId=270251204714755198', '3': 'https://trade.tmall.com/detail/orderDetail.htm?bizOrderId=269636709380755198', '4': 'https://trade.tmall.com/detail/orderDetail.htm?bizOrderId=269837382169755198', '5': 'https://buyertrade.taobao.com/trade/detail/trade_item_detail.htm?bizOrderId=267102950091755198', '6': 'https://buyertrade.taobao.com/trade/detail/trade_item_detail.htm?bizOrderId=265543012205755198', '7': 'https://buyertrade.taobao.com/trade/detail/trade_item_detail.htm?bizOrderId=264630119256755198', '8': 'https://buyertrade.taobao.com/trade/detail/trade_item_detail.htm?bizOrderId=264087975412755198', '9': 'https://buyertrade.taobao.com/trade/detail/trade_item_detail.htm?bizOrderId=263970599442755198', '10': 'https://buyertrade.taobao.com/trade/detail/trade_item_detail.htm?bizOrderId=262827973347755198', '11': 'https://buyertrade.taobao.com/trade/detail/trade_item_detail.htm?bizOrderId=262464549113755198', '12': 'https://buyertrade.taobao.com/trade/detail/trade_item_detail.htm?bizOrderId=259738628118755198', '13': 'https://train.trip.taobao.com/orderDetail.htm?mainBizOrderId=259559206842755198'}
# parse_method = {
#     '//buyertrad':parse_buytertrade,
#     '//trade':parse_tradetmall,
#     '//train':parse_traintrip,
#     '//tradearchive':parse_tradearchive,
#     '//diannying':parse_dianying,
# }
# for k,v in dict1.items():
#     startwith = v.split(':')[-1].split('.')[0]
#     fun = parse_method.get(startwith, False)
#     if fun:
#         print(fun("hello"))
#     else:
#         print("没有对应的函数")
    # print(startwith,parse_method.get(startwith,"error"))

# text = '郑帅，18309169600 '
# print(text.split('，')[0])
# print(text.split('，')[-1])

# text = '郑帅\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t 18309169600 \t\t\t\t\t\t000000\t\t\t\t\t\t\t\t\t'
# print(text.split(' ')[0].strip(),text.split(' ')[1].strip(),text.split(' ')[-1].strip())

# text = '郑帅,86-18309169600,浙江省 杭州市 西湖区 文新街道 紫荆花路188号骆家庄西苑1区 ,310012'
# deliver_name = text.split(',')[0]
# deliver_mobilephone = text.split(',')[1]
# province = text.split(',')[2].split('省')[0]
# city = text.split(',')[2].split(' ')[1].rstrip('市')
# deliver_address = text.split(',')[2].strip()
# deliver_postcode = text.split(',')[3]
# print(deliver_name)
# print(deliver_mobilephone)
# print(province)
# print(city)
# print(deliver_address)
# print(deliver_postcode)

# text = '郑帅\n\t\t\t\t\t\t\t\t\t\t\t，18309169600\t\t\t\t\t\t，\t\t\t\t\t\t，陕西省 西安市 雁塔区 西高新团结南路南窑头社区西区92排9号楼 \t\t\t\t\t\t，000000\t\t\t\t\t\t\t\t\t'
# deliver_name = text.split('，')[0].strip()
# province = text.split('，')[3].split('省')[0]
# city = text.split('，')[3].split(' ')[1].rstrip('市')
# code = text.split('，')[4]
# print(deliver_name)
# print(province,city,code)

# import os
# import sys
#
# # curPath = os.path.abspath(os.path.dirname(__file__))
# # rootPath = os.path.split(curPath)[0]
# # sys.path.append(rootPath)
# python_path = 'D:/Spiderenv/Scripts/python.exe'
# file_path = 'D:/PycharmProjects/taobao/restruct_taobao/userinfos.py'
# log_txt = 'log.txt'
# execute_str = python_path+" "+file_path
# os.system(execute_str)

class Test():
    def __init__(self):
        self.userinfos = {}
        self.test()

    def test(self):
        self.userinfos['name'] = 'zs'

t = Test()
print(t.userinfos)













