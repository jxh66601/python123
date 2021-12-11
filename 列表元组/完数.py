def isPrime(n):          #判断素数的函数
    if n < 2:
        return False     #0和1不是素数
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    else:
        return True
def isPerfect(m):   #判断完数的函数
	if isPrime(m) and isPrime(2**m-1):
		s = 2**(m-1)*(2**m-1)
		ls.append(s)
		for i in range(2, s // 2 + 1):
			if s % i == 0:
				factor.append(i)
		return s
	else:
		return False

n = int(input())
count,num = 0, 1
ls = []
while count <n:
	factor = []
	if isPerfect(num):
		print('{}=1'.format(ls[count]), end='')
		for j in factor:
			print("+{}".format(j), end='')
		count = count + 1
		print()
	num = num + 1