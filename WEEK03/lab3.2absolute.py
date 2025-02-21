# Run a program to print absolute value of a number
# Author Deepika Gusain
# prompt user to enter a number and convert to float which is stored in variable number
number = float(input("Enter a number:"))
# used function abs to take number as argument and store in variable absolteValue
absoluteValue = abs(number)
# Print the absolute value of the entered number in the order
print ("{} absolute is {}".format(number,absoluteValue))