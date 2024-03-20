'''import math
import sys

new_limit = 1500
sys.setrecursionlimit(new_limit)
from fractions import Fraction

def dec_to_frac(x):
    fraction = Fraction(x).limit_denominator()
    numerator = fraction.numerator
    denominator = fraction.Denominator
    return fraction


def sqrt_loop(n):
    if n == 1:
        return 1 / 2
    else:
        return 1 / (2 + sqrt_loop(n - 1))

count = 0
for j in range(1,1000):
    if len(str(dec_to_frac(1+sqrt_loop(j)).numerator)) >len(str(dec_to_frac(1+sqrt_loop(j)).denominator)):
        count+= 1

print(count)'''


# you don't need to use recursion

# An = An-1.numerator + 2*denominator / An-1 numerator + denominator

def sqrt_continued_fraction(iterations):
    numerator, denominator = 3, 2  # Initial values
    count = 0  # Counter for the desired fractions
    for _ in range(2, iterations + 1):
        numerator, denominator = numerator + 2 * denominator, numerator + denominator
        if len(str(numerator)) > len(str(denominator)):
            count += 1
    return count


# Find the count of fractions where numerator has more digits than denominator in the first 1000 expansions
result = sqrt_continued_fraction(1000)
print(result)
