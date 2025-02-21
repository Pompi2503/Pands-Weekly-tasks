# run a program to generate random number with defined range
# Author Deepika Gusain
# import module random
import random
# User input for range
min_value = int(input("Enter the min value: "))
max_value = int(input("Enter the max value: "))
# Generate a random number within the specified range
num = random.randint(min_value,max_value)
# print the random number
print(f"Here is a random numer: {num}")

