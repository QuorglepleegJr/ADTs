from random import randint, seed

def probability(x, total):

    product = 1

    for i in range(1,x):

        product *= total-i
    
    product /= (total ** (x-1))

    return product

def monte_carlo(x, total, PRECISION=1000000):

    count = 0

    for i in range(PRECISION):

        vals = {randint(0, total-1) for i in range(x)}

        if len(vals) != x:

            count += 1
    
    return 1-(count/PRECISION)

for i in range(2, 100000001):

    p = 1-probability(i, 100000000)

    print(i, ":", p)

    if p > 1/3:

        break