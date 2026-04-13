# Define a function to calculate the revenue for each product
def calculate_revenue(prices, quantities_sold):
    revenue = [] # Initialize a list to store the calculated revenues
    for i in range(len(prices)): # Iterate through the `prices` and `quantities_sold` lists using indexing
        revenue.append(prices[i] * quantities_sold[i]) # Append the revenue (price * quantity) for each product to the revenue list
    return revenue # Return the list of revenues
#Define a function to format and display the sorted revenues
def formatted_output(revenues):
    for revenue in sorted(revenues):
        # Print the formatted output for each product and its corresponding revenue
        print(f"{revenue[0]} has total revenue of ${revenue[1]}")

# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold

#  Call the `calculate_revenue()` function to get total `revenue` for each product
revenue = calculate_revenue(prices, quantities_sold)
# Use `zip()` to combine the products and their corresponding revenues into a list
revenue_per_product = list(zip(products, revenue))
# Last, display the sorted revenues using the `formatted_output()` function
formatted_output(revenue_per_product)