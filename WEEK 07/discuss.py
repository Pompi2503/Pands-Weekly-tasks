# initialising a file 
import os.path 
FILENAME = "count.txt" 
def writeNumber(number):
    with open(FILENAME, "wt") as f:  # Use "wt" mode to write as text
        f.write(str(number))  # Convert the number to a string before writing
if not os.path.isfile(FILENAME): 
 print("File does not exist") 
#initialise file here 
writeNumber(0)