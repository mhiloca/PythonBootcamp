from csv import reader, writer


def delete_users(name, last_name):
    with open('users.csv') as file:
        csv_reader = reader(file)
        users = list(csv_reader)
    count, deleted = 0, ''
    for index, user in enumerate(users):
        if [name, last_name] == user:
            deleted = users.pop(index)
            count += 1
    with open('users.csv', 'w') as new_file:
        csv_writer = writer(new_file)
        for user in users:
            csv_writer.writerow(user)
    return f'{deleted[0]} {deleted[1]} was sucessfully removed'


print(delete_users('Mhirley', 'Lopes'))