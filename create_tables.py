import sqlite3

#creating tables for user and items

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

query_user = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text )"
cursor.execute(query_user)

query_item = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name text, price real)"
cursor.execute(query_item)

connection.commit()
connection.close()
