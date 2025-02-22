# Run a program to tell the use if the number is even or odd
# Auhtor Deepika Gusain
# prompt user to enter string "enter an integer" and store in variable number
number = int(input("Enter an integer"))
# check using modulus operator whether number is even or odd, check if remainder is 0
if (number % 2) == 0:
# print msg if remainder is 0
    print (f"{number} is an even number")
# this is executed if the if condition is false when number is not divisible by 2 wiht no remainder
else:
# prints the msg if the number is odd
    print (f"{number} is an odd number")