# promots user to guess anumber, until the user gets the right number
# Author Deepika Gusain
# 30 is set as number to be guessed in var numerToGuess
numberToGuess = 30
# prompts user to guess, input takes the input as string and int( )converts to int and store in guess variable
guess = int(input("Guess the number:"))
# this loop will until user guess matches numberToguess
while guess!= numberToGuess:
# print wrong if wrong guess and ask user to guess again and the loop repeat itself
    print("Wrong")
    guess = int(input("Guess again"))
# prints congratulatory msg on correct guess
print("Well done! yes the number was", numberToGuess) 
