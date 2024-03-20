def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(x ** 0.5) + 1, 2):
        if x % i == 0:
            return False
    return True


def count_ways(n, primes_list):
    ways = [0] * (n + 1)
    ways[0] = 1
    for prime in primes_list:
        for i in range(prime, n + 1):
            ways[i] += ways[i - prime]
    return ways[n]


def find_first_value(target_ways):
    primes = []
    i = 2
    while True:
        if is_prime(i):
            primes.append(i)
            ways = count_ways(i, primes)
            if ways > target_ways:
                return i
        i += 1


first_value = find_first_value(5000)
print(first_value)
