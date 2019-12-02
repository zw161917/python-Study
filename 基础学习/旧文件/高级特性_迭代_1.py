#dict的迭代
d = {'a':1,'b':2,'c':3}

# 打出key键
for key in d :
    print(key)
# 打出value值
for value in d.values():
    print(value)
#键—值都打印
for k,v in d.items():
    print(k,v)

#字符串的迭代
for ch in 'ABC':
    print(ch)

#判断对象是否可以迭代
from collections import Iterable
print(isinstance('abc',Iterable))
print(isinstance([1,2,3],Iterable))
print(isinstance(123,Iterable))

#添加下标循环
for i,vaas in enumerate(['A','B','C']):
    print(i,vaas)

#同时引用两个变量
for x,y in [(2,8),(1,4),(3,2)]:
    print('(',x,',',y,')')
