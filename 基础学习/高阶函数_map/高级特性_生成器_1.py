#生成器（generator）简单操作
#列表生成式
L = [x * x for x in range(10)]
print(L)

#生成器
g = (x * x for x in  range(10))
print(g)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
#用for循环来运行生成器
for x in g:
    print(x)

#斐波拉契数列1,1,2,3,5,7.。。。。
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        print(b)
        a,b = b,a+b
        n = n + 1
    return 'done'
print(fib(5))

#用生成器来写
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b,a+b
        n = n + 1
    return 'done'

for x in fib(8):
    try:
        print(x)
    except StopIteration as e:
        print(e.value)
        break


#如果想出现返回值
g = fib(10)
while True:
    try:
        x = next(g)
        print('g:',x)
    except StopIteration as e:
        print('Generator return value:',e.value)
        break

#练习
asa = []
for x in range(10):
    for i in x:
        asa[i] = i
        print(asa)
