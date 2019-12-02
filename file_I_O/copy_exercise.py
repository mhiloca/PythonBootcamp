def copy_file(file, new_file):
    with open(file, "r") as f:
        data = f.read()
    with open(new_file, "w") as nf:
        nf.write(data[::-1])


copy_file('haiku.txt', 'new_reversed_haiku.txt')
