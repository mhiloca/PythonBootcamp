def min_max_key_dict(dictionary):
    key_dict = dictionary.keys()
    min_key, max_key = min(key_dict), max(key_dict)
    return [min_key, max_key]


print(min_max_key_dict({2: 'a', 0: 'b', 123: 'c', 10: 'd', 4: 'e'}))
