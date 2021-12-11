#黑客语（Leet）是从网络发展起来的一种文字书写方式。通常将英语中的字母替换为数字和特殊符号。这种方式被很多黑客组织所使用。
# 由于具有隐密性，所以它也广泛被用于密码中。使用Leet书写的密码，不会增加密码记忆的复杂度，但却可以提高密码的强度。
# 常见的转化规律有，5替换s,3替换e，4替换a，0替换o，1替换i等。例如，cats使用Leet书写，就变为c475。
# 一个纯字母的密码就转化为字母、数字、特殊符号构成的复杂密码了。
# table = ''.maketrans(before, after)     #这条语句可以创建映射表，str1.translate(table)语句可以将table中的字符按映射表中的顺序进行替换。
# 0 1 3 4 5 6 7
# o i e a s g t
#M4k3 G006l3 Y0ur H0m3p463!
#str1 = 'M4k3 G006l3 Y0ur H0m3p463!'
#str1 = 'Make Google Your Homepage!'
str1 = input()
before = '0134567'
after = 'oieasgt'
table = ''.maketrans(before, after)     #创建映射表
print(str1.translate(table))