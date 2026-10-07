number = int(input("Enter number: "))
digit_Sum = 0
while number > 0:
    lastDigit = number % 10
    digit_Sum += lastDigit
    number = number // 10 

print("the sum of all digits is :", digit_Sum)
