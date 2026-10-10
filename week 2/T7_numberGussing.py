
correct_number = 7
number_of_attempts = 0

while number_of_attempts < 5:
    player_guess = int(input("Guess the secret number (1-10): "))
    number_of_attempts = number_of_attempts + 1

    if player_guess == correct_number:
        print("Congratulations!")
        print("You guessed the number in", number_of_attempts, "attempts.")
        break
    elif player_guess < correct_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

if player_guess != correct_number:
    print("Game Over!")
