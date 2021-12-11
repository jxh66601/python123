price = float(input())
month = int(input())
mode = input()
rate = float(input())
if mode in ['AC','ACPI'] and 24 > month >= 3:
    if mode == 'AC':
        ls = []
        for i in range(1,month + 1):
            repayment = price / month + (price - price / month * i) * rate
            ls.append(round(repayment,2))
        print(ls)
    if mode == 'ACPI':
        repayment = price * rate * (1 + rate) ** month /((1 + rate) ** month - 1)
        print(round(repayment,2))
else:
    print('还款方式输入错误')