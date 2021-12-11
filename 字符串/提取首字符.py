s = input()
if s[0] != '':
    key = s[0]
else:
    key = ''
for i in range(len(s)):
    if s[i] == ' ' and s[i+1] != ' ':
        key = key + s[i+1]
print(key)