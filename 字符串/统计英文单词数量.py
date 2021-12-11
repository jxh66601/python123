import string
s=input()
for i in string.punctuation:
    s = s.replace(i, ' ')
print(len(s.split()))