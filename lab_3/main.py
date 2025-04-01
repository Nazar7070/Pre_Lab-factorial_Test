import itertools

class User:
    def __init__(self, user_id: int, name: str, email: str):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.orders = []

    def register(self):
        print(f"User {self.name} successfully registered.")

    def login(self):
        print(f"User {self.name} has logged in.")

    def view_orders(self):
        return self.orders


class Product:
    def __init__(self, product_id: int, name: str, price: float, stock: int):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def is_available(self, quantity: int):
        return self.stock >= quantity and quantity > 0


class OrderItem:
    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity

    def get_total_price(self):
        return self.product.price * self.quantity


class Order:
    order_counter = itertools.count(1)

    def __init__(self, user: User):
        self.order_id = next(Order.order_counter)
        self.user = user
        self.items = []
        self.status = "Pending"

    def add_item(self, product: Product, quantity: int):
        if product.is_available(quantity):
            self.items.append(OrderItem(product, quantity))
        else:
            print(f"Error: Not enough stock for {product.name} or invalid quantity.")

    def calculate_total(self):
        return sum(item.get_total_price() for item in self.items)

    def complete_order(self):
        self.status = "Completed"
        print(f"Order {self.order_id} completed.")


class ShoppingCart:
    def __init__(self, user: User):
        self.user = user
        self.items = []

    def add_product(self, product: Product, quantity: int):
        if product.is_available(quantity):
            self.items.append(OrderItem(product, quantity))
        else:
            print(f"Error: Insufficient stock for {product.name} or invalid quantity.")

    def remove_product(self, product: Product):
        self.items = [item for item in self.items if item.product != product]

    def checkout(self):
        if not self.items:
            print("Cart is empty. Creating empty order.")
            empty_order = Order(self.user)
            self.user.orders.append(empty_order)
            return empty_order

        new_order = Order(self.user)
        new_order.items = self.items.copy()
        self.user.orders.append(new_order)
        self.items.clear()
        print(f"Order {new_order.order_id} created and cart cleared.")
        return new_order
