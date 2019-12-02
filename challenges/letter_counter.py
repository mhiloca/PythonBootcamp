def letter_counter(string):
    def inner(char):
        return string.lower().count(char)
    return inner


counter = letter_counter('Amazing')
print(counter('a'))
print(counter('i'))