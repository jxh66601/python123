def product(L):
    from functools import reduce

    def mul(n1, n2):
        return n1 * n2
    return reduce(mul, L)


numbers = eval(input())  # [1,2,3,4,5]
print(product(numbers))