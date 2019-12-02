from csv import writer
from validate import go_on

with open('users.csv', 'w') as file:
    csv_writer = writer(file)
    csv_writer.writerow(['First Name', 'Last Name'])
    while True:
        name = input('First name: ').strip().title()
        last = input('Lastname: ').strip().title()
        csv_writer.writerow([name, last])
        if go_on('fullname') == 'N':
            break
