l=list(map(int,input().split()))
[print(i) for i in list(set(l)) if l.count(i)%2!=0]
# ls=list(map(int,input().split()))
# t=ls[0]
# for i in ls[1:]:
#     t^=i
# print(t)


'''
超时程序示例
ls=list(map(int,input().split()))
for i in ls:
    if ls.count(i)%2==1:
        print(i)
        break
'''