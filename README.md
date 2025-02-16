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
amt1 = int(input ("Enter first amount in cents: ")) # input first amount
amt2 = int(input ("Enter Second amount in cents: ")) # input second amount
Total_Amount=amt1+amt2 # calculate total sum of the two amounts
Euro_part=Total_Amount//100 # retrive the Euro part
Cents_part=Total_Amount%100 # Retrive the Cents part
print(f"The total of two amounts is € {Euro_part}.{Cents_part:02d}") # print the total amount in Euro and cents upto two decimal places
### References
1. Python comments : https://www.w3schools.com/python/python_comments.asp
2. Python Variables: https://www.w3schools.com/python/python_variables.asp
3. Python Numbers: https://www.w3schools.com/python/python_numbers.asp
4. Python Arithmetic Operators: https://www.w3schools.com/python/python_operators.asp
