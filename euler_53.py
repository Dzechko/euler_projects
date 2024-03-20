def factorial(x):
    f = 1
    if x == 0:
        return f
    for j in range(1, x + 1):
        f = f * j
    return f


def combination(n, r):
    counts = int(factorial(n) / (factorial(r) * factorial(n - r)))
    return counts


count = 0
for i in range(23, 101):
    for j in range(i):
        x = combination(i, j)
        if x > 1000000:
            count += 1
print(count)

