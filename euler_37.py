ls = [3, 7, 9, 7]
for j in range(len(ls) - 1):
    string1 = "".join(map(str, ls[:-1 - j]))
    string2 = "".join(map(str, ls[j+1:]))
    print(string1)
    print("---------------------")
    print(string2)

