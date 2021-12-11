print(sorted(list(input())))

#或用以下方法
ls = list(input())
for i in range( len(ls) ):
    for j in range( 1, len(ls)-i ):
        if ls[j-1] > ls[j]:
            ls[j-1], ls[j] = ls[j], ls[j-1]
print(ls)