import math


def is_pentagon(x):
    n = (math.sqrt(24 * x + 1) + 1) / 6
    return n == int(n)


def is_triangle(x):
    n = (-1 + math.sqrt(1 + 8 * x)) / 2
    return n == int(n)


def is_hexagon(x):
    n = (math.sqrt(8 * x + 1) + 1) / 4
    return n == int(n)


def pentagon(p):
    v = (p * (3 * p - 1)) // 2
    return v


def triangle(p):
    v = (p * (p + 1)) // 2
    return v


def hexagon(p):
    v = p * (2 * p - 1)
    return v


for t in range(1, 1000000):
    if is_pentagon(triangle(t)):
        if is_hexagon(triangle(t)):
            print(triangle(t))
