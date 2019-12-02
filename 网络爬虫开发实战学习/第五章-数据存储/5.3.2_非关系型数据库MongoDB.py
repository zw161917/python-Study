import pymongo
#非关系型数据库MongoDB存储
client = pymongo.MongoClient(host='localhost',port='27017')
db = client.test
collection = db.students
print(client) 