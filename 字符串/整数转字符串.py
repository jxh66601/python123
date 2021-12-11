alphalist = [chr(x) for x in range(ord("A"), ord("Z")+1)]

def num2alpha(num):
    if num > 26:
        alpha, remainder = (num-1) // 26, num%26
        temp = result + num2alpha(alpha) + num2alpha(remainder)
    elif num>=0:
        temp = result + alphalist[num-1]
    else:
        temp = result
    return temp


if __name__ == "__main__":
    result = ""
    num = int(input())
    print(num2alpha(num))