# # Print an outcome of addition of two amounts in Euro denomination with upto two decimal points
# Author Deepika
# Input first amount (https://www.w3schools.com/python/python_reference.asp)
amt1 = int(input("Enter first amount in cents: ")) 

# Input second amount (https://www.w3schools.com/python/python_reference.asp)
amt2 = int(input("Enter Second amount in cents: "))

# Calculte summation of two amounts in cents(https://www.geeksforgeeks.org/python-operators/)
Total_Amount = amt1 + amt2

# Convert Cents to Euros(https://www.w3schools.com/python/python_reference.asp)
# First retrieve the Euro part
Euro_part = Total_Amount // 100
# Retrieve cents part
Cents_part = Total_Amount % 100
# Print total amount in Euro and cents upto 2 decimal places *https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/
print(f"The total of two amounts is € {Euro_part}.{Cents_part:02d}")
