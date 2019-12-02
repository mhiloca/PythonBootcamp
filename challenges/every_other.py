def every_other(lista):
    new_list = [lista[x] for x in range(len(lista)) if x % 2 == 0]
    return new_list


num = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(every_other(num))
