import input as inp
import output

def gpa_key(student):
    # Return GPA for sorting
    return student.get_gpa()

def main():
    # Load data if exists
    students, courses = inp.load_data_from_compressed()

    if students is None or courses is None:
        # Input new data
        students = inp.students()
        courses = inp.courses()
        inp.marks(students, courses)
        
        # Save data immediately after input
        inp.save_data_to_compressed(students, courses)

    # Calculate GPA
    for s in students:
        s.calculate_gpa(courses)

    # Sort by GPA (desc)
    students.sort(key=gpa_key, reverse=True)

    # Show results
    output.students(students)
    output.courses(courses)

    print("\nView Marks")
    course_id = input("Enter course ID: ")
    output.show_marks(students, courses, course_id)

    # Save compressed data
    inp.save_data_to_compressed(students, courses)
    print("\nProgram closed successfully!")

if __name__ == "__main__":
    main()