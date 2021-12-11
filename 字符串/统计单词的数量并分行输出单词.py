import string
s = input()
for i in string.punctuation:
    if i in string.punctuation:
        s = s.replace(i,' ')
ls = s.split()
print(len(ls))
for i in ls:
    print(i)