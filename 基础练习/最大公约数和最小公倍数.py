import math

num1 = int(input())
num2 = int(input())

print( math.gcd(num1,num2),int(num1*num2/math.gcd(num1,num2)))
#
# def gcd(x, y):
#     if x > y:
#         smaller = y
#     else:
#         smaller = x
#     for i in range(1, smaller + 1):
#         if ((x % i == 0) and (y % i == 0)):
#             gcd = i
#     return gcd
#
#
# def lcm(x, y):
#     if x > y:
#         greater = x
#     else:
#         greater = y
#
#     while (True):
#         if ((greater % x == 0) and (greater % y == 0)):
#             lcm = greater
#             break
#         greater += 1
#
#     return lcm
# #math.gcd(num1.num2)
# num1 = int(input())
# num2 = int(input())
#
# print( gcd(num1, num2),lcm(num1,num2))