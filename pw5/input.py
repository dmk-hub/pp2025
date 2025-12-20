from domains.student import Student
from domains.course import Course
import os, zipfile

def load_data_from_compressed():
    if os.path.exists("students.dat"):
        print("Found students.dat, loading data...")
        with zipfile.ZipFile("students.dat", 'r') as zip_file:
            zip_file.extractall()

        students, courses = [], []

        with open("students.txt", 'r') as f:
            for line in f:
                id, name, dob = line.strip().split(',')
                students.append(Student(id, name, dob))

        with open("courses.txt", 'r') as f:
            for line in f:
                id, name, credits = line.strip().split(',')
                courses.append(Course(id, name, int(credits)))

        with open("marks.txt", 'r') as f:
            for line in f:
                student_id, course_id, mark = line.strip().split(',')
                for student in students:
                    if student.get_id() == student_id:
                        student.add_mark(course_id, float(mark))

        print("Data loaded successfully!")
        return students, courses
    return None, None

def students():
    lst = []
    n = int(input("Number of students: "))
    for i in range(n):
        print(f"\nStudent {i+1}:")
        id = input("  ID: ")
        name = input("  Name: ")
        dob = input("  DoB (dd/mm/yyyy): ")
        lst.append(Student(id, name, dob))
    return lst

def courses():
    lst = []
    n = int(input("\nNumber of courses: "))
    for i in range(n):
        print(f"\nCourse {i+1}:")
        id = input("  ID: ")
        name = input("  Name: ")
        credits = int(input("  Credits: "))
        lst.append(Course(id, name, credits))
    return lst

def marks(students, courses):
    print("\nInput Marks")
    for student in students:
        print(f"\nStudent: {student.get_name()}")
        for course in courses:
            mark = float(input(f"  {course.get_name()}: "))
            student.add_mark(course.get_id(), mark)

def save_students_to_file(students):
    with open("students.txt", 'w') as f:
        for s in students:
            f.write(f"{s.get_id()},{s.get_name()},{s.get_dob()}\n")

def save_courses_to_file(courses):
    with open("courses.txt", 'w') as f:
        for c in courses:
            f.write(f"{c.get_id()},{c.get_name()},{c.get_credits()}\n")

def save_marks_to_file(students):
    with open("marks.txt", 'w') as f:
        for s in students:
            for cid, mark in s.get_marks().items():
                f.write(f"{s.get_id()},{cid},{mark}\n")

def compress_to_dat():
    print("\nCompressing files to students.dat...")
    with zipfile.ZipFile("students.dat", 'w', zipfile.ZIP_DEFLATED) as zip_file:
        zip_file.write("students.txt")
        zip_file.write("courses.txt")
        zip_file.write("marks.txt")
    os.remove("students.txt")
    os.remove("courses.txt")
    os.remove("marks.txt")
    print("Compression completed! Data saved to students.dat")
