from csv import DictReader

with open('users.csv') as file:
    csv_reader = DictReader(file)
    for user in csv_reader:
        print(f'{user["First Name"]} {user["Last Name"]}')
