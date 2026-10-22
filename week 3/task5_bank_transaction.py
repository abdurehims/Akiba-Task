def deposit(balance, amount, history):
    if amount <= 0:
        print("Invalid amount!")
    else:
        balance += amount
        history.append({"type": "deposit", "amount": amount,
                        "balance_after": balance})
    return balance


def withdraw(balance, amount, history, daily_withdrawn):
    if amount <= 0:
        print("Invalid amount!")
    elif amount > balance:
        print("Insufficient balance!")
    elif daily_withdrawn + amount > 1000:
        print("Daily withdrawal limit exceeded!")
    else:
        balance -= amount
        daily_withdrawn += amount
        history.append({"type": "withdraw", "amount": amount,
                        "balance_after": balance})
    return balance, daily_withdrawn


def check_balance(balance):
    print("Current balance:", balance)


def transaction_summary(history, balance):
    deposited = 0
    withdrawn = 0

    print("\nTransaction History:")
    for transaction in history:
        print(transaction)

        if transaction["type"] == "deposit":
            deposited += transaction["amount"]
        else:
            withdrawn += transaction["amount"]

    print("Total deposited:", deposited)
    print("Total withdrawn:", withdrawn)
    print("Final balance:", balance)


balance = float(input("Opening balance: "))
history = []
daily_withdrawn = 0

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check balance")
    print("4. Transaction summary")
    print("5. Exit")

    choice = input("Choose: ")

    if choice == "1":
        amount = float(input("Deposit amount: "))
        balance = deposit(balance, amount, history)

    elif choice == "2":
        amount = float(input("Withdraw amount: "))
        balance, daily_withdrawn = withdraw(
            balance, amount, history, daily_withdrawn
        )

    elif choice == "3":
        check_balance(balance)

    elif choice == "4":
        transaction_summary(history, balance)

    elif choice == "5":
        break

    else:
        print("Invalid choice!")