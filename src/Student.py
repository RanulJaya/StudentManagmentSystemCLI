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
        config_file = pathlib.Path("data/user.json")

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
        course_file = pathlib.Path("data/courses.json")
        user_file = pathlib.Path("data/user.json")

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
            
    # Student to be removed 
    def studentTobeRemoved(self):
        
        with open(file="data/user.json", encoding="utf-8", mode="r") as file:
            studentRemove = json.load(file)

        for iter in studentRemove:
            if iter["studentName"] == self.studentname:
                for st in range(len(studentRemove)):
                    if iter == studentRemove[st]:
                        del studentRemove[st]
                        break
                break

        with open(file="data/user.json", encoding="utf-8", mode="w") as file:
            json.dump(studentRemove, file, indent=4)

        print("Student has been deleted sucessfully!")