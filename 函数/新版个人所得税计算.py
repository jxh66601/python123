# 新版个人所得税计算
salary = eval(input())
amount = salary - 5000
tax = 0

if salary < 0:
    print('请输入正数！')
else:
    if amount < 0:
        tax = 0
    elif amount > 0 and amount <= 3000:
        tax = amount * 0.03
    elif amount > 3000 and amount <= 12000:
        tax = amount * 0.1
    elif amount > 12000 and amount <= 25000:
        tax = amount * 0.2
    elif amount > 25000 and amount <= 35000:
        tax = amount * 0.25
    elif amount > 35000 and amount <= 55000:
        tax = amount * 0.3
    elif amount > 55000 and amount <= 80000:
        tax = amount * 0.35
    else:  # amount >80000:
        tax = amount * 0.45

    print('{:.1f}'.format(tax))