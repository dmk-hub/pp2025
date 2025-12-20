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
        inp.save_students_to_file(students)

        courses = inp.courses()
        inp.save_courses_to_file(courses)

        inp.marks(students, courses)
        inp.save_marks_to_file(students)

    # Calculate GPA
    for s in students:
        s.calculate_gpa(courses)

    # Sort by GPA (desc)
    students.sort(key=gpa_key, reverse=True)

    # Show results
    output.students(students)
    output.courses(courses)

    print("\nView Marks")
    course_id = input("Enter course ID: ")  # now this is the built‑in input()
    output.show_marks(students, courses, course_id)

    # Save compressed data
    inp.compress_to_dat()
    print("\nProgram closed successfully!")

if __name__ == "__main__":
    main()
