def oldest_age(lista):
    # oldest = lista.pop(lista.index(max(lista)))
    # second = lista.pop(lista.index(max(lista)))
    # return [second, oldest]
    return sorted(lista)[-2:]


nums = [34, 75, 12, 98, 56, 32]
print(oldest_age(nums))
