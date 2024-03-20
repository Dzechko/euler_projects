def seq_e(n):
    ls=[1]
    for i in range(2,n):
        if i % 2 ==0:
            ls.append(i)
        else:
            ls.append(1)
            ls.append(1)
    return ls

print(seq_e(36))


