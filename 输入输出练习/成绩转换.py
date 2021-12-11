#用户输入百分制的学生成绩，成绩大于或等于60的判定为“pass”，否则为“fail”
#用于初学，不考虑异常数据

score = float(input())
if score >= 60:
    print('pass')
else:
    print('fail')