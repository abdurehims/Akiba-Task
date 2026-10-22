def check_length(password, minimum=8):
    return len(password) >= minimum


def check_uppercase(password):
    for letter in password:
        if letter.isupper():
            return True
    return False


def check_lowercase(password):
    for letter in password:
        if letter.islower():
            return True
    return False


def check_digit(password):
    for letter in password:
        if letter.isdigit():
            return True
    return False


def check_special(password):
    for letter in password:
        if not letter.isalnum():
            return True
    return False


def analyze_password(password, minimum=8):
    results = {
        "Length": check_length(password, minimum),
        "Uppercase": check_uppercase(password),
        "Lowercase": check_lowercase(password),
        "Digit": check_digit(password),
        "Special character": check_special(password)
    }

    missing = []

    for rule in results:
        if results[rule] == False:
            missing.append(rule)

    return {"results": results, "missing": missing}


passwords = ["Abdurehim123!", "mighot", "HELLO123!",
             "HelloWorld", "Abc@1234"]

for password in passwords:
    report = analyze_password(password)

    print("\nPassword:", password)
    print("Results:", report["results"])
    print("Missing requirements:", report["missing"])