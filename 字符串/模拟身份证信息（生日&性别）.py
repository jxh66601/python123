c=input()
if len(c)!=18:
    print("ERROR")
else:
    print("{}年{}月{}日".format(c[6:10],c[10:12],c[12:14]))
    if int(c[-2])%2==1:
        print("男")
    else:
        print("女")