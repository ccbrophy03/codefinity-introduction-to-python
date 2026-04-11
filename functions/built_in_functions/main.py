# Dictionary of products with price and quantity sold as strings
products = {
    "Apple": ["1.20", "50"],   # "Item": [price, quantity sold]
    "Banana": ["0.50", "100"],
    "Cherry": ["2.50", "25"],
    "Mango": ["1.75", "40"]
}
total_sales_list = [] # Initialize list before looping

# In the for loop, convert the price values to floats and the quantity sold values to integers
for item, (price, quantity) in products.items():
    price = float(price)
    quantity = int(quantity)
    total_sales = price * quantity # Multiply price and quantity to get totals for each item
    total_sales_list.append(total_sales) # Add each product's total sales
    print(f"Total sales for {item}: ${total_sales}") # Print total sales for each item
    
total_sum = sum(total_sales_list) # Assign a variable named total_sum for the total sum of the sales
min_sales = min(total_sales_list) # Assign a variable named min_sales for the minimum sale value in the list
max_sales = max(total_sales_list) # Assign a variable named max_sales for the maxiumum sale value in the list
print(f"Total sum of all sales: ${total_sum}") # Print total sum of all sales
print(f"Minimum sales: ${min_sales}") # Print min sale
print(f"Maximum sales: ${max_sales}") # Print max sale