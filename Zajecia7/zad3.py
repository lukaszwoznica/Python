import sqlite3

connection = sqlite3.connect("baza1.db")
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users(id integer PRIMARY KEY AUTOINCREMENT , first_name text, 
                  last_name text, age integer)''')
cursor.execute('''INSERT INTO users VALUES(NULL,'Jan','Kowalski',35)''')
cursor.execute('''INSERT INTO users VALUES(NULL,'Piotr','Nowak',22)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS books(id integer PRIMARY KEY AUTOINCREMENT , title text, author text)''')
cursor.execute('''INSERT INTO books VALUES (NULL, 'Pan Tadeusz', 'Mickiewicz')''')
cursor.execute('''INSERT INTO books VALUES (NULL, 'Krzyzacy', 'Sienkiewicz')''')

cursor.execute('''CREATE TABLE IF NOT EXISTS rents(id integer PRIMARY KEY AUTOINCREMENT, user_id integer, book_id integer, 
                  FOREIGN KEY(user_id) REFERENCES users(id), 
                  FOREIGN KEY (user_id) REFERENCES books(id))''')
cursor.execute('''INSERT INTO rents VALUES(NULL,1,2)''')
cursor.execute('''INSERT INTO rents VALUES(NULL,2,1)''')

connection.commit()

for row in cursor.execute('''SELECT * FROM users'''):
    print(row)
for row in cursor.execute('''SELECT * FROM books'''):
    print(row)
for row in cursor.execute('''SELECT * FROM rents'''):
    print(row)


connection.close()
