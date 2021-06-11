# -*- coding: utf-8 -*-
from functools import reduce
def str2float(s):
   for n in range(len(s)):
       if s[n]=='.':
           count=len(s)-n-1
           break
   s=s.split('.',1)
   def fn(x, y):
        return x * 10 + y
   def char2num(s):
       return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
   num1=reduce(fn,map(char2num,s[0]))
   num2=reduce(fn,map(char2num,s[1]))/(10**count)
   return num1+num2

str_num_float = input()

res = str2float(str_num_float)
print(res)