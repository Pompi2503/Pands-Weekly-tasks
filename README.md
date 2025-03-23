# Week02 Task

## Overview 
This python program, prompts the use to enter two amounts in cents, add them, and display the sum in a format with a Euro sign and a decimal point separating Euros and cents.

## Requirements
 Python and Jupyter notebook (for running interactively)

## Usage
 1. The program will prompt user to enter two amounts in cents
 2. It will then add the amounts and display the total formatter amount in Euros (€).
 3. We can run program using python interpreter or a Jupyter notebook.

## Program Output
  Enter first Amount in cents:
  Enter second amount in cents:
  Total:

## Code Implementation
``` python
amt1 = int(input("Enter first amount in cents: "))  # input first amount
amt2 = int(input("Enter Second amount in cents: ")) # input second amount

Total_Amount = amt1 + amt2 # calculate total sum of the two amounts

Euro_part = Total_Amount // 100 # retrive the Euro part
Cents_part  Total_Amount % 100 # Retrive the Cents part

print(f"The total of two amounts is € {Euro_part}.{Cents_part:02d}") # print the total amount in Euro and cents upto two decimal places
```

## References
1. Python comments : https://www.w3schools.com/python/python_comments.asp
2. Python Variables: https://www.w3schools.com/python/python_variables.asp
3. Python Numbers: https://www.w3schools.com/python/python_numbers.asp
4. Python Arithmetic Operators: https://www.w3schools.com/python/python_operators.asp

# Week03 Task

## Overview 
This python program, prompts the use to enter 10 character a/c number and replaces forst digits with X and display last 4 digits

## Requirements
 Python, Visual Studio and Jupyter notebook (for running interactively)

## Usage
 1. The program will prompt user 10 char account number 
 2. It will then mask first 6 digits with X and displays last 4 digits

## Program Output
  Visible Account Num = XXXXXX1234

## Code Implementation
``` python
# Run a program that reads in a 10-character a/c number and replaces first 6 digits with X and show last 4
# Author Deepika Gusain
# Prompts the user to print 10-char acc number and stored in variable acc_num
acc_num = input("Enter a 10-character account number:")

# validate lenght of the account number to 10 char or else program display error msg
# if acc num is 10 char, firt 6 digits are replaced with X and keep last 4 using String slicing
if len(acc_num) == 10:
      visible_acc = 'XXXXXX' + acc_num[-4:]

# prints the account number first 6 digit masked      
      print("Visible Account number:", visible_acc)
else:
 # print error if account number do not meet length requirements    
      print("Invalid account number! Enter correct account number.")
``` 
## References
1. Python comments : https://www.w3schools.com/python/python_comments.asp
2. Python Variables: https://www.w3schools.com/python/python_variables.asp
3. Python if else: https://www.w3schools.com/python/python_conditions.asp
4. Python Arithmetic Operators: https://www.w3schools.com/python/python_operators.asp
5. Python String Slicing: https://www.w3schools.com/python/python_strings_slicing.asp

# Week04 Task

## Overview 
This program implements the Collatz sequence using a function collatz(n) and prompts the user to enter a positive integer to generate the sequence.

## Requirements
 Python, Visual Studio and Jupyter notebook (for running interactively)

## Usage
1.This program is a simple way to explore a famous unsolved mathematical problem.
2. Enters a positive integer when prompted and the program outputs the sequence follwoing collatz rules.
3. The sequence stops when 1 is reached.

## Program Output

## Code Implementation
     # collatz.py
     # Author Deepika Gusain
    # This implement Collatz conjecture
    # Function to calculate the next value in the Collatz sequence
    def collatz(n):
    while n != 1:
      print(n, end=" ")  # Print the current value, with space between numbers
      if n % 2 == 0:     # If the number is even
            n = n // 2
      else:              # If the number is odd
            n = 3 * n + 1
    print(1)  # Finally print 1, as the sequence ends when the value reaches 1

    # Main Program
    def main():
    # Prompt user to input a positive integer
    number = int(input("Please enter a positive integer: "))
    
    # Validate input (check if the number is positive)
    if number <= 0:
      print("Please enter a positive integer greater than 0.")
    else:
      collatz(number)  # Call the collatz function to generate the sequence

     # Run the program
     if __name__ == "__main__":
      main()
      
## References
1. Python comments : https://www.w3schools.com/python/python_comments.asp
2. Python Variables: https://www.w3schools.com/python/python_variables.asp
3. Collatz Conjecture: Wikipedia
4. Python Integer Division (//): Python Docs
5. Conditionals in Python: Python If-Else

# Week05 Task
## Overview 
This programs check whether today is a weekday or weekend

## Requirements
 Python, Visual Studio and Jupyter notebook (for running interactively)

## Usage
 The program will check on today's day

## Program Output
 ("Yes, unfortunately today is a weekday") if it is a weekday and ("It is the weekend") if it is weekend.
## Code Implementation
``` python
# program to check whether today is a weekday or a weekend
# this will import datetime module to access current date
import datetime
# Retrive today's day of the week
today = datetime.datetime.today().weekday()
# check if weekday or weekend
if today < 5:
    print("Yes, unfortunately today is a weekday")
else:
    print("It is the weekend")
```

## References
1.Python datetime Module: https://docs.python.org/3/library/datetime.html
2.Python weekday() Method: https://docs.python.org/3/library/datetime.html#datetime.date.weekday
3.Python Conditional Statements: https://docs.python.org/3/tutorial/controlflow.html

# WEEK06 Task

## Overview 
This program calculated the square root of a positive floating number by using Newton's method.

# Requirements
Python and Jupyter notebook (for running interactively)

## Purpose
1. This program will define the fucntion to calculate approximate square root of the positive floating number using Newtons's method, by taking parameters number whose sqaure root is to be approximated and  tolerance (stopping condition for approximation is 1e-6).Lower the tolerance, higher the iteration and precision in the output it delivers. Newton's methos ian iterative program that starts with initial guess and refines it. The initial guess for the square root is number/2.0 for many number, their actual square roos is close to half of the number.
2. Newton's method starts with an initial guess and iteratively refines it by averaging the entered number and the current estimate, effectively finding the midpoint between them. This process continues until the approximation reaches the desired accuracy, as defined by the set tolerance.
3. User input handling is performed using try-except to ensure that the user enters a valid positive number.It handles error if user enters a negative number by asking again to enter input.
4. The reuslt is computed by calling function sqrt and printing the result to 1 decimal place.

## Program Output
Please enter a positive number: 14.5
The square root of 14.5 is approx. 3.8.

## Code Implementation
``` python
def sqrt(number, tolerance=1e-6):# function sqrt is defined with arument number and tolerance parameter which sets the level of precision

    result = number / 2.0 # # Intiate guess on the assumption that most number guess is half of the number

    while abs(result * result - number) > tolerance: # It controls the loop in Newton's method and ensure that the iteration continues untill the approximatiin is accuateg enough

        result = (result + number / result) / 2.0 ## this ensures that new approximation is more accurate by averaging the current and alternative guess. It then calculates midpoint between the two estimates
    return result  # Return the final apporximate result

while True:# User input loop to ensure valid positive number 


    try: # try-except statement is used to ensure the program does not crash if the user enter the invalid input 
        user_input = float(input("Please enter a positive number: ")) # Take input

        if user_input <= 0: # If loop used checks  if input less than 0, it will proint error     
            print("Error: Please enter a positive number.")

            continue # Prompt again to enter number

        break # It will exit looping when valid input is entered

    except ValueError: # Try-expect part is part of exception handling
        print("Error: Invalid input. Please enter a valid floating-point number.")

result = sqrt(user_input)  #Calculate square root approximation

print(f"The square root of {user_input} is approx. {result:.1f}.") # Display output to 1 decimal point
```

## References
1. https://www.w3schools.com/python/python_while_loops.asp)
2. https://www.w3schools.com/python/python_functions.asp
3. https://www.w3schools.com/python/python_try_except.asp
4. https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Babylonian_method



