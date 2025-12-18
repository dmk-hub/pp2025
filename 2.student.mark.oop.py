class Student:
    def __init__(self, id, name, dob):
        self.__id = id
        self.__name = name
        self.__dob = dob
        self.__marks = {}
    
    # Getter methods
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_mark(self, course_id):
        return self.__marks.get(course_id)
    
    # Other methods
    def add_mark(self, course_id, mark):
        self.__marks[course_id] = mark
    
    def display(self):
        print(f"ID: {self.__id}, Name: {self.__name}, DoB: {self.__dob}")


class Course:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
    
    # Getter methods
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def display(self):
        print(f"ID: {self.__id}, Name: {self.__name}")


class System:
    def __init__(self):
        self.__students = []
        self.__courses = []
    
    def input_students(self):
        n = int(input("Enter number of students: "))
        for i in range(n):
            print(f"\nStudent {i+1}:")
            id = input("ID: ")
            name = input("Name: ")
            dob = input("DoB (dd/mm/yyyy): ")
            self.__students.append(Student(id, name, dob))
    
    def input_courses(self):
        n = int(input("\nEnter number of courses: "))
        for i in range(n):
            print(f"\nCourse {i+1}:")
            id = input("ID: ")
            name = input("Name: ")
            self.__courses.append(Course(id, name))
    
    def input_marks(self):
        print("\nEnter marks:")
        for student in self.__students:
            print(f"\nStudent: {student.get_name()}")
            n = int(input("Number of courses: "))
            for i in range(n):
                course_id = input(f"  Course ID: ")
                mark = float(input(f"  Mark: "))
                student.add_mark(course_id, mark)
    
    def list_students(self):
        print("\n Students")
        for student in self.__students:
            student.display()
    
    def list_courses(self):
        print("\n Courses")
        for course in self.__courses:
            course.display()
    
    def show_marks(self, course_id):
        # Find course
        course = None
        for c in self.__courses:
            if c.get_id() == course_id:
                course = c
                break
        
        if course:
            print(f"\n Marks for {course.get_name()} ")
            for student in self.__students:
                mark = student.get_mark(course_id)
                if mark is not None:
                    print(f"{student.get_name()}: {mark}")
                else:
                    print(f"{student.get_name()}: No mark")
        else:
            print("Course not found!")


# Main program
system = System()
system.input_students()
system.input_courses()
system.input_marks()
system.list_students()
system.list_courses()

print("\nView Marks")
course_id = input("Enter course ID: ")
system.show_marks(course_id)