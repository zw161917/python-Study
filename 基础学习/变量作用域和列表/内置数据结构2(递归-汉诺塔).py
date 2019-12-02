#汉诺塔结构
'''
规则：
1.n=1：直接把A上的数据放到C上
2.n=2：把A上的数据先放到B上一个，再将A上剩余的一个数据放到C上，再将B上的数据放到C上
2.n=n：把A上的n-1个数据借助C放到B上，再将A上剩余的一个数据放到C上让后再将B上的数据放到C上
'''
def hano(n,a,b,c):
    if n == 1:
        print(a,"-->",c)
        return None
    '''
        if n == 2:
        print(a,"-->",b)
        print(a,"-->",c)
        print(b,"-->",c)
        return None
    '''
#把n-1个数据，从a借助c挪到b上
    hano(n-1,a,c,b)
    print(a,"-->",c)
#把n-1个数据，从b借助a挪到c上
    hano(n-1,b,a,c)
a = "A"
b = "B"
c = "C"
n = 3
hano(n,a,b,c)