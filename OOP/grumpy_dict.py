class GrumpyDict(dict):
    def __repr__(self):
        return super().__repr__()

    def __missing__(self, key):
        return f'YOU WANT {key}, WELL IT AINT HERE!'

    def __setitem__(self, key, value):
        print('HERE YOU COME, CHANING THINGS! ARGH!')
        super().__setitem__(key, value)


d = GrumpyDict({'first': 'Frida', 'animal': 'cat'})
d['city'] = 'Florianópolis'
print(d)

