import json

#JSON文件存储
str = '''
[{
    "name": "Bob",
    "gender": "male",
    "birthday": "1992-10-18"
}, {
    "name": "Selina",
    "gender": "female",
    "birthday": "1995-10-18"
}]
''' 
'''
print(type(str))
data = json.loads(str)
print(data)
print(type(data))
print(data[0]['name'])
print(data[0].get('name'))
#get()方法可传入第二个参数（即默认值）
print(data[0].get('age',18))
with open('data.json','r') as file:
    strs = file.read()
    data = json.loads(strs)
    #调用json方法蒋JSON对象转化为字符串
    with open('data.json','a') as file:
        file.write(json.dumps(data))
    #想保存JSON数据的格式可加一个参数
    with open('data.json', 'a') as file:
        file.write(json.dumps(data,indent=2))
    print(data)
'''
#添加ensure_ascii=False规定文件输出的编码
data = [{
    'name': '王伟',
    'gender': '男',
    'birthday': '1992-10-18'
}]
with open('data.json', 'a',encoding='utf-8') as file:
    file.write(json.dumps(data, indent=2,ensure_ascii=False))

