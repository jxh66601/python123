width = eval(input())
length = eval(input())
area = width * length
print(round(area,2))  #round(x[,ndigits])四舍五入，保留ndigits位小数,round(x)返回四舍五入整数值

#
a = float(input())
b = float(input())
print('{:.2f}'.format(a*b))