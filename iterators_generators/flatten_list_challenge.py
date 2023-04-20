lst = [[1, 2, 3], [4],[5, 6], [7, 8],[9, 10], [11, 12]]

flst = [
        ele
        for inner_lst in lst
        for ele in inner_lst
    ]
print(flst)

nested_lst = [[1, 2, 3], [4],[5, 6], [7, 8],[9, 10], [11, 12]]
def flatten_list(nested_list):
    if not nested_list:
        return []
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result

print(flatten_list(nested_lst))

lst = [[[1, 2], [3, 0]], [[4, 0],[5, 6]]]
flatten_list2 = [ele for inner_lst in lst for mid_lst in inner_lst for ele in mid_lst]
print(flatten_list2)

