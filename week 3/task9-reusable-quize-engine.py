questions = [
    ["Capital of Ethiopia?", ["A. Dessie", "B. Addis Ababa", "C. Mekelle"], "B"],
    ["What is 2 + 3?", ["A. 4", "B. 5", "C. 6"], "B"],
    ["Which is a Python data type?", ["A. list", "B. monitor", "C. mouse"], "A"],
    ["HTML is used for?", ["A. Web pages", "B. Cooking", "C. Driving"], "A"],
    ["What does CPU stand for?", ["A. Central Processing Unit", "B. Computer Power Unit", "C. Control Program Unit"], "A"]
]

def play_quiz():
    score = 0

    for q in questions:
        print("\n" + q[0])
        for option in q[1]:
            print(option)

        answer = input("Your answer: ").strip().upper()

        while answer not in ["A", "B", "C"]:
            print("Invalid answer!")
            answer = input("Choose A, B, or C: ").strip().upper()

        if answer == q[2]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")

    percentage = score / len(questions) * 100

    print("\nCorrect:", score)
    print("Incorrect:", len(questions) - score)
    print("Percentage:", percentage, "%")

    if percentage >= 80:
        print("Excellent!")
    elif percentage >= 60:
        print("Good!")
    elif percentage >= 40:
        print("Pass!")
    else:
        print("Needs improvement!")

while True:
    play_quiz()

    again = input("\nPlay again? (yes/no): ").strip().lower()
    if again != "yes":
        break