import pymongo

# mongoDB的连接方式。
"""
# 万能模板
MONGODB_USER = ""  # MongoDB用户
MONGODB_PASSWORD = ""  # 用户的password
MONGODB_IP = ""  # IP
MONGODB_PORT = ""  # 端口，默认为27017
MONGODB_CLIENT = "mongodb://"+MONGODB_USER+":"+MONGODB_PASSWORD+"@"+MONGODB_IP+":"+MONGODB_PORT+"/"
"""
# 本地无密码使用下面方式
MONGODB_CLIENT = "mongodb://127.0.0.1:27017"


class DeleteRepeatMongoData:
    # 需要传入清洗的database，collection
    def __init__(self, database, collection):
        self.repeat_orderNo = set()
        self.database = database
        self.collection = collection
        self.client = pymongo.MongoClient(MONGODB_CLIENT)

    def save_repeat_order_2_txt(self, _filter=None):
        db = self.client[self.database]
        col = db[self.collection]
        # 根据条件查询
        documents = col.find(_filter)
        orderNo_list = []
        for document in documents:
            orderNo = document["orderNo"]
            if orderNo not in orderNo_list:
                orderNo_list.append(orderNo)
            else:
                self.repeat_orderNo.add(orderNo)
        # 将重复orderNo保存到文件中
        with open("./mongo_data/test.txt", "a", newline="\n") as f:
            for number in self.repeat_orderNo:
                f.write(number + "\n")
        return "save to txt success"

    def dlt_repeat_order(self,_filter=None):
        db = self.client[self.database]
        col = db[self.collection]
        # 根据条件查询
        documents = col.find(_filter)
        orderNo_list = []
        for document in documents:
            orderNo = document["orderNo"]
            if orderNo not in orderNo_list:
                orderNo_list.append(orderNo)
            else:
                # 删除操作，慎用
                col.delete_one({"orderNo":orderNo})


if __name__ == '__main__':
    m = DeleteRepeatMongoData("database", "collection")
    result = m.save_repeat_order_2_txt(_filter={"orderNo": 1})  # 查询条件
    print(result)
