Name = input("Enter Your Name: ")
weight = float(input("Enter your Weight in kilograms: "))
height = float(input("Enter your height in meters: "))
BMI = weight / (height * height)

print(f"""
================================
          BMI REPORT
================================

Name: {Name}
Weight: {weight} kg
Height: {height} m

BMI: {BMI}
================================

""")