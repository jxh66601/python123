n=eval(input())
sstr=input()
llen=len(sstr)

#如下最后一列不足n的用空格补齐
if llen%n !=0:
    sstr=sstr+' '*(n-llen%n)

#古风输出
for i in range(n):
    print(sstr[i::n][::-1])