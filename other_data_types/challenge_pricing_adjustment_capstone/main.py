# Create grocery inventory - title of item: (type, price, quantity)
grocery_inventory = {
    "Milk":("Dairy", 3.50, 8),
    "Eggs": ("Dairy", 5.50, 30),
    "Bread": ("Bakery", 2.99, 15),
    "Apples":("Produce", 1.50, 50)
}
print(grocery_inventory)
# Get the price of eggs and print based on the conditions
egg_category, egg_price, egg_stock = grocery_inventory["Eggs"]
if egg_price > 5:
    print("Eggs are too expensive, reducing the price by $1.")
    new_egg_price = egg_price - 1
    grocery_inventory["Eggs"] = (egg_category, new_egg_price, egg_stock)
else:
    print("The price of Eggs is reasonable.")
# Add tomatoes to grocery inventory and print new details
grocery_inventory.update({"Tomatoes":("Produce", 1.20, 30)})
print("Inventory after adding Tomatoes: ", grocery_inventory)
# Check the stock of milk and print based on the conditions. First, we need to define each part of the milk's details and then we can update
milk_category, milk_price, milk_stock = grocery_inventory["Milk"]
if milk_stock < 10:
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    new_milk_stock = milk_stock + 20
    grocery_inventory["Milk"] = (milk_category, milk_price, new_milk_stock)
else:
    print("Milk has sufficient stock.")
# print(new_milk_stock) 
# Remove apples based on price
apple_price = grocery_inventory["Apples"][1]
if apple_price > 2:
    print("Apples removed from inventory due to high price.")
    grocery_inventory.pop("Apples")
# Print updated, final grocery_inventory
print("Updated inventory: ", grocery_inventory)