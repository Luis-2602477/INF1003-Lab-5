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