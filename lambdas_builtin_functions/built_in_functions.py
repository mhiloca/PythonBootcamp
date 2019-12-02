print(all([0, 1, 2, 3,4]))
print('- ' *( 5))
names = [ 'Mhirley', 'Micheline', 'Maria']
print(all([name[0] == 'M' for name in names]))
print(all(name[0] == 'M' for name in names))
largest = max(names, key=lambda n: len(n))
print(largest)
print('- ' * 5)
names.append('Joao')
print(any([name[0] == 'G' for name in names]))
print(any(name[0] == 'J' for name in names))

l = [2, 'a', 'b', 'c']
print(all(type(x) == str for x in l))

nums = [2, 5, 1, 4, 7, 2]
print(sorted(nums, reverse=True))
print(nums)

num = 8, 5, 2, 9, 2
nu = sorted(num, reverse=True)
print(num)
print(nu)

users = [
    {'username': 'samuel', 'tweets': ['I love cats', 'I love dogs']},
    {'username': 'katie', 'tweets': ['I love my cat']},
    {'username': 'jeff', 'tweets': []},
    {'username': 'bob123', 'tweets': []},
    {'username': 'doggo_luvr', 'tweets': 'I love dogs'},
    {'username': 'guitar_gal', 'tweets': []}
]
user_names = sorted(users, key=lambda user: user['username'])
for c in user_names:
    print(c['username'])
print('- ' * 15)
songs = [
    {'title': 'happy birthday', 'playcount': 1},
    {'title': 'Survive', 'playcount': 6},
    {'title': 'YMCA', 'playcount': 99},
    {'title': 'Toxic', 'playcount': 66}
]
play_count = sorted(songs, key=lambda song: song['playcount'], reverse=True)
for i in play_count:
    print(i['title'])
print('- ' * 15)
least_played = min(songs, key=lambda s: s['playcount'])['title']
print(f'The least song played is {least_played}')
most_played = max(songs, key=lambda s: s['playcount'])['title']
print(f'The most played song is {most_played}')
