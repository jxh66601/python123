#**问题描述**
#给定一个整数列表 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的列表索引。
#每种输入只需要对应一个答案。但是，你不能重复使用这个数组中同样位置的元素。
#如果没找到解，输出“Fail”

nums = input().split()
nums = [int(nums[i]) for i in range(len(nums))]
target = eval(input())
lens = len(nums)
x = -1
for i in range(lens):
    if (target - nums[i]) in nums:
        if (nums.count(target - nums[i]) == 1) and (target - nums[i] == nums[i]):
            continue
        else:
            x = nums.index(target - nums[i], i + 1)
            break
if x > 0:
    print('{} {}'.format(i, x))
else:
    print('Fail')




#给定某数字A（1≤A≤9）以及非负整数N（0≤N≤100000），求数列之和S=A+AA+AAA+⋯+AA⋯A（N个A）。例如A=1, N=3时，S=1+11+111=123。
#当输入数字不符合要求时输出“data error”

# A = int(input())
# N = int(input())
# sum = 0
# if 1 <= A <= 9 and 0 <= N <= 100000:
#     tmp = A
#     for i in range(N):
#         sum = sum + tmp
#         tmp = tmp * 10 +A
#     print(sum)
# else:
#     print('data error')