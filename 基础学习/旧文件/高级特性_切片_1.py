# 切片操作
L = ['ASDASFD','asdfasd','asdasdas','aswrwetrw','gvbty','asfdasde','asfwe']
#取前三个元素——笨办法
print(L[0],L[2],L[3])
# 简单方法
print(L[0:3])
print(L[:3])
print(L[1:3])
print(L[-2:-1])
print(L[-2:])


cal = list(range(100))
print(cal)
print(cal[:10])
print(cal[-10:])
print(cal[10:20])
print(cal[:10:2])
print(cal[::5])
print(cal[:])

# 切片——tuple
print((1,2,3,4)[:2])

#切片——字符串
print('asfasasd'[:4])
print('asdfdsfsd'[::2])

