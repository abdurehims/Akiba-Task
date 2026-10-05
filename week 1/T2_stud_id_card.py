stud_name = input("Enter Student Name: ")
stud_Id= input("Enter Student ID: ")
department = input("Enter Your Department: ")
year = int(input("Enter Year: "))
University = input("Enter Your University: ")
Phone = input("Enter Phone Number: ")

line  = "+--------------------------------+"
bar = "|"

print(line)
print(f" {bar} \t AKIBA STUDENT CARD \t {bar}")
print(line)
print(f"{bar} Name: {stud_name} \t \t {bar}")
print(bar + "ID: "+ stud_Id + "\t \t" +bar )
print(f"{bar} Department: {department} \t \t {bar}")
print(f"{bar} Year: {year} \t \t {bar}")
print(f"{bar} University: {University} \t \t {bar}")
print(f"{bar} Phone: {Phone} \t \t {bar}")
print(line)
