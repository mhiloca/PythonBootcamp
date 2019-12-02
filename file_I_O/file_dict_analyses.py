# def statistic(file):
#     with open(file) as file:
#         data = file.read()
#     lines = data.split('\n')
#     words = [len(x.split(' ')) for x in lines]
#     char = list(map(lambda b: sum(list(map(lambda d: len(d), b))),
#                     map(lambda c: c.split(' '), lines)))
#     status = dict(lines=len(lines), words=sum(words), char=sum(char))
#     return status
#
#
# print(statistic('haiku.txt'))

# with open("haiku.txt") as file:
#     characters = file.read()
#     file.seek(0)
#     data = file.readlines()
# words = map(lambda a: a.split(' '), data)
# soma = 0
# for x in words:
#     for y in x:
#         soma += (len(y.replace(' ', '')))
# tog = characters.replace(' ', '').replace('\n', '')
# print(tog)

with open('haiku.txt') as file:
    characters = file.read()
    file.seek(0)
    data = file.readlines()
lines = len(data)
words = sum(map(lambda x: len(x.split(' ')), data))
char = len(characters.replace(' ', '').replace('\n', ''))
status = dict(lines=lines, words=words, char=char)
print(status)