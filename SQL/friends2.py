import sqlite3
from validate import go_on

connection = sqlite3.connect('other_friends.db')
c = connection.cursor()
# c.execute('CREATE TABLE friends (firs_name, last_name, closeness);')
# people = [
#     ('André', 'Godoy', 8),
#     ('Magali', 'Luiz', 10),
#     ('Camila', 'Aschermann', 9),
#     ('Elaine', 'Sallas', 10),
#     ('Daniele', 'Coelho', 3),
#     ('Marcello', 'Tonelli', 2)
# ]
# c.executemany('INSERT INTO friends VALUES (?, ?, ?);', people)
while True:
    first = input('First name: ').strip().title()
    last = input('Last name: ').strip().title()
    closeness = int(input('Closeness [1-10]: ').strip())
    data = (first, last, closeness)
    c.execute('INSERT INTO friends VALUES (?, ?, ?);', data)
    if go_on('friend') == 'N':
        break
connection.commit()
connection.close()
