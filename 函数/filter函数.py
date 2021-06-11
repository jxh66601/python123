def isLoopNum(n):
    for x, y in zip(str(n), str(n)[::-1]):
        if x == y:
            a = True
        else:
            a = False
            break
    return a

n = eval(input())
res = filter(isLoopNum,n)
print(list(res))