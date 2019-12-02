import sqlite3

connection = sqlite3.connect('my_friends.db')
# create the cursor
c = connection.cursor()
# execute some sql
# c.execute("CREATE TABLE friends (first_name TEXT, last_name text, closeness INTEGER);")
# insert_querys = "INSERT INTO friends VALUES ('Renata', 'Domingues', 9)"
# form_first = 'Micheline'
# form_last = 'Lopes'
# form_closeness = 10
# BAD WAY! DON'' DO IT!
# query = f'INSERT INTO friends VALUES ("{form_first}", "{form_last}", "{form_closeness}")'
# BETTERWAY
data = ('Leonardo', 'Brighi', 10)
query = 'INSERT INTO friends VALUES (?, ?, ?)'
c.execute(query, data)
# commit changes
connection.commit()
connection.close()
