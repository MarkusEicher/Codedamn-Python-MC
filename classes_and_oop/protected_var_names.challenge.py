# using namedtuple for easy class creation
from collections import namedtuple

Student = namedtuple("Student", ('name', 'age'))

class Course:
    def __init__(self, title):
        self.title = title
        self._students = []
        
    def add_student(self, student):
        self._students.append(student)

    def total_students(self):
        return len(self._students)

# test code
py_course = Course("Python")

py_course.add_student(Student("Dale", 27))
py_course.add_student(Student("Hary", 33))
py_course.add_student(Student("John", 21))

print(py_course.total_students())