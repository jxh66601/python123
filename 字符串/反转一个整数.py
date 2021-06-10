#反转一个整数
#入一个非 0 十进制整数(不允许前导0的存在，即不允许类似 0123 这样的输入)，将其反转输出。
a = input()
b = list(a)
b.reverse()
if eval(a)<0:
    print('-',end=(''))
    del b[len(b)-1]
for i in b :
    if i!='0':
        print(i,end='')