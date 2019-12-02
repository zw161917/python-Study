#直接传入匿名函数 lambda代表匿名函数
import functools

print(list(map(lambda x: x * x,[1,2,3,4,5,6,7,8,9])))

#把匿名函数当做变量
f = lambda x: x * x
print(f)
print(f(5))

#把匿名函数当做返回值返回
def build(x,y):
    return lambda : x * x + y * y
fd = build(1,2)
print(fd())

#还可以将函数对象 *args **kw
int2 = functools.partial(int,base=2)
print(int2('1000'))

#把所给的数加在左边
max2 = functools.partial(max,10)
print(max2(11  ,2,3))
