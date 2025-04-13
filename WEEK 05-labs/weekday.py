# weekday.py 
# Author Deepika Gusain
# program to check whether today is a weekday or a weekend

# this will import datetime module to access current date(https://www.w3schools.com/python/python_datetime.asp)
import datetime

# Retrive today's day of the week(https://docs.python.org/3/library/datetime.html)
today = datetime.datetime.today().weekday()

# check if weekday or weekend (https://www.w3schools.com/python/python_conditions.asp)
if today < 5:
    print("Yes, unfortunately today is a weekday")
else:
    print("It is the weekend")
