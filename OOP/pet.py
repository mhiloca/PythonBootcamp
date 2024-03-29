class Pet:

    allowed = ['cat', 'dog', 'fish', 'rat']

    def __init__(self, name, species):
        if species not in Pet.allowed:
            raise ValueError(f'You cannot have a {species} pet')
        self.name = name
        self.species = species


cat = Pet('Blue', 'cat')
dog = Pet('Fluffy', 'dog')
croc = Pet('Martin', 'crocodile')

