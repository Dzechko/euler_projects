from itertools import permutations


def permuted_digits(digit):
    perm = []
    perms = permutations(str(digit))
    for p in perms:
        perm.append(int(''.join(map(str, p))))
    return perm


for i in range(100, 1000000):
    k = len(str(i))
    if len(str(2 * i)) == k and len(str(3 * i)) == k and len(str(4 * i)) == k and len(str(5 * i)) == k and len(
            str(6 * i)) == k:
        ls = permuted_digits(i)
        if all(i * j in ls for j in range(2, 7)):
            print(i)
