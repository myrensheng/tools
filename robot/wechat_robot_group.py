from wxpy import *

KEY = '8edce3ce905a4c1dbb965e6b35c3834d'
# 初始化机器人，扫码登录
bot = Bot()

group = bot.groups().search("集贤舍")[0]
# 给群发消息
group.send('大家好，我是机器人？这里有人吗？')
# 回复朋友的消息
@bot.register(group)
def reply_my_friend(msg):
    # msg就是朋友发送的消息
    # 将msg发送给图灵机器人
    TL = Tuling(api_key=KEY)
    return TL.reply_text(msg)

bot.join()

