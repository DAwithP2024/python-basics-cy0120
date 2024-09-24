# Products available in the store by category
products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}

def display_sorted_products(products_list, sort_order):
    sorted_products = sorted(products_list, key=lambda x: x[1], reverse=(sort_order == "desc"))
    for product, price in sorted_products:
        print(f"{product}: ${price:.2f}")

def display_products(products):
    for category, items in products.items():
        print(f"\n{category}:")
        display_sorted_products(items, "asc")

def display_categories():
    print("Available Categories:")
    for category in products.keys():
        print(f"- {category}")

def add_to_cart(cart, product, quantity):
    if product in cart:
        cart[product] += quantity
    else:
        cart[product] = quantity

def display_cart(cart):
    print("\nYour Cart:")
    total_cost = 0
    for product, quantity in cart.items():
        price = next((p[1] for cat in products.values() for p in cat if p[0] == product), 0)
        total_cost += price * quantity
        print(f"{product} (x{quantity}): ${price:.2f}")
    print(f"Total Cost: ${total_cost:.2f}")
    return total_cost

def generate_receipt(name, email, cart, total_cost, address):
    print("\n--- Receipt ---")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Address: {address}")
    print("Items Purchased:")
    for product, quantity in cart.items():
        print(f"{product} (x{quantity})")
    print(f"Total Cost: ${total_cost:.2f}")

def validate_name(name):
    return isinstance(name, str) and len(name) > 0

def validate_email(email):
    return "@" in email and "." in email

def main():
    display_categories()
    
    cart = {}
    while True:
        product = input("\nEnter product name to add to cart (or 'done' to finish): ")
        if product.lower() == 'done':
            break
        quantity = int(input("Enter quantity: "))
        add_to_cart(cart, product, quantity)
    
    total_cost = display_cart(cart)
    
    name = input("Enter your name: ")
    while not validate_name(name):
        name = input("Invalid name. Please enter again: ")
    
    email = input("Enter your email: ")
    while not validate_email(email):
        email = input("Invalid email. Please enter again: ")
    
    address = input("Enter your address: ")
    generate_receipt(name, email, cart, total_cost, address)

if __name__ == "__main__":
    main()
