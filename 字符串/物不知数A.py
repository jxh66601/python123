# “今有物不知其数，三三数之剩二，五五数之剩三，七七数之剩二,问物几何？”
n = int(input())
for i in range(n):
	if i % 3 == 2 and i % 5== 3 and i % 7 ==2:
		print(i)