def normalize(name_item):
    return name_item[0].upper() + name_item[1:].lower()

name_list = eval(input())
res = map(normalize, name_list)
print(list(res))