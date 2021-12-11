ean13 = input()

C1 = 0
C2 = 0
for i in range(0,12,2):
    C1 = C1 + int(ean13[i])

for i in range(1,12,2):
    C2 = C2 + int(ean13[i])*3

CC = int(str((C1 + C2))[-1])
C = str((10 - CC))[-1]
if C == ean13[-1]:
    print('校验已通过')
else:
    print('校验未通过')