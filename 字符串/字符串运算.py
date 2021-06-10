#字符串运算
#描述

#用户输入一个整数 x， 将字符串 '1\t5\t3\t9\n' 中的整数取出，分别与 x 相乘，再求和。
#**map(int,sep) 可将序列sep中的数字字符串转为对应的整数，例如：s= ['1','2','3']**
#**print(list(map(int,s)))  #[1, 2, 3]**

x = int(input())
s = '1\t5\t3\t9\n'
ls = s.strip().split('\t')
print(sum(x*a for a in map(int,ls)))