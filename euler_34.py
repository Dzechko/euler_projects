

def fact(x):
    factorial = 1
    for j in range(x):
        factorial *= (x - j)
    return factorial


for i in range(10, 10000000):
    ls = [int(x) for x in str(i)]
    sum = 0
    for j in range(len(ls)):
        sum += fact(ls[j])
    if sum == i:
        print(sum)


