ip = input()
list=[]
for c in ip:
    if c not in ['0','1']:
        print('data error!')
if len(ip) == 32:
    for i in range(4):
        list+=[str(int(ip[i*8:(i+1)*8],2))]
    print('.'.join(list))
else:
    print('data error!')