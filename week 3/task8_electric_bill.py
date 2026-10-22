def validate_units(units):
    return units >= 0


def calculate_charge(units):
    first = min(units, 50) * 0.50
    second = min(max(units - 50, 0), 100) * 0.75
    third = max(units - 150, 0) * 1.20
    return first, second, third


def total_bill(units, service_fee=0):
    charges = calculate_charge(units)
    return sum(charges) + service_fee


def billing_summary(units, service_fee=0):
    if not validate_units(units):
        print("Invalid units!")
        return

    charges = calculate_charge(units)
    print("First tier:", charges[0], "Birr")
    print("Second tier:", charges[1], "Birr")
    print("Third tier:", charges[2], "Birr")
    print("Total bill:", total_bill(units, service_fee), "Birr")


units = float(input("Enter units: "))
billing_summary(units, 10)