import math

a = eval(input())
b = eval(input())
x = (-b+math.sqrt(2 * a * math.sin(math.pi / 3)*math.cos(math.pi / 3)))/(2 * a)
print(x)