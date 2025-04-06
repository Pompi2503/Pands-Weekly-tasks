# Initialize the student dictionary
student = {}
student["name"] = input("Enter student name: ")

# Initialize an empty list for modules
student["modules"] = []

# Keep reading module names and grades until a blank module name is entered
while True:
    course_name = input("Enter module name (or press Enter to finish): ")
    
    if course_name == "":  # Stop when the user enters a blank module name
        break
    
    grade = int(input(f"Enter grade for {course_name}: "))  # Read the grade
    
    # Append the module details as a dictionary to the list
    student["modules"].append({"courseName": course_name, "grade": grade})

# Print out the entered student details
print("\nStudent Details:")
print(f"Student: {student['name']}")
for module in student["modules"]:
    print(f"\t{module['courseName']} \t: {module['grade']}")
    