import input
import output

def main():
    # Input data
    students = input.students()
    courses = input.courses()
    input.marks(students, courses)
    
    # Calculate GPA
    for student in students:
        student.calculate_gpa(courses)
    
    # Sort by GPA descending
    students.sort(key=lambda s: s.get_gpa(), reverse=True)
    
    # Output results
    output.students(students)
    output.courses(courses)

if __name__ == "__main__":
    main()
