import json
import pathlib
from Courses import Courses

class Student(Courses):
 
    def __init__(self, studentname: str,studentage: int, studencourse:str): 
        super().__init__(courseid=0, coursename = studencourse)
        self.studentname = studentname
        self.studentage = studentage


    def promptUser():
        # Ask the user for information
        studentname = input("What is your name? ")
        studentage = input("What is your age? ")
        studentcourse = input("Which course do you want to enroll in? ")

        # Check if the age is an integer
        while not studentage.isdigit():
            if studentage.isdigit():
                break
            else:
                print("User has entered in the incorrect value, please enter in a number: ")
                studentage = input("What is your age? ")
        #return values
        return studentname, studentage, studentcourse
        

    def readfromFileAndAppend(self):
        
        # Path of the user.json file to use Pathlib functions
        config_file = pathlib.Path("StudentManagmentSystem/data/user.json")

        # read file contents of the json 
        with config_file.open(mode="r", encoding="utf-8") as file:
            config = json.load(file)
        
        # add contents of the user to a dictionary 
        data = {"studentid": config[-1]["studentid"] + 1, "studentName": self.studentname, "age": self.studentage, "courseid": self.courseid}
        config.append(data)

        # Overwrite contents of the json and indent the data by 4
        with config_file.open("w") as file:
            json.dump(config, file, indent=4)
            

    def checkStudentCourse(self):
        # Path of the courses.json file to use Pathlib functions
        course_file = pathlib.Path("StudentManagmentSystem/data/courses.json")
        user_file = pathlib.Path("StudentManagmentSystem/data/user.json")

        # read files of user and course 
        with course_file.open(mode="r", encoding="utf-8") as file:
            scrapedCourses = json.load(file)
        
        with user_file.open(mode="r", encoding="utf-8") as file:
            scrapedStudents = json.load(file)
        
        # loop through the student json (user.json)
        for iterstudent in scrapedStudents:
            if iterstudent["studentName"] == self.studentname:
                updatedStudent = Student(studentname=iterstudent["studentName"], studentage=iterstudent["age"],studencourse= "")
                updatedStudent.courseid = iterstudent["courseid"]
                print(self.studentname + " does " + updatedStudent.retrieveCourse(scrapedCourses))
                break


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


def runCheckStudentCourse():
    # Check the user name
    studentname = input("Who is the student info you want to check? ")
    stu = Student(studentname=studentname, studentage= "", studencourse="")
    
    # Run to check the student course
    stu.checkStudentCourse()

def runMainLoop():
    userinput = ""
    # Run the loop until user exists
    while userinput != "6":
        print("Hi User, what do you want to do? \n 1: Add Student to a course \n 2: Update student \n 3: remove student \n 4: remove course \n 5: Check the student \n 6: exit")
        userinput = input("Please enter in a number: ")
        
        # Add user to the list from the courses listed
        if userinput == "1":
            runPrompt()
        
        # Check the student info
        elif userinput == "5":
            runCheckStudentCourse()


if __name__ == "__main__":
    runMainLoop()




        


