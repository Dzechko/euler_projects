from itertools import permutations
def is_prime(x):
    if x < 2:
        return False
    for p in range(2, int(x ** 1 / 2) + 1):
        if x % p == 0:
            return False
    return True


def is_permuted(x, y):
    x = str(x)
    y = str(y)
    ls = []
    perms = permutations(x)
    for perm in perms:
        ls.append(''.join(perm))
    if y in ls:
        return True


def main():
    for j in range(1300, 3000):
        if is_prime(j):
            for k in range(j + 1, 9000):
                if is_prime(k) and is_permuted(k, j):
                    d = k - j
                    f = k + d
                    if is_prime(f) and is_permuted(k, f):
                        print(j, k, f)


if __name__ == '__main__':
    main()
