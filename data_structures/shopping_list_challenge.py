# data
store = {
#    name     price
    "Muffin": 6.8, 
    "Cake":   11.2,
    "Chips":  1.4, 
    "Egg":    2.8,
    "Bread":  1.2, 
    "Milk":   2.6,
    "Curd":   4.5, 
    "Egg":    2.8,
}

purchased = {
#   name    quantity 
    "Egg":     4,
    "Bread":   2,
    "Curd":    3,
    "Cake":    1,
    "Muffin":  6,
}

# My solution
amount = 0
print(f"{'Name':<8}{'Price':<8}{'Qty.':>8}{'Amount':>8}")
print("_" *32)
for name, quantity in purchased.items():
    print(f"{name:<8}{store[name]:<8}{quantity:>8}{quantity * store[name]:>8}")
    amount = amount + quantity * store[name]
print("_" *32)
print(f"{'Subtotal:':<16}{amount:>16}")

print('\n') # Separator for output only

# Solution from Codedamn challenge
total = 0
print(f"{'Name':<8}{'Price':<8}{'Qty.':>8}{'Amount':>8}")
print("-"*32)
for name, quantity in purchased.items():
    price = store[name]
    amount = price * quantity
    total += amount
    print(f"{name:<8}{price:<8}{amount:>8}{amount:>8}")

print("-"*32)
print(f"{'Subtotal:':<16}{total:>16}")