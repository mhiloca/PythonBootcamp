def find_the_duplicate(lista):
    # num = filter(lambda a: lista.count(a) > 1, lista)
    # try:
    #     return next(num)
    # except StopIteration:
    #     return None
    for item in lista:
        if lista.count(item) > 1:
            return item
    return None


nums = [1, 2, 3, 4, 5]
print(find_the_duplicate(nums))
