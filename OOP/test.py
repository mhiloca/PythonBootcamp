def make_song(num, txt):
    while num >= 0:
        if num == 1:
            yield f'Only {num} bottle of {txt} left'
        elif num == 0:
            yield f'No more {txt}'
        else:
            yield f'{num} bottles of {txt} on the wall'
        num -= 1


song = make_song(5, 'koombucha')
print(next(song))
print(next(song))
print(next(song))
print(next(song))
print(next(song))
print(next(song))


