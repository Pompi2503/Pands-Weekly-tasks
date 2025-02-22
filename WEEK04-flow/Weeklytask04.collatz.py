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