class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade


class Course:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)


# Create a course
course = Course("Math")

# Create students
student1 = Student("De-R", 9)
student2 = Student("Miro", 9)

# Add students to the course
course.add_student(student1)
course.add_student(student2)

# Display the students in the course
print("Course:", course.name)

for student in course.students:
    print("Student:", student.name," Grade:", student.grade)
