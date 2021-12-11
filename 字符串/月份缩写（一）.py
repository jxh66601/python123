#month.py
months = "Jan.Feb.Mar.Apr.May.Jun.Jul.Aug.Sep.Oct.Nov.Dec."
n = int(input())
pos = (n - 1) *4
monthAbbrev = months[pos:pos+4]
print(monthAbbrev)

#或
a=int(input())
s = ['Jan.','Feb.','Mar.','Apr.','May.','Jun.','Jul.','Aug.','Sep.','Oct.','Nov.','Dec.']
print(s[a-1])