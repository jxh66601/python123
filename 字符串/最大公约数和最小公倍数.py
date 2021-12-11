import math

num1 = int(input())
num2 = int(input())

print( math.gcd(num1,num2),int(num1*num2/math.gcd(num1,num2)))