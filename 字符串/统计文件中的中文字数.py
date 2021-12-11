def readFile(filename):
    txt = open(filename,'rb')
    content = txt.read().decode('utf-8')
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~\n！？，。：；、｛｝【】“”％￥＃＠……＆×（）——＋':
        content = content.replace(ch, "")   #将文本中特殊字符替换为空格
    return content
name = input()
lsWords = readFile(name).split()
print(len(readFile(name)))