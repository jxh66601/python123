for i in range(100000, 1000000):
    if int(str(i)[:3]) + int(str(i)[3:]) == 999 and int(str(i)[:2]) + int(str(i)[2:4]) + int(str(i)[4:]) == 99 and i * 7 == 999999:
        print(i)




for i in range(100000,1000000):
	if len(set(str(i))) < 6:
		continue
	for j in range(1,7):
		if set(str(i)) - set(str(i* j)):
			break
	else:
		print(i)