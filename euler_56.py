def digit_sum(x):
    s = str(x)
    dsum = 0
    for i in range(len(s)):
        dsum += int(s[i])
    return dsum


ls = []
for a in range(1, 100):
    for b in range(1, 100):
        ls.append(digit_sum(a ** b))

print(max(ls))


