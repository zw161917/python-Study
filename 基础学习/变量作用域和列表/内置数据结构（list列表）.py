'''
list(列表)
-del:删除
'''
#del 删除 id不变是在原数据区域进行的删除，不生成新的列表
a = [12,21,34,45,76]
del a[3]
print(a)

#列表相加，使用加号链接两个列表
b = [1,2,3,4,5]
c = a + b
print(c)

#使用乘号操作列表，相当于把n个列表链接在一起
x = a * 5
print(x)

#成员资格运算，判断一个元素是否在list列表中(in后为列表)
e = 34
t = 65
z = e in a
w = t in a
print(z)
print(w)

#not in ：判断一个元素在list列表中(in后为列表)
qw = t not in a
print(qw)

#链表的遍历
#for
#逐个打印list列表里的元素
#in 后面的变量要求是可迭代
for i in a:
    print(i)
#rang不是列表
for i in range(1,10):
    print(i)
print(type(range(1,10)))
#while循环访问列表（一般不用while编列list）
leagth = len(a)
#indx表示list的下标
indx = 0
while indx < leagth:
    print(a[indx])
    indx += 1

#双层列表循环
#li为嵌套列表，或者双层列表
li  = [["one",5],["two",1],["there",11],["four",55]]
#这是一种特异，一般用于字典
for k,v in li:
    print(k,"-->",v)

#双层列表循环变异
li  = [["one",5,"and"],["two",1,"asd"],["there",11,"hes"],["four",55,"asda"]]
for k,v ,w in li:
    print(k,"-->",v,"...",w)

#列表内涵：list content
#通过简单方法创建列表
#for创建
zx = [10,50,2]
#用list a 创建list b
#下面代码含义，对于所有a中的元素，逐个放入新列表b中
b = [i for i in zx]
print(b)
#对于所有a中的元素乘以10，生成一个新的列表
tm = [i*10 for i in zx]
print(tm)
#还可以过滤原来list中的内容放到新的list中
#比如把han列表中所有的偶数生成新的列表
han = [x for x in range(1,40)]
shu = [m for m in han if m%2==0]
print(han)
print(shu)

#列表生成式也可以嵌套
qian = [i for i in range(1,10)]
tao = [i for i in range(10,1000) if i % 100==0]
#进行嵌套
sheng  = [m + n for m in qian for n in tao]
print(qian)
print(tao)
print(sheng)
#也可以用条件表达式
shengs  = [m + n for m in qian for n in tao if m+n<700]
print(shengs)

#关于列表的常用函数
'''
len：求列表的长度
max：求列表的最大值
list：将其他格式转换成list
--要求：必须是可迭代的才能转换
'''
#len：求列表的长度
chang = [x for x in range(1,100)]
print(len(chang))
#max：求列表的最大值
print(max(chang))
#list：将其他格式转换成list
liss = [1,2,3]
print(list(liss))
s = "I love you"
print(list(s))
print(list(range(12,15)))


