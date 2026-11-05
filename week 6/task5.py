class Product:
    store_name = "TechMart"

    def __init__(self, name: str, price: float):
        self.name = name
        if self.is_valid_price(price):
            self.price = price
        else:
            raise ValueError("Price must be greater than zero.")

    def display_product(self):
        print(f"Product: {self.name:<15} | Price: ${self.price:.2f} | Store: {Product.store_name}")

    @classmethod
    def change_store_name(cls, new_name: str):
        cls.store_name = new_name

    @staticmethod
    def is_valid_price(price: float) -> bool:
        return price > 0


class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product: Product):
        if isinstance(product, Product):
            self.products.append(product)
            print(f"Added '{product.name}' to the cart.")
        else:
            raise TypeError("Only Product instances can be added to the cart.")

    def calculate_total(self) -> float:
        return sum(p.price for p in self.products)

    def display_cart(self):
        print("\n--- Shopping Cart ---")
        if not self.products:
            print("Cart is empty.")
            return

        for product in self.products:
            product.display_product()
            
        print("-" * 25)
        print(f"Total Amount: ${self.calculate_total():.2f}\n")


# ==========================================
# Example Usage / Demonstration
# ==========================================
if __name__ == "__main__":
    print(f"Is $25.00 valid? {Product.is_valid_price(25.00)}")  # True
    print(f"Is $-5.00 valid? {Product.is_valid_price(-5.00)}")  # False

    p1 = Product("Laptop", 999.99)
    p2 = Product("Mouse", 25.50)
    p3 = Product("Keyboard", 45.00)

    cart = ShoppingCart()
    cart.add_product(p1)
    cart.add_product(p2)
    cart.add_product(p3)

    cart.display_cart()

    Product.change_store_name("MegaTech Superstore")
    print("Updated Store Name:")
    p1.display_product()