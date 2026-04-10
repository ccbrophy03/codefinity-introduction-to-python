produce = ["Tomatoes", "Lettuce"]
dairy = ["Milk", "Cheese"]
# Combine the lists
groceries = [produce, dairy]

for section in groceries: # outer loop - each section is a list, calls both lists since groceries includes both produce and dairy
    for item in section: # inner loop - each item in the produce and diary lists (now combined in groceries) will be a string
        print("Item name: ", item)