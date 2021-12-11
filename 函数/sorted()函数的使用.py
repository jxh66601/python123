##L =[('Bob',75), ('Adam',92), ('Bart',66), ('Lisa',88)]

L = eval(input())

by_name = sorted(L, key=lambda t: t[0].lower())
by_score = sorted(L, key=lambda t: t[1])

print(by_name)
print(by_score)