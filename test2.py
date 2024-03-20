def is_pentagonal(x):
    n = (1 + (1 + 24 * x) ** 0.5) / 6
    return n.is_integer()

def pentagonal(n):
    return n * (3 * n - 1) // 2

min_diff = float('inf')

for j in range(1, 10000):
    Pj = pentagonal(j)
    for k in range(j + 1, 10000):
        Pk = pentagonal(k)
        diff = Pk - Pj
        if is_pentagonal(Pk + Pj) and is_pentagonal(diff):
            if diff < min_diff:
                min_diff = diff

print("The minimum difference D for which the sum and difference are pentagonal is:", min_diff)
