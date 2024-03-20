def is_prime(x):
    if x<2:
        return False
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            return False
    return True


def generate_primes(limit):
    primes= [2]
    for i in range(3,limit,2):
        if is_prime(i):
            primes.append(i)
    return primes

def is_circular_prime(n):
    str_n = str(n)
    for i in range(len(str_n)):
        rotated = int(str_n[i:] + str_n[:i])
        if not is_prime(rotated):
            return False
    return True

def count_circular_prime(limit):
    circular_primes_count = 0
    primes = generate_primes(limit)

    for prime in primes:
        if is_circular_prime(prime):
            circular_primes_count += 1

    return circular_primes_count


result = count_circular_prime(1000000)
print(result)
