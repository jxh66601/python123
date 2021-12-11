#将输入中的中文数字替换为阿拉伯数字
s = input()
sIn = '零一二三四五六七八九'
sOut = '0123456789'
trans = str.maketrans(sIn,sOut)
print(s.translate(trans))