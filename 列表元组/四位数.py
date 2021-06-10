#**描述**
#一个四位数，各位数字互不相同，所有数字之和等于6，并且这个数是11的倍数。
#满足这种要求的四位数有多少个？各是什么？

list1=[]
for num in range(1000,10000): #生成4位数
    num1=str(num)
    if num1[0] != num1[1]!= num1[2] != num1[3]:
        num2=int(num1)
        if num2 %11 == 0:
            num3=str(num2)
            s=sum(int(i) for i in num3)
            if s == 6:
                #print(num3)
                list1.append(num3)
                #for i in num3:
print(len(list1))
list1.sort()
print(list1)

