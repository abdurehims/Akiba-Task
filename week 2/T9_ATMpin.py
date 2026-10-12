
correct_pin = "1234"
attempts = 3

while attempts > 0:
    pin = input("Enter PIN: ")

    if pin == correct_pin:
        print("Access granted!")
        break
    else:
        attempts -= 1
        print("Incorrect PIN.")
        print("Attempts remaining:", attempts)

if attempts == 0 and pin != correct_pin:
    print("ATM locked!")
