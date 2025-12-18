from domains.student import Student
from domains.course import Course

def students():
    students = []
    n = int(input("Number of students: "))
    for i in range(n):
        print(f"\nStudent {i+1}:")
        students.append(Student(
            input("ID: "),
            input("Name: "),
            input("DoB: ")
        ))
    return students

def courses():
    courses = []
    n = int(input("\nNumber of courses: "))
    for i in range(n):
        print(f"\nCourse {i+1}:")
        courses.append(Course(
            input("ID: "),
            input("Name: "),
            int(input("Credits: "))
        ))
    return courses

def marks(students, courses):
    print("\nInput Marks")
    for student in students:
        print(f"\nStudent: {student.get_name()}")
        for course in courses:
            mark = float(input(f"  {course.get_name()}: "))
            student.add_mark(course.get_id(), mark)
