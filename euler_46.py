def is_oddComp(x):
    count = 0
    if x % 2 != 0:

        for j in range(1, x + 1):
            if x % j == 0:
                count += 1
    if count > 2:
        return True


def is_twice_square(n):
    sqrt_half = (n / 2) ** 0.5
    if sqrt_half.is_integer():
        return True


def prime(x):
    if x < 2:
        return False
    for f in range(2, int(x ** 0.5) + 1):
        if x % f == 0:
            return False
    return True


ls = []
ls2 = []
for j in range(9, 10000):
    if is_oddComp(j):
        is_sum = False
        for p in range(2, j - 1):
            if prime(p):
                s = j - p
                if is_twice_square(s):
                    ls.append(j)

ls = list(set(ls))
print(ls)
for k in range(9,10000):
    if is_oddComp(k):
        if k not in ls:
            print("values", k)
