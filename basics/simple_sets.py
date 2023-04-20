discounted = { 'A', 'C', 'Y', 'X', 'L'}
coupons = { 'Y', 'M', 'R', 'C', 'E'}

print(discounted.intersection(coupons)) 
print(coupons.intersection(discounted)) 

print(discounted.difference(coupons))  
print(coupons.difference(discounted)) 

print(discounted.union(coupons))
print(coupons.union(discounted)) 

print(discounted.symmetric_difference(coupons))
print(coupons.symmetric_difference(discounted))

# print(discounted.issuperset(coupons))
# print(discounted.issuperset(discounted))
# print(coupons.issuperset(coupons))
# print(coupons.issuperset(discounted))

# print(discounted.issubset(coupons))
# print(discounted.issubset(discounted))   
# print(coupons.issubset(coupons))
# print(coupons.issubset(discounted))

print(type(discounted))
print(type(coupons))