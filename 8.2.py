def sum_and_difference(list1, list2):
    return list(map(lambda x, y: (x + y, x - y), list1, list2))

list1 = [6, 5, 3, 9]
list2 = [0, 1, 7, 7]
result = sum_and_difference(list1, list2)
print(result)
