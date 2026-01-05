import input as inp
import output

def gpa_key(student):
    # Return GPA for sorting
    return student.get_gpa()

def main():
    # Load data if exists
    students, courses = inp.load_data()

    if not students or not courses:
        # Input new data
        students = inp.input_students()
        courses = inp.input_courses()
        inp.input_marks(students, courses)
        
        # Save data immediately after input (background)
        save_thread = inp.save_data(students, courses, background=True)
    else:
        save_thread = None

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

    # Wait for background save if any
    if save_thread:
        save_thread.join()

    # Final synchronous save before exit
    inp.save_data(students, courses, background=False)
    print("\nProgram closed successfully!")

if __name__ == "__main__":
    main()
