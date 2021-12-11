import math
m = int(input())
n = int(input())

areaM = int(m * 2.54)/2
areaN = int(n * 2.54)/2
num = (areaM*areaM)/(areaN*areaN)
print(math.ceil(num))
#也可用以下方法处理：
# if num > int(num):  #当num小数位有有效数字时
#     num = int(num) + 1
# print(int(num))