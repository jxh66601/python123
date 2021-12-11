items = 1
while items < 4:
    username = input()
    password = input()
    if username == 'admin' and password == '123456':
        print("登录成功！")
        break
    else:

        if items != 3:
            print("第{}次登录失败,请重新输入！".format(items))

        elif items == 3:
            print("登录失败3次，账号已锁定！")
            break
        items += 1