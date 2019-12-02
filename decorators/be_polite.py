def be_polite(fn):
    def wrapper(person):
        print('What a pleasure to meet you!')
        fn(person)
        print('Have a great day!')
    return wrapper


@be_polite
def greet(person):
    print(f'My name is {person}')


@be_polite
def rage(person):
    print(f'I HATE YOU, {person}')


greet('Mhirley')
print('- ' * 15)
rage('Jackass!')
