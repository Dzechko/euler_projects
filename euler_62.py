from itertools import permutations
import math


def perms(x):
    ls = []
    perm = permutations(str(x))
    for p in perm:
        k = ''.join(p)
        ls.append(int(k))
    return ls



def cube(x):
    return x * x * x


def cube_root(x):
    y = x**(1/3)
    z = math.ceil(y)
    if z ** 3 == x:
        return True



'''print(perms(3453))
print(cube(78))'''

for j in range(345,346):
    k = perms(cube(j))
    print(len(k))
    u = list(set(k))
    print(len(u))
