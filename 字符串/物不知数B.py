n = int(input())
for i in range(n):
	if i % 2 == 1 and i % 3 == 0 and i % 4 == 1 and i % 5 == 1 and i % 6 == 3 \
			and i % 7 == 0 and i % 8 == 1 and i % 9 == 0:
		print(i)