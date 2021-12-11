import string

str = input()
number = int(input())
def kaisa(str, number):
    lower = string.ascii_lowercase          #小写字母
    upper = string.ascii_uppercase          #大写字母
    before = string.ascii_letters
    after = lower[number:] + lower[:number] + upper[number:] + upper[:number]
    table = ''.maketrans(before, after)
    return str.translate(table)

print(kaisa(str, number))