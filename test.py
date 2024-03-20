from mpmath import mp

str1 = '414213562373095048801688724209698078569671875376948073176679737990732478462107038850387534327641572'
ls = [int(x) for x in str(str1)]
print(sum(ls))
print(len(str1))






# Set the desired precision to 101 decimal places
mp.dps = 101

# Calculate the square root of 2
sqrt_of_2 = mp.sqrt(2)

# Convert the result to a string for display
sqrt_str = str(sqrt_of_2)

# Print the result
print(sqrt_str)
