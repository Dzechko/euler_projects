def generate_primes(limit):
    primes = []
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            primes.append(i)
            for j in range(i*i, limit + 1, i):
                sieve[j] = False
    for i in range(int(limit**0.5) + 1, limit + 1):
        if sieve[i]:
            primes.append(i)
    return primes

def find_longest_consecutive_prime_sum(primes):
    max_length = 0
    max_prime_sum = 0
    for i in range(len(primes)):
        current_sum = primes[i]
        length = 1
        for j in range(i + 1, len(primes)):
            current_sum += primes[j]
            length += 1
            if current_sum > 1000000:
                break
            if current_sum in primes and length > max_length:
                max_length = length
                max_prime_sum = current_sum
    return max_prime_sum

print(generate_primes(40))
