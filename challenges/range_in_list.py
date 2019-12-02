def range_in_list(lista, start=0, end=None):
    return sum(lista[start:end+1]) if end else sum(lista[start:])


lista = [1, 2, 4, 6, 7, 5, 7, 2, 3]
print(range_in_list(lista))
