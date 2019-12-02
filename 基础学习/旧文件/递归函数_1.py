#递归函数_1在函数中引用自己本身——尾递归
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)

print(fact(3))
print(fact(100))

#递归函数_1优化递归

def facts(n):
    return facts_s(n,1)
def facts_s(num,product):
    if num == 1:
        return product
    else:
        return facts_s(num-1,num * product)

print(facts(10))
print(facts_s(1,120))


# 递归函数_1  练习
def move(n,a,b,c):
    if n == 1:
        print('moev',a,'-->',c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)
print(move(4,'a','b','c'))
