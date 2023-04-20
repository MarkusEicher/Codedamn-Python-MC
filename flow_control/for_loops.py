""" grocery_list = ["milk", "eggs", "bread", "cheese"]

index = 0

for item in grocery_list:
    print(grocery_list[index])
    index += 1 """

""" grocery_list = ["milk", "eggs", "bread", "cheese"]

index = 0

for index in range(len(grocery_list)):
    print(index, grocery_list[index])
    index += 1 """

product_items = {
#   Title      Price    
    "Cookies": 5, 
    "Cake":    12.5, 
    "Muffin":  0.8, 
    "Can":     1.4,
}

# Helper variables
total = 0
product_names = ['Cookies', 'Cake', 'Muffin', 'Can']

# 👇 Find the total here...
for item in product_names:
    total = total + product_items[item]

# Printing the total
print(total)