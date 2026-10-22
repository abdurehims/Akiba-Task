def is_prime(number):
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def get_divisors(number):
    divisors = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
    return divisors


def sum_of_digits(number):
    total = 0
    number = abs(number)

    while number > 0:
        total += number % 10
        number //= 10
    return total


def reverse_number(number):
    sign = -1 if number < 0 else 1
    number = abs(number)
    reverse = 0

    while number > 0:
        reverse = reverse * 10 + number % 10
        number //= 10
    return reverse * sign


def analyze_number(number):
    if number == 0:
        print("Zero is neither even nor odd?") 
        print("Prime:", False)
        print("Sum of digits:", 0)
        print("Reverse:", 0)
        print("Divisors: [No positive divisors]")
        return

    print("Even" if number % 2 == 0 else "Odd")
    print("Prime:", is_prime(number))
    print("Sum of digits:", sum_of_digits(number))
    print("Reverse:", reverse_number(number))

    if number > 0:
        print("Divisors:", get_divisors(number))
    else:
        print("Divisors: [Use the absolute value]")


number = int(input("Enter a number: "))
analyze_number(number)