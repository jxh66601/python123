#18位身份证号码：第7、8、9、10位为出生年份(四位数)，第11、第12位为出生月份，第13、14位代表出生日期，
#第17位代表性别，奇数为男，偶数为女。
#datetime.datetime.now().year
# datetime.datetiem.now().mouth
# datetime.datetiem.now().day

import datetime
id = input()
year = id[6:10]
month = id[10:12]
day = id[12:14]
if int(id[16]) % 2 == 0:
    sex = '女'
if int(id[16]) % 2 == 1:
    sex = '男'
print('你出生于{}年{}月{}日'.format(year,month,day))
print('你今年{}周岁'.format(datetime.datetime.now().year-int(year)))
print('你的性别为{}'.format(sex))