# collatz.py
# Author Deepika Gusain
# This implement Collatz conjecture
# collatz.py
# This program implements the Collatz Conjecture
# Author: Your Name

# Function to calculate and print the Collatz sequence
def collatz(n):
    while n != 1:
        print(n, end=" ")  # Print the current value
        if n % 2 == 0:     # If the number is even
            n = n // 2     # Divide it by 2
        else:              # If the number is odd
            n = 3 * n + 1  # Multiply by 3 and add 1
    print(1)  # Finally print 1, as the sequence ends when the value reaches 1

# Main Program
def main():
    # Ask the user to input a positive integer
    try:
        number = int(input("Please enter a positive integer: "))
        
        # Validate the input (check if the number is positive)
        if number <= 0:
            print("Please enter a positive integer greater than 0.")
        else:
            collatz(number)  # Call the collatz function to print the sequence
    except ValueError:
        print("Please enter a valid integer.")

# ensures code inside the main runs only when the scripts is executed dicrectly both a standalone and resuable program
if __name__ == "__main__":
    main()