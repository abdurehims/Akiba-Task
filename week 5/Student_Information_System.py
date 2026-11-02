class Student:
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Department: {self.department}")
        print("-------------------")


student1 = Student("Abdurehim", 21, "Software Engineering")
student2 = Student("Ebrahim", 22, "Computer Science")
student3 = Student("Mubarek", 20, "Information Technology")

student1.display_info()
student2.display_info()
student3.display_info()