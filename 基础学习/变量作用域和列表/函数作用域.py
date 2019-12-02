#变量作用域
'''
-变量由作用范围限制
-分类：按照作用域范围
    -全局（global）
    -局部（local）
-LEGB原则
    -L(local) 局部作用域
    -E（Enclosing function locale）外部嵌套作用域
    -G（Global module）函数定义所在模块作用域
    -B（Buildin）:  python内置模块作用域
'''
#将局部变量变为全局变量,变量前加global，并且不能同时赋值
def fun():
    global s
    s=100
    print(s)
#print(s)不能在函数运行前调用，因为global还没有执行所以找不到
fun()
print(s)
#查看全局变量以及局部变量(globals(),locals())
a = 1
b = 2
def stu(c,d):
    e = 388
    print("Globals={0}".format(globals()))
    print("locals={0}".format(locals()))
stu(100,200)



'''
eval()函数
-把一个字符串当做一个表达式来执行，返回表达式执行的结果
-语法：eval(string_code,globals=None,locals=None)

exec()跟eval()功能类似但不返回结果
-语法：exec(string_code,globals=None,locals=None)
'''
#eval()实例
x=100
y=200
z1 = x+y
print(z1)
z2 = eval("x+y")
print(z2)

#exec()实例
print(z1)
z2 = exec("x+y")
print(z2)