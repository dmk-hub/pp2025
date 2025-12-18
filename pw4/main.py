import input
import output

def main():
    students = []
    courses = []
    
    # Input students
    num_students = input.input_number_of_students()
    for i in range(num_students):
        print(f"\nStudent {i+1}:")
        students.append(input.input_student_info())
    
    # Input courses
    num_courses = input.input_number_of_courses()
    for i in range(num_courses):
        print(f"\nCourse {i+1}:")
        courses.append(input.input_course_info())
    
    # Input marks for selected course
    input.input_marks_for_course(students, courses)
    
    # Calculate GPA for all students
    for student in students:
        student.calculate_gpa(courses)
    
    # Sort students by GPA descending
    students.sort(key=lambda s: s.get_gpa(), reverse=True)
    
    # List students and courses
    output.list_students(students)
    output.list_courses(courses)
    
    # Show marks for a given course
    print("\n=== View Marks ===")
    course_id = input("Enter course ID: ")
    output.show_student_marks(students, courses, course_id)

if __name__ == "__main__":
    main()
