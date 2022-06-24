

from sympy import div


x = [*range(1,21)]
print(x)

def divideBy(num):
    divCheck = 0
    for l in x:
        if num % l == 0:
            divCheck += 1

    return divCheck == 20

y = False
sumnum = 2520
while y == False:

    if divideBy(sumnum) == False:
        sumnum += 2520
        print(sumnum)
    elif divideBy(sumnum) == True:
        print(sumnum)
        y = True



