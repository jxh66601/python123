#求1+3+5+……+（2n-1）前n项和

n = int(input())
sum = 0
for i in range(1,2*n,2):
    sum = sum + i
print(sum)