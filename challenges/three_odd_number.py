def three_odd_number(lista):
    check = []
    p = 0
    while p < len(lista)-3:
        c = total = 0
        index = p
        while c < 3:
            total += lista[index]
            c += 1
            index += 1
        p += 1
        if total % 2 == 1:
            return True
    return False


nums = [1, 2, 3, 4, 5]
print(three_odd_number(nums))
