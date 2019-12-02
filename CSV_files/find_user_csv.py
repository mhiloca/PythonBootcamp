from csv import reader


def find_user(name, last_name):
    with open('users.csv') as file:
        csv_reader = reader(file)
        users = list(csv_reader)
        if [name, last_name] in users:
            print(users.index([name, last_name]))
        else:
            print(f'{name} {last_name} not found')


find_user('Alan', 'Turing')