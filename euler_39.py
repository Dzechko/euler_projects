def sides_of_triange(x):
    ls = []
    for a in range(2, x // 2):
        for b in range(2, x // 2):
            c = x - a - b
            sides = []
            if (a ** 2) + (b ** 2) == (c ** 2):
                sides = [a, b, c]

                ls.append(sides)
    unique_list = list(set(tuple(sorted(sub_list)) for sub_list in ls))

    return (unique_list)


s = []
for i in range(3,1000):
    if len(sides_of_triange(i)) == 8:
        print(sides_of_triange(i))




