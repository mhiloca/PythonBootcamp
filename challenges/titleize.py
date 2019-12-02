def titleize(string):
    # new_str = string.split()
    # new_str = map(lambda a: a[0].upper() + a[1:], new_str)
    # return ' '.join(new_str)
    return ' '.join(s[0].upper + s[1:] for s in string.split())


text = 'I love rOCk and rOll'
print(titleize(text))
