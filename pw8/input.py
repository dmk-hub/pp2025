from domains.student import Student
from domains.course import Course
import pickle
import gzip
import threading

FILENAME = "students.pkl.gz"

def load_data():
    """Load data using pickle with gzip compression"""
    try:
        with gzip.open(FILENAME, 'rb') as f:
            data = pickle.load(f)
            students = data['students']
            courses = data['courses']
        print("Data loaded successfully!")
        return students, courses
    except FileNotFoundError:
        print("No data file found. Starting fresh.")
        return [], []
    except Exception as e:
        print(f"Error loading data: {e}")
        return [], []

def input_students():
    """Input student information"""
    lst = []
    n = int(input("Number of students: "))
    for i in range(n):
        print(f"\nStudent {i+1}:")
        sid = input("  ID: ")
        name = input("  Name: ")
        dob = input("  DoB (dd/mm/yyyy): ")
        lst.append(Student(sid, name, dob))
    return lst

def input_courses():
    """Input course information"""
    lst = []
    n = int(input("\nNumber of courses: "))
    for i in range(n):
        print(f"\nCourse {i+1}:")
        cid = input("  ID: ")
        name = input("  Name: ")
        credits = int(input("  Credits: "))
        lst.append(Course(cid, name, credits))
    return lst

def input_marks(students, courses):
    """Input marks for students"""
    print("\nInput Marks")
    for student in students:
        print(f"\nStudent: {student.get_name()}")
        for course in courses:
            mark = float(input(f"  {course.get_name()}: "))
            student.add_mark(course.get_id(), mark)

def save_data(students, courses, background=True):
    """Save data using pickle with gzip compression, optionally in background thread"""
    def write_task():
        with gzip.open(FILENAME, 'wb') as f:
            pickle.dump({'students': students, 'courses': courses}, f)
        print("\n[✓] Data saved!")

    if background:
        t = threading.Thread(target=write_task, daemon=True)
        t.start()
        print("Saving in background...")
        return t
    else:
        write_task()
