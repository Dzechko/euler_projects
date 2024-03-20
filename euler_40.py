ls = "".join(str(i) for i in range(1,1000000))
k = [int(i) for i in str(ls)]
p = k[0]*k[9]*k[99]*k[999]*k[9999]*k[99999]*k[999999]
print(p)