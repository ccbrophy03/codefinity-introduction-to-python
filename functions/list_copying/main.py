# Define the function for discounts
def apply_discount(prices):
    prices_copy = prices.copy() # Create a copy of the original price list
    for price in range(len(prices_copy)):
        if prices_copy[price] > 2.00:
            prices_copy[price] -= prices_copy[price] * 0.10
    return prices_copy

# List of product prices
product_prices = [1.50, 2.50, 3.00, 0.99, 2.30]

# Call the function and store the updated prices
updated_prices = apply_discount(product_prices)
#print(f"Original: {product_prices}")
print(f"Updated product prices: {updated_prices}")