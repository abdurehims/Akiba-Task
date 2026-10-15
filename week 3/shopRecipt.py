
def calculate_subtotal(items):
    total = 0
    for item in items:
        if item["price"] < 0 or item["quantity"] < 0:
            print("Invalid price or quantity!")
            return -1
        total += item["price"] * item["quantity"]
    return total


def calculate_discount(subtotal):
    if subtotal >= 3000:
        return subtotal * 0.10
    elif subtotal >= 1000:
        return subtotal * 0.05
    else:
        return 0


def calculate_tax(amount, tax_rate):
    if tax_rate < 0 or tax_rate > 1:
        print("Invalid tax rate!")
        return -1
    return amount * tax_rate


def generate_receipt(items, tax_rate):
    subtotal = calculate_subtotal(items)

    if subtotal == -1:
        return

    discount = calculate_discount(subtotal)
    amount = subtotal - discount
    tax = calculate_tax(amount, tax_rate)

    if tax == -1:
        return

    print("Subtotal:", subtotal)
    print("Discount:", discount)
    print("Tax:", tax)
    print("Final Amount:", amount + tax)


items = [
    {"name": "Notebook", "price": 80, "quantity": 3},
    {"name": "Pen", "price": 15, "quantity": 5}
]

generate_receipt(items, 0.15)
