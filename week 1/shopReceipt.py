Customer_name =input("Enter Customor Name: ")
Product_name = input("Enter Product Name: ")
Price = float(input("Enter Price: "))
Quantity = int(input("Enter Quantity: "))

total_price = Price * Quantity
line = "========================================"
hyphen = "----------------------------------------"
print(f"{line} \n RECEIPT \n {line} \n \t Customer: {Customer_name} \n Product        Price       Qty \n {hyphen}")
print(f"  {Product_name} \t {Price} ETB   {Quantity} \n \n Total: {total_price} \n Thank you for shopping! \n {line}")