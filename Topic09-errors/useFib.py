# useFib.py
import myFunctions

n = int(input("How many Fibonacci numbers? "))
try:
    print(myFunctions.fibonacci(n))
except ValueError as ve:
    print("Error:", ve)
    