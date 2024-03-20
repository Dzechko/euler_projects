def is_pandigital(x):
    digits = set(x)
    if len(digits) == 9 and all(digit in digits for digit in range(1, 10)):
        return True
    else:
        return False

pan = []

for i in range(1, 10000):
    ls = []
    for j in range(1, 1000):
        k = str(i * j)
        ls.extend([int(d) for d in str(k)])
        if len(ls) == 9:
            if is_pandigital(ls):
                final = ''.join(map(str, ls))
                pan.append(final)
                break

print(pan)

