# 生成[1*1,2*2,3*3......]
l = []
for x in range(1,11):
    l.append(x * x)
print(l)


# 用列表生成器
print([x * x for x in range(1,11)])

#加上if判断
print([x * x for x in range(1,11) if x % 2 == 0])

#双重循环，可生成排列
print([n + m for n in 'asd' for m in 'zxc'])

#列出当前目录下的所有文件和目录名
import  os
print([d for d in os.listdir('.')])

#同时使用多个for循环，同时迭代key和value
d = {'a':'z','s':'x','d':'c'}
print([k + ' = '+ v for k,v in d.items()])

#把一个list中的所有字符变为小写
L = ['Asdf','Zxcv','Qwer']
print([s.lower() for s in L])

#练习
A = ['Asdf','Qwer',12,'Zxcv']
print([s.lower() for s in A if isinstance(s,str )])

