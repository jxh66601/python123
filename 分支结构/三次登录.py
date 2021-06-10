#**用户登录的三次机会**
#给用户三次输入用户名和密码的机会，要求如下：
    #如输入第一行输入用户名为 **‘Kate’**，第二行输入密码为 **‘666666’**，输出 ‘登录成功！’，退出程序；
    #当一共有 3 次输入用户名或密码不正确输出 “3次用户名或者密码均有误！退出程序。

for i in range(3):
    userName =  input()
    passWord = input()
    if userName == 'Kate' and passWord == '666666':
        print("登录成功！")
        break
else:
    print("3次用户名或者密码均有误！退出程序。")
