p = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
s = 'FGHIJKLMNOPQRSTUVWXYZABCDEdefghijklmnopqrstuvwxyzabc'
#大写字母用后面第5个替换，小写字母用后面第3个替换
plaincode = input()  #输入明文
ciphertext = ''      #密文
for i in plaincode:
    n = p.find(i)  #返回 i 在 字符串p中的位置序号，找不到时返回-1
    if n == -1:
        ciphertext = ciphertext + i
    else:
        ciphertext = ciphertext + s[n]
print(ciphertext)