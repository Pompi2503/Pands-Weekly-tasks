# program to check whether today is a weekday or a weekend
# this will import datetime module to access current date
import datetime
# Retrive today's day of the week
today = datetime.datetime.today().weekday()
# check if weekday or weekend
if today < 5:
    print("Yes, unfortunately today is a weekday")
else:
    print("It is the weekend")
