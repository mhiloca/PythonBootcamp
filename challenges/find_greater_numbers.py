def find_greater_number(lista):
    count = 0
    for i in range(len(lista)):
        for x in range(i):
            if lista[i] > lista[x]:
                count += 1
    return count


nums = 5, 6, 1, 10, 7, 2
print(find_greater_number(nums))
