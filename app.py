inventory = {}
def add_item(item, price, stock):
    if item in inventory:
        print(f"Error: Item '{item}' already exists.")
    else:
        inventory[item] = {"price" : float(price), "stock" : int(stock)}
        print(f"Item '{item}' added successfully.")
def update_stock(item, quantity):
    if item not in inventory:
        print(f"Error: Item '{item}' not found.")
    else:
        new_stock = inventory[item]["stock"] + quantity
        if new_stock  < 0:
            print(f"Error: Insufficient stock for '{item}'.")
        else:
            inventory[item]["stock"] = new_stock
            print(f"Stock for '{item}' updated successfully.")
def check_availability(item):
    if item not in inventory:
        return "Item not found"
    return inventory[item]["stock"]
def sales_report(sales):
    total_reve = 0
    for item, qty in sales.items():
        try:
            qty = int(qty)
        except (TypeError, ValueError):
            print(f"Error: Invalid quantity for '{item}'.")
            continue
        if item not in inventory:
            print(f"Error: Item '{item}' not found.")
            continue
        if inventory[item]["stock"] < qty:
            print(f"Error: Insufficient stock for '{item}'.")
            continue
        inventory[item]["stock"] -= qty
        total_reve += inventory[item]["price"] * qty
    return f"Total revenue: ${total_reve:.2f}"
add_item("Apple", 0.5, 50)
add_item("Banana", 0.2, 60)
sales = {"Apple": 30, "Banana": 20, "Orange": 10}  # Orange should print an error
print(sales_report(sales))  # Should output: 19.0
print(inventory)
