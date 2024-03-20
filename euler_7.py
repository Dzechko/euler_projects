def is_prime(x):
    if x <= 1:
        return False
    else:
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True


x = 2
ls = []
while len(ls)<10001:
    if is_prime(x):
        ls.append(x)
    x += 1

print(ls[-1:])