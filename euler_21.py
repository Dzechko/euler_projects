amicable_numbers = []

for i in range(2, 10000):
    sum_divisors_i = sum(j for j in range(1, i) if i % j == 0)

    # Check if the sum of divisors of i is a valid number and not equal to i
    if sum_divisors_i != i and sum_divisors_i < 10000:
        sum_divisors_sum = sum(j for j in range(1, sum_divisors_i) if sum_divisors_i % j == 0)

        # Check if the sum of divisors of the sum_divisors_i equals i
        if sum_divisors_sum == i:
            amicable_numbers.append((i, sum_divisors_i))

