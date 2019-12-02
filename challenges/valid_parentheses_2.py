def valid_parentheses(string):
    # dict_par = {'(': -1, ')': 1}
    # check_num = 0
    # for par in string:
    #     check_num += dict_par[par]
    #     if check_num > 0:
    #         return False
    # return check_num == 0
    par = ['()']
    while any(x in string for x in par):
        for p in par:
            string = string.replace(p, '')
    return not string



text = ')(()))'
print(valid_parentheses(text))
