def combine_words(word, **kwargs):
    if 'prefix' in kwargs:
        return f'{kwargs["prefix"]}{word}'
    elif 'suffix' in kwargs:
        return f'{word}{kwargs["suffix"]}'
    return f'{word}'


print(combine_words('prepared', prefix='un'))