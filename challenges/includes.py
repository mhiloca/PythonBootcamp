def includes(col, val, index=0):
    # if type(col) == dict:
    #     return True if val in col.values() else False
    # else:
    #     return True if val in col[index:] else False
    if type(col) == dict:
        return val in col.values()
    return val in col[index:]


dic = {'a': 1, 'b': 2}
lis = [1, 7, 3, 5]
print(includes(lis, 5, 2))
print(includes(dic, 1))
