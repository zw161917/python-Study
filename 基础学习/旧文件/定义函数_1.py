#定义函数_1——定义求绝对值
def my_abs(x):
    if x >= 0:
        return x
    else:
        return  -x

print (my_abs(10))
print (my_abs(-12.2))

#定义函数_1——pass（空函数）
def nop():
    pass

#定义函数_1——设定数据类型
def dy_abs(x):
    if not isinstance(x,(int,float)):
        raise  TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
print (dy_abs(10.1),dy_abs(-10.2),dy_abs(12))

#定义函数_1——返回多个值
import math

def move(x,y,step,angle = 0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx,ny
x,y = move(100,100,60,math.pi / 6)
print(x,y)

#定义函数_1——练习
def qusdratic(a,b,c):
    x1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
    x2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
    return x1,x2
print(qusdratic(1,4,4))
