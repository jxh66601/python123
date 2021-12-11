binaryIP = input()
decimalIP = str(int(binaryIP[0:8], 2))
for i in range(1,4):
	decimalIP = decimalIP +'.' +  str(int(binaryIP[i * 8:(i + 1) * 8], 2))
print(decimalIP)
# 或用列表推导式实现

binaryIP = input()
decimalIP = [str(int(binaryIP[i * 8:(i + 1) * 8], 2)) for i in range(4)]
print('.'.join(decimalIP))
