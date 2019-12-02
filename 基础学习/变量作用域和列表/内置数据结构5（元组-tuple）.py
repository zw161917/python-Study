'''
元组-tuple
-元组可以看成一个不可更改的list
'''
#创建空元组
t = ()
print(type(t))

#创建一个只有一个值的元组
t = (1,)
print(t)
print(type(t))

a = 1,
print(a)
print(type(a))

#创建多个元组
t = (1,2,3,4,5)
print(t)
print(type(t))

#使用其他结构创建
l = [1,2,3,4,5]
ls = tuple(l)
print(type(ls))
print(ls)

#元组的特性
'''
-是序列表，有序
-元组数据可以访问，不能修改(内容不能修改，但可以以一个新的元组进行覆盖)
-元组数据可以是任意数据类型
-list的所有属性除了可修改外，元组都具有（索引，分片，序列相加，相乘，成员资格操作等等）
'''
#切片可以超标
lss = ls[2:100]
print(type(lss))
print(lss)

#成员检测数量
if 4 in l:
    print("YES")
else:
    print("NO")

#双层元组遍历
t = ((1,2,3),(12,32,43),("asda","asda","xzc"))
for i in t:
    print(i)
for i in t:
    print(i, end=" ")
print()
for k,i,v in t:
    print(k,"--",i,"--",v)
'''
关于元组的函数
-len:获取元组的长度
-max,min:最大值，最小值
-tuple:转化或创建元组

元组的函数
-基本上和list通用
-count:计算指定元素出现的次数
-index：求指定元素在元组中的索引位置（如果多次出现则返回第一个）
'''
#元组变量交换法
#两个变量交换
a = 1
b = 2
a,b =b,a
print(a)
print(b)