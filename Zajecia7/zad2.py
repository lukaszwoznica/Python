import sqlite3

connection = sqlite3.connect("baza.db")
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS ksiazki (id integer, title text, author text)''')

cursor.execute('''INSERT INTO ksiazki VALUES (1, 'Pan Tadeusz', 'Mickiewicz')''')
cursor.execute('''INSERT INTO ksiazki VALUES (2, 'Krzyzacy', 'Sienkiewicz')''')


for row in cursor.execute('SELECT title FROM ksiazki'):
    print(row)

connection.rollback()

for row in cursor.execute('SELECT title FROM ksiazki'):
    print(row)

connection.close()
