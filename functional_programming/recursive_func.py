def reduce(num):
    while num:
        print(num)
        num -= 1

# reduce(5)

def reduce(num):
    print(f"Called reduce ({num})")
    
    if num:
        print(f"reducing num by {num - 1 = }")
        reduce(num -1)

print("We are calling reduce (5)")
reduce(5)

