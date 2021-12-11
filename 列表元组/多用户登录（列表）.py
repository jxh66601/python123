l1=["aaa","bbb","ccc"]
l2=["123456","888888","333333"]

#多用户登录
a=input()
b=input()
if a in l1:
    if b in l2 and l2.index(b)==l1.index(a):
        print("Success")
    else:
        print("Fail")
else:
    print("Wrong User")