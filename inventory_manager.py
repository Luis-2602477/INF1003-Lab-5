import json
import os

INVENTORY_FILE = "inventory.json"
LINE = "-" * 48


def load_inventory():
    if not os.path.exists(INVENTORY_FILE):
        print(f"{INVENTORY_FILE} not found. Starting with an empty inventory.")
        return []

    print(f"{INVENTORY_FILE} found.")
    try:
        with open(INVENTORY_FILE, "r") as f:
            inventory = json.load(f)
        print("Inventory loaded successfully.")
        return inventory
    except json.JSONDecodeError:
        print("Inventory file is unreadable. Starting with an empty inventory.")
        return []


def save_inventory(inventory):
    """Write the product list to inventory.json."""
    with open(INVENTORY_FILE, "w") as f:
        json.dump(inventory, f, indent=4)


def get_int(prompt):
    while True:
        value = input(prompt).strip()
        if value.isdigit():
            return int(value)
        print(f"Error: '{value}' is not a valid whole number.")


def get_price(prompt):
    while True:
        value = input(prompt).strip()
        try:
            price = float(value)
            if price >= 0:
                return price
            print("Error: Price cannot be negative.")
        except ValueError:
            print(f"Error: '{value}' is not a valid price.")


def find_product(inventory, product_id):
    """Return the product dictionary with this ID, or None if it doesn't exist."""
    for product in inventory:
        if product["id"] == product_id:
            return product
    return None

def display_all(inventory):
    print("Current Inventory")
    print(LINE)
    if not inventory:
        print("No products in inventory.")
    for p in inventory:
        print(f"ID: {p['id']} | Name: {p['name']} | Price: ${p['price']:.2f} | Stock: {p['stock']}")
    print(LINE)


def add_product(inventory):
    print("Add New Product")
    product_id = input("Product ID: ").strip().upper()
    if find_product(inventory, product_id):
        print(f"Error: A product with ID {product_id} already exists.")
        return

    name = input("Product Name: ").strip()
    price = get_price("Price: ")
    stock = get_int("Stock Quantity: ")

    inventory.append({"id": product_id, "name": name, "price": price, "stock": stock})
    print("Product added successfully!")


def update_stock(inventory):
    print("Update Stock")
    product_id = input("Enter Product ID: ").strip().upper()
    product = find_product(inventory, product_id)
    if product is None:
        print("Product not found.")
        return

    print("Product Found:")
    print(f"Name: {product['name']}")
    print(f"Current Stock: {product['stock']}")
    product["stock"] = get_int("New Stock Quantity: ")
    print("Stock updated successfully!")


def search_product(inventory):
    print("Search Product")
    product_id = input("Enter Product ID: ").strip().upper()
    product = find_product(inventory, product_id)
    if product is None:
        print("Product not found.")
        return

    print("Product Found")
    print(LINE)
    print(f"ID: {product['id']}")
    print(f"Name: {product['name']}")
    print(f"Price: ${product['price']:.2f}")
    print(f"Stock: {product['stock']}")
    print(LINE)