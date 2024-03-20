def is_prime(x):
    if x <= 1:
        return False
    else:
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True



n = 0
sum1 = 0
while n < 2000000:
    if is_prime(n):
        sum1 = sum1 + n
    n+=1

print(sum1)
