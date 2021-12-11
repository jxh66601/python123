#在指定位置插入元素
x = input()
i = int(input())
ls = ['2', '3', '0', '1', '5']
ls.insert(i,x)
#ls.insert(len(ls),x)
ls.append(x)
print(ls)