import math


def distinct_prime_factors(n):
    factors = set()
    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0:
            factors.add(i)
            n //= i
    if n > 1:
        factors.add(n)
    return factors


consecutive_count = 0
current_number = 1

while consecutive_count < 4:
    prime_factors = distinct_prime_factors(current_number)
    if len(prime_factors) == 4:
        consecutive_count += 1
    else:
        consecutive_count = 0
    current_number += 1

first_number = current_number - 4
print(first_number)
