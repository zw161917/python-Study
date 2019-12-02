# 函数作为返回值返回
def lazy(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


p = lazy(1, 3, 5, 7, 9)
print(p())


# 闭包
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1(),f2(),f3())

#应用循环变量
def couns():
    def f(j):
        def g():
            return j * j
        return g
    ft = []
    for i in range(1,4):
        ft.append(f(i))
    return ft
f4, f5, f6 = couns()
print(f4(),f5(),f6())

#练习
def counss():
    def fa(j):
        def ga():
            return j + 1
        return ga
    fta = []
    for i in range(0,3):
        fta.append(fa(i))
    return fta
fa, fs, fd = counss()
print(fa(),fs(),fd())



