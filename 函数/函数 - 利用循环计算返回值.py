def fact(num3):
    if num3 == 0 or num3 == 1:
        return 1
    else:
        return (num3 * fact(num3 - 1))

number=int(input())
print(fact(number))


# 使用高阶函数
#from functools import reduce
#num4 = input()
#print(reduce(lambda x, y: x * y, range(1, num4 + 1)))