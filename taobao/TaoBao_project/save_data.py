# coding=gbk
import pymongo

connection = 'mongodb://admin:admin123@192.168.193.128:27017/'
client = pymongo.MongoClient(connection)
db = client.test
collection = db.students
student = {
    'id': '20190304',
    'name': 'zs',
    'sex': '男',
}
result = collection.insert_one(student)
print(result)
print(result.inserted_id)
