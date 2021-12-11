num=input()
ls,l=['ling','yi','er','san','si','wu','liu','qi','ba','jiu','fu'],[]
for i in num:
    if i == '-':
        print(ls[-1],end = ' ')
    else:
        l.append(ls[int(i)])
print(*l)
# num=input()
# py=['ling','yi','er','san','si','wu','liu','qi','ba','jiu']
# flag=0
# if num[0]=='-':
#     start=1
#     print('fu',end='')
#     flag=1
# else:
#     start=0
# for i in range(start,len(num)):
#     if flag==1:
#         print(' {}'.format(py[int(num[i])]),end='')
#     else:
#         print('{}'.format(py[int(num[i])]),end='')
#         flag=1