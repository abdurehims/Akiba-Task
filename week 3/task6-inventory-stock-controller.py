inventory = {}

def add_product(name, price, stock):
    if name == "" or name in inventory:
        print("Invalid or duplicate product name")
    elif price < 0 or stock < 0:
        print("Price and stock cannot be negative")
    else:
        inventory[name] = {"price": price, "stock": stock}
        print("Product added")

def search_product(name):
    if name in inventory:
        print(inventory[name])
    else:
        print("Product not found")

def update_price(name, price):
    if name in inventory and price >= 0:
        inventory[name]["price"] = price
        print("Price updated")
    else:
        print("Invalid product or price")

def increase_stock(name, quantity):
    if name in inventory and quantity > 0:
        inventory[name]["stock"] += quantity
        print("Stock increased")
    else:
        print("Invalid product or quantity")

def sell_product(name, quantity):
    if name in inventory and 0 < quantity <= inventory[name]["stock"]:
        inventory[name]["stock"] -= quantity
        print("Product sold")
    else:
        print("Invalid sale or insufficient stock")

def total_value():
    total = 0
    for product in inventory.values():
        total += product["price"] * product["stock"]
    print("Total inventory value:", total)

def low_stock(limit=5):
    for name, product in inventory.items():
        if product["stock"] < limit:
            print(name, "Stock:", product["stock"])


# Test the functions
add_product("Laptop", 30000, 4)
add_product("Mouse", 500, 10)

search_product("Laptop")
update_price("Mouse", 600)
increase_stock("Laptop", 3)
sell_product("Laptop", 2)
total_value()
low_stock()      
low_stock(8)      