
def sumSquares(num):
    l = 0
    for i in range(1,num+1):
        l += i ** 2
    return l

def sqSum(num):
    rng = sum(range(1,num+1))
    return rng ** 2


sumnum = 100
print((sqSum(sumnum) - sumSquares(sumnum)))

