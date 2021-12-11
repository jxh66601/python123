ss=input()
while ss != 'over':
    n=0
    for x in ss:
        if not x.isalpha() :
            n=n+1
    print('非英文字母的字符数量为:',n)
    ss=input()  