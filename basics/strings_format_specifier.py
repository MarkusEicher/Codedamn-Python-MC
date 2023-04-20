pi = 3.14159
print (f"The value of pi is approximately {pi:.2f}.")

import datetime
date = datetime.date.today()
print (date)
print (f"The date is {date:%Y-%B-%d, %A}.")

num = 1000000
print (f"{num:,}")

persons = {
    "Alice": 999001,
    "Bobby": 999002,
    "Benjamin": 999003
}

for name in persons:
    print(f"{name:<10}{persons[name]:>10}")

multiP = [1,2,3,4,5,6,7,8,9,10]

for num in range(1, 11):
    print(f"15 x {num} = {num*15}")

# for item in multiP:
#     print(f"{item:<3}x{multiP[item - 1]:^4}={item * multiP[item - 1]:>4}")

