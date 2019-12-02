#删掉偶数，保留奇数
def is_ood(n):
    return n%2==1
print(list(filter(is_ood,[5,4,3,2,1,6,7,8,9])))

#把序列里的空字符删除
def not_odd(s):
    return s and s.strip()
print(list(filter(not_odd,['A',' ','b','X','','x'])))

#用filter求素数
def san():
     n = 1
     while True:
         n = n + 2
         yield n

def not_asd(n):
    return lambda x: x % n >0
def prim():
     yield 2
     it = san()
     while True:
           n = next(it)
           yield n
           it = filter(not_asd(n),it)
           for n in prim():
               if n < 1000:
                    print(n)
               else:
                    break
