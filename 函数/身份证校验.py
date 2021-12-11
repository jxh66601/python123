nums=list(input())#18位身份证号码
weight=(7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2)
s=0
for i in range(17):
    s+=int(nums[i])*weight[i] #加权和，注意原身份证号码都是字符，需要转换为整数再参与计算
y=s%11 #和与11除的余数
code=(12-y)%11 #验证码=（12-余数）%11
if str(code)==nums[-1] or code==10 and nums[-1]=='X'  :
    print("这是一个正确的身份证号码。")
else:
    print("这是一个错误的身份证号码。")