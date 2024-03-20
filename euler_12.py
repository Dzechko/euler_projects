s = 0
i = 1

while True:
    s += i
    count = 0

    for j in range(1, int(s**0.5) + 1):
        if s % j == 0:
            count += 2  # Count both j and s/j as divisors

    # If s is a perfect square, reduce the count by 1
    if int(s**0.5)**2 == s:
        count -= 1

    if count > 500:
        break

    i += 1

print(s)
'''j = 1: 28 % 1 == 0, so count is incremented by 2.
j = 2: 28 % 2 == 0, so count is incremented by 2.
j = 3: 28 % 3 != 0, no change in count.
j = 4: 28 % 4 == 0, so count is incremented by 2.
j = 5: 28 % 5 != 0, no change in count.'''