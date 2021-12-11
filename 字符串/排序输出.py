def bubble_sort(lists):
    # 冒泡排序
    count = len(lists)
    for i in range(0, count):
        for j in range(i + 1, count):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
        #print(lists[i],end = ' ')
    #print()
    return lists

lists = list(map(int,input().split(' ')))
bubble_sort(lists)
print(','.join(map(str,lists)))