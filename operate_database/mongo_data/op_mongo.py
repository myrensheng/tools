import pymongo

# MONGODB_CLIENT = "mongodb://root:Ii1mNI&1191^$(Y@dds-bp1da1e2b98c33b41436-pub.mongodb.rds.aliyuncs.com:3717"
MONGODB_CLIENT = "mongodb://47.110.233.191:27017"
client = pymongo.MongoClient(MONGODB_CLIENT)
db = client["backup"]
col = db["userscore"]
no = col.count({"appId":"HZRESK006"})
documents = col.find({"appId":"HZRESK006"})
# col.update_many({"appId":"HZRESK006"},{"Time":"ISODate("})
import datetime
def ISODate(str_time):
    timestamp = datetime.datetime.strptime(str_time,'%Y-%m-%d %H:%M:%S')
    utc_timestamp = timestamp - datetime.timedelta(hours=8)
    print(timestamp)
    print(utc_timestamp)
    pass
ISODate("2019-05-01 03:06:35")
# for document in documents:
#     orderNo = document["orderNo"]
#     str_time = document["Time"]
#     col.update({"orderNo":orderNo}, {"Time": ISODate("+str_time+")})
#     print(document["Time"])
# documents = col.find({"appid":"HZRESK006"})
# print(no)