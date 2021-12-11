#一个字符串，如果各字符反向排列与原字符串相同，则称为回文，如“上海自来水来自海上”，用户输入一个字符串，判断该字符串是否为回文。
str = input()
if str == str[::-1]:
    print('True')
else:
    print('False')