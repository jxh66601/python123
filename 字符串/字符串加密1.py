#用户输入包括大小写字母和数字的字符串，将其中的大写字母用该字符后的第4个字符替代，实现加密

str = input()
for i in str:
    if ord('A') <= ord(i) <= ord('Z'):    #判断大写字母，对其进行加密
        print(chr(ord('A') + (ord(i) - ord('A') + 4) % 26),end='')
    else:
        print(i,end='')

p = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
s = 'EFGHIJKLMNOPQRSTUVWXYZABCD'
plaincode = input()  #输入明文
ciphertext = ''      #密文
for i in plaincode:
    n = p.find(i)  #返回 i 在 字符串p中的位置序号，找不到时返回-1
    if n == -1:
        ciphertext = ciphertext + i
    else:
        ciphertext = ciphertext + s[n]
print(ciphertext)