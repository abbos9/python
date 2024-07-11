import sqlite3

conn = sqlite3.connect('new.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS pizza(
    id INTEGER,
    name TEXT,
    price REAL,
    description TEXT,
    photo TEXT
)
""")

conn.commit()
print('code worked')
