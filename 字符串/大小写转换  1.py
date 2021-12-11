#本题要求编写程序，用户输入一个字符串，将其小写字母全部转换成大写字母，把大写字母全部转换成小写字母，其他字符不变输出。
import string
str1 = input()
for i in str1:
    if i in string.ascii_lowercase:   #string.ascii_lowercase返回所有小写字母
        print(i.upper(),end='')       #str.upper()作用是将小写字母转换为大写字母输出
    elif i in string.ascii_uppercase: #string.ascii_uppercase返回所有大写字母
        print(i.lower(),end='')       #str.lower()作用是将大写字母转为小写字母输出
    else:
        print(i,end='')