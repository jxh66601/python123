id = input()
year = id[6:10]
month = id[10:12]
day = id[12:14]
if int(id[16]) % 2 == 0:
    gender = '女'
else:
    gender = '男'
print('出生：{}年{}月{}日'.format(year,month,day))
print('性别：{}'.format(gender))