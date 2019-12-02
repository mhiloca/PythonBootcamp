def sum_pair(lista, num):
    new_list = []
    for index in range(len(lista)-1):
        if lista[index] + lista[index+1] == num:
            new_list.append(lista[index])
            new_list.append(lista[index+1])
            break
    return new_list


nums = [5, 2, 10, 5, 1]
print(sum_pair(nums, 100))

