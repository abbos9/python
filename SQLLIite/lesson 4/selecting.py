import sqlite3

conn = sqlite3.connect('mars.db')

cursor = conn.cursor()

product = cursor.execute("SELECT * FROM evos").fetchall()

for i in product:
    print(i)
