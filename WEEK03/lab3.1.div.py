# run a program that reads in two numbers
# ouput integer valye and the remainder
# Author Deepika Gusain
# Read the first number
x = int(input("Enter the first numb: ")) 
# Read the second number
y = int(input("ENter the second num: "))
# Perform the division function with no decimal value
ans = x//y
# Perform fucntion to give remainder
remainder = x%y
print("{} divided by {} is {} with remainder {}".format (x,y,ans,remainder))
