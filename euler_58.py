def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for j in range(3, int(x ** 0.5) + 1, 2):
        if x % j == 0:
            return False
    return True


def seq(n):
    sequence1 = []
    sequence2 = []
    sequence3 = []
    sequence4 = []

    complete_list = []

    for s in range(1, n, 2):
        sequence1.append(s ** 2)
    for s in range(2, n, 2):
        sequence2.append(s ** 2 + 1)
    for s in range(1, n - 1, 2):
        sequence3.append(s ** 2 + (s + 1))
    for s in range(2, n, 2):
        sequence4.append(s ** 2 + (s + 1))

    complete_list = sequence3 + sequence4 + sequence2 + sequence1

    count = 0
    for j in range(len(complete_list)):
        if is_prime(complete_list[j]):
            count += 1

    return count/len(complete_list)

for j in range(3,5000):
    if seq(j) < 0.10:
        print(j,seq(j))
