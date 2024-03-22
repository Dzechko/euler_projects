# no of rectangles in a grid of mxn
# count = [m(m+1)n(n+1)]/4


def no_of_rectangles(m, n):
    return int(m * (m + 1) * n * (n + 1) / 4)


min_value = 0
target = 2000000
m = 0
n = 0

for i in range(1, 500):
    for j in range(1, 500):
        if no_of_rectangles(i, j) < target:
            x = no_of_rectangles(i, j)
            if x > min_value:
                min_value = x
                m = i
                n = j

print(m*n)
