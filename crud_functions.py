import sqlite3

connection = sqlite3.connect('Users.db')

cursor = connection.cursor()

cursor.execute('DELETE FROM Users')
cursor.execute('DELETE FROM Products')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Products(
id INTEGER PRIMARY KEY,
title TEXT NOT NULL,
description TEXT,
price INTEGER NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER NOT NULL,
balance INTEGER NOT NULL
)
''')

def add_user(username, email, age, balance=1000):
    check_user = cursor.execute('SELECT * FROM Users WHERE username=?', (username,))
    if check_user.fetchone() is None:
        cursor.execute('INSERT INTO Users (username, email, age, balance)'
                       ' VALUES (?, ?, ?, ?)', (f'{username}', f'{email}', f'{age}', f'{balance}'))
    connection.commit()


def is_included(username):
    base = cursor.execute(f'SELECT username FROM Users WHERE username="{username}"').fetchone()
    return base

def initiate_db():
    for i in range(1, 5):
        cursor.execute(
        'INSERT INTO Products (title, description, price)'
        ' VALUES (?, ?, ?)',(f'Продукт {i}', f'Описание {i}', f'{i * 100}')
                      )

def get_all_products():
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Products')
    db = cursor.fetchall()
    return list(db)

