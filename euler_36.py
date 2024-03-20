def binary(x):
    ls = []
    while x > 0:
        a = x % 2
        x = x // 2
        ls.append(a)
    ls = ls[::-1]
    return "".join(map(str, ls))


def palindrome(n):
    flag = 0
    ns = [int(i) for i in str(n)]
    for j in range(int(len(ns) / 2)):
        if ns[j] == ns[len(ns) - j - 1]:
            flag = 0
        else:
            flag = 1
            break
    if flag == 0:
        return "".join(map(str, ns))


sum = 0
for i in range(1000000):
    if palindrome(i):
        if palindrome(binary(i)):
            sum += i

print(sum)
