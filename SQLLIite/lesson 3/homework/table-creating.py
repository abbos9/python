import sqlite3

conn = sqlite3.connect('mars.db')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS evos(
    id INTEGER,
    price REAL,
    name TEXT,
    photo TEXT,
    describe TEXT
)
""")

conn.commit()
conn.close()
