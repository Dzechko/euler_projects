cl = []
for i in range(2, 1000000):
    ls = []
    s = []
    while i != 1:
        if i % 2 == 0:
            i = i // 2
        else:
            i = 3 * i + 1
        ls.append(i)

    cl.append(len(ls))

print(cl)
count = 2
while cl[i] != max(cl):
    count  += 1
    i+=1
print(count)