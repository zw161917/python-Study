#函数参数_1——参数的n次方
from typing import Any


def qwer(x,n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(qwer(2,3))

#函数参数_1——默认参数
def qwers(x,n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(qwers(3))

def asd(name,gender):
    print('name:',name)
    print('gender:',gender)
print(asd('Sacads','F'))

#函数参数_1——可变参数
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc([1,2,3]))
print(calc([1,3,5,7]))
nums = [1,2,3]  # type: Any
print(calc([*nums]))
print(calc([nums[1],nums[2],nums[0]]))

#函数参数_1——关键字参数
def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)
print(person('Michael',30))
print(person('Bob',45,city = 'Beijing'))
print(person('Adom',45,gender = 'M',job = 'Engineer'))
extar = ['Cate','Biejing','job','Enginge']
print(person('Jack',24,city = extar[1],jbd = extar[3]))
print(person('jack',24))

#函数参数_1——参数组合
def fl(a,b,c = 0,*args,**kw):
    print('a = ',a,'b = ',b,'c = ',c,'args = ',args,'kw = ',kw )

def f2(a,b,c = 0,*,d,**kw):
    print('a = ',a,'b = ',b,'c = ',c,'d = ',d,'kw = ',kw)

print(fl(1,2))
print(fl(1,2,3))
print(fl(1,2,3,extar[1],asca = extar[2]))
print(f2(1,2,d = 99,acsa = 'dsfswadf'))
args = (1,2,3,4)
kw = {'d',99,'x','#'}
print(fl(*args,aca = [kw]))
