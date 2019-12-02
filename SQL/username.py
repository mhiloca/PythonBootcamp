import sqlite3
from validate import go_on

conn = sqlite3.connect('users_db.db')
c = conn.cursor()
# c.execute('CREATE TABLE users (username TEXT, password TEXT)')
# while True:
#     username = input('Username: ').strip().lower()
#     password = input('Password: ').strip()
#     c.execute('INSERT INTO users VALUES (?, ?)', (username, password))
#     if go_on('username') == 'N':
#         break
u = input('username: ').strip()
p = input('password: ').strip()
# c.execute(f'SELECT * FROM users WHERE username="{u}" AND password="{p}"')
query = 'SELECT * FROM users WHERE username=? AND password=?'
c.execute(query, (u, p))
res = c.fetchone()
print('WELCOME BACK') if res else print('FAILED LOGIN')
conn.commit()
conn.close()
