import requests
from wxpy import Bot

def chat_with_friend():
    # 初始化机器人，扫码登录
    bot = Bot(cache_path=True)
    while True:
        friend_name = input("输入你给微信好友的备注：")
        friend_list = bot.friends().search(friend_name)  # 朋友列表
        if not friend_list:  # 没有找到朋友信息
            print("我找不到"+friend_name+">_<")
        else:
            # global friend_name
            first_say = input("发一句话给" + friend_name + ":")
            # 找朋友聊天
            my_friend = friend_list[0]
            # 给朋友发消息
            my_friend.send(first_say)
            # 回复朋友的消息
            @bot.register(my_friend)
            def reply_my_friend(msg):
                print(msg)
                res = reply_msg(msg)
                print(res)
                return res
            bot.join()


def reply_msg(msg):
    url = "http://api.qingyunke.com/api.php"
    params = {
        "key": "free",
        "appid": "0",
        "msg": msg
    }
    res = requests.get(url, params)
    res.encoding = "utf-8"
    res_dict = eval(res.text)
    return res_dict["content"]


if __name__ == '__main__':
    chat_with_friend()
