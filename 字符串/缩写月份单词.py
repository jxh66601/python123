# str.upper()	转换字符串str中所有字母为大写
# # str.lower()	转换字符串str中所有字母为小写
# # str.capitalize()	把字符串str的第一个字符大写

month = input().lower().capitalize()
monthlist = ['January','February','March','April','May','June','July','August','September','October','November','December']
if month in monthlist:
    print(month[:3]+'.')
else:
    print('spelling mistake')