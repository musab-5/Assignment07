class CartItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_item_price(self):
        return self.price * self.quantity


class ElectronicsItem(CartItem):
    def __init__(self, name, price, quantity, warranty):
        super().__init__(name, price, quantity)
        self.warranty = warranty

    def calculate_item_price(self):
        return super().calculate_item_price() * (1 - 0.1)  # 10% discount for electronics


class ClothingItem(CartItem):
    def __init__(self, name, price, quantity, size):
        super().__init__(name, price, quantity)
        self.size = size

    def calculate_item_price(self):
        return super().calculate_item_price() * (1 - 0.2)  # 20% discount for clothing


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"{item.name} added to the cart.")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"{item.name} removed from the cart.")
        else:
            print(f"{item.name} is not in the cart.")

    def show_cart(self):
        print("Shopping Cart Contents:")
        for item in self.items:
            print(f"{item.name} - Quantity: {item.quantity}, Price: ${item.calculate_item_price():.2f}")

    def calculate_total_price(self):
        total_price = sum(item.calculate_item_price() for item in self.items)
        return total_price


# Instantiate items
electronics_item = ElectronicsItem("Laptop", 1000, 1, "2 years")
clothing_item = ClothingItem("T-shirt", 20, 3, "Medium")

# Create a ShoppingCart instance
cart = ShoppingCart()

# Add items to the cart
cart.add_item(electronics_item)
cart.add_item(clothing_item)

# Display cart contents
cart.show_cart()

# Calculate and display total cart price
total_price = cart.calculate_total_price()
print(f"Total Cart Price: ${total_price:.2f}")
