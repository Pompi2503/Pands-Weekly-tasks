# run a program which accepts floating point input and uses absolute value of the input and print result in cents
# Author Deepika Gusain
# prompt to enter number in dollars and convert to floating number 
# Converted amount is stored in variable amt_in_dollars
amt_in_dollars = float (input("Enter the number:"))
# convert number to absolute value and store in variable abs_Value
abs_Value = abs(amt_in_dollars)
# Convert amount in cents as accepted by the bank
amt_in_cents = abs_Value * 100
# convert to integer to remove any decimal fractions
amt_in_cents = int(amt_in_cents)
# print the amount in cents with no decimal places
print(f"The amount in cents:{amt_in_cents}")