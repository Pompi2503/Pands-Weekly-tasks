# run a program which takes float number and output an int
# Author Deepika Gusain
# Import math module
import math
# prompt user to enter number and convert it to float and store in variable numberTofloor
numberTofloor = float(input("Enter the number:"))
# using floor function from math module entered number is converted and stored in variable flooredNumber
flooredNumber = math.floor(numberTofloor)
# print the floored number in order
print("{} floored is {}".format(numberTofloor,flooredNumber))