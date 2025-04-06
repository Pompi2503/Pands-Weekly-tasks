# This program only define function to diaply Modules and  and DoView, there is no O/P
# no list and decitinary is defined here

def displayModules(modules):
    print("\tName \tGrade")  # Print header
    for module in modules:  # Loop through the list of modules
        print(f"\t{module['name']} \t{module['grade']}")  # Corrected f-string

def doView(students):
    for currentStudent in students:  # Loop through the list of students
        print(currentStudent["name"])  # Print student name
        displayModules(currentStudent["modules"])  # Call function to display modules
