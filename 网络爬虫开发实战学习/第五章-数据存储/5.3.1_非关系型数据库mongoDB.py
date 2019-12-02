import pymongo
'''
#连接MongoDB
client = pymongo.MongoClient(host='localhost', port=27017)
#指定数据库
database = client["test"]
#指定集合
collection = database["students"]
student = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}
#插入数据
result = collection.insert(student)
print(result)
'''
#同时插入多条数据
client = pymongo.MongoClient(host='localhost',port=27017)
database = client.test
collection = database.students
'''
student1 = {
    'id': '20170111',
    'name': 'Jor',
    'age': 20,
    'gender': 'male'
}

student2 = {
    'id': '20170212',
    'name': 'Mike',
    'age': 21,
    'gender': 'male'
}
result = collection.insert([student1,student2])
print(result)
'''
#在PyMongo 3.x版本中，官方已经不推荐使用insert()方法了。
# 官方推荐使用insert_one()和insert_many()方法来分别插入单条记录和多条记录
'''
student = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}
 
result = collection.insert_one(student)
print(result)
print(result.inserted_id)

student1 = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}
 
student2 = {
    'id': '20170202',
    'name': 'Mike',
    'age': 21,
    'gender': 'male'
}
 
result = collection.insert_many([student1, student2])
print(result)
print(result.inserted_ids)
'''
'''
#可以利用find_one()或find()方法进行查询
# 其中find_one()查询得到的是单个结果，find()则返回一个生成器对象
result = collection.find_one({"name" : "Jor"})
print(result)
result = collection.find({"age" :20})
for res in result:
    print(res)
#查询年龄大于20的数据
results = collection.find({'age': {'$gt': 18}})
for resa in result:
    print(result)
#统计所有数据条数可以调用count()方法
ret = collection.find({"age" :20}).count()
print(ret)
'''
'''
#排序直接调用sort()方法
results = collection.find().sort('name',pymongo.ASCENDING)
print([result['name'] for result in results])
#偏移可以利用skip()方法
result = collection.find().sort('name',pymongo.ASCENDING).skip(1)
print([res['name'] for res in result])
#用limit()方法指定要取的结果个数
result = collection.find().sort('name',pymongo.ASCENDING).skip(1).limit(2)
print([res['name'] for res in result])
#更新使用update()方法
condition = {'name': 'Mike'}
student = collection.find_one(condition)
student['age'] = 23
result = collection.update(condition, student)
print(result)
'''
#update()方法其实也是官方不推荐使用的方法。这里也分为update_one()方法和update_many()方法
condition = {'name': 'Mike'}
student = collection.find_one(condition)
student['age'] = 26
result = collection.update_one(condition, {'$set': student})
print(result)
print(result.matched_count, result.modified_count)
#年龄加1
condition = {'age': {'$gt': 20}}
result = collection.update_one(condition, {'$inc': {'age': 1}})
print(result)
print(result.matched_count, result.modified_count)
#调用update_many()方法，则会将所有符合条件的数据都更新
condition = {'age': {'$gt': 20}}
result = collection.update_many(condition, {'$inc': {'age': 1}})
print(result)
print(result.matched_count, result.modified_count)
#remove()方法指定删除的条件
result = collection.remove({'name': 'Jor'})
print(result)
