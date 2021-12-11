def sum():
    two_num = input()
    ss = two_num.split(' ')
    #print(ss)
    ss.remove('')
    #print(ss)
    sum = 0
    for x in ss:
        sum += int(x)
    print(sum)


sum()