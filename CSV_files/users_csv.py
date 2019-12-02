from csv import reader, writer

# with open('users.csv', 'w') as file:
#     csv_writer = writer(file)
#     csv_writer.writerow(['First Name', 'Last Name'])
#     csv_writer.writerow(['Colt', 'Steele'])


# def add_user(a, b):
#     with open('users.csv', 'a') as f:
#         csv_writer = writer(f)
#         csv_writer.writerow([a, b])
#
#
# add_user('Gustavo', 'Cabezita')

def print_file(file):
    with open(file) as f:
        csv_reader = reader(f)
        next(csv_reader)
        for user in csv_reader:
            for name in user:
                print(name, end=' ')
            print()


print_file('users.csv')

