def students(students):
    print("\nStudents (sorted by GPA)")
    for s in students:
        print(f"ID: {s.get_id()}, Name: {s.get_name()}, GPA: {s.get_gpa()}")

def courses(courses):
    print("\nCourses")
    for c in courses:
        print(f"ID: {c.get_id()}, Name: {c.get_name()}, Credits: {c.get_credits()}")
