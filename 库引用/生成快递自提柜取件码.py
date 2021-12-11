import random

n = input()
random.seed(int(n)) #随机数种子n由用户输入
Sn = '' #空字符串
characters = 'ABCDEFGHIJ0123456789'
for i in range(6):
Sn = Sn + random.choice(characters) #生成的字符连接到字符串上
print(Sn)