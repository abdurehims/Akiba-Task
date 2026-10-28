expenses = [
    {"description": "Lunch", "category": "Food", "amount": 180},
    {"description": "Taxi", "category": "Transport", "amount": 120},
    {"description": "Groceries", "category": "Food", "amount": 450},
    {"description": "Internet", "category": "Bills", "amount": 300}
]


def add_expense(description, category, amount):
    if description and category and amount >= 0:
        expenses.append({
            "description": description,
            "category": category,
            "amount": amount
        })


def total_expenses():
    total = 0
    for expense in expenses:
        total += expense["amount"]
    return total


def spending_by_category():
    categories = {}
    for expense in expenses:
        category = expense["category"]
        categories[category] = categories.get(category, 0) + expense["amount"]
    return categories


def largest_expense():
    return max(expenses, key=lambda e: e["amount"])


def above_threshold(limit=200):
    for expense in expenses:
        if expense["amount"] > limit:
            print(expense["description"], expense["amount"])


def spending_report():
    total = total_expenses()
    categories = spending_by_category()

    print("\nTotal expenses:", total)
    print("Spending by category:")

    for category, amount in categories.items():
        print(category, amount, "-", round(amount / total * 100, 1), "%")

    largest_category = max(categories, key=categories.get)
    print("Highest spending category:", largest_category)
    print("Largest expense:", largest_expense())
    print("\nExpenses above 200:")
    above_threshold()



add_expense("Coffee", "Food", 50)
spending_report()