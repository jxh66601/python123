
while 1:
        n=input()
        a, b, c, d = 0, 0, 0, 0
        if n != 'over':

            for i in n:
                if i.isdigit():
                    b = b + 1

                elif i.isalpha():
                    a = a + 1
                elif i.isspace():
                    c = c + 1
                else:
                    d = d + 1

        else:
            break
        print('非英文字母的字符数量为:', b + c + d)
