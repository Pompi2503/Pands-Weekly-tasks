# accounts.py 

# Run a program that reads in a 10-character a/c number and replaces first 6 digits with X and show last 4
# Author Deepika Gusain

# Prompts the user to print 10-char acc number and stored in variable acc_num (https://www.w3schools.com/python/python_reference.asp)
acc_num = input("Enter a 10-character account number:")

# validate lenght of the account number to 10 char or else program display error msg
# (https://www.w3schools.am/python/ref_func_len.html#gsc.tab=0)

# if acc num is 10 char, firt 6 digits are replaced with X and keep last 4 using Strong slicing
if len(acc_num) == 10:
# (https://www.w3schools.com/python/python_strings.asp)
      visible_acc = 'XXXXXX' + acc_num[-4:]

# prints the account number first 6 digit masked(https://www.w3schools.com/python/python_reference.asp)     
      print("Visible Account number:", visible_acc)
else:
# print error if account number do not meet length requirements    
      print("Invalid account number! Enter correct account number.")



