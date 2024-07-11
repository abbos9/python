import sqlite3

conn = sqlite3.connect('mars.db')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS my_IT_class(
    id INTEGER,
    name TEXT,
    age REAL,
    address TEXT,
    phone_num TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS classmates(
    id INTEGER,
    name TEXT,
    age REAL,
    address TEXT,
    phone_num TEXT
)
""")

conn.commit()
conn.close()
