# Create Student Dict with course name and grades
# Auhtor Deepika Gusain
# define a dictionary named studeny with two keys name and modules. 
# Modules key stores a list of two dictionary representing course and grade
student = { 
    "name": "Mary", 
    "modules": [ 
        { 
            "courseName": "Programming", 
            "grade": 45 
        }, 
        { 
            "courseName": "History", 
            "grade": 99 
        } 
    ] 
}
# retrieves student name from the dictionar
print("Student: {}".format(student["name"]))
# Iterates over each dictionary inside the "modules" list.
for module in student["modules"]:
# module["courseName"] retrieves the course name
# module["grade"] retrieves the grade.
# The \t adds a tab space for better formatting.
    print("\t {} \t: {}".format(module["courseName"], module["grade"]))