# 在一行中输入三个用空格分隔的数
a, b, c = map(int, input().split())
d = max(a, b, c)
print(d)
