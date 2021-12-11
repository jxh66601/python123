#判断密码字符串长度是否大于8
#是否包含数字     string.digits          可返回'0123456789'
#是否包含小写字母 string.ascii_lowercase 可返回'abcdefghijklmnopqrstuvwxyz'
#是否包含大写字母 string.ascii_uppercase 可返回'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#是否包含特殊字符 string.punctuation     可返回'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
#长度小于8弱密码，长度大于等于8且包含至少2种字符为中等强度，包含3种字符为较强，包含全部4种字符为极强。


import string

pwd = input()
strong = d = al = au = pu = 0
for ch in pwd:
    if ch in string.digits:   #是否包含数字
        d = 1
    elif ch in string.ascii_lowercase:  #是否包含小写字母
        al = 1
    elif ch in string.ascii_uppercase:   #是否包含大写字母
        au = 1
    elif ch in string.punctuation:  #是否包含指定的标点符号
        pu = 1
if len(pwd) < 8:
    strong = 0
else:
    strong = d + al + au + pu
if strong < 2:
    print('弱')
elif strong == 2:
    print('中')
elif strong == 3:
    print('强')
elif strong == 4:
    print('极强')