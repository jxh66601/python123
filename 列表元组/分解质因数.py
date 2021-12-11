import math
number = int(input())
ls = []
def getChildren(num):
    isZhishu = True
    for i in range(2, int(math.sqrt(1 + num)) + 1):  # 多加个1
        if num % i == 0 and i != num:
            ls.append(i)
            isZhishu = False
            getChildren(num // i)
            break
    if isZhishu:
        ls.append(num)

getChildren(number)
print(ls)