import random
import math

trail=[(0,0)]
sd = random.seed(int(input()))
X,Y=0,0
count=0
while count<5:
    xDirection=random.choice([1,-1])
    xGo=random.choice([1,2,3,4,5,6,7,8,9,10])
    xNew=X+xDirection * xGo
    yDirection=random.choice([1,-1])
    yGo=random.choice([1,2,3,4,5,6,7,8,9,10])
    yNew=Y+yDirection * yGo
    count+=1
    X,Y=xNew,yNew
    trail.append((X,Y))
print(trail)
dist=0
x1,y1=0,0
for x2,y2 in trail[1:]:
    d=math.sqrt((x1-x2)**2+(y1-y2)**2)
    x1,y1=x2,y2
    dist += d
print("{:.2f}".format(dist))