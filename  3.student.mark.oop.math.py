import math
import numpy as np
# Encapsulation
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
        # Floor to 1 decimal
        self.__marks[course_id] = math.floor(mark * 10) / 10
    
    def calculate_gpa(self, courses):
        marks = []
        credits = []
        
        for course in courses:
            if course.get_id() in self.__marks:
                marks.append(self.__marks[course.get_id()])
                credits.append(course.get_credits())
        
        if marks:
            marks_np = np.array(marks)
            credits_np = np.array(credits)
            self.__gpa = math.floor(np.sum(marks_np * credits_np) / np.sum(credits_np) * 10) / 10
        return self.__gpa
    
    def display(self):
        print(f"ID: {self.__id}, Name: {self.__name}, DoB: {self.__dob}, GPA: {self.__gpa}")


class Course:
    def __init__(self, id, name, credits):
        self.__id = id
        self.__name = name
        self.__credits = credits
    
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_credits(self):
        return self.__credits
    
    def display(self):
        print(f"ID: {self.__id}, Name: {self.__name}, Credits: {self.__credits}")


class System:
    def __init__(self):
        self.__students = []
        self.__courses = []
    
    def input_students(self):
        n = int(input("Number of students: "))
        for i in range(n):
            print(f"\nStudent {i+1}:")
            self.__students.append(Student(
                input("ID: "),
                input("Name: "),
                input("DoB: ")
            ))
    
    def input_courses(self):
        n = int(input("\nNumber of courses: "))
        for i in range(n):
            print(f"\nCourse {i+1}:")
            self.__courses.append(Course(
                input("ID: "),
                input("Name: "),
                int(input("Credits: "))
            ))
    
    def input_marks(self):
        print("\nInput Marks")
        for student in self.__students:
            print(f"\nStudent: {student.get_name()}")
            for course in self.__courses:
                mark = float(input(f"  {course.get_name()}: "))
                student.add_mark(course.get_id(), mark)
    
    def calculate_gpa(self):
        for student in self.__students:
            student.calculate_gpa(self.__courses)
    
    def sort_by_gpa(self):
        self.__students.sort(key=lambda s: s.get_gpa(), reverse=True)
    
    def list_students(self):
        print("\nStudent List (sorted by GPA)")
        for student in self.__students:
            student.display()
    
    def list_courses(self):
        print("\nCourse List")
        for course in self.__courses:
            course.display()


# Main
system = System()
system.input_students()
system.input_courses()
system.input_marks()
system.calculate_gpa()
system.sort_by_gpa()
system.list_students()
system.list_courses()
