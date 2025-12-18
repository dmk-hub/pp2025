from domains.student import Student
from domains.course import Course

def input_number_of_students():
    return int(input("Number of students: "))

def input_student_info():
    print("Enter student information:")
    id = input("  ID: ")
    name = input("  Name: ")
    dob = input("  DoB (dd/mm/yyyy): ")
    return Student(id, name, dob)

def input_number_of_courses():
    return int(input("\nNumber of courses: "))

def input_course_info():
    print("Enter course information:")
    id = input("  ID: ")
    name = input("  Name: ")
    credits = int(input("  Credits: "))
    return Course(id, name, credits)

def input_marks_for_course(students, courses):
    print("\n=== Select a course to input marks ===")
    for i, course in enumerate(courses):
        print(f"{i+1}. {course.get_name()} (ID: {course.get_id()})")
    
    choice = int(input("Select course number: ")) - 1
    if 0 <= choice < len(courses):
        selected_course = courses[choice]
        print(f"\nInput marks for {selected_course.get_name()}:")
        for student in students:
            mark = float(input(f"  {student.get_name()}: "))
            student.add_mark(selected_course.get_id(), mark)
    else:
        print("Invalid choice!")