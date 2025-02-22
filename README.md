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
  
  
  Total:
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