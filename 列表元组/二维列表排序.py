#使用匿名函数lambda
m = int(input())
n = int(input())

myList = [('dungeon',7),('winterfell',4),('bran',9),('meelo',6)]
if m > len(myList):
    m = len(myList)
print(sorted(myList, key=lambda x:x[1])[:m])

score = [[ 'Angle', '0121701100106',99], [ 'Jack', '0121701100107',86], [ 'Tom', '0121701100109',65], [ 'Smith', '0121701100111', 100], ['Bob', '0121701100115',77], ['Lily', '0121701100117', 59]]
if n > len(score):
    n = len(score)
print(sorted(score, key=lambda x:x[0])[:n])
print(sorted(score, key=lambda x:x[2])[:n])