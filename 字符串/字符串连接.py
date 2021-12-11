#用.将用户输入的4个字符串连接成一个字符串（第一个字符串前不能有'.'）


s = input()
str = s
for i in range(3):
    s = input()
    str = str + '.' + s
print(str)