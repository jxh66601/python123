n = input()
c1=0 #奇数和
c2=0 #偶数和
c3=0 #总和
c4=0
cc=0
for i in range(1,len(n)-1,2):
    c2+=int(n[i])
#print(c2)
for i in range(0,len(n)-1):
    c3+=int(n[i])
#print(c3)
c1=c3-c2
#print(c1)
c4=c2*3
cc=(c1+c2)%10
c=10-cc
#print(c)
#print(n[-1])
if c==int(n[-1]):
    print('校验已通过')
else:
    print('校验未通过')