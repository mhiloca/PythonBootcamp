from csv import reader, writer



def update_users(old_name, old_last, new_name, new_last):
    with open('users.csv') as file:
        csv_reader = reader(file)
        users = list(csv_reader)
    c = 0
    for user in users:
        if [old_name, old_last] == user:
            user[0], user[1] = new_name, new_last
            c += 1
    with open('users.csv', 'w') as new_file:
        csv_writer = writer(new_file)
        for user in users:
            csv_writer.writerow(user)
    return f'{c} names were updated'


print(update_users('Mhirley', 'Lopes', 'Mhiloca', 'Chiqueirenta'))
