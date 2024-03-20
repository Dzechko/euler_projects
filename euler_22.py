
sorted_list=[]
score = []
with open("0022_names.txt", "r")as file:
    for line in file:
        x = line.split(",")

names_list = [name.strip("'") for name in x]
sorted_list = sorted(names_list)
sorted_list = [name.strip('"') for name in sorted_list]


def alphabet_sum(word):
    alphabet = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11,
                'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21,
                'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

    word = word.upper()

    total_sum = sum(alphabet[letter] for letter in word if letter in alphabet)

    return total_sum
x = 0
for i in range(len(sorted_list)):
    x = (i+1) * (alphabet_sum(sorted_list[i]))
    score.append(x)
print(score)


print(sum(score))



