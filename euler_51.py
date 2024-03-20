import math


def is_prime(x):
    if x < 2:
        return False
    for j in range(2, int(math.sqrt(x)) + 1):
        if x % j == 0:
            return False
    return True


def no_of_primes(ls):
    count = 0
    for n in range(len(ls)):
        if is_prime(ls[n]):
            count += 1
    return count


def permutation_of_same_digit(fp, sp, k):
    total = []
    kl = k[:]
    for m in range(10):
        kl[fp] = m
        kl[sp] = m
        digit = ''.join(map(str, kl))
        digit = int(digit)
        if is_prime(digit):
            total.append(digit)
    return total


def input(digit):
    k = [int(x) for x in str(digit)]
    for f in range(len(k)):
        for s in range(f + 1, len(k)):
            z = permutation_of_same_digit(f, s, k)
            if no_of_primes(z) == 7:
                print(z)

input()
