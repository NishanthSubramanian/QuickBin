
import sqlite3

conn = sqlite3.connect('database.db')
print ("Opened database successfully")

conn.execute('CREATE TABLE students (name_id INTEGER PRIMARY KEY, name TEXT, addr TEXT, pin TEXT)')
print ("Table created successfully")
conn.close()