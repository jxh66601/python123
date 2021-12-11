#编写一个str2float函数，支持把字符串’123.456’转换成浮点数123.456。
#要求利用map和reduce实现。
# 代码尽可能精简：使用lambda表达式
# 需要增加函数处理‘意外’的能力：
#  - 输入不带小数点的数字，也可以正确执行得到结果
#  - 输入的数字位数小于2位，比如1.1，也应该可以正确得到结果。

def str2float(str_num):

    def filter_inputs():
        s = str(str_num)
        if s.find('.') < 0:
            # print("找不到小数点")
            s += '.0'
        s = s.split('.')  # 小数部分和整数部分分开['123', '45']
        if len(s[0]) < 2:
            s[0] = '0' + s[0]
        if len(s[1]) < 2:
            s[1] += '0'
        return s

    filtered = filter_inputs()
    from functools import reduce

    def get_num(s):
        return int(ord(s) - ord('0'))

    res_pre = reduce(lambda x,y: x*10 + y, map(get_num, filtered[0]))          # 整数部分
    res_later = reduce(lambda x, y:x*0.1 + y*0.01,map(get_num, filtered[1]) )  # 小数部分map(get_num, s[1])
    # print(res_pre)
    # print(res_later)
    return float(res_pre + res_later)


res = str2float(input())
print(res)