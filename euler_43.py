from itertools import permutations


prime = [2, 3, 5, 7, 11, 13, 17]
ls = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
permutation = permutations(ls)
sum = 0
for words in permutation:
    flag = 1

    for j in range(1, 8):
        product = words[j]+words[j+1]+words[j+2]
        product = int(product)

        if product % prime[j-1] == 0:
            flag = 1
        else:
            flag = 0
            break

    if flag == 1:
        num = int(''.join(map(str,words)))
        sum += num
print(sum)