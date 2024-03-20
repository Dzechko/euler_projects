def is_palindrome(x):
    x = str(x)
    for i in range(len(x) // 2):
        if x[i] != x[len(x) - 1 - i]:
            return False
    return True


def reverse(x):
    x1 = str(x)
    rev = x1[::-1]
    return int(rev)


lychrel_count = 0
for i in range(196, 10000):
    true = i
    for k in range(50):
        if is_palindrome(i + reverse(i)):
            break
        else:
            i += reverse(i)
        if k == 49 and not is_palindrome(i + reverse(i)):
            lychrel_count += 1

print(lychrel_count)
