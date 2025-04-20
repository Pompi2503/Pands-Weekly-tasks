import datetime as dt
from timesheetentry import Timesheetentry  # Import the Timesheetentry class

class Employee:
    # Instance-level attribute for storing timesheets specific to an employee
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.timesheets = []  # Initialize the timesheets list for this employee

    def __str__(self):
        return f"{self.first} {self.last}"

    # Method to log minutes worked on a project
    def logminutes(self, project, minutes):
        now = dt.datetime.now()  # Correctly call datetime.now()
        timesheetentry = Timesheetentry(project, now, minutes)  # Create Timesheetentry instance
        self.timesheets.append(timesheetentry)  # Add the entry to the employee's timesheets

    # Method to get the total time worked from all logged timesheets
    def gettotaltime(self):
        total_minutes = 0
        for ts in self.timesheets:  # Loop over the timesheet entries
            total_minutes += ts.duration  # Add the duration of each entry
        return total_minutes


# Main logic to test the functionality
if __name__ == '__main__':
    # Create an Employee instance
    test = Employee('some', 'one')
    print(test)  # This will call the __str__ method
    assert ('some one' == str(test))  # Assertion to check correct output

    # Log some timesheet entries
    test.logminutes('p1', 30)
    test.logminutes('p1', 60)

    # Get and print the total time worked
    mins = test.gettotaltime()
    print(mins)  # Expected output: 90

    # Assert that the total time is correct
    assert (mins == 90)

    print('all good')
