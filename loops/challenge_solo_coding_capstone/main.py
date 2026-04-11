# Inventory dictionary with stock, price, and discount price
inventory = {
    "Bread": [42, 1.20, 0.99],  # "Item": [current stock, regular price, discounted price]
    "Eggs": [225, 2.12, 1.99],  # Eggs should be sold at a discount
    "Apples": [9, 1.50, 1.35]   # Apples need to be restocked
}


# Loop through each item
for item in inventory:
    stock, reg_price, discount_price = inventory[item] # Label each value from the dictionary
    if stock < 30:
        print(f"{item} need restocking.")
    if stock > 100:
        print(f"{item} should be sold at the discounted price of {discount_price:.2f}.")
    if 30 <= stock <= 100:
        print(f"{item} should be sold at the regular price of {reg_price:.2f}.")

"""
for item in inventory:
    stock, reg_price, discount_price = inventory[item]
    if stock < 30:
        print(f"{item} need restocking.")
    elif stock > 100:
        print(f"{item} should be sold at the discounted price of {discount_price:.2f}.")
    else:  # 30 ≤ stock ≤ 100
        print(f"{item} should be sold at the regular price of {reg_price:.2f}.")
"""