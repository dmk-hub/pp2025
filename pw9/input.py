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
        return students, courses
    except FileNotFoundError:
        return [], []
    except Exception as e:
        print(f"Error loading data: {e}")
        return [], []

def add_student(students, sid, name, dob):
    """Add a student object to the list"""
    students.append(Student(sid, name, dob))

def add_course(courses, cid, name, credits):
    """Add a course object to the list"""
    courses.append(Course(cid, name, credits))

def add_mark(student, course_id, mark):
    """Add a mark for a student in a given course"""
    student.add_mark(course_id, mark)

def save_data(students, courses, background=True):
    """Save data using pickle with gzip compression, optionally in background thread"""
    def write_task():
        with gzip.open(FILENAME, 'wb') as f:
            pickle.dump({'students': students, 'courses': courses}, f)
        print("Data saved!")

    if background:
        t = threading.Thread(target=write_task, daemon=True)
        t.start()
        return t
    else:
        write_task()
