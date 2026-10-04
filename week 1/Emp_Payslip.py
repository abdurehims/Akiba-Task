Employee_name = input("Enter Employee Name: ")
Basic_salary = float(input("Enter Salary: "))
Transport_allowance = float(input("Enter Transport allowance: "))
Food_allowance = float(input("Enter Food allowance: "))

Gross_Salary = Basic_salary + Transport_allowance + Food_allowance
line = "========================================"
sline = "----------------------------------------"
print(f"{line}\n    EMPLOYEE PAYSLIP \n {line}")
print(f"Employee: {Employee_name} \n Basic Salary: {Basic_salary} \n Transport Allowance: {Transport_allowance} \n")
print(f"Food Allowance:  {Food_allowance} \n{sline} \n Gross Salary: {Gross_Salary} \n {line}")