from random import randint


def sum_up_diagonals(matrix):
    # sum_up, mat, colu = 0, len(matrix), len(matrix) - 1
    # for li in range(mat):
    #     for co in range(len(matrix[li])):
    #         if li == co:
    #             sum_up += matrix[li][co]
    # for lin in range(mat):
    #     for col in range(len(matrix[lin])):
    #         sum_up += matrix[lin][colu]
    #         break
    #     colu -= 1
    # return sum_up
    sum_up = 0
    for i, v in enumerate(matrix):
        sum_up += matrix[i][i]
        sum_up += matrix[i][-1-i]
    return sum_up


matriz = [[randint(0, 5) for x in range(4)] for y in range(4)]
print(matriz)
print(sum_up_diagonals(matriz))
