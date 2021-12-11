c = input()
str = input()
pos = str.find(c)
if pos == -1:
    print('Not Found')
else:
    print('index = {}'.format(pos))