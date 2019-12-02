import pymysql

#mysql的存储
'''
db = pymysql.connect(host='localhost',user='root',password='',port=3306)
cursor = db.cursor()
cursor.execute('SELECT VERSION()')
data = cursor.fetchone()
print('Database version:',data)
#创建数据库
cursor.execute('CREATE DATABASE spiders DEFAULT CHARACTER SET utf8')
db.close()
'''
'''
#创建表
db = pymysql.connect(host='localhost',user='root',password='',port=3306,db='spiders')
cursor = db.cursor()
sql = 'CREATE TABLE IF NOT EXISTS students (id varchar(255) not null,name varchar(255) not null,age int not null,PRIMARY KEY(id))'
cursor.execute(sql)
db.close()
'''
#插入数据
'''
id = '20120001'
user = 'Bob'
age = 20
db = pymysql.connect(host='localhost',user='root',password='',port=3306,db='spiders')
cursour = db.cursor()
sql = 'INSERT INTO students(id,name,age) values(%s,%s,%s)'
try:
    cursour.execute(sql,(id,user,age))
    print('插入成功')
    db.commit()
except:
    db.rollback()
db.close()
'''
#使用join格式插入
'''
db = pymysql.connect(host='localhost',user='root',password='',port=3306,db='spiders')
cursor = db.cursor()
data = {
    'id':'20120002',
    'name':'jock',
    'age':18
}
table = 'students'
keys = ','.join(data.keys())
values = ','.join(['%s'] * len(data))
sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table,keys=keys,values=values)
try:
    if cursor.execute(sql,tuple(data.values())):
        print('Successful')
        db.commit()
except:
    print('Failed')
    db.rollback()
db.close()
'''
#更新数据（数据的修改）
'''
db = pymysql.connect(host='localhost',user='root',password='',port=3306,db='spiders')
cuesor=db.cursor()
sql = 'UPDATE students SET name=%s WHERE age=%s'
try:
    cuesor.execute(sql,('dog','20'))
    db.commit()
except:
    db.rollback()
db.close()
'''
#覆盖数据
'''
db = pymysql.connect(host='localhost',user='root',password='',port=3306,db='spiders')
cursor = db.cursor()
data = {
    'id':'20120001',
    'name':'bob',
    'age':18
}
table = 'students'
keys = ','.join(data.keys())
values = ','.join(['%s'] * len(data))
sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'.format(table=table,keys=keys,values=values)
update = ','.join([" {key}=%s".format(key=key) for key in data])
sql += update
try:
    if cursor.execute(sql,tuple(data.values())*2):
        print('Successful')
        db.commit()
except:
    print('Failed')
    db.rollback()
db.close()
'''
#删除数据
'''
db = pymysql.connect(host='localhost',user='root',password='',port=3306,db='spiders')
cursor = db.cursor()
table = 'students'
condition = 'age > 20'
sql = 'DELETE FROM  {table} WHERE {condition}'.format(table=table, condition=condition)
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
db.close()
'''
#查旬数据
'''
db = pymysql.connect(host='localhost',user='root',password='',port=3306,db='spiders')
cursor = db.cursor()
sql = 'SELECT * FROM students WHERE age >= 15'
try:
    cursor.execute(sql)
    print('查询条数：',cursor.rowcount)
    one = cursor.fetchone()
    print('第一条：',one)
    results = cursor.fetchall()
    print('剩余查讯结果：',results)
    print('遍历结果：')
    for row in results:
        print(row)
except:
    print('Error')
'''
#逐条取数据
db = pymysql.connect(host='localhost',user='root',password='',port=3306,db='spiders')
cursor = db.cursor()
sql = 'SELECT * FROM students WHERE age >= 15'
try:
    cursor.execute(sql)
    row = cursor.fetchone()
    while row:
        print("Row：",row)
        row = cursor.fetchone()
except:
    print('Error')