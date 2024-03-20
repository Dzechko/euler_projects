from mpmath import mp


def is_irrational(x):
    sqrt_result = mp.sqrt(x)
    if sqrt_result != round(sqrt_result):
        return True


mp.dps = 105
final_sum = 0
for i in range(1, 101):
    if is_irrational(i):
        value = str(mp.sqrt(i))
        dec_part = value.split('.')
        k = dec_part[1][:99]
        ls = [int(x) for x in str(k)]
        z = sum(ls)+int(dec_part[0])
        final_sum += z
print(final_sum)
