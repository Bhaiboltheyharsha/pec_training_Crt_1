class Student:
    student_name=""
    def __init__(self,name):
        print("object created")
        self.student_name=name
        print(name)
        print(self.student_name)
s1 = Student("harsha")
