def students(students):
    print("\nStudents (sorted by GPA)")
    for s in students:
        print(f"ID: {s.get_id()}, Name: {s.get_name()}, GPA: {s.get_gpa()}")

def courses(courses):
    print("\nCourses")
    for c in courses:
        print(f"ID: {c.get_id()}, Name: {c.get_name()}, Credits: {c.get_credits()}")

def show_marks(students, courses, course_id):
    course = None
    for c in courses:
        if c.get_id() == course_id:
            course = c
            break
    if course:
        print(f"\nMarks for {course.get_name()}")
        for s in students:
            mark = s.get_marks().get(course_id, "No mark")
            print(f"{s.get_name()}: {mark}")
    else:
        print("Course not found!")
