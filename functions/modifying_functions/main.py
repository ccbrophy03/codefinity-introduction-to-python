# Function for defining discount with price and fixed discount amount of 5%
def apply_discount(price, discount = 0.05):
    total_price_discount = price * (1- discount)
    return total_price_discount
# Function for defining tax
def apply_tax(price, tax = 0.07):
    total_price_tax = price * (1 + tax)
    return total_price_tax
# Function when appling both above functions
def calculate_total(price, discount = 0.05, tax = 0.07):
    discounted = apply_discount(price, discount)
    total = apply_tax(discounted, tax)
    return total
# Call total with default discount and tax amounts
total_price_default = calculate_total(120)
print(f"Total cost with default discount and tax: ${total_price_default}")
# Call total with custom values
total_price_custom = calculate_total(100, discount = 0.10, tax = 0.08)
print(f"Total cost with custom discount and tax: ${total_price_custom}")