
class Student:

    def __init__(self, name, student_id, department):
        self.name = name
        self.student_id = student_id
        self.department = department

    def display_info(self):
        print("Student Name:", self.name)
        print("Student ID:", self.student_id)
        print("Department:", self.department)

 
    def introduce(self):
        print(f"Hello! My name is {self.name}. I am a student in {self.department} department.")


student1 = Student("Abdurehim", "SE001", "Software Engineering")
student2 = Student("Ebrahim", "SE002", "Software Engineering")
student3 = Student("Mubarek", "SE003", "Computer Science")
student4 = Student("Kedir", "IT001", "Information Technology")




print("===== Student 1 =====")
student1.display_info()
student1.introduce()


print("\n===== Student 2 =====")
student2.display_info()
student2.introduce()


print("\n===== Student 3 =====")
student3.display_info()
student3.introduce()

print("\n===== Student 4 =====")
student4.display_info()
student4.introduce()
