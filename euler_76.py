
def sum_as_positive_numbers(n):
    for i in range(1,n):
        ls = []
        k = n - i
        ls.append(k)
        for j in range(n-k,0,-1):
            ls.append(j)
            if sum(ls) == n:
                pass
                

sum_as_positive_numbers(12)