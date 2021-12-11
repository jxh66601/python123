#计算a除以b，结果保留2位小数


a = eval(input())
b = eval(input())
if b != 0:
    print(round(a/b,2))
else:
    print('除零错误')