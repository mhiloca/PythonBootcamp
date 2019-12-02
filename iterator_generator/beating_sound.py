def current_beat():
    nums = 1, 2, 3, 4
    i = 0
    while i < len(nums):
        if i >= len(nums): i = 0
        yield nums[i]
        i += 1


def make_song(verses=99, txt='soda'):
    for i in range(verses, -1, -1):
        if i > 1:
            yield f'{i} bottles of {txt} on the wall.'
        elif i == 1:
            yield f'Only 1 bottle of {txt} left!'
        else:
            yield f'No more {txt}!'


beat = current_beat()
print(next(beat))

print('- ' * 15)
song = make_song(10, 'vodca')
for x in range(11):
    print(next(song))
