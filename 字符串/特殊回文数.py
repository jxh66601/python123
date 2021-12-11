'''
123321是一个非常特殊的数，它从左边读和从右边读是一样的，我们称这样的数为回文数。
给你一个正整数n， 编程求所有这样的五位和六位十进制数，满足各位数字之和等于n(5<=n<=54)。 按从小到大的顺序输出满足条件的整数。
def Palindrome(n):
    for i in range(10000, 1000000):
        number = list(str(i))
        #使用reversed把列表进行反向迭代， eval求值连接后的字符串
        if number == list(reversed(number)) and eval('+'.join(number)) == n:
            print(i)
Palindrome(52)
'''
def reverse(n):
    # 返回一个整数的逆序
    return int(str(n)[::-1])
#然后定义一个累加整数各项数字的函数。方法不止一种，这里通过分解成字符后来处理。
def accumulate(n):
    # 返回一个整数的各位数之和
    return sum([int(x) for x in str(n)])
#循环找出满足要求的数
# 寻找 10000 到 1000000 之间满足各位数之和为 n 的回文数
n = int(input())
flag = 0
if n > 54 or n < 1:
    print('输入错误，请重新输入！')
else:
    for i in range(10000,1000000):
        if i == reverse(i) and accumulate(i) ==n:
            print(i)
            flag = 1
    if flag == 0:
        print('无满足条件的数！')