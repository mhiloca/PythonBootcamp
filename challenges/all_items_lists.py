def list_check(lista):
    return all(True if type(item) == list else False for item in lista)


ex = [[0, 1], ['mama'], [0, 1, 2]]
print(list_check(ex))
