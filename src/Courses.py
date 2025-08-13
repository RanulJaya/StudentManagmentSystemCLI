import json
import pathlib

class Courses:
    
    def __init__(self, courseid, coursename):
        self.courseid = courseid
        self.coursename = coursename

   
    def checkCourseExists(self):
        # Path of the courses.json file to use Pathlib functions
        config_file = pathlib.Path("StudentManagmentSystem/data/courses.json")

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
