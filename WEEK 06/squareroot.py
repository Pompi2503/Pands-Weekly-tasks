# squreroort.py
# Author Deepika Gusain

# Program will create approximate square root using Newton's method (https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Babylonian_method)
# Function is defined to calculate approx, square root of a positive floating number (https://www.w3schools.com/python/python_functions.asp)

# function sqrt is defined with arument number and tolerance parameter which sets the level of precision
def sqrt(number, tolerance=1e-6):

# Intiate guess on the assumption that most number guess is half of the number
    result = number / 2.0 

# It controls the loop in Newton's method and ensure that the iteration continues untill the approximatiin is accuateg enough
    while abs(result * result - number) > tolerance:

# this ensures that new approximation is more accurate by averaging the current and alternative guess
# It then calculates midpoint between the two estimates
        result = (result + number / result) / 2.0 
        
# Return the final apporximate result
    return result

# User input loop to ensure valid positive number 
while True:

# try-except statement is used to ensure the program does not crash if the user enter the invalid input 
    try:
# Take input
        user_input = float(input("Please enter a positive number: ")) 
# If loop used checks  if input less than 0, it will proint error      
        if user_input <= 0:
            print("Error: Please enter a positive number.")
# Prompt again to enter number
            continue
# It will exit looping when valid input is entered
        break
# Try-expect part is part of exception handling
    except ValueError:
        print("Error: Invalid input. Please enter a valid floating-point number.")

# Calculate square root approximation
result = sqrt(user_input)

# Display output
print(f"The square root of {user_input} is approx. {result:.1f}.")
