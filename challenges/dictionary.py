def dictionary(list1, list2):
    return {list1[x]: (list2[x] if x < len(list2) else None) for x in range(len(list1))}


list1 = [1, 2, 4, 5, 7, 9, 3, 1, 6, 9]
list2 = [9, 7, 5, 6, 7, 8, 6]
print(dictionary(list1, list2))
