prices = [29.99, 45.50, 12.75, 38.20]
#dis1 = 0.10
#dis2 = 0.20
#dis3 = 0.15
#dis4 = 0.05
"""
if prices[0]: 
        prices[updated_price] -= prices[updated_price] * dis1 
        print(f"Updated price for item {updated_price}: ${prices[updated_price]:.2f}")
    elif prices[1:]:
        prices[updated_price] -= prices[updated_price] * dis2
        dis2 -= 0.05
        print(f"Updated price for item {updated_price + 1}: ${prices[updated_price]:.2f}")
"""
# Iterate over the list of prices using range(len())
for idx in range(len(prices)):
    if idx == 0: 
        discount = 0.10
        prices[idx] -= prices[idx] * discount
        print(f"Updated price for item {idx}: ${prices[idx]:.2f}")
    elif idx == 1:
        discount = 0.20
        prices[idx] -= prices[idx] * discount
        print(f"Updated price for item {idx}: ${prices[idx]:.2f}")
    elif idx == 2:
        discount = 0.15
        prices[idx] -= prices[idx] * discount
        print(f"Updated price for item {idx}: ${prices[idx]:.2f}")
    elif idx == 3:
        discount = 0.05
        prices[idx] -= prices[idx] * discount
        print(f"Updated price for item {idx}: ${prices[idx]:.2f}")

formatted = [f"{p:.2f}" for p in prices]
print("Updated prices: ", formatted)