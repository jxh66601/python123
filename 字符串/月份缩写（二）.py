#month.py
months = "Jan.Feb.Mar.Apr.May.Jun.Jul.Aug.Sep.Oct.Nov.Dec."
n = int(input())
if n in range(1,13):
    pos = (n - 1) *4
    monthAbbrev = months[pos:pos+4]
    print(monthAbbrev)
else:
    print('请输入1~12之间的数字！')

或

a=int(input())
s = ['Jan.','Feb.','Mar.','Apr.','May.','Jun.','Jul.','Aug.','Sep.','Oct.','Nov.','Dec.']
if n in range(1,13):
    print(s[a-1])
else:
    print('请输入1~12之间的数字！')