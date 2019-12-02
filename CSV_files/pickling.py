import pickle
from chicken import Chicken

hen1 = Chicken('Marilu', 'hen')
hen2 = Chicken('Mark', 'cock')
# with open('chicken.pickle', 'wb') as file:
#     pickle.dump((hen1, hen2), file)

with open('chicken.pickle', 'rb') as file:
    chick1, chick2 = pickle.load(file)
    print(chick1.get_eggs())
    print(chick2)

