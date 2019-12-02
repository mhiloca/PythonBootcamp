songs = [
    {'title': 'happy birthday', 'playcount': 1},
    {'title': 'Survive', 'playcount': 6},
    {'title': 'YMCA', 'playcount': 99},
    {'title': 'Toxic', 'playcount': 66}
]

# titles = [s['title'].upper() for s in songs]  list comprehension
titles = list(map(lambda s: s['title'].title(), songs))
print(titles)
print('- ' * 15)
# most_played = [s['title'] for s in sorted(songs, key=lambda s: s['playcount'], reverse=True)]
most_played = [
    s['title'] for s in sorted(
        songs, key=lambda s: s['playcount'],
        reverse=True
    )
]
print(most_played)
print('- ' * 15)
# played = [x['title'] for x in songs if x['playcount'] > 10]  list comprehension
played = [so['title'].upper() for so in filter(lambda y: y['playcount'] > 10, songs)]
print(played)
print('- ' * 15)
mp_song = max(songs, key=lambda s: s['playcount'])['title']
print(mp_song)
print('- ' * 15)
not_song = min(songs, key=lambda s: s['playcount'])['title']
print(not_song.upper())
