fib = [1, 1]
i = 0
while True:
    x = (fib[i] + fib[i+1])
    fib.append(x)
    i = i + 1
    if len(str(x)) == 1000:
        print(i+2) # because fib[0] and fib[1] already defined
        break






