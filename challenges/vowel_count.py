from collections import Counter


def vowel_count(string):
    str_low = string.lower()
    vowels = filter(lambda a: a in 'aeiou', str_low)
    return dict(Counter(sorted(vowels)))


name = 'Ariel'
print(vowel_count(name))
