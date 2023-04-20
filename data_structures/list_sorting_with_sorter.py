lst = ["10 Min", "5 Min", "2 Min", "9 Min", "14 Min"]
lst2 = ["Min 10", "Min 5", "Min 2", "Min 9", "Min 14"]
def sorter(ele):
    num = ele.split()[0]
    return int(num) # convert string to int and return it - using negative int sorts descending

lst.sort(key=sorter)
print(lst)