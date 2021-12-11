def cash(x):
    C1="零壹贰叁肆伍陆柒捌玖"
    C2="分角元拾佰仟万拾佰仟亿"
    m=round(x*100)
    i=0
    res=""
    while m != 0:
        n=m%10
        res=C1[n]+C2[i]+res
        m=m//10
        i=i+1
    return res

x=eval(input())
print(cash(x))