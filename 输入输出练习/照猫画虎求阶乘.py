n = int(input())           #把用户输入赋值给变量n，int()的作用是将输入的字符串转成整数
fact = 1                   #fact赋初值为1
for i in range(1,n+1):     #括号里取值范围是从1到n，不包括n+1
    fact = fact * i        #每次循环时把i值加到sum上
print(fact)