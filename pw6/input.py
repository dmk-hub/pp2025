from domains.student import Student
from domains.course import Course
import pickle
import gzip

def load_data_from_compressed():
    """Load data using pickle with gzip compression"""
    try:
        with gzip.open("students.pkl.gz", 'rb') as f:
            data = pickle.load(f)
            students = data['students']
            courses = data['courses']
        print("Data loaded successfully!")
        return students, courses
    except FileNotFoundError:
        print("No data file found. Starting fresh.")
        return None, None
    except Exception as e:
        print(f"Error loading data: {e}")
        return None, None

def students():
    """Input student information"""
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
    """Input course information"""
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
    """Input marks for students"""
    print("\nInput Marks")
    for student in students:
        print(f"\nStudent: {student.get_name()}")
        for course in courses:
            mark = float(input(f"  {course.get_name()}: "))
            student.add_mark(course.get_id(), mark)

def save_data_to_compressed(students, courses):
    """Save data using pickle with gzip compression"""
    print("\nSaving data to students.pkl.gz...")
    data = {
        'students': students,
        'courses': courses
    }
    with gzip.open("students.pkl.gz", 'wb') as f:
        pickle.dump(data, f)
    print("Data saved successfully!")