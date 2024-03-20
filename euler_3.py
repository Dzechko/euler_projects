def is_prime(n):

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def divisor(x):
    ls = []
    i = 2
    while i <= x:
        if is_prime(i) and x % i == 0:
            ls.append(i)
            x = x // i  # Reduce x by dividing it by the prime factor
        else:
            i += 1

    print(ls)

divisor(600851475143)
