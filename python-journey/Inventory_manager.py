def check_inventory(inventory):
    for gadgets, quantity in inventory.items():
        if quantity >= 1:
            print(f"{gadgets}: In stock")
        else:
            print(f"{gadgets}: Out of stock")

inventory = {
    "Phone": 1,
    "Tablet": 2,
    "Camera": 0
}

inventor = check_inventory(inventory)
print(inventor)