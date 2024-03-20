def is_relative_prime(a, b):
    for r in range(2, min(a, b) + 1):
        if a % r == 0 and b % r == 0:
            return False
    return True


def calculate_phi(n):
    phi = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            phi -= phi // p
        p += 1
    if n > 1:
        phi -= phi // n
    return phi


max_ratio = 0
max_position = 0

for i in range(2, 1000000):
    phi = calculate_phi(i)
    ratio = i / phi
    if ratio > max_ratio:
        max_ratio = ratio
        max_position = i
print(max_position)
