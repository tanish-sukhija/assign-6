class Student:
    pass
class Marks:
    pass
student_1 = Student()
student_2 = Student()
marks_1 = Marks()
marks_2 = Marks()
print(isinstance(student_1, Student))
print(isinstance(student_2, Student))
print(isinstance(marks_1, Marks))
print(isinstance(marks_2, Marks))
print(issubclass(Student, object))
print(issubclass(Marks, object))