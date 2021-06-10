def normalize(name_lst):
    result = name_lst[0].upper() + name_lst[1:].lower()
    return result


name_list = eval(input())
res = list(map(normalize, name_list))
print(res)