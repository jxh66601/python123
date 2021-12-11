import math      #下面使用math库，要先导入数学库

n = int(input())
#print(math.factorial(n)) #math库里有factorial(n)函数可直接求解n的阶乘，可用于替换下面4行程序
fact = 1
for i in range(1,n+1):    #range()默认从0开始，这里range(1,n+1)表示从1 开始取值1至n
    fact = fact * i
print(fact)