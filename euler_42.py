def Trinum(x):
    i = 0
    flag = 0
    while True:
        if x == i/2*(i+1):
            flag = 1
            break
        i +=1
        if i > x/2:
            flag=0
            break
    if flag ==1:
        return True
    else:
        return False

words=[]
with open("words.txt", 'r') as file:
    file_contents = file.read()
    words = file_contents.split(",")
    words = [word.strip('""') for word in words]
alp = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

count = 0
for i in range(len(words)):
    sum = 0
    for j in range(len(words[i])):
        ls = [l for l in words[i]]
    for k in range(len(ls)):
        sum += alp[ls[k]]
    if Trinum(sum):
        print(words[i],sum)
        count+=1

print(count)






