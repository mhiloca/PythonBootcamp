import sqlite3

connection = sqlite3.connect('other_friends.db')
c = connection.cursor()
c.execute('SELECT * FROM friends WHERE closeness < 6 ORDER BY closeness')
res = c.fetchall()
for person in res:
    print(f'{person[0]} {person[1]}: {person[2]}')
connection.close()
