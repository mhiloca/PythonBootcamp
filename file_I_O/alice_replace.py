# with open("haiku.txt", 'r') as file:
#     data = file.read()
# with open("haiku.txt", "w") as f:
#     f.write(data.replace('o', '0'))
#
# help(truncate())

with open("haiku.txt", "r+") as file:
    text = file.read()
    file.seek(0)
    file.write(text.replace('0', 'o'))

