from fractions import Fraction

'''def hcf(a, b):
    hcf = 0
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            cf = i
            if cf > hcf:
                hcf = cf
    return hcf
'''


def hcf_euclidean(a, b):
    while b != 0:
        a, b = b, a % b
    return a


'''value = 0
for n in range(1, 12000):
    for d in range(n + 1, 12001):
        if n < d:
            if hcf_euclidean(n, d) == 1:
                if Fraction(1, 3) < Fraction(n, d) < Fraction(1, 2):
                    value += 1

print(value)'''

count = 0
for d in range(2, 12001):
    for n in range(d//3 + 1, (d - 1) // 2 + 1):
        if hcf_euclidean(n, d) == 1:
            count += 1

print(count)
