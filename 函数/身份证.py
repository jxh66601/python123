n = input("请输入18位身份证号:")
factor = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
n = str(n)
sum = 0
for i in range(0, 17):
    sum += int(n[i]) * factor[i]
sum %= 11
b=(12-sum)%11
if(str(b)==n[-1]):
    print("这是一个正确的身份证号码。")
else:
    print("这是一个错误的身份证号码。")
