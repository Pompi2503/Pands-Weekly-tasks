# Modified version of accounts.py
# input account number of any length
# Assumption 1 if account number has 4 or less than 4 digist we need to show the full A/c num
# Assumptions 2 if it has more than 4 digits, we will show last 4 digits and mask rest
# Assumptions 3 program should check for any non-numeric characters and prompt user
# prompt user to enter accout number of any length
acc_num = input("Enter the account number:")
# check if account lenght is 0, prompt user to enter value, and display error
if len(acc_num) == 0:
    print("Invalid Account number! Need value on account number")
# check if acc number does not contain any special char or spaces and prompt user    
elif not acc_num.isalnum():
    print("Invalid Account number! should not have alphanumeric char")
else:
# if lenght is greater than 4,all char are replaced expect last 4    
    if len(acc_num) > 4:
        visible_acc = "X" * (len(acc_num) - 4) + acc_num[-4:]
    else:
# if account number is 4 char or fewer, it will display in full      
        visible_acc = acc_num
 # print the masked account number       
print("Visible Acc number:",visible_acc)


