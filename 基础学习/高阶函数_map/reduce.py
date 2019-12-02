#map()的使用
def f(x):
    return x * x
r = map(f,[1,2,3,4,5])
print(list(r))

#把所有数字转换成字符串
print(list(map(str,[1,2,3,4,5])))

#reduce的使用
from functools import reduce
def add(x,y):
    return x + y
print(reduce(add,[1,2,3,4,5]))

#可将[1,2,3.4.5]变为整数12345
def fn(x,y):
    return x * 10 + y

def char(s):
    digits = {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7}
    return digits[s]
print(reduce(fn,map(char,'1357')))

#整理成一个函数
dig = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}

def str2(s):
    def fa(x,y):
        return x * 10 + y

    def ch(s):
        return dig[s]
    return reduce(fa,map(ch,s))
print(str2('13579'))

#还可以用lambda进一步的简化
def char2(s):
    return dig[s]
def strs2(s):
    return reduce(lambda x,y:x * 10 + y,map(char2,s))
print(strs2('13579'))

#练习
