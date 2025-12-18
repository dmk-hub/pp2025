import math
import numpy as np

class Student:
    def __init__(self, id, name, dob):
        self.__id = id
        self.__name = name
        self.__dob = dob
        self.__marks = {}
        self.__gpa = 0.0
    
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_gpa(self):
        return self.__gpa
    
    def add_mark(self, course_id, mark):
        self.__marks[course_id] = math.floor(mark * 10) / 10
    
    def calculate_gpa(self, courses):
        marks, credits = [], []
        for course in courses:
            if course.get_id() in self.__marks:
                marks.append(self.__marks[course.get_id()])
                credits.append(course.get_credits())
        if marks:
            marks_np = np.array(marks)
            credits_np = np.array(credits)
            self.__gpa = math.floor(np.sum(marks_np * credits_np) / np.sum(credits_np) * 10) / 10
