# Program will read a text file and output number of e's in the file.
# Author: Deepika Gusain
# Import the sys module, which allows access to command-line arguments (https://docs.python.org/3/library/sys.html)
import sys

# Function count_e is defined that will take the filename as an argument
def count_e(filename):
    # To handle exceptions, a try block is used. The file will be opened in read mode. (https://docs.python.org/3/library/functions.html#open)  
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            # Reads the entire file into a string variable text.
            text = file.read()
            # This line of code ensures that all e's are counted and converts to lowercase in case of case-sensitive files (https://docs.python.org/3/library/stdtypes.html#str.count)
            return text.lower().count('e')
    # This will print an error message if the file is not found (https://docs.python.org/3/library/exceptions.html#FileNotFoundError)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None
    # It checks if the filename is a directory, not a text file (https://docs.python.org/3/library/exceptions.html#IsADirectoryError)
    except IsADirectoryError:
        print(f"Error: '{filename}' is a directory, not a file.")
        return None
    # This will print an error message if the file is not a valid text file (https://docs.python.org/3/library/exceptions.html#UnicodeDecodeError)
    except UnicodeDecodeError:
        print(f"Error: The file '{filename}' is not a valid text file.")
        return None
    # Catches any other unexpected errors and prints them
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Ensures that the script only runs when executed directly, not when imported as a module (https://docs.python.org/3/library/__main__.html)
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python count_e.py <filename>")
    else:
        filename = sys.argv[1]
        e_count = count_e(filename)
        if e_count is not None:
            print(f"The number of 'e' characters in '{filename}' is: {e_count}")
