from Student import Student

# Main Loop functions
def runPrompt():
    # Prompt user to info
    user = Student.promptUser()
    
    # Initialize the constructor of the Student
    student = Student(studentname=user[0], studentage=user[1], studencourse=user[2])
    
    # Check the course
    courseexists = student.checkCourseExists()

    #if it exists, then add user to the json
    if courseexists:
        student.readfromFileAndAppend()
        print("Student added to the course")
    else:
        print("Course could not be added in")

# Update the student information (course)
def updateStudentInfo():
    checkStudent = input("Who is the student that you want to update? ")
    updateCourse = input("What course do you want to update to? ")

    stu = Student(studentname=checkStudent, studentage="", studencourse=updateCourse)
    # run the function to update the student
    stu.updateCourseofStudent(stu.studentname)

def runCheckStudentCourse():
    # Check the user name
    studentname = input("Who is the student info you want to check? ")
    stu = Student(studentname=studentname, studentage= "", studencourse="")
    
    # Run to check the student course
    stu.checkStudentCourse()

def removeStudentFromList():
    userinput = input("Which student do you want to remove? ")
    stu = Student(studentname=userinput, studentage="", studencourse="")
    stu.studentTobeRemoved()

def runMainLoop():
    userinput = ""
    # Run the loop until user exists
    while userinput != "6":
        print("Hi User, what do you want to do? \n 1: Add Student to a course \n 2: Update student \n 3: remove student \n 4: remove course \n 5: Check what the student is enrolled to \n 6: exit")
        userinput = input("Please enter in a number: ")
        
        # Add user to the list from the courses listed
        if userinput == "1":
            runPrompt()
        
        elif userinput == "2":
            updateStudentInfo()
        
        elif userinput == "3":
            removeStudentFromList()
        
        # Check the student info
        elif userinput == "5":
            runCheckStudentCourse()


if __name__ == "__main__":
    runMainLoop()



