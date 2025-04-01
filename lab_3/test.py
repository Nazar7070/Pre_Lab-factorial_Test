import pytest
from main import User, Product, OrderItem, Order, ShoppingCart

@pytest.fixture
def test_data():
    user = User(user_id=1, name="Jec Doe", email="jec@gmail.com")
    laptop = Product(product_id=1, name="Laptop", price=1000.0, stock=10)
    phone = Product(product_id=2, name="Phone", price=500.0, stock=20)
    cart = ShoppingCart(user)
    return user, laptop, phone, cart

# Перевірка реєстрації користувача
def test_user_registration(test_data):
    user, _, _, _ = test_data
    user.register()
    assert user.name == "Jec Doe"
    assert user.email == "jec@gmail.com"

# Перевірка додавання товару в кошик
def test_adding_product_to_cart(test_data):
    _, laptop, _, cart = test_data
    cart.add_product(laptop, 2)
    assert len(cart.items) == 1
    assert cart.items[0].product == laptop
    assert cart.items[0].quantity == 2

# Перевірка додавання кількох товарів у кошик
def test_adding_multiple_products(test_data):
    _, laptop, phone, cart = test_data
    cart.add_product(laptop, 2)
    cart.add_product(phone, 1)
    assert len(cart.items) == 2
    assert cart.items[1].product == phone
    assert cart.items[1].quantity == 1

# Перевірка оформлення замовлення
def test_order_checkout(test_data):
    user, laptop, _, cart = test_data
    cart.add_product(laptop, 2)
    order = cart.checkout()
    assert len(order.items) == 1
    assert order.items[0].quantity == 2
    assert order.user == user
    assert order.order_id > 0

# Перевірка підрахунку загальної вартості замовлення
def test_order_total_price(test_data):
    user, laptop, _, _ = test_data
    order = Order(user)
    order.add_item(laptop, 2)
    order.add_item(laptop, 3)
    assert order.calculate_total() == 5000.0  # 2 * 1000 + 3 * 1000

# Перевірка видалення товару з кошика
def test_removing_product_from_cart(test_data):
    _, laptop, _, cart = test_data
    cart.add_product(laptop, 2)
    cart.remove_product(laptop)
    assert len(cart.items) == 0

# Перевірка підрахунку вартості одиниці товару
def test_order_item_total_price(test_data):
    _, laptop, _, _ = test_data
    order_item = OrderItem(product=laptop, quantity=3)
    assert order_item.get_total_price() == 3000.0  # 3 * 1000

# Перевірка створення кількох замовлень
def test_creating_multiple_orders(test_data):
    user, laptop, _, cart = test_data
    cart.add_product(laptop, 2)
    first_order = cart.checkout()
    cart.add_product(laptop, 1)
    second_order = cart.checkout()
    assert len(user.orders) == 2
    assert first_order.order_id != second_order.order_id

# Перевірка оформлення замовлення без товарів
def test_checkout_with_empty_cart(test_data):
    user, _, _, cart = test_data
    order = cart.checkout()
    assert len(order.items) == 0
    assert order.status == "Pending"

# Перевірка коректного відображення товару в замовленні
def test_correct_product_in_order(test_data):
    _, laptop, _, cart = test_data
    cart.add_product(laptop, 2)
    order = cart.checkout()
    assert order.items[0].product.name == "Laptop"
    assert order.items[0].quantity == 2
