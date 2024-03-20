def is_pentagonal(x):
    n = (1 + (1 + 24 * x) ** 0.5) / 6
    return n.is_integer()

def pentagonal(n):
    return n * (3 * n - 1) // 2

for j in range(1,10000):
    pj = pentagonal(j)
    for k in range(j+1,10000):
        pk = pentagonal(k)
        diff = abs(pk -pj)
        if is_pentagonal(pk+pj) and is_pentagonal(diff):
            print(diff)

