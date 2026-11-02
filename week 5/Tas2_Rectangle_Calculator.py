
class Student:
    school_name = "Akiba Academy"

    def __init__(self, name, score, department):
        self.name = name
        self.score = score
        self.department = department


    def display(self):
        print(f"""School Name : {Student.school_name}
Name        : {self.name}
Score       : {self.score}
Department  : {self.department}
------------------------------""")

student1 = Student("Alice", 85, "Science")
student2 = Student("Bob", 78, "Arts")
student3 = Student("Charlie", 92, "Commerce")

print("=== Original Student Information ===")
student1.display()
student2.display()
student3.display()


student1.score = 95


print("=== After Updating Alice's Score ===")
student1.display()


print("=== Showing Independent Scores ===")
print(f"Alice's score  : {student1.score}")
print(f"Bob's score    : {student2.score}")
print(f"Charlie's score: {student3.score}")