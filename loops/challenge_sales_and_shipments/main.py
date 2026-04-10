# List of products with their initial stock levels at the start of the week
products = [
    ["Apples", 150],  
    ["Bananas", 200],
    ["Oranges", 100],
    ["Mangoes", 120]
]

# List of products sold by the end of the week
units_sold = [["Apples", 30], ["Bananas", 45], ["Oranges", 20], ["Mangoes", 10]]
# First for loop with units_sold
for i in range(len(products)):
    products[i][1] -= units_sold[i][1]

print("Updated product of units sold: ", products)
    
# New shipment received at the end of the week
shipment_received = [["Apples", 50], ["Bananas", 70], ["Oranges", 30], ["Mangoes", 40]]
# Second for loop with shipment_received
for i in range(len(products)):
    products[i][1] += shipment_received[i][1]

print("Final stock levels for all products:", products)