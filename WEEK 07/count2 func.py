FILENAME = "count.txt"

def readNumber():
    # Open the file and read the current count
    with open(FILENAME) as f:
        number = int(f.read())  # Convert the content to an integer
    return number

def writeNumber(number):
    # Open the file in write mode and save the updated count
    with open(FILENAME, "wt") as f:
        f.write(str(number))  # Write the number as a string

# Main part of the program
num = readNumber()  # Read the current count from the file
num += 1  # Increment the count
print(f"We have run this program {num} times")  # Print the updated count
writeNumber(num)  # Write the updated count back to the file