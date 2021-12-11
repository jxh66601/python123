p = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
plaincode = input()  #输入明文
uppern = int(input())
lowern = int(input())
s = p[uppern:26]+p[0:uppern]+p[26+lowern:53]+p[26:26+lowern]

ciphertext = ''      #密文
for i in plaincode:
    n = p.find(i)  #返回 i 在 字符串p中的位置序号，找不到时返回-1
    if n == -1:
        ciphertext = ciphertext + i
    else:
        ciphertext = ciphertext + s[n]
print(ciphertext)