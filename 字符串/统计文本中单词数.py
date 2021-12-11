def readFile(filename):
    txt = open(filename,'r').read()
    for ch in '!"#$%&()*+,./:;<=>?@[\\]^_‘{|}~\n':
        txt = txt.replace(ch, " ")   #将文本中特殊字符替换为空格
    return txt
name = input()
lsWords = readFile(name).split()
print(len(lsWords))