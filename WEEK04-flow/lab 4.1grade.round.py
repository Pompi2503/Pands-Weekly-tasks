# The program read in a students pecentage
# prints out the corresponding grade
# Author Deepika Gusain
# prompt user to enter a % value and input function takes user value as string
# float converts the input string into a floating point number and store in var percentage
percentage = float(input("Enter the percentage"))
# convert the percentage to nearest whole number
percentage = round(percentage)
# print the rounded number
print(f"Rounded percentage: {percentage}")
# checks if the entered % is out of range, if out of range simply prints the number
if percentage < 0 or percentage > 100:
    print ("Enter a number between 0 and 100")
# If the percentage is less than 40, it prints "Fail"
elif percentage < 40:
    print("Fail")
# If the percentage is less than 50 but greater than 40, it prints "Pass"
elif percentage < 50:
    print("Pass")
# If the percentage is less than less 60 but greater than 50, it prints "Merit1"
elif percentage < 60:
     print ("Merit1")
# If the percentage is less than 70 but greater than 60, it prints "Merit2"
elif percentage < 70:
    print("Merit2")
# If the percentage is greater than 70 and less than 100, it prints "Distinction" 
else:
    print("Distinction")