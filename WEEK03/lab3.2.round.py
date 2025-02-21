# run a program to round a number
# Author Deepika Gusain
# displays the prompt " Enter the number" and converts the input from a string to a floatig point number
# converted float is stored in variable numberToround
numberToround = float(input("Enter a number:"))
# round function takes numberToround as an argument and covert to nearest integer
# Store the rounded number in variable roundNumber
roundNumber = round(numberToround)
# Print function is used to display the output on screen
# first placeholder hold numerToround and second will hold roundnumber
# format take the values of numberTo round and roundNumber and insert in string in the order they appear
print("{} rounded is {}".format(numberToround,roundNumber))

