def isLoopNum(n):
    mirror = n[::-1]
    return n == mirror


L = eval(input())
res = filter(isLoopNum, L)
print(list(res))