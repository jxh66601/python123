def id15218(id15):
    ls = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    ecc = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
    sum = 0
    j = 0
    if int(id15[6:8]) >= 5:
        id17 = id15[0:6] + '19' + id15[6:]
    else:
        id17 = id15[0:6] + '20' + id15[6:]
    for i in id17:
        sum = sum + int(i) * ls[j]
        j = j + 1
    id18 = id17 + ecc[sum % 11]
    return id18

n = int(input())
with open('id15.txt','r',encoding='utf-8') as file:
    for i in range(n):
        line = file.readline()
        line = line.replace(line[0:15],id15218(line[0:15]))
        print(line.strip())
        # ls.append(line)
# with open('id18.txt','w',encoding='utf-8') as file:
#     file.writelines(ls)
# with open('id18.txt','w',encoding='utf-8') as file:
#     file.writelines(ls)