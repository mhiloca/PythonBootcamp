multiply = lambda x,y: x * y
print(multiply(4, 3))

cube = lambda x: x ** 3
print(cube(3))

nums = [2, 3, 4, 5]
doubles = map(lambda x: x*2, nums)
for n in doubles:
    print(n)
print(doubles)
dupl = list(map(lambda x: x*2, nums))
print(dupl)

names = [
    {'first': 'Rusty', 'last': 'Steele'},
    {'first': 'Colt', 'last': 'Steele'},
    {'first': 'Blue', 'last': 'Steele'}
]
first_names = list(map(lambda x: x['first'], names))
print(first_names)

users = [
    {'username': 'samuel', 'tweets': ['I love cats', 'I love dogs']},
    {'username': 'katie', 'tweets': ['I love my cat']},
    {'username': 'jeff', 'tweets': []},
    {'username': 'bob123', 'tweets': []},
    {'username': 'doggo_luvr', 'tweets': 'I love dogs'},
    {'username': 'guitar_gal', 'tweets': []}
]
inactive_users = list(map(lambda na: na['username'], filter(lambda u: not u['tweets'], users)))
print(inactive_users)

name = ['Lassie', 'Colt', 'Rusty']
instructor = list(map(lambda n: f'Your instructor is {n}', filter(lambda x: x[0] == 'C', name)))
print(instructor)

