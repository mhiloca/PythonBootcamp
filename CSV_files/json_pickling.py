from chicken import Chicken
import jsonpickle


# hen = Chicken('Marilu', 'hen')
# cock = Chicken('Mark', 'cock')
# with open('hen.json', 'w') as file:
#     frozen = jsonpickle.encode((hen, cock))
#     file.write(frozen)

with open('hen.json') as file:
    contents = file.read()
    unfrozen = jsonpickle.decode(contents)

for animal in unfrozen:
    print(repr(animal))
