def sort_list(numbers, sorter):
    sorted_numbers = numbers.copy() # create a copy of original list
    
    match sorter:
        case 'asc':
            sorted_numbers.sort() # sort in ascending order
        case 'desc':
            sorted_numbers.sort(reverse=False) # sort in descending order
        case 'none':
            sorted_numbers
        case _:
            print('Invalid sorter')
    
    return sorted_numbers # return sorted list

print(sort_list([10,3,56,48,77,0,33,66], 'desc'))