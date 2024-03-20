ls1 = []
ls2 = []
ls = []
for i in range(10, 98):
    for j in range(i + 1, 100):
        num_digits = [int(x) for x in str(i)]
        den_digits = [int(x) for x in str(j)]
        k = i / j
        for digits in num_digits:
            if digits in den_digits:
                num_digits.remove(digits)
                den_digits.remove(digits)
                break

        if den_digits[0] != 0 and len(num_digits) == 1 and len(den_digits) == 1 and (i % 10 and j % 10) != 0 and k == \
                num_digits[0] / den_digits[0]:
            print(f"{i}/{j} is equal to {num_digits[0]}/{den_digits[0]}")
