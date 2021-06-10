#**列表操作**
##描述
#输入一个1-100之间的正整数 n, 以 n 为随机数种子随机生成一个不大于 n 的正整数 m 。
# 生成一个包含元素为 1，2，3……n 的列表 ls，在列表 ls 中删除值为 m 的整数倍的元素，
# 在两行中输出原始列表和删除 m 倍数后的列表。
import random
n = int(input())
random.seed(n)
m = random.randint(0,n)+1
list1 = []
list2 = []
for i in range(1,n+1):
    list1.append(i)
print(list1)
for i in range(1,n+1):
    if i%m != 0:
        list2.append(i)
print(list2)
