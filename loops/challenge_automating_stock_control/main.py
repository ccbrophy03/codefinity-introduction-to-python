# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

discount_threshold = 100
# Printing processing info
print("Processing started.")

for items in inventory:
    print(f"Processing {items}")
    current, minimum, restock_amount, on_sale = inventory[items]
    while current < minimum:
        current += restock_amount
    inventory[items][0] = current
    if current > discount_threshold and not on_sale:
        inventory[items][3] = True
print("Processing completed.")
