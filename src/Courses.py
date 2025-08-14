import json
import pathlib

class Courses:
    
    def __init__(self, courseid, coursename):
        self.courseid = courseid
        self.coursename = coursename

   
    def checkCourseExists(self):
        # Path of the courses.json file to use Pathlib functions
        config_file = pathlib.Path("data/courses.json")

        with config_file.open(mode = "r", encoding="utf-8") as file:
            config = json.load(file)
        
        for iter in config:
            if iter["subjects"] == self.coursename:
                self.courseid = int(iter["id"])
                break
        
        return self.courseid is not 0


    def retrieveCourse(self, getSubjectInfo):
        for iter in getSubjectInfo:
            if self.courseid == iter["id"]:
                self.coursename = iter["subjects"]
                break
        
        return self.coursename


    def updateStudentCourse(self, studentName):
        # Path of the users.json file to use Pathlib functions
        config_file = pathlib.Path("data/user.json")

        with config_file.open(mode="r", encoding="utf-8") as file:
            studentCouseUpdate = json.load(file)
        
        # update student to a new course
        for i in range(len(studentCouseUpdate)):
            if studentCouseUpdate[i]["studentName"] == studentName:
                studentCouseUpdate[i]["courseid"] = self.courseid
                print("Student course has been updated!")
                break

        with config_file.open(mode="w", encoding="utf-8") as file:
            json.dump(studentCouseUpdate, file, indent=4) 


    # function to update student from the main loop
    def updateCourseofStudent(self, studentName):
        if self.checkCourseExists():
            self.updateStudentCourse(studentName)


    # function to add course to a list
    def addCourseToList(self):
        with open(file = "data/courses.json", encoding="utf-8", mode="r") as file:
            addCourse = json.load(file)
        
        data = {"id" : addCourse[-1]["id"] + 1, "subjects" : self.coursename}
        addCourse.append(data)

        with open(file="data/courses.json", encoding="utf-8", mode="w") as file:
            json.dump(addCourse, file, indent=4)
        
        print(self.coursename + " has been added in!")

        