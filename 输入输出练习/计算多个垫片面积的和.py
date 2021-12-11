PI = 3.14159
R = eval(input())
r = eval(input())
n = eval(input())
areaSum = n * (PI * R * R-PI * r * r)
print('{:.2f}'.format(areaSum))