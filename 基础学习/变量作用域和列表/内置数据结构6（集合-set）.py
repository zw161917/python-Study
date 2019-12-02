'''
集合-set
-一堆确定的无序的唯一的数据，集合中每一个数据成为一个元素
'''
#集合的定义
s = set()
print(type(s))
print(s)
#如果只是用大括号定义并没有元素生成，这定义的是一个dict类型
d = {}
print(d)
print(type(d))

'''
#集合的特征
-集合内数据无序，无法使用索引和分片
-集合内部数据元素具有唯一性，可以用来排除重复数据
集合内的数据，str，int，float，tuple，冰冻集合等，即内部只能放置可哈希数据
'''
#集合序列操作
#成员检测（in，not in）
'''
-成员检测（in，not in）
集合遍历操作
-for循环
-集合里面不允许嵌套集合
集合函数
len max min和其他函数一样
add:向集合中添加元素
set：生成一个集合
clear：可将内部元素清空
copy：拷贝
remove：移除指定的值，直接改变原有值，如果删除的值不存在，会报错
discard：移除集合中指定的值，如果删除的值不存在，不会报错
pop：随机移除一个元素
intersection：交集
difference：差集
union：并集
issubset：检查一个集合是否是另一个的子集
issuperset：检查一个集合是否为另一个的超集
'''
#集合的内涵
#普通集合内涵
#可在初始化后自动过滤掉重复的元素
s = {1,12,32,12,1,1,45,67,12}
print(s)

#带条件的集合内函
sss = {i for i in s if i % 2==0}
print(sss)
#也可多循环

s1 = {1,2,3,4,5,6}
s2 = {5,6,7,8,9}
#两集合的交集
s_1 = s1.intersection(s2)
print(s_1)
#两集合的差集
s_2 = s1.difference(s2)
print(s_2)
#两集合的并集
s_3 = s1.union(s2)
print(s_3)
#检查一个集合是否是另一个的子集
s_4 = s1.issubset(s2)
print(s_4)

'''
集合的数学操作
-只有减号
'''
s_5 = s1-s2
print(s_5)

'''
frozenset:冰冻集合
-冰冻就是不可进行任何修改的集合
-除修改外的其他操作和set一样
'''
#创建frozenset
s = frozenset()
print(type(s))
print(s)

'''
dict:字典
-数据以键值对的形式出现
-字典是序列类型，但是却是无序参数，所以没有分片和索引
-key:必须是可哈希的值（int string float tuple），但是list，set，dict不行
-value：可以是任何值
'''
#有值字典
#带关键字参数
#字典的遍历在python2和python3中代码不通用
#遍历特殊用法
d = {"one":1,"two":2,"three":3}
for k,v in d.items():
    print(k,"--",v)
#加限制条件
dd = {k:v for k,v in d.items() if v%2 == 0}
print(dd)
'''
字典相关格式
通用函数：len，max，min，dict
str（字典）：返回的字典是字符串格式
clear：清空字典
items：将返回的键值对变换为元组形式
keys：将字典中的键组成个一个解构返回
value：将字典中的值返回成一个可迭代的结构
get：根据指定键返回相应的值，可以设置默认值
fromkeys：使用指定的序列作为键，使用一个值作为字典的所有键的值
'''
l = ["name","age","xing"]
ddd = dict.fromkeys(l,"saasasasas")
print(ddd)