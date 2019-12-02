#paixu
S = [2,-21,-12,12,23,45,5342,1]
print(sorted(S))

#还可以接受函数 按绝对值排序
print(sorted(S,key=abs))

#对字符串的排序
A = ['asfkm','tsfasd','Vsdasdqw','Qswdfef','Ddfsasf']
print(sorted(A))

#忽略大小写的排序
print(sorted(A,key=str.lower))

#反向排序
print(sorted(A,key=str.lower,reverse=True ))