
first_number = int(input("Enter the starting number: "))
last_number = int(input("Enter the ending number: "))

for number in range(first_number, last_number + 1):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
