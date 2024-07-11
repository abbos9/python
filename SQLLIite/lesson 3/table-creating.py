import sqlite3

conn = sqlite3.connect('mars.db')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS shop (
    id INTEGER,
    name TEXt,
    cost INTEGER,
    photo TEXT,
    count INTEGER    

)
""")

conn.commit()
conn.close()
