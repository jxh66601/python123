n = int(input())  # 输入一个正整数 n
for i in range(n):
	print(i)  # 每行一个数字输出 0 -（n-1）

for i in range(n):
	print(i, end=' ')  # 在一行内输出 0 -（n-1），每个数字后输出一个空格
print()                # 此行保留，不要修改

for i in range(n):
	print(i, end='')  # 在一行内输出 0 -（n-1），每个数字间没有分格
print()                # 此行保留，不要修改

for i in range(n):
	print(i, end=',')  # 在一行内输出 0 -（n-1），每个数字后输出一个逗号
print()                # 此行保留，不要修改

for i in range(n):
	if i != n - 1:
		print(i, end=',')  # 在一行内输出 0 -（n-1），每个数字后输出一个逗号，最后一个数字后不能有逗号
	else:
		print(i)