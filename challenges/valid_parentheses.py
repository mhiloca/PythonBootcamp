def valid_parentheses(string):
    # check = []
    # for p in string:
    #     if p == '(':
    #         check.append('(')
    #     if p == ')':
    #         check.remove('(') if check else check.append('(')
    # return not check
    count = item = 0
    while item < len(string):
        if string[item] == '(':
            count += 1
        if string[item] == ')':
            count -= 1
        item += 1
        if count < 0:
            return False
    return not count



para = '()()()()()()'
print(valid_parentheses(para))
