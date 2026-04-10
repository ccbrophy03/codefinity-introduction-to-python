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

"""
PROCESSING_START = "Processing started"
PROCESSING_END   = "Processing completed"

print(PROCESSING_START)
for item in inventory:
    print(f"Processing {item}")
    stock_data = inventory[item]
    current_stock, min_stock, restock_amount, on_sale = stock_data

    # restock in one calculation instead of looping
    needed = max(0, min_stock - current_stock)
    increments = -(-needed // restock_amount)
    current_stock += increments * restock_amount
    inventory[item][0] = current_stock

    if current_stock > discount_threshold and not on_sale:
        inventory[item][3] = True

print(PROCESSING_END)
"""