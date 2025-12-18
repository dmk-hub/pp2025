def list_courses(courses):
    print("\n Course List z")
    for course in courses:
        print(f"ID: {course.get_id()}, Name: {course.get_name()}, Credits: {course.get_credits()}")

def list_students(students):
    print("\n=== Student List ===")
    for student in students:
        print(f"ID: {student.get_id()}, Name: {student.get_name()}, GPA: {student.get_gpa()}")

def show_student_marks(students, courses, course_id):
    course = None
    for c in courses:
        if c.get_id() == course_id:
            course = c
            break
    
    if course:
        print(f"\n=== Marks for {course.get_name()} ===")
        for student in students:
            # Get mark from student's marks
            marks = student._Student__marks
            mark = marks.get(course_id, "No mark")
            print(f"{student.get_name()}: {mark}")
    else:
        print("Course not found!")