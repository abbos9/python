import sqlite3

conn = sqlite3.connect('mars.db')

cursor = conn.cursor()


cursor.execute("""
UPDATE evos SET price=28 WHERE id=1;
""")

conn.commit()
conn.close()