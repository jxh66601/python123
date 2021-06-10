##**判断字符串结尾**
## 描述
#输入一个字符串，当输入字符串结尾是 “PY” 时，输出“YES”，否则输出“NO”。
a = input()
if a[len(a)-2:] == 'PY':
    print('YES')
else:
    print('NO')