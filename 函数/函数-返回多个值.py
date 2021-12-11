def max_min(num):
    #print(num)
    return max(num), min(num)

ss =  input()
sss = ss.split(' ')
#print(sss)

a, b  = max_min(sss)
print(a, b)