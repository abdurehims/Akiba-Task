Student_name = input("Enter Student Name: ")
Python_score = float(input("Enter Python Score: "))
English_score = float(input("Enter English Score: "))
Mathematics_score = float(input("Enter Mathematics Score: "))
average = (Python_score + English_score + Mathematics_score) / 3

line = "========================================"
hyphen = "----------------------------------------"
print(f"""{line} \n  STUDENT RESULT \n {line} 
Student: {Student_name}

Python:       {Python_score}
English:      {English_score}
Mathematics:  {Mathematics_score}
----------------------------------------
Average:      {average}
""")

