def add_positive_numbers(x, y):
    assert x > 0 and y > 0, 'Both numbers must be positive!'
    return x + y


def eat_junk(food):
    assert food in [
        'pizza',
        'candy',
        'ice cream',
        'fried butter'
    ], 'This is not junk food!'
    return f'NOM, NOM, NOM, I\'m eating {food}'


# DON'T WRITE CODE LIKE THIS

def do_something_bad(user):
    assert user.is_admin, 'Only admin can do bad things'
    destroy_a_bunch_of_stuff()
    return 'Mua ha, ha, ha'

# if you are running a Python file with an -O flag, assertions will not
# be evaluated, and you can have your whole app destroyed by a no admin
# at this point.


print(add_positive_numbers(1, 1))
# print(add_positive_numbers(1, -1))
print(eat_junk('ice cream'))
