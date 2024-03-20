import  inflect
p = inflect.engine()
count = 0

for i in range(1, 1001):
    x = p.number_to_words(i)
    without_spaces = x.replace(" ", "")
    final = without_spaces.replace('-', '')
    count = count + len(final)
print(count)