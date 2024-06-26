text = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

lines = text.split('\n')
arrayline = []
for line in lines:
    numbers = [int(x) for x in line.split()]
    arrayline.append(numbers)

def find_max_sum(row, col):
    # Base case: If we reach the bottom row, return the value
    if row == len(arrayline) - 1:
        return arrayline[row][col]

    # Recursive case: Move to the next row and consider the adjacent elements
    left_sum = find_max_sum(row + 1, col)
    right_sum = find_max_sum(row + 1, col + 1)

    # Return the maximum of the two possible paths plus the current element
    return arrayline[row][col] + max(left_sum, right_sum)

# Start the brute-force search from the top
max_sum = find_max_sum(0, 0)

print("Maximum sum from top to bottom:", max_sum)
