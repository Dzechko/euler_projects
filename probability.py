import random
for i in range(1,7):
    count = 0
    for j in range(100):
        r = random.randint(1,6)
        if r == i:
            count += 1
    print("probability of ",i,"is",count/100)



