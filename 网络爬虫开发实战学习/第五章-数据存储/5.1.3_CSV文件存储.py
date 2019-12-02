import csv
import pandas as pd
#csv存储的使用
#调用csv的writer()方法初始化写入对象
with open('datas.csv','w') as file:
    writer = csv.writer(file)
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['10001', 'Mike', 20])
    writer.writerow(['10002', 'Bob', 22])
    writer.writerow(['10003', 'Jordan', 21])

#delimiter=属性修改分隔符
with open('datas.csv','w') as file:
    writer = csv.writer(file,delimiter=' ')
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['10001', 'Mike', 20])
    writer.writerow(['10002', 'Bob', 22])
    writer.writerow(['10003', 'Jordan', 21])

#调用writerows()方法可同时写入多行，参数为二维列表
with open('datas.csv','w') as file:
    writer = csv.writer(file,delimiter=' ')
    writer.writerow(['id', 'name', 'age'])
    writer.writerows([['10001', 'Mike', 21],['10002', 'Bob', 22],['10003', 'Jordan', 21]])

#csv库中字典的写入方法
with open('datas.csv','w') as file:
    fieldname = ['id', 'name', 'age']
    writer = csv.DictWriter(file,fieldnames=fieldname)
    writer.writeheader()
    writer.writerow({'id': '10001', 'name': 'Mike', 'age': 20})
    writer.writerow({'id': '10002', 'name': 'Bob', 'age': 22})
    writer.writerow({'id': '10003', 'name': 'Jordan', 'age': 21})

#写入中文是需要加入编码格式
with open('datas.csv', 'a', encoding='utf-8') as csvfile:
    fieldnames = ['id', 'name', 'age']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writerow({'id': '10005', 'name': '王伟', 'age': 22})

#读取文件
with open('datas.csv', 'r', encoding='utf-8') as csvfile:
    read = csv.reader(csvfile)
    for row in read:
        print(row)
#pandas读取
df = pd.read_csv('datas.csv')
print(df)