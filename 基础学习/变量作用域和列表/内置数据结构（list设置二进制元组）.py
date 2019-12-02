'''
传值和传址的问题
对于简单的数值，采用传值的操作，即函数内部对参数的操作不影响外部的变量
对于复杂的变量（list，set，类），采用传址的操作，此时函数内的参数和外部变量是同一份内容，即函数内部对参数的操作可改变外部的变量
'''
def a(n):
    n[2] = 200
    print(n)
    return None
def c(n):
    n += 100
    print(n)
    return None

acs = [12,24,123,32]
cs = 10
print(acs)
a(acs)
print(acs)

print(cs)
c(cs)
print(cs)
#关于列表的函数
#列表里面可以放不同类型的数据
l = ['a',"I live you",32,4.12]
print(l)
'''
list方法：
-数据的插入
-数据的删除
'''
#在末尾追加
jia = [i for i in range(1,8)]
jia.append(100)
print(jia)
#insert:指定位置插入insert(index,data),index是插入位置
jia.insert(3,100)
print(jia)
#del:删除
#pop：从队尾拿出一个元素，即把最后一个元素取出
last_pop = jia.pop()
print(last_pop)
print(jia)
#remove:删除列表中指定的元素
#如果要删除的值不在list中则会报错，所以删除list元素是要使用try...excepty语句，或者先行判断
jia.remove(6)
print(jia)
#clear：清空列表(并且列表地址保持不变)
jia.clear()
print(jia)
#reverse:翻转(id不变)
jia = [i for i in range(1,8)]
print(id(jia))
jia.reverse()
print(id(jia))
print(jia)
#extend：扩展列表，两个列表，把一个直接拼到另一个（id 不变）
jias = [i for i in range(12,15)]
print(jia)
print(id(jia))
jia.extend(jias)
print(jia)
print(id(jia))
#count:查找列表中指定值或元素的个数
jia.append(4)
jia.insert(3,4)
print(jia)
print(jia.count(4))
#copy:拷贝，浅拷贝
#列表类型赋值实例
li = [1,2,3,4]
print(id(li))
print(li)
#list类型，简单赋值操作，是传的的地址
lis = li
lis[2] = 33
print(li)
print(lis)
print(id(lis))
#为了解决以上问题，list赋值采用copy函数
liss = li.copy()
liss[2] = 88
print(li)
print(liss)
print(id(li))
print(id(liss))
#深拷贝和浅拷贝的区别
ac = [1,2,3,[12,34,56]]
ass = ac.copy()
print(id(ac))
print(id(ass))
print(id(ac[3]))
print(id(ass[3]))
print(ass)
#浅拷贝只拷贝一层，如果是嵌套列表的话，外部的list列表id会改变，但内部的list列表id不变
#深拷贝所有内容，要使用特定工具



